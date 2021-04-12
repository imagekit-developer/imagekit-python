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


class Url:
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
        
        # important to strip the trailing slashes. later logic assumes no trailing slashes.
        path = options.get("path", "").strip("/")
        src = options.get("src", "").strip("/")
        url_endpoint = options.get("url_endpoint", "").strip("/")
        transformation_str = self.transformation_to_str(options.get("transformation"))
        transformation_position = options.get("transformation_position", Default.DEFAULT_TRANSFORMATION_POSITION.value)

        if transformation_position not in Default.VALID_TRANSFORMATION_POSITION.value:
            raise ValueError(ERRORS.INVALID_TRANSFORMATION_POSITION.value)

        if (path == "" and src == ""):
            return ""

        # if path is present then it is given priority over src parameter
        if path:
            if transformation_position == "path" and len(transformation_str) != 0:
                temp_url = "{}/{}:{}/{}".format(
                    url_endpoint,
                    Default.TRANSFORMATION_PARAMETER.value,
                    transformation_str.strip("/"),
                    path
                )
            else:
                temp_url = "{}/{}".format(
                    url_endpoint,
                    path
                )
        else:
            temp_url = src
            # if src parameter is used, then we force transformation position in query
            transformation_position = Default.QUERY_TRANSFORMATION_POSITION.value

        url_object = urlparse(temp_url)

        query_params = dict(parse_qsl(url_object.query))
        query_params.update(options.get("query_parameters", {}))
        if transformation_position == Default.QUERY_TRANSFORMATION_POSITION.value and len(transformation_str) != 0:
            query_params.update({Default.TRANSFORMATION_PARAMETER.value: transformation_str})
        query_params.update({Default.SDK_VERSION_PARAMETER.value: Default.SDK_VERSION.value})

        # Update query params in the url
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

            """
            If the expire_seconds parameter is specified then the output URL contains
            ik-t parameter (unix timestamp seconds when the URL expires) and 
            the signature contains the timestamp for computation. 
            
            If not present, then no ik-t parameter and the value 9999999999 is used.
            """
            if expire_seconds:
                query_params.update({Default.TIMESTAMP_PARAMETER.value: expiry_timestamp, Default.SIGNATURE_PARAMETER.value: url_signature})
            else:
                query_params.update({Default.SIGNATURE_PARAMETER.value: url_signature})
            
            # Update signature related query params
            url_object = url_object._replace(query=urlencode(query_params))

        return url_object.geturl()

    @staticmethod
    def get_signature_timestamp(expiry_seconds: int = None) -> int:
        """
        this function returns the signature timestamp to be used
        with the generated url. 
        If expiry_seconds is provided, it returns expiry_seconds added
        to the current unix time, otherwise the default time stamp
        is returned.
        """
        if not expiry_seconds:
            return Default.DEFAULT_TIMESTAMP.value
        current_timestamp = int(dt.now().timestamp())

        return current_timestamp + expiry_seconds

    @staticmethod
    def get_signature(private_key, url, url_endpoint, expiry_timestamp : int) -> str:
        """"
        create signature(hashed hex key) from
        private_key, url, url_endpoint and expiry_timestamp
        """
        # ensure url_endpoint has a trailing slash
        if url_endpoint[-1] != '/':
            url_endpoint += '/'

        if expiry_timestamp < 1:
            expiry_timestamp = Default.DEFAULT_TIMESTAMP.value

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
                    value = transformation[i][key]
                    if isinstance(value, bool):
                        value = str(value).lower()
                    if transform_key == "oi"  or transform_key == "di":
                        value = value.strip("/")
                        value = value.replace("/","@@")
                    parsed_transform_step.append(
                        "{}{}{}".format(
                            transform_key,
                            Default.TRANSFORM_KEY_VALUE_DELIMITER.value,
                            value,
                        )
                    )

            parsed_transforms.append(
                Default.TRANSFORM_DELIMITER.value.join(parsed_transform_step))

        return Default.CHAIN_TRANSFORM_DELIMITER.value.join(parsed_transforms)
