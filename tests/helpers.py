import unittest
from typing import Any
from unittest.mock import Mock, patch

from requests import Response

from imagekitio.client import ImageKit
from tests.dummy_data.file import AUTHENTICATION_ERR_MSG, SUCCESS_GENERIC_RESP
try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json import JSONDecodeError


class ClientTestCase(unittest.TestCase):
    """
    Base TestCase for Client
    """
    private_key="fake122"

    @patch("imagekitio.file.File")
    @patch("imagekitio.resource.ImageKitRequest")
    def setUp(self, mock_file, mock_req):
        """
        Tests if list_files work with skip and limit
        """
        self.options = {
            "skip": "10",
            "limit": "1",
        }
        self.client = ImageKit(
            public_key="fake122", private_key=ClientTestCase.private_key, url_endpoint="fake122",
        )


def get_mocked_failed_resp(message=None, status=401):
    """GET failed mocked response customized by parameter
    """
    mocked_resp = Mock(spec=Response)
    mocked_resp.status_code = status
    if not message:
        mocked_resp.json.return_value = AUTHENTICATION_ERR_MSG
    else:
        mocked_resp.json.return_value = message
    return mocked_resp


def get_mocked_failed_resp_text():
    """GET failed mocked response returned as text not json
    """
    mocked_resp = Mock(spec=Response)
    mocked_resp.status_code = 502
    mocked_resp.text = 'Bad Gateway'
    mocked_resp.json.side_effect = JSONDecodeError("Expecting value: ", "Bad Gateway", 0)
    return mocked_resp


def get_mocked_success_resp(message: dict = None, status: int = 200):
    """GET success mocked response customize by parameter
    """
    mocked_resp = Mock(spec=Response)
    mocked_resp.status_code = status
    if not message:
        mocked_resp.json.return_value = SUCCESS_GENERIC_RESP
    else:
        mocked_resp.json.return_value = message
    return mocked_resp
