import base64
import json
import re
import unittest
from unittest.mock import patch

from imagekitio.client import ImageKit
from imagekitio.models.ListAndSearchFileRequestOptions import (
    ListAndSearchFileRequestOptions,
)


class ClientTestCase(unittest.TestCase):
    """
    Base TestCase for Client
    """

    private_key = "fake122"

    @patch("imagekitio.file.File")
    @patch("imagekitio.resource.ImageKitRequest")
    def setUp(self, mock_file, mock_req):
        """
        Tests if list_files work with skip and limit
        """
        self.options = ListAndSearchFileRequestOptions(
            type="file",
            sort="ASC_CREATED",
            path="/",
            search_query="created_at >= '2d' OR size < '2mb' OR format='png'",
            file_type="all",
            limit=1,
            skip=0,
            tags="Tag-1, Tag-2, Tag-3",
        )
        self.opt = ListAndSearchFileRequestOptions(
            type="file",
            sort="ASC_CREATED",
            path="/",
            search_query="created_at >= '2d' OR size < '2mb' OR format='png'",
            file_type="all",
            limit=1,
            skip=0,
            tags=["Tag-1", "Tag-2", "Tag-3"],
        )
        self.client = ImageKit(
            public_key="fake122",
            private_key=ClientTestCase.private_key,
            url_endpoint="fake122",
        )


def create_headers_for_test():
    headers = {"Accept-Encoding": "gzip, deflate"}
    headers.update(get_auth_headers_for_test())
    return headers


def get_auth_headers_for_test():
    encoded_private_key = base64.b64encode(
        (ClientTestCase.private_key + ":").encode()
    ).decode("utf-8")
    return {"Authorization": "Basic {}".format(encoded_private_key)}
