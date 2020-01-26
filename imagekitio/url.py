import hashlib
import hmac
from datetime import datetime as dt
from typing import Any, Dict, List
from urllib.parse import ParseResult, urlparse, urlunparse

from imagekitio.constants.defaults import Default
from imagekitio.constants.supported_transform import SUPPORTED_TRANS
from imagekitio.utils.formatter import camel_dict_to_snake_dict, flatten_dict
from imagekitio.constants.supported_transform import SUPPORTED_TRANS
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
        if options.get("src"):
            options["transformation_position"] = DEFAULT_TRANSFORMATION_POSITION
        extended_options = self.request.extend_url_options(options)
        return self.build_url(extended_options)

    def build_url(self, options: dict) -> str:
        """
        builds url for from all options,
        """
        path = options.get("path", "")
        src = options.get("src", "")
        url_endpoint = options.get("url_endpoint", "")
        transformation_position = options.get("transformation_position")
        if transformation_position not in Default.VALID_TRANSFORMATION_POSITION.value:
            raise ValueError(ERRORS.INVALID_TRANSFORMATION_POSITION.value)

        if src or (
            options.get("transformation_position") == QUERY_TRANSFORMATION_POSITION
        ):
            src_param_used_for_url = True
        else:
            src_param_used_for_url = False
        if not (path or src):
            return ""
        result_url_dict = {"netloc": "", "path": "", "query": ""}
        if path:
            parsed_url = urlparse(path)
            parsed_host = urlparse(url_endpoint)
            result_url_dict["scheme"] = parsed_host.scheme
            result_url_dict["netloc"] = (parsed_host.netloc + parsed_host.path).lstrip(
                "/"
            )
            result_url_dict["path"] = parsed_url.path.strip("/")

        else:
            parsed_url = urlparse(src)
            host = parsed_url.netloc
            if parsed_url.username:
                # creating host like username:password@domain.com if username is there in parsed url
                host = "{}:{}@{}".format(
                    parsed_url.username, parsed_url.password, parsed_url.netloc
                )
            result_url_dict["netloc"] = host
            result_url_dict["scheme"] = parsed_url.scheme
            result_url_dict["path"] = parsed_url.path
            src_param_used_for_url = True

        query_params = options.get("query_parameters", {})
        transformation_str = self.transformation_to_str(options.get("transformation"))
        if transformation_str:
            if (
                transformation_position == Default.QUERY_TRANSFORMATION_POSITION.value
            ) or src_param_used_for_url:
                result_url_dict["query"] = "{}={}".format(
                    TRANSFORMATION_PARAMETER, transformation_str
                )

            else:
                result_url_dict["path"] = "{}:{}/{}".format(
                    TRANSFORMATION_PARAMETER,
                    transformation_str,
                    result_url_dict["path"],
                )

        result_url_dict["scheme"] = result_url_dict["scheme"] or "https"

        # Signature String and Timestamp
        # We can do this only for URLs that are created using urlEndpoint and path parameter
        # because we need to know the endpoint to be able to remove it from the URL to create a signature
        # for the remaining. With the src parameter, we would not know the "pattern" in the URL
        if options.get("signed") and (not options.get("src")):
            expire_seconds = options.get("expire_seconds")
            private_key = options.get("private_key")
            expiry_timestamp = self.get_signature_timestamp(expire_seconds)

            intermediate_url = urlunparse(
                result_url_dict.get(f, "") for f in ParseResult._fields
            )
            url_signature = self.get_signature(
                private_key=private_key,
                url=intermediate_url,
                url_endpoint=url_endpoint,
                expiry_timestamp=expiry_timestamp,
            )
            if expiry_timestamp and (expiry_timestamp != DEFAULT_TIMESTAMP):
                query_params[TIMESTAMP_PARAMETER] = expiry_timestamp
            query_params[SIGNATURE_PARAMETER] = url_signature
            query_params_str = "&".join(
                str(k) + "=" + str(v) for k, v in query_params.items()
            )
            result_url_dict["query"] = query_params_str
        result_url_dict = self.prepare_dict_for_unparse(result_url_dict)
        generated_url = urlunparse(
            result_url_dict.get(f, "") for f in ParseResult._fields
        )
        if result_url_dict["query"]:
            generated_url = generated_url + "&sdk-version=" + Default.SDK_VERSION.value
        else:
            generated_url = generated_url + "?sdk-version=" + Default.SDK_VERSION.value
        return generated_url

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
        replaced_url = url.replace(url_endpoint, "") + str(expiry_timestamp)
        signature = hmac.new(
            key=replaced_url.encode(), msg=private_key.encode(), digestmod=hashlib.sha1
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

            parsed_transforms.append(TRANSFORM_DELIMITER.join(parsed_transform_step))

        return CHAIN_TRANSFORM_DELIMITER.join(parsed_transforms)
