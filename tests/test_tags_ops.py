import json
import os

import responses

from imagekitio.client import ImageKit
from imagekitio.constants.url import URL
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.utils.formatter import camel_dict_to_snake_dict
from tests.helpers import (
    ClientTestCase,
    get_auth_headers_for_test,
)

imagekit_obj = ImageKit(
    private_key="private_fake:",
    public_key="public_fake123:",
    url_endpoint="fake.com",
)


class TestTags(ClientTestCase):
    """
    TestTags class used to test Add and Remove methods
    """

    filename = "test"

    file_id = "fake_123"

    @responses.activate
    def test_add_tags_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/addTags".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.add_tags(
                file_ids=[self.file_id], tags=["add-tag-1", "add-tag-2"]
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_add_tags_succeeds(self):
        """
        Tests if add tags succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/addTags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.POST,
            url,
            body='{"successfullyUpdatedFileIds": ["fake_123"]}',
            headers=headers,
        )

        resp = self.client.add_tags(
            file_ids=[self.file_id], tags=["add-tag-1", "add-tag-2"]
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {"successfullyUpdatedFileIds": ["fake_123"]},
        }
        request_body = json.dumps(
            json.loads(
                """{
                "fileIds": ["fake_123"],
                "tags": ["add-tag-1", "add-tag-2"]
            }"""
            )
        )
        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(["fake_123"], resp.successfully_updated_file_ids)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/addTags", responses.calls[0].request.url
        )

    @responses.activate
    def test_add_tags_fails_with_404_exception(self) -> None:
        """Test add tags raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/addTags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.POST,
                url,
                status=404,
                body="""{
                    "message": "The requested file(s) does not exist.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "missingFileIds": ["fake_123"]
                }""",
                headers=headers,
            )
            self.client.add_tags(
                file_ids=[self.file_id], tags=["add-tag-1", "add-tag-2"]
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file(s) does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual(["fake_123"], e.response_metadata.raw["missingFileIds"])

    @responses.activate
    def test_remove_tags_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/removeTags".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.remove_tags(
                file_ids=[self.file_id], tags=["remove-tag-1", "remove-tag-2"]
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual("Your account cannot be authenticated.", e.message)
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_remove_tags_succeeds(self):
        """
        Tests if remove tags succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/removeTags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.POST,
            url,
            body='{"successfullyUpdatedFileIds": ["fake_123"]}',
            headers=headers,
        )

        resp = self.client.remove_tags(
            file_ids=[self.file_id], tags=["remove-tag-1", "remove-tag-2"]
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {"successfullyUpdatedFileIds": ["fake_123"]},
        }
        request_body = json.dumps(
            json.loads(
                """{
                "fileIds": ["fake_123"],
                "tags": ["remove-tag-1", "remove-tag-2"]
            }"""
            )
        )
        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(["fake_123"], resp.successfully_updated_file_ids)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/removeTags", responses.calls[0].request.url
        )

    @responses.activate
    def test_remove_tags_fails_with_404_exception(self) -> None:
        """Test remove tags raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/removeTags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.POST,
                url,
                status=404,
                body="""{
                    "message": "The requested file(s) does not exist.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "missingFileIds": ["fake_123"]
                }""",
                headers=headers,
            )
            self.client.remove_tags(
                file_ids=[self.file_id], tags=["remove-tag-1", "remove-tag-2"]
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file(s) does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual(["fake_123"], e.response_metadata.raw["missingFileIds"])


class TestAITags(ClientTestCase):
    """
    TestAITags class used to test Remove AITags method
    """

    image = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "dummy_data/image.png"
    )
    filename = "test"

    file_id = "fake_123"

    @responses.activate
    def test_remove_ai_tags_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/removeAITags".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.remove_ai_tags(
                file_ids=[self.file_id], ai_tags=["remove-ai-tag1", "remove-ai-tag2"]
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_remove_ai_tags_succeeds(self):
        """
        Tests if Remove AI tags succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/removeAITags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.POST,
            url,
            body='{"successfullyUpdatedFileIds": ["fake_123"]}',
            headers=headers,
        )

        resp = self.client.remove_ai_tags(
            file_ids=[self.file_id], ai_tags=["remove-ai-tag-1", "remove-ai-tag-2"]
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {"successfullyUpdatedFileIds": ["fake_123"]},
        }
        request_body = json.dumps(
            json.loads(
                """{
                "fileIds": ["fake_123"],
                "AITags": ["remove-ai-tag-1", "remove-ai-tag-2"]
            }"""
            )
        )
        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(["fake_123"], resp.successfully_updated_file_ids)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/removeAITags", responses.calls[0].request.url
        )

    @responses.activate
    def test_remove_ai_tags_fails_with_404_exception(self) -> None:
        """Test Remove AI tags raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/removeAITags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.POST,
                url,
                status=404,
                body="""{
                    "message": "The requested file(s) does not exist.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "missingFileIds": ["fake_123"]
                }""",
                headers=headers,
            )
            self.client.remove_ai_tags(
                file_ids=[self.file_id], ai_tags=["remove-ai-tag-1", "remove-ai-tag-2"]
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file(s) does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual(["fake_123"], e.response_metadata.raw["missingFileIds"])
