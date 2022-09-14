import json

import responses

from imagekitio import ImageKit
from imagekitio.constants.url import URL
from imagekitio.exceptions.BadRequestException import BadRequestException
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.InternalServerException import InternalServerException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.exceptions.UnknownException import UnknownException
from imagekitio.models.CopyFolderRequestOptions import CopyFolderRequestOptions
from imagekitio.models.CreateFolderRequestOptions import CreateFolderRequestOptions
from imagekitio.models.DeleteFolderRequestOptions import DeleteFolderRequestOptions
from imagekitio.models.MoveFolderRequestOptions import MoveFolderRequestOptions
from imagekitio.utils.formatter import camel_dict_to_snake_dict
from tests.helpers import (
    ClientTestCase,
    create_headers_for_test,
)

imagekit_obj = ImageKit(
    private_key="private_fake:",
    public_key="public_fake123:",
    url_endpoint="fake.com",
)


class TestFolders(ClientTestCase):
    """
    TestFolders class used to test create and Delete folders
    """

    @responses.activate
    def test_create_folder_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.create_folder(
                options=CreateFolderRequestOptions(
                    folder_name="folder_name", parent_folder_path="/test"
                )
            )
            self.assertRaises(ForbiddenException)
        except UnknownException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata.http_status_code, 403)

    @responses.activate
    def test_create_folder_succeeds(self):
        """
        Tests if create_folder succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        headers = create_headers_for_test()
        responses.add(responses.POST, url, status=201, body="{}", headers=headers)
        resp = self.client.create_folder(
            options=CreateFolderRequestOptions(
                folder_name="folder_name", parent_folder_path="/test"
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 201,
            "raw": {},
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("http://test.com/v1/folder", responses.calls[0].request.url)
        self.assertEqual(
            '{"folderName": "folder_name", "parentFolderPath": "/test"}',
            responses.calls[0].request.body,
        )

    @responses.activate
    def test_create_folder_fails_with_400(self):
        """
        Tests if create folder fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body="""{"message": "folderName parameter cannot have a slash.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.create_folder(
                options=CreateFolderRequestOptions(
                    folder_name="folder_name", parent_folder_path="/test"
                )
            )
            self.assertRaises(BadRequestException)
        except UnknownException as e:
            self.assertEqual(e.message, "folderName parameter cannot have a slash.")
            self.assertEqual(e.response_metadata.http_status_code, 400)

    @responses.activate
    def test_delete_folder_fails_with_400(self):
        """
        Tests if Delete folder fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.DELETE,
                url,
                status=404,
                body="""{
                    "message": "No folder found with folderPath test",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "reason": "FOLDER_NOT_FOUND"
                }""",
            )
            self.client.delete_folder(
                options=DeleteFolderRequestOptions(folder_path="/test")
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No folder found with folderPath test", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual("FOLDER_NOT_FOUND", e.response_metadata.raw["reason"])

    @responses.activate
    def test_delete_folder_succeeds(self):
        """
        Tests if Delete folder succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        responses.add(
            responses.DELETE,
            url,
            status=204,
            body="{}",
        )
        resp = self.client.delete_folder(
            options=DeleteFolderRequestOptions(folder_path="/folderName")
        )
        mock_response_metadata = {
            "raw": None,
            "httpStatusCode": 204,
            "headers": {"Content-Type": "text/plain"},
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("http://test.com/v1/folder", responses.calls[0].request.url)
        self.assertEqual('{"folderPath": "/folderName"}', responses.calls[0].request.body)


class TestCopyFolder(ClientTestCase):
    """
    TestCopyFolder class used to test copy folder
    """

    @responses.activate
    def test_copy_folder_fails_with_400(self):
        """
        Tests if Copy folder fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/copyFolder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body="""{
                    "message": "sourceFolderPath and destinationPath cannot be same.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
            )
            self.client.copy_folder(
                options=CopyFolderRequestOptions(
                    source_folder_path="/test",
                    destination_path="/test",
                    include_file_versions=False,
                )
            )
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "sourceFolderPath and destinationPath cannot be same.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_copy_folder_fails_with_404(self):
        """
        Tests if Copy folder fails with 404
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/copyFolder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=404,
                body="""{
                    "message": "No files & folder found at sourceFolderPath /test",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "reason": "NO_FILES_FOLDER"
                }""",
            )
            self.client.copy_folder(
                options=CopyFolderRequestOptions(
                    source_folder_path="/test",
                    destination_path="/test1",
                    include_file_versions=False,
                )
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual(
                "No files & folder found at sourceFolderPath /test", e.message
            )
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual("NO_FILES_FOLDER", e.response_metadata.raw["reason"])

    @responses.activate
    def test_copy_folder_succeeds(self):
        """
        Tests if Copy folder succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/copyFolder".format(URL.API_BASE_URL)
        responses.add(
            responses.POST,
            url,
            body='{"jobId": "62de84fb1b02a58936cc740c"}',
        )
        resp = self.client.copy_folder(
            options=CopyFolderRequestOptions(
                source_folder_path="/test",
                destination_path="/test1",
                include_file_versions=True,
            )
        )
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {"jobId": "62de84fb1b02a58936cc740c"},
        }
        request_body = json.dumps(
            json.loads(
                """{
                "sourceFolderPath": "/test",
                "destinationPath": "/test1",
                "includeFileVersions": true
            }"""
            )
        )
        self.assertEqual("62de84fb1b02a58936cc740c", resp.job_id)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/bulkJobs/copyFolder", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_copy_folder_succeeds_with_include_file_versions_false(self):
        """
        Tests if Copy folder succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/copyFolder".format(URL.API_BASE_URL)
        responses.add(
            responses.POST,
            url,
            body='{"jobId": "62de84fb1b02a58936cc740c"}',
        )
        resp = self.client.copy_folder(
            options=CopyFolderRequestOptions(
                source_folder_path="/test",
                destination_path="/test1",
                include_file_versions=False,
            )
        )
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {"jobId": "62de84fb1b02a58936cc740c"},
        }
        request_body = json.dumps(
            json.loads(
                """{
                "sourceFolderPath": "/test",
                "destinationPath": "/test1",
                "includeFileVersions": false
            }"""
            )
        )
        self.assertEqual("62de84fb1b02a58936cc740c", resp.job_id)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/bulkJobs/copyFolder", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_copy_folder_succeeds_without_include_file_versions(self):
        """
        Tests if Copy folder succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/copyFolder".format(URL.API_BASE_URL)
        responses.add(
            responses.POST,
            url,
            body='{"jobId": "62de84fb1b02a58936cc740c"}',
        )
        resp = self.client.copy_folder(
            options=CopyFolderRequestOptions(
                source_folder_path="/test",
                destination_path="/test1",
            )
        )
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {"jobId": "62de84fb1b02a58936cc740c"},
        }
        request_body = json.dumps(
            json.loads(
                """{
                "sourceFolderPath": "/test",
                "destinationPath": "/test1"
            }"""
            )
        )
        self.assertEqual("62de84fb1b02a58936cc740c", resp.job_id)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/bulkJobs/copyFolder", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)


class TestMoveFolder(ClientTestCase):
    """
    TestMoveFolder class used to test move folder
    """

    @responses.activate
    def test_move_folder_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/moveFolder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.move_folder(
                options=MoveFolderRequestOptions(
                    source_folder_path="/test", destination_path="/test1"
                )
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_move_folder_fails_with_400(self):
        """
        Tests if Move folder fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/moveFolder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body="""{
                    "message": "sourceFolderPath and destinationPath cannot be same.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
            )
            self.client.move_folder(
                options=MoveFolderRequestOptions(
                    source_folder_path="/test", destination_path="/test"
                )
            )
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "sourceFolderPath and destinationPath cannot be same.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_move_folder_fails_with_404(self):
        """
        Tests if Move folder fails with 404
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/moveFolder".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=404,
                body="""{
                    "message": "No files & folder found at sourceFolderPath /test",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "reason": "NO_FILES_FOLDER"
                }""",
            )
            self.client.move_folder(
                options=MoveFolderRequestOptions(
                    source_folder_path="/test", destination_path="/test1"
                )
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual(
                "No files & folder found at sourceFolderPath /test", e.message
            )
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual("NO_FILES_FOLDER", e.response_metadata.raw["reason"])

    @responses.activate
    def test_move_folder_succeeds(self):
        """
        Tests if Move folder succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/moveFolder".format(URL.API_BASE_URL)
        responses.add(
            responses.POST,
            url,
            body='{"jobId": "62de84fb1b02a58936cc740c"}',
        )
        resp = self.client.move_folder(
            options=MoveFolderRequestOptions(
                source_folder_path="/test", destination_path="/test1"
            )
        )
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {"jobId": "62de84fb1b02a58936cc740c"},
        }
        request_body = json.dumps(
            json.loads(
                """{
                "sourceFolderPath": "/test",
                "destinationPath": "/test1"
            }"""
            )
        )
        self.assertEqual("62de84fb1b02a58936cc740c", resp.job_id)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/bulkJobs/moveFolder", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)


class TestGetBulkJobStatus(ClientTestCase):
    """
    TestGetBulkJobStatus class used to get bulk job status
    """

    job_id = "mock_job_id"

    @responses.activate
    def test_get_bulk_job_status_fails_with_500(self):
        """
        Tests if get_bulk_job_status succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/{}".format(URL.API_BASE_URL, self.job_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=500,
                body="""{"message": "We have experienced an internal error while processing your request.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_bulk_job_status(self.job_id)
            self.assertRaises(InternalServerException)
        except InternalServerException as e:
            self.assertEqual(
                "We have experienced an internal error while processing your request.",
                e.message,
            )
            self.assertEqual(500, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_bulk_job_status_succeeds(self):
        """
        Tests if get_bulk_job_status succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/bulkJobs/{}".format(URL.API_BASE_URL, self.job_id)
        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""{
                "jobId": "mock_job_id",
                "type": "COPY_FOLDER",
                "status": "Completed"
            }""",
            headers=headers,
        )
        resp = self.client.get_bulk_job_status(self.job_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {
                "jobId": "mock_job_id",
                "status": "Completed",
                "type": "COPY_FOLDER",
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("mock_job_id", resp.job_id)
        self.assertEqual("Completed", resp.status)
        self.assertEqual("COPY_FOLDER", resp.type)
        self.assertEqual(
            "http://test.com/v1/bulkJobs/mock_job_id", responses.calls[0].request.url
        )
