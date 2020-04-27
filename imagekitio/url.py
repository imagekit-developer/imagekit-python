import hashlib
import hmac
import sys
from datetime import datetime as dt
from typing import Any, Dict, List
from urllib.parse import ParseResult, urlparse, urlunparse, parse_qsl, urlencode

from imagekitio.constants.defaults import Default
from imagekitio.constants.supported_transform import SUPPORTED_TRANS
from imagekitio.utils.formatter import camel_dict_to_snake_dict, flatten_dict

from .constants import ERRORS

TRANSFORMATION_PARAMETER = "tr"
DEFAULT_TRANSFORMATION_POSITION = "path"
QUERY_TRANSFORMATION_POSITION = "query"
CHAIN_TRANSFORM_DELIMITER = ":"
TRANSFORM_DELIMITER = ","
TRANSFORM_KEY_VALUE_DELIMITER = "-"

SIGNATURE_PARAMETER = "ik-s"
TIMESTAMP_PARAMETER = "ik-t"
DEFAULT_TIMESTAMP = "9999999999"


class Url(object):
    """
    Url class holds the request and related methods
    to generate url(signed and unsigned)
    """

    def __init__(self, request_obj):
        self.request = request_obj

    def generate_url(self, options: Dict = None) -> str:
        options = camel_dict_to_snake_dict(options)
        extended_options = self.request.extend_url_options(options)
        return self.build_url(extended_options)

    def build_url(self, options: dict) -> str:
        """
        builds url for from all options,
        """
        
        path = options.get("path", "").strip("/")
        src = options.get("src", "").strip("/")
        url_endpoint = options.get("url_endpoint", "").strip("/")
        transformation_str = self.transformation_to_str(options.get("transformation"))
        transformation_position = options.get("transformation_position") or DEFAULT_TRANSFORMATION_POSITION

        if transformation_position not in Default.VALID_TRANSFORMATION_POSITION.value:
            raise ValueError(ERRORS.INVALID_TRANSFORMATION_POSITION.value)

        if (path is "" and src is ""):
            return ""

        if src:
            temp_url = src.strip("/")
            transformation_position = QUERY_TRANSFORMATION_POSITION
        else:
            if transformation_position == "path":
                temp_url = "{}/{}:{}/{}".format(
                    url_endpoint.strip("/"),
                    TRANSFORMATION_PARAMETER,
                    transformation_str.strip("/"),
                    path.strip("/")
                )
            else:
                temp_url = "{}/{}".format(
                    url_endpoint.strip("/"),
                    path.strip("/")
                )

        url_object = urlparse(temp_url.strip("/"))

        query_params = dict(parse_qsl(url_object.query))
        query_params.update(options.get("query_parameters", {}))
        if transformation_position == QUERY_TRANSFORMATION_POSITION:
            query_params.update({"tr": transformation_str})
        query_params.update({"ik-sdk-version": Default.SDK_VERSION.value})

        # Update query params
        url_object = url_object._replace(query=urlencode(query_params))

        if options.get("signed"):
            expire_seconds = options.get("expire_seconds")
            private_key = options.get("private_key")
            expiry_timestamp = self.get_signature_timestamp(expire_seconds)
            url_signature = self.get_signature(
                private_key=private_key,
                url=url_object.geturl(),
                url_endpoint=url_endpoint,
                expiry_timestamp=expiry_timestamp,
            )
            query_params.update({TIMESTAMP_PARAMETER: expiry_timestamp, SIGNATURE_PARAMETER: url_signature})
            # Update signature related query params
            url_object = url_object._replace(query=urlencode(query_params))

        return url_object.geturl()

    @staticmethod
    def get_signature_timestamp(seconds: int = None) -> int:
        """
        this function returns either default time stamp
        or current unix time and expiry seconds to get
        signature time stamp
        """
        if not seconds:
            return Default.DEFAULT_TIMESTAMP.value
        current_timestamp = int(dt.now().strftime("%s"))

        return current_timestamp + seconds

    @staticmethod
    def prepare_dict_for_unparse(url_dict: dict) -> dict:
        """
        remove and add required back slash of 'netloc' and 'path'
        to parse it properly, urllib.parse.unparse() function can't
        create url properly if path doesn't have '/' at the start
        """
        url_dict["netloc"] = url_dict["netloc"].rstrip("/")
        url_dict["path"] = "/" + url_dict["path"].strip("/")

        return url_dict

    @staticmethod
    def get_signature(private_key, url, url_endpoint, expiry_timestamp) -> str:
        """"
        create signature(hashed hex key) from
        private_key, url, url_endpoint and expiry_timestamp
        """
        # ensure url_endpoint has a trailing slash
        if url_endpoint[-1] != '/':
            url_endpoint += '/'

        if isinstance(expiry_timestamp, int) and expiry_timestamp < 1:
            expiry_timestamp = DEFAULT_TIMESTAMP

        replaced_url = url.replace(url_endpoint, "") + str(expiry_timestamp)

        signature = hmac.new(
            key=private_key.encode(), msg=replaced_url.encode(), digestmod=hashlib.sha1
        )
        return signature.hexdigest()

    @staticmethod
    def is_valid_trans_options(options: Dict[str, Any]) -> bool:
        """
        check if transformation options parameter provided by user is valid
        so that ValueError exception can be raised with appropriate error
        message in the ImageKitRequest Class
        """
        supported_trans_keys = SUPPORTED_TRANS.keys()
        # flattening to dict from list of dict to check key validation
        transformation_dict = flatten_dict(options.get("transformation", []))
        for key in transformation_dict:
            if key not in supported_trans_keys:
                return False
        return True

    @staticmethod
    def is_valid_transformation_pos(trans_pos: str) -> bool:
        """
        Returns if transformation position is valid as per Server Documentation
        """
        return trans_pos in Default.VALID_TRANSFORMATION_POSITION.value

    @staticmethod
    def transformation_to_str(transformation):
        """
            creates transformation_position string for url from
            transformation_position dictionary
        """
        if not isinstance(transformation, list):
            return ""
        parsed_transforms = []
        for i in range(len(transformation)):
            parsed_transform_step = []
            for key in transformation[i]:
                transform_key = SUPPORTED_TRANS.get(key, "")
                if not transform_key:
                    transform_key = key

                if transformation[i][key] == "-":
                    parsed_transform_step.append(transform_key)
                else:
                    parsed_transform_step.append(
                        "{}{}{}".format(
                            transform_key,
                            TRANSFORM_KEY_VALUE_DELIMITER,
                            transformation[i][key],
                        )
                    )

            parsed_transforms.append(
                TRANSFORM_DELIMITER.join(parsed_transform_step))

        return CHAIN_TRANSFORM_DELIMITER.join(parsed_transforms)
