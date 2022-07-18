import base64
from datetime import datetime as dt
from typing import Dict

import requests
from requests import Response

from .constants.defaults import Default
from .constants.errors import ERRORS


class ImageKitRequest(object):
    """
    ImageKitRequest is holds the methods and attributes about server
    communications and communicates to server, used by Internal classes
    """

    def __init__(
        self, private_key, public_key, url_endpoint, transformation_position, options
    ):
        self.private_key = private_key
        self.public_key = public_key
        self.url_endpoint = url_endpoint
        self.transformation_position = (
            transformation_position or Default.DEFAULT_TRANSFORMATION_POSITION.value
        )
        self.options = options or {}

        if not (self.private_key and self.public_key and self.url_endpoint):
            raise ValueError(ERRORS.MANDATORY_INITIALIZATION_MISSING.value)

    def create_headers(self):
        """Create headers dict and sets Authorization header
        """
        headers = {"Accept-Encoding": "gzip, deflate"}
        headers.update(self.get_auth_headers())
        return headers

    def get_auth_headers(self):
        """Create dictionary with encoded private key
        The out put is used in request header as authorization header

        :return: dictionary of encoded private key
        """
        encoded_private_key = base64.b64encode((self.private_key + ":").encode()).decode(
            "utf-8"
        )
        return {"Authorization": "Basic {}".format(encoded_private_key)}

    @staticmethod
    def request(method, url, headers, params=None, files=None, data=None) -> Response:
        """Requests from ImageKit server used,by internal methods
        """
        resp = requests.request(
            method=method,
            url=url,
            params=params,
            files=files,
            data=data,
            headers=headers,
        )

        return resp

    def extend_url_options(self, options: Dict) -> Dict:
        """
        adds data to the options from the object, so that
        required data can be used by url builder
        """
        attr_dict = {
            "public_key": self.public_key,
            "private_key": self.private_key,
            "url_endpoint": self.url_endpoint,
            "transformation_position": self.transformation_position,
        }

        extended_options = {**self.options, **attr_dict, **options}
        return extended_options

    @staticmethod
    def get_signature_timestamp(seconds: int = None) -> int:
        """
        Returns either default time stamp
        or current unix time and expiry seconds to get
        signature time stamp
        """

        if not seconds:
            return Default.DEFAULT_TIMESTAMP.value
        current_timestamp = int(dt.now().timestamp())

        return current_timestamp + seconds
