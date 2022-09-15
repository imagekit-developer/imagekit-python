import base64
import json
import os

import responses
from responses import matchers

from imagekitio.client import ImageKit
from imagekitio.constants.url import URL
from imagekitio.exceptions.BadRequestException import BadRequestException
from imagekitio.exceptions.ConflictException import ConflictException
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.exceptions.UnknownException import UnknownException
from imagekitio.models.CopyFileRequestOptions import CopyFileRequestOptions
from imagekitio.models.MoveFileRequestOptions import MoveFileRequestOptions
from imagekitio.models.RenameFileRequestOptions import RenameFileRequestOptions
from imagekitio.models.UpdateFileRequestOptions import UpdateFileRequestOptions
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions
from imagekitio.utils.formatter import camel_dict_to_snake_dict
from tests.helpers import (
    ClientTestCase,
    create_headers_for_test,
    get_auth_headers_for_test,
)

imagekit_obj = ImageKit(
    private_key="private_fake:",
    public_key="public_fake123:",
    url_endpoint="fake.com",
)


class TestUpload(ClientTestCase):
    """
    TestUpload class used to test upload method
    """

    image = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "dummy_data/image.png"
    )

    sample_image = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "sample.jpg"
    )
    filename = "test"

    @responses.activate
    def test_upload_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{"message": "Your account cannot be authenticated."
                                    , "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.upload_file(
                file=self.image,
                file_name=self.filename,
                options=UploadFileRequestOptions(
                    use_unique_file_name=False,
                    tags=["abc", "def"],
                    folder="/testing-python-folder/",
                    is_private_file=False,
                    custom_coordinates="10,10,20,20",
                    response_fields=[
                        "tags",
                        "custom_coordinates",
                        "is_private_file",
                        "embedded_metadata",
                        "custom_metadata",
                    ],
                    extensions=(
                        {
                            "name": "remove-bg",
                            "options": {"add_shadow": True, "bg_color": "pink"},
                        },
                        {
                            "name": "google-auto-tagging",
                            "minConfidence": 80,
                            "maxTags": 10,
                        },
                    ),
                    webhook_url="https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
                    overwrite_file=True,
                    overwrite_ai_tags=False,
                    overwrite_tags=False,
                    overwrite_custom_metadata=True,
                    custom_metadata={"testss": 12},
                ),
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata.http_status_code, 403)

    @responses.activate
    def test_binary_upload_succeeds(self):
        """
        Tests if  upload succeeds
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        headers = create_headers_for_test()
        responses.add(
            responses.POST,
            url,
            body="""{
                        "fileId": "fake_file_id1234",
                        "name": "file_name.jpg",
                        "size": 102117,
                        "versionInfo": {
                            "id": "62d670648cdb697522602b45",
                            "name": "Version 11"
                        },
                        "filePath": "/testing-python-folder/file_name.jpg",
                        "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                        "fileType": "image",
                        "height": 700,
                        "width": 1050,
                        "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                        "tags": [
                            "abc",
                            "def"
                        ],
                        "AITags": [
                            {
                                "name": "Computer",
                                "confidence": 97.66,
                                "source": "google-auto-tagging"
                            },
                            {
                                "name": "Personal computer",
                                "confidence": 94.96,
                                "source": "google-auto-tagging"
                            }
                        ],
                        "isPrivateFile": true,
                        "extensionStatus": {
                            "remove-bg": "pending",
                            "google-auto-tagging": "success"
                        }
                    }""",
            headers=headers,
        )

        with open(self.sample_image, mode="rb") as img:
            imgstr = base64.b64encode(img.read())
        resp = self.client.upload_file(
            file=imgstr,
            file_name="file_name.jpg",
            options=UploadFileRequestOptions(
                use_unique_file_name=False,
                tags=["abc", "def"],
                folder="/testing-python-folder/",
                is_private_file=True,
                response_fields=["is_private_file", "tags"],
                extensions=(
                    {
                        "name": "remove-bg",
                        "options": {"add_shadow": True, "bg_color": "pink"},
                    },
                    {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10},
                ),
                webhook_url="url",
                overwrite_file=True,
                overwrite_ai_tags=False,
                overwrite_tags=False,
                overwrite_custom_metadata=True,
                custom_metadata={"test100": 11},
            ),
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [
                    {
                        "confidence": 97.66,
                        "name": "Computer",
                        "source": "google-auto-tagging",
                    },
                    {
                        "confidence": 94.96,
                        "name": "Personal computer",
                        "source": "google-auto-tagging",
                    },
                ],
                "extensionStatus": {
                    "google-auto-tagging": "success",
                    "remove-bg": "pending",
                },
                "fileId": "fake_file_id1234",
                "filePath": "/testing-python-folder/file_name.jpg",
                "fileType": "image",
                "height": 700,
                "isPrivateFile": True,
                "name": "file_name.jpg",
                "size": 102117,
                "tags": ["abc", "def"],
                "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                "versionInfo": {"id": "62d670648cdb697522602b45", "name": "Version 11"},
                "width": 1050,
            },
        }
        request_body = b'----randomBoundary---------------------\r\nContent-Disposition: form-data; name="file"\r\n\r\n <BINARY FILE DATA>  \r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="fileName"\r\n\r\nfile_name.jpg\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="useUniqueFileName"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="tags"\r\n\r\nabc,def\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="folder"\r\n\r\n/testing-python-folder/\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="isPrivateFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="responseFields"\r\n\r\nisPrivateFile,tags\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="extensions"\r\n\r\n[{"name": "remove-bg", "options": {"add_shadow": true, "bg_color": "pink"}}, {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10}]\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="webhookUrl"\r\n\r\nurl\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteTags"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteCustomMetadata"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="customMetadata"\r\n\r\n{"test100": 11}\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteAITags"\r\n\r\nfalse\r\n----randomBoundary-----------------------\r\n'
        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(url, responses.calls[0].request.url)

    @responses.activate
    def test_upload_succeeds_with_url(self):
        """
        Tests if  upload succeeds
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        headers = create_headers_for_test()
        responses.add(
            responses.POST,
            url,
            body="""{
                        "fileId": "fake_file_id1234",
                        "name": "file_name.jpg",
                        "size": 102117,
                        "versionInfo": {
                            "id": "62d670648cdb697522602b45",
                            "name": "Version 11"
                        },
                        "filePath": "/testing-python-folder/file_name.jpg",
                        "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                        "fileType": "image",
                        "height": 700,
                        "width": 1050,
                        "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                        "tags": [
                            "abc",
                            "def"
                        ],
                        "AITags": [
                            {
                                "name": "Computer",
                                "confidence": 97.66,
                                "source": "google-auto-tagging"
                            },
                            {
                                "name": "Personal computer",
                                "confidence": 94.96,
                                "source": "google-auto-tagging"
                            }
                        ],
                        "isPrivateFile": true,
                        "extensionStatus": {
                            "remove-bg": "pending",
                            "google-auto-tagging": "success"
                        }
                    }""",
            headers=headers,
        )

        file_upload_url = "https://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg"
        resp = self.client.upload_file(
            file=file_upload_url,
            file_name="file_name.jpg",
            options=UploadFileRequestOptions(
                use_unique_file_name=False,
                tags=["abc", "def"],
                folder="/testing-python-folder/",
                is_private_file=True,
                response_fields=["is_private_file", "tags"],
                extensions=(
                    {
                        "name": "remove-bg",
                        "options": {"add_shadow": True, "bg_color": "pink"},
                    },
                    {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10},
                ),
                webhook_url="url",
                overwrite_file=True,
                overwrite_ai_tags=False,
                overwrite_tags=False,
                overwrite_custom_metadata=True,
                custom_metadata={"test100": 11},
            ),
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [
                    {
                        "confidence": 97.66,
                        "name": "Computer",
                        "source": "google-auto-tagging",
                    },
                    {
                        "confidence": 94.96,
                        "name": "Personal computer",
                        "source": "google-auto-tagging",
                    },
                ],
                "extensionStatus": {
                    "google-auto-tagging": "success",
                    "remove-bg": "pending",
                },
                "fileId": "fake_file_id1234",
                "filePath": "/testing-python-folder/file_name.jpg",
                "fileType": "image",
                "height": 700,
                "isPrivateFile": True,
                "name": "file_name.jpg",
                "size": 102117,
                "tags": ["abc", "def"],
                "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg",
                "url": "https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg",
                "versionInfo": {"id": "62d670648cdb697522602b45", "name": "Version 11"},
                "width": 1050,
            },
        }
        request_body = b'----randomBoundary---------------------\r\nContent-Disposition: form-data; name="file"\r\n\r\nhttps://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="fileName"\r\n\r\nfile_name.jpg\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="useUniqueFileName"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="tags"\r\n\r\nabc,def\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="folder"\r\n\r\n/testing-python-folder/\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="isPrivateFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="responseFields"\r\n\r\nisPrivateFile,tags\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="extensions"\r\n\r\n[{"name": "remove-bg", "options": {"add_shadow": true, "bg_color": "pink"}}, {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10}]\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="webhookUrl"\r\n\r\nurl\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteFile"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteTags"\r\n\r\nfalse\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteCustomMetadata"\r\n\r\ntrue\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="customMetadata"\r\n\r\n{"test100": 11}\r\n----randomBoundary---------------------\r\nContent-Disposition: form-data; name="overwriteAITags"\r\n\r\nfalse\r\n----randomBoundary-----------------------\r\n'

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(url, responses.calls[0].request.url)

    def test_upload_fails_without_file_name(self) -> None:
        """Test upload raises error on missing required params"""
        try:
            with open(self.sample_image, mode="rb") as img:
                imgstr = base64.b64encode(img.read())
            self.client.upload_file(file=imgstr)
        except TypeError as e:
            self.assertEqual(
                {"message": "Missing fileName parameter for upload", "help": ""},
                e.args[0],
            )

    def test_upload_fails_without_file(self) -> None:
        """Test upload raises error on missing required params"""
        try:
            self.client.upload_file(file_name="file_name.jpg")
        except TypeError as e:
            self.assertEqual(
                {"message": "Missing file parameter for upload", "help": ""}, e.args[0]
            )

    @responses.activate
    def test_upload_fails_with_400_exception(self) -> None:
        """Test upload raises 400 error"""

        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body="""{
                        "message": "A file with the same name already exists at the exact location. We "
                        "could not overwrite it because both overwriteFile and "
                        "useUniqueFileName are set to false."
                    }""",
            )
            self.client.upload_file(
                file=self.image,
                file_name=self.filename,
                options=UploadFileRequestOptions(
                    use_unique_file_name=False,
                    tags=["abc", "def"],
                    folder="/testing-python-folder/",
                    is_private_file=False,
                    custom_coordinates="10,10,20,20",
                    response_fields=[
                        "tags",
                        "custom_coordinates",
                        "is_private_file",
                        "embedded_metadata",
                        "custom_metadata",
                    ],
                    extensions=(
                        {
                            "name": "remove-bg",
                            "options": {"add_shadow": True, "bg_color": "pink"},
                        },
                        {
                            "name": "google-auto-tagging",
                            "minConfidence": 80,
                            "maxTags": 10,
                        },
                    ),
                    webhook_url="https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
                    overwrite_file=True,
                    overwrite_ai_tags=False,
                    overwrite_tags=False,
                    overwrite_custom_metadata=True,
                    custom_metadata={"testss": 12},
                ),
            )
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "A file with the same name already exists at the exact location. We could not overwrite "
                "it because both overwriteFile and useUniqueFileName are set to false.",
                e.message,
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestListFiles(ClientTestCase):
    """
    TestListFiles class used to test list_files method
    """

    @responses.activate
    def test_list_files_fails_on_unauthenticated_request(self) -> None:
        """Tests unauthenticated request restricted for list_files method"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.list_files(self.options)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual("Your account cannot be authenticated.", e.message)
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_list_files_succeeds_with_basic_request_tags_with_array(self) -> None:
        """
        Tests if list_files work with options which contains type, sort, path, searchQuery, fileType, limit, skip and tags
        """

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""[{
                "type": "file",
                "name": "sample-cat-image_gr64HPlJS.jpg",
                "createdAt": "2022-06-15T08:19:00.843Z",
                "updatedAt": "2022-06-15T08:19:45.169Z",
                "fileId": "62a995f4d875ec08dc587b72",
                "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                "AITags": "",
                "versionInfo": {
                    "id": "62a995f4d875ec08dc587b72",
                    "name": "Version 1"
                },
                "embeddedMetadata": {
                    "XResolution": 250,
                    "YResolution": 250,
                    "DateCreated": "2022-06-15T08:19:01.523Z",
                    "DateTimeCreated": "2022-06-15T08:19:01.524Z"
                },
                "customCoordinates": "10,10,20,20",
                "customMetadata": {
                    "test100": 10
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                "fileType": "image",
                "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }]""",
            headers=headers,
            match=[
                matchers.query_string_matcher(
                    "%7B%22type%22:%20%22file%22,%20%22sort%22:%20%22ASC_CREATED%22,%20%22path%22:%20%22/%22,%20%22searchQuery%22:%20%22created_at%20%3E=%20'2d'%20OR%20size%20%3C%20'2mb'%20OR%20format='png'%22,%20%22fileType%22:%20%22all%22,%20%22limit%22:%201,%20%22skip%22:%200,%20%22tags%22:%20%22Tag-1,%20Tag-2,%20Tag-3%22%7D"
                )
            ],
        )

        resp = self.client.list_files(self.opt)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": [
                {
                    "AITags": "",
                    "createdAt": "2022-06-15T08:19:00.843Z",
                    "customCoordinates": "10,10,20,20",
                    "customMetadata": {"test100": 10},
                    "embeddedMetadata": {
                        "DateCreated": "2022-06-15T08:19:01.523Z",
                        "DateTimeCreated": "2022-06-15T08:19:01.524Z",
                        "XResolution": 250,
                        "YResolution": 250,
                    },
                    "fileId": "62a995f4d875ec08dc587b72",
                    "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                    "fileType": "image",
                    "hasAlpha": False,
                    "height": 354,
                    "isPrivateFile": False,
                    "mime": "image/jpeg",
                    "name": "sample-cat-image_gr64HPlJS.jpg",
                    "size": 23023,
                    "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                    "type": "file",
                    "updatedAt": "2022-06-15T08:19:45.169Z",
                    "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                    "versionInfo": {
                        "id": "62a995f4d875ec08dc587b72",
                        "name": "Version " "1",
                    },
                    "width": 236,
                }
            ],
        }
        self.assertEqual(
            "http://test.com/v1/files?%7B%22type%22:%20%22file%22,%20%22sort%22:%20%22ASC_CREATED%22,%20%22path%22:%20%22/%22,%20%22searchQuery%22:%20%22created_at%20%3E=%20'2d'%20OR%20size%20%3C%20'2mb'%20OR%20format='png'%22,%20%22fileType%22:%20%22all%22,%20%22limit%22:%201,%20%22skip%22:%200,%20%22tags%22:%20%22Tag-1,%20Tag-2,%20Tag-3%22%7D",
            responses.calls[0].request.url,
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )

    @responses.activate
    def test_list_files_succeeds_with_basic_request(self) -> None:
        """
        Tests if list_files work with options which contains type, sort, path, searchQuery, fileType, limit, skip and tags
        """

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""[{
                "type": "file",
                "name": "sample-cat-image_gr64HPlJS.jpg",
                "createdAt": "2022-06-15T08:19:00.843Z",
                "updatedAt": "2022-06-15T08:19:45.169Z",
                "fileId": "62a995f4d875ec08dc587b72",
                "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                "AITags": "",
                "versionInfo": {
                    "id": "62a995f4d875ec08dc587b72",
                    "name": "Version 1"
                },
                "embeddedMetadata": {
                    "XResolution": 250,
                    "YResolution": 250,
                    "DateCreated": "2022-06-15T08:19:01.523Z",
                    "DateTimeCreated": "2022-06-15T08:19:01.524Z"
                },
                "customCoordinates": "10,10,20,20",
                "customMetadata": {
                    "test100": 10
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                "fileType": "image",
                "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }]""",
            headers=headers,
            match=[
                matchers.query_string_matcher(
                    "%7B%22type%22:%20%22file%22,%20%22sort%22:%20%22ASC_CREATED%22,%20%22path%22:%20%22/%22,%20%22searchQuery%22:%20%22created_at%20%3E=%20'2d'%20OR%20size%20%3C%20'2mb'%20OR%20format='png'%22,%20%22fileType%22:%20%22all%22,%20%22limit%22:%201,%20%22skip%22:%200,%20%22tags%22:%20%22Tag-1,%20Tag-2,%20Tag-3%22%7D"
                )
            ],
        )

        resp = self.client.list_files(self.options)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": [
                {
                    "AITags": "",
                    "createdAt": "2022-06-15T08:19:00.843Z",
                    "customCoordinates": "10,10,20,20",
                    "customMetadata": {"test100": 10},
                    "embeddedMetadata": {
                        "DateCreated": "2022-06-15T08:19:01.523Z",
                        "DateTimeCreated": "2022-06-15T08:19:01.524Z",
                        "XResolution": 250,
                        "YResolution": 250,
                    },
                    "fileId": "62a995f4d875ec08dc587b72",
                    "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                    "fileType": "image",
                    "hasAlpha": False,
                    "height": 354,
                    "isPrivateFile": False,
                    "mime": "image/jpeg",
                    "name": "sample-cat-image_gr64HPlJS.jpg",
                    "size": 23023,
                    "tags": ["Tag_1", " Tag_2", " Tag_3", "tag-to-add-2"],
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                    "type": "file",
                    "updatedAt": "2022-06-15T08:19:45.169Z",
                    "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                    "versionInfo": {
                        "id": "62a995f4d875ec08dc587b72",
                        "name": "Version " "1",
                    },
                    "width": 236,
                }
            ],
        }
        self.assertEqual(
            "http://test.com/v1/files?%7B%22type%22:%20%22file%22,%20%22sort%22:%20%22ASC_CREATED%22,%20%22path%22:%20%22/%22,%20%22searchQuery%22:%20%22created_at%20%3E=%20'2d'%20OR%20size%20%3C%20'2mb'%20OR%20format='png'%22,%20%22fileType%22:%20%22all%22,%20%22limit%22:%201,%20%22skip%22:%200,%20%22tags%22:%20%22Tag-1,%20Tag-2,%20Tag-3%22%7D",
            responses.calls[0].request.url,
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )

    @responses.activate
    def test_list_files_fails_with_400_exception(self) -> None:
        """Test get list of files raises 400 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Invalid search query - createdAt field must have a valid date value. Make "
                                            "sure the value is enclosed within quotes. Please refer to the "
                                            "documentation for syntax specification.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
                match=[
                    matchers.query_string_matcher(
                        "%7B%22type%22:%20%22file%22,%20%22sort%22:%20%22ASC_CREATED%22,%20%22path%22:%20%22/%22,%20%22searchQuery%22:%20%22created_at%20%3E=%20'2d'%20OR%20size%20%3C%20'2mb'%20OR%20format='png'%22,%20%22fileType%22:%20%22all%22,%20%22limit%22:%201,%20%22skip%22:%200,%20%22tags%22:%20%22Tag-1,%20Tag-2,%20Tag-3%22%7D"
                    )
                ],
            )
            self.client.list_files(self.options)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Invalid search query - createdAt field must have a valid date value. Make "
                "sure the value is enclosed within quotes. Please refer to the "
                "documentation for syntax specification.",
                e.message,
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestGetFileDetails(ClientTestCase):
    """
    TestGetFileDetails class used to test get_file_details method
    """

    file_id = "fake_file_id1234"
    file_url = "https://example.com/default.jpg"

    @responses.activate
    def test_get_file_details_fails_on_unauthenticated_request(self) -> None:
        """Tests of get_file_details raise error on unauthenticated request"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.get_file_details(self.file_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_file_details_succeeds_with_id(self) -> None:
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""{
                        "type": "file",
                        "name": "default-image.jpg",
                        "createdAt": "2022-06-15T08:19:00.843Z",
                        "updatedAt": "2022-08-19T12:19:22.726Z",
                        "fileId": "fake_file_id1234",
                        "tags": [
                            "{Software",
                            " Developer",
                            " Engineer}",
                            "tag-to-add-2"
                        ],
                        "AITags": null,
                        "versionInfo": {
                            "id": "62a995f4d875ec08dc587b72",
                            "name": "Version 1"
                        },
                        "embeddedMetadata": {
                            "XResolution": 250,
                            "YResolution": 250,
                            "DateCreated": "2022-06-15T08:19:01.523Z",
                            "DateTimeCreated": "2022-06-15T08:19:01.524Z"
                        },
                        "customCoordinates": "10,10,20,20",
                        "customMetadata": {
                            "test100": 10
                        },
                        "isPrivateFile": false,
                        "url": "https://ik.imagekit.io/xyxt2lnil/default-image.jpg",
                        "thumbnail": "https://ik.imagekit.io/xyxt2lnil/tr:n-ik_ml_thumbnail/default-image.jpg",
                        "fileType": "image",
                        "filePath": "/default-image.jpg",
                        "height": 354,
                        "width": 236,
                        "size": 23023,
                        "hasAlpha": false,
                        "mime": "image/jpeg"
                    }""",
            headers=headers,
        )
        resp = self.client.get_file_details(self.file_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": None,
                "createdAt": "2022-06-15T08:19:00.843Z",
                "customCoordinates": "10,10,20,20",
                "customMetadata": {"test100": 10},
                "embeddedMetadata": {
                    "DateCreated": "2022-06-15T08:19:01.523Z",
                    "DateTimeCreated": "2022-06-15T08:19:01.524Z",
                    "XResolution": 250,
                    "YResolution": 250,
                },
                "fileId": "fake_file_id1234",
                "filePath": "/default-image.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 354,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "default-image.jpg",
                "size": 23023,
                "tags": ["{Software", " Developer", " Engineer}", "tag-to-add-2"],
                "thumbnail": "https://ik.imagekit.io/xyxt2lnil/tr:n-ik_ml_thumbnail/default-image.jpg",
                "type": "file",
                "updatedAt": "2022-08-19T12:19:22.726Z",
                "url": "https://ik.imagekit.io/xyxt2lnil/default-image.jpg",
                "versionInfo": {"id": "62a995f4d875ec08dc587b72", "name": "Version 1"},
                "width": 236,
            },
        }

        self.assertEqual(
            "http://test.com/v1/files/fake_file_id1234/details",
            responses.calls[0].request.url,
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_file_id1234", resp.file_id)

    @responses.activate
    def test_file_details_fails_with_400_exception(self) -> None:
        """Test get file details raises 400 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_details(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestDeleteFile(ClientTestCase):
    file_id = "fax_abx1223"
    bulk_delete_ids = ["fake_123", "fake_222"]

    @responses.activate
    def test_bulk_file_delete_fails_on_unauthenticated_request(self) -> None:
        """Test bulk_file_delete on unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if bulk_delete is only restricted to authenticated
        requests
        """

        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.bulk_file_delete(self.bulk_delete_ids)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata.http_status_code, 403)

    @responses.activate
    def test_bulk_file_delete_succeeds(self):
        """Test bulk_delete  on authenticated request
        this function tests if bulk_file_delete working properly
        """

        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())

        responses.add(
            responses.POST,
            url,
            body='{"successfullyDeletedFileIds": ["fake_123", "fake_222"]}',
            headers=headers,
        )

        resp = self.client.bulk_file_delete(self.bulk_delete_ids)

        mock_response_metadata = {
            "raw": {"successfullyDeletedFileIds": ["fake_123", "fake_222"]},
            "httpStatusCode": 200,
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }
        self.assertEqual(
            '{"fileIds": ["fake_123", "fake_222"]}', responses.calls[0].request.body
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(["fake_123", "fake_222"], resp.successfully_deleted_file_ids)
        self.assertEqual(
            "http://test.com/v1/files/batch/deleteByFileIds",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_bulk_file_delete_fails_with_404_exception(self) -> None:
        """Test bulk_file_delete raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
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
                    "missingFileIds": ["fake_123", "fake_222"]
                }""",
                headers=headers,
            )
            self.client.bulk_file_delete(self.bulk_delete_ids)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file(s) does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)
            self.assertEqual(
                ["fake_123", "fake_222"], e.response_metadata.raw["missingFileIds"]
            )

    @responses.activate
    def test_file_delete_fails_with_400_exception(self):
        """Test delete_file on unavailable content
        this function raising 400 if the file
        is not available
        """

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}".format(URL.API_BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.DELETE,
                url,
                status=400,
                body="""{
                    "message": "Your request contains invalid fileId parameter.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
                headers=headers,
            )
            self.client.delete_file(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_file_delete_succeeds(self):
        """Test delete file on authenticated request
        this function tests if delete_file working properly
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}".format(URL.API_BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())

        responses.add(responses.DELETE, url, body="{}", status=204, headers=headers)

        resp = self.client.delete_file(self.file_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/fax_abx1223", responses.calls[0].request.url
        )


class TestPurgeCache(ClientTestCase):
    fake_image_url = "https://example.com/fakeid/fakeimage.jpg"

    @responses.activate
    def test_purge_file_cache_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files/purge"
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.purge_file_cache(self.fake_image_url)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_purge_file_cache_fails_with_400(self):
        """
        Tests if the purge_file_cache fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files/purge"
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body='{"message": "Invalid url"}',
            )
            self.client.purge_file_cache("url")
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Invalid url", e.message)
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_purge_file_cache_succeeds(self):
        """
        Tests if purge_file_cache succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files/purge"
        responses.add(
            responses.POST,
            url,
            status=201,
            body='{"requestId": "requestId"}',
        )
        resp = self.client.purge_file_cache(self.fake_image_url)
        mock_response_metadata = {
            "raw": {"requestId": "requestId"},
            "httpStatusCode": 201,
            "headers": {"Content-Type": "text/plain"},
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("requestId", resp.request_id)
        self.assertEqual(
            "http://test.com/v1/files/purge", responses.calls[0].request.url
        )
        self.assertEqual(
            '{"url": "https://example.com/fakeid/fakeimage.jpg"}',
            responses.calls[0].request.body,
        )


class TestPurgeCacheStatus(ClientTestCase):
    cache_request_id = "fake1234"

    @responses.activate
    def test_purge_file_cache_status_fails_with_400(self):
        """
        Tests if the purge_file_cache_status fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/purge/{}".format(URL.API_BASE_URL, self.cache_request_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "No request found for this requestId.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_purge_file_cache_status(self.cache_request_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("No request found for this requestId.", e.message)
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_purge_file_cache_status_succeeds(self):
        """
        Tests if purge_file_cache_status succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/purge/{}".format(URL.API_BASE_URL, self.cache_request_id)
        responses.add(
            responses.GET,
            url,
            body="""{"status": "Completed"}""",
        )
        resp = self.client.get_purge_file_cache_status(self.cache_request_id)
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {"status": "Completed"},
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("Completed", resp.status)
        self.assertEqual(
            "http://test.com/v1/files/purge/fake1234", responses.calls[0].request.url
        )


class TestGetMetaData(ClientTestCase):
    file_id = "fake_file_xbc"

    fake_image_url = "https://example.com/fakeid/fakeimage.jpg"

    @responses.activate
    def test_get_file_metadata_fails_with_400(self):
        """
        Tests if the get_file_metadata fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/metadata".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io .",
                                 "type": "INVALID_PARAM_ERROR"}""",
            )
            self.client.get_file_metadata(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)
            self.assertEqual("INVALID_PARAM_ERROR", e.response_metadata.raw["type"])

    @responses.activate
    def test_get_file_metadata_succeeds(self):
        """
        Tests if get_file_metadata succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/metadata".format(URL.API_BASE_URL, self.file_id)
        responses.add(
            responses.GET,
            url,
            body="""{
                "height": 354,
                "width": 236,
                "size": 7390,
                "format": "jpg",
                "hasColorProfile": false,
                "quality": 0,
                "density": 250,
                "hasTransparency": false,
                "exif": {},
                "pHash": "2e0ed1f12eda9525"
            }""",
        )
        resp = self.client.get_file_metadata(self.file_id)
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {
                "density": 250,
                "exif": {},
                "format": "jpg",
                "hasColorProfile": False,
                "hasTransparency": False,
                "height": 354,
                "pHash": "2e0ed1f12eda9525",
                "quality": 0,
                "size": 7390,
                "width": 236,
            },
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/fake_file_xbc/metadata",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_get_remote_file_url_metadata_fails_with_400(self):
        """
        Tests if the get_remote_file_url_metadata fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/metadata".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{
                    "message": "https://example.com/fakeid/fakeimage.jpg should be accessible using your ImageKit.io account.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
                match=[
                    matchers.query_string_matcher(
                        "url=https://example.com/fakeid/fakeimage.jpg"
                    )
                ],
            )
            self.client.get_remote_file_url_metadata(self.fake_image_url)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "https://example.com/fakeid/fakeimage.jpg should be accessible using your ImageKit.io account.",
                e.message,
            )
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_remote_file_url_metadata_succeeds(self):
        """
        Tests if get_remote_file_url_metadata succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/metadata".format(URL.API_BASE_URL)
        responses.add(
            responses.GET,
            url,
            body="""{
                "height": 354,
                "width": 236,
                "size": 7390,
                "format": "jpg",
                "hasColorProfile": false,
                "quality": 0,
                "density": 250,
                "hasTransparency": false,
                "exif": {},
                "pHash": "2e0ed1f12eda9525"
            }""",
            match=[
                matchers.query_string_matcher(
                    "url=https://example.com/fakeid/fakeimage.jpg"
                )
            ],
        )
        resp = self.client.get_remote_file_url_metadata(self.fake_image_url)
        mock_response_metadata = {
            "headers": {"Content-Type": "text/plain"},
            "httpStatusCode": 200,
            "raw": {
                "density": 250,
                "exif": {},
                "format": "jpg",
                "hasColorProfile": False,
                "hasTransparency": False,
                "height": 354,
                "pHash": "2e0ed1f12eda9525",
                "quality": 0,
                "size": 7390,
                "width": 236,
            },
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/metadata?url=https%3A%2F%2Fexample.com%2Ffakeid%2Ffakeimage.jpg",
            responses.calls[0].request.url,
        )


class TestUpdateFileDetails(ClientTestCase):
    """
    TestUpdateFileDetails class used to update file details method
    """

    file_id = "fake_123"

    valid_options = UpdateFileRequestOptions(
        tags=["tag1", "tag2"], custom_coordinates="10,10,100,100"
    )

    @responses.activate
    def test_update_file_details_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.update_file_details(
                file_id=self.file_id, options=self.valid_options
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_update_file_details_succeeds_with_id(self):
        """
        Tests if  update file details succeeds with file id
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.PATCH,
            url,
            body="""{
                    "type": "file",
                    "name": "default-image.jpg",
                    "createdAt": "2022-07-21T10:31:22.529Z",
                    "updatedAt": "2022-07-21T10:37:11.848Z",
                    "fileId": "fake_123",
                    "tags": ["tag1", "tag2"],
                    "AITags": [{
                        "name": "Corridor",
                        "confidence": 99.39,
                        "source": "aws-auto-tagging"
                    }, {
                        "name": "Floor",
                        "confidence": 97.59,
                        "source": "aws-auto-tagging"
                    }],
                    "versionInfo": {
                        "id": "versionId",
                        "name": "Version 2"
                    },
                    "embeddedMetadata": {
                        "XResolution": 1,
                        "YResolution": 1,
                        "DateCreated": "2022-07-21T10:35:34.497Z",
                        "DateTimeCreated": "2022-07-21T10:35:34.500Z"
                    },
                    "customCoordinates": "10,10,100,100",
                    "customMetadata": {
                        "test": 11
                    },
                    "isPrivateFile": false,
                    "url": "https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/default-image.jpg",
                    "fileType": "image",
                    "filePath": "/default-image.jpg",
                    "height": 1000,
                    "width": 1000,
                    "size": 184425,
                    "hasAlpha": false,
                    "mime": "image/jpeg",
                    "extensionStatus": {
                        "remove-bg": "pending",
                        "google-auto-tagging": "success"
                    }
                }""",
            headers=headers,
        )

        request_body = json.dumps(
            json.loads(
                """{
                "removeAITags": ["ai-tag1", "ai-tag2"],
                "webhookUrl": "url",
                "extensions": [{
                    "name": "remove-bg",
                    "options": {
                        "add_shadow": true,
                        "bg_color": "red"
                    }
                }, {
                    "name": "google-auto-tagging",
                    "minConfidence": 80,
                    "maxTags": 10
                }],
                "tags": ["tag1", "tag2"],
                "customCoordinates": "10,10,100,100",
                "customMetadata": {
                    "test": 11
                }
            }"""
            )
        )
        resp = self.client.update_file_details(
            file_id=self.file_id,
            options=UpdateFileRequestOptions(
                remove_ai_tags=["ai-tag1", "ai-tag2"],
                webhook_url="url",
                extensions=[
                    {
                        "name": "remove-bg",
                        "options": {"add_shadow": True, "bg_color": "red"},
                    },
                    {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10},
                ],
                tags=["tag1", "tag2"],
                custom_coordinates="10,10,100,100",
                custom_metadata={"test": 11},
            ),
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [
                    {
                        "confidence": 99.39,
                        "name": "Corridor",
                        "source": "aws-auto-tagging",
                    },
                    {
                        "confidence": 97.59,
                        "name": "Floor",
                        "source": "aws-auto-tagging",
                    },
                ],
                "createdAt": "2022-07-21T10:31:22.529Z",
                "customCoordinates": "10,10,100,100",
                "customMetadata": {"test": 11},
                "embeddedMetadata": {
                    "DateCreated": "2022-07-21T10:35:34.497Z",
                    "DateTimeCreated": "2022-07-21T10:35:34.500Z",
                    "XResolution": 1,
                    "YResolution": 1,
                },
                "extensionStatus": {
                    "google-auto-tagging": "success",
                    "remove-bg": "pending",
                },
                "fileId": "fake_123",
                "filePath": "/default-image.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 1000,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "default-image.jpg",
                "size": 184425,
                "tags": ["tag1", "tag2"],
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/default-image.jpg",
                "type": "file",
                "updatedAt": "2022-07-21T10:37:11.848Z",
                "url": "https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
                "versionInfo": {"id": "versionId", "name": "Version 2"},
                "width": 1000,
            },
        }
        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_123", resp.file_id)
        self.assertEqual(
            "http://test.com/v1/files/fake_123/details/", responses.calls[0].request.url
        )

    @responses.activate
    def test_update_file_details_fails_with_404_exception(self) -> None:
        """Test update file details raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=404,
                body="""{"message": "The requested file does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.update_file_details(
                file_id=self.file_id,
                options=UpdateFileRequestOptions(
                    remove_ai_tags=["ai-tag1", "ai-tag2"],
                    webhook_url="url",
                    extensions=[
                        {
                            "name": "remove-bg",
                            "options": {"add_shadow": True, "bg_color": "red"},
                        },
                        {
                            "name": "google-auto-tagging",
                            "minConfidence": 80,
                            "maxTags": 10,
                        },
                    ],
                    tags=["tag1", "tag2"],
                    custom_coordinates="10,10,100,100",
                    custom_metadata={"test": 11},
                ),
            )
            self.assertRaises(UnknownException)
        except UnknownException as e:
            self.assertEqual("The requested file does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)


class TestGetFileVersions(ClientTestCase):
    """
    TestGetFileVersions class used to get file versions and it's details
    """

    file_id = "fake_123"

    version_id = "fake_version_123"

    valid_options = {"tags": ["tag1", "tag2"], "custom_coordinates": "10,10,100,100"}

    @responses.activate
    def test_get_file_versions_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.get_file_versions(self.file_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_versions_succeeds_with_id(self):
        """
        Tests if get file versions succeeds with file id
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)

        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.GET,
            url,
            body="""[{
                "type": "file",
                "name": "new_car.jpg",
                "createdAt": "2022-06-15T11:34:36.294Z",
                "updatedAt": "2022-07-04T10:15:50.067Z",
                "fileId": "fake_123",
                "tags": ["Tag_1", "Tag_2", "Tag_3"],
                "AITags": [{
                    "name": "Clothing",
                    "confidence": 98.77,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Smile",
                    "confidence": 95.31,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Shoe",
                    "confidence": 95.2,
                    "source": "google-auto-tagging"
                }],
                "versionInfo": {
                    "id": "versionId",
                    "name": "Version 4"
                },
                "embeddedMetadata": {
                    "DateCreated": "2022-07-04T10:15:50.066Z",
                    "DateTimeCreated": "2022-07-04T10:15:50.066Z"
                },
                "customCoordinates": "",
                "customMetadata": {
                    "test100": 10,
                    "test10": 11
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 7390,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }, {
                "type": "file-version",
                "name": "new_car.jpg",
                "createdAt": "2022-07-04T10:15:49.698Z",
                "updatedAt": "2022-07-04T10:15:49.734Z",
                "fileId": "fileId",
                "tags": ["Tag_1", "Tag_2", "Tag_3"],
                "AITags": [{
                    "name": "Clothing",
                    "confidence": 98.77,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Smile",
                    "confidence": 95.31,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Shoe",
                    "confidence": 95.2,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Street light",
                    "confidence": 91.05,
                    "source": "google-auto-tagging"
                }],
                "versionInfo": {
                    "id": "62c2bdd5872375c6b8f40fd4",
                    "name": "Version 1"
                },
                "embeddedMetadata": {
                    "XResolution": 250,
                    "YResolution": 250,
                    "DateCreated": "2022-06-15T11:34:36.702Z",
                    "DateTimeCreated": "2022-06-15T11:34:36.702Z"
                },
                "customCoordinates": "10,10,40,40",
                "customMetadata": {
                    "test100": 10,
                    "test10": 11
                },
                "isPrivateFile": false,
                "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": false,
                "mime": "image/jpeg"
            }]""",
            headers=headers,
        )
        resp = self.client.get_file_versions(self.file_id)
        mock_response_metadata = {
            "raw": [
                {
                    "type": "file",
                    "name": "new_car.jpg",
                    "createdAt": "2022-06-15T11:34:36.294Z",
                    "updatedAt": "2022-07-04T10:15:50.067Z",
                    "fileId": "fake_123",
                    "tags": ["Tag_1", "Tag_2", "Tag_3"],
                    "AITags": [
                        {
                            "name": "Clothing",
                            "confidence": 98.77,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Smile",
                            "confidence": 95.31,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Shoe",
                            "confidence": 95.2,
                            "source": "google-auto-tagging",
                        },
                    ],
                    "versionInfo": {"id": "versionId", "name": "Version 4"},
                    "embeddedMetadata": {
                        "DateCreated": "2022-07-04T10:15:50.066Z",
                        "DateTimeCreated": "2022-07-04T10:15:50.066Z",
                    },
                    "customCoordinates": "",
                    "customMetadata": {"test100": 10, "test10": 11},
                    "isPrivateFile": False,
                    "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg",
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg",
                    "fileType": "image",
                    "filePath": "/new_car.jpg",
                    "height": 354,
                    "width": 236,
                    "size": 7390,
                    "hasAlpha": False,
                    "mime": "image/jpeg",
                },
                {
                    "type": "file-version",
                    "name": "new_car.jpg",
                    "createdAt": "2022-07-04T10:15:49.698Z",
                    "updatedAt": "2022-07-04T10:15:49.734Z",
                    "fileId": "fileId",
                    "tags": ["Tag_1", "Tag_2", "Tag_3"],
                    "AITags": [
                        {
                            "name": "Clothing",
                            "confidence": 98.77,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Smile",
                            "confidence": 95.31,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Shoe",
                            "confidence": 95.2,
                            "source": "google-auto-tagging",
                        },
                        {
                            "name": "Street light",
                            "confidence": 91.05,
                            "source": "google-auto-tagging",
                        },
                    ],
                    "versionInfo": {
                        "id": "62c2bdd5872375c6b8f40fd4",
                        "name": "Version 1",
                    },
                    "embeddedMetadata": {
                        "XResolution": 250,
                        "YResolution": 250,
                        "DateCreated": "2022-06-15T11:34:36.702Z",
                        "DateTimeCreated": "2022-06-15T11:34:36.702Z",
                    },
                    "customCoordinates": "10,10,40,40",
                    "customMetadata": {"test100": 10, "test10": 11},
                    "isPrivateFile": False,
                    "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                    "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                    "fileType": "image",
                    "filePath": "/new_car.jpg",
                    "height": 354,
                    "width": 236,
                    "size": 23023,
                    "hasAlpha": False,
                    "mime": "image/jpeg",
                },
            ],
            "http_status_code": 200,
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_123", resp.list[0].file_id)
        self.assertEqual("fileId", resp.list[1].file_id)
        self.assertEqual(
            "http://test.com/v1/files/fake_123/versions", responses.calls[0].request.url
        )

    @responses.activate
    def test_get_file_versions_fails_with_404_exception(self) -> None:
        """Test get file versions raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=404,
                body="""{"message": "The requested asset does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_versions(self.file_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested asset does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_version_details_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}""",
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_version_details_succeeds_with_id(self):
        """
        Tests if get file version details succeeds with file id
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )

        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.GET,
            url,
            body="""{
                        "type": "file-version",
                        "name": "new_car.jpg",
                        "createdAt": "2022-06-27T09:24:25.251Z",
                        "updatedAt": "2022-06-27T12:11:11.247Z",
                        "fileId": "fake_123",
                        "tags": ["tagg", "tagg1"],
                        "AITags": "",
                        "versionInfo": {
                            "id": "fake_version_123",
                            "name": "Version 1"
                        },
                        "embeddedMetadata": {
                            "XResolution": 250,
                            "YResolution": 250,
                            "DateCreated": "2022-06-15T11:34:36.702Z",
                            "DateTimeCreated": "2022-06-15T11:34:36.702Z"
                        },
                        "customCoordinates": "10,10,20,20",
                        "customMetadata": {
                            "test100": 10
                        },
                        "isPrivateFile": false,
                        "url": "https://ik.imagekit.io/your-imagekit-id/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                        "thumbnail": "https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                        "fileType": "image",
                        "filePath": "/new_car.jpg",
                        "height": 354,
                        "width": 236,
                        "size": 23023,
                        "hasAlpha": false,
                        "mime": "image/jpeg"
                    }""",
            headers=headers,
        )
        resp = self.client.get_file_version_details(self.file_id, self.version_id)
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": "",
                "createdAt": "2022-06-27T09:24:25.251Z",
                "customCoordinates": "10,10,20,20",
                "customMetadata": {"test100": 10},
                "embeddedMetadata": {
                    "DateCreated": "2022-06-15T11:34:36.702Z",
                    "DateTimeCreated": "2022-06-15T11:34:36.702Z",
                    "XResolution": 250,
                    "YResolution": 250,
                },
                "fileId": "fake_123",
                "filePath": "/new_car.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 354,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "new_car.jpg",
                "size": 23023,
                "tags": ["tagg", "tagg1"],
                "thumbnail": "https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                "type": "file-version",
                "updatedAt": "2022-06-27T12:11:11.247Z",
                "url": "https://ik.imagekit.io/your-imagekit-id/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                "versionInfo": {"id": "fake_version_123", "name": "Version 1"},
                "width": 236,
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fake_123", resp.file_id)
        self.assertEqual("fake_version_123", resp.version_info.id)
        self.assertEqual(
            "http://test.com/v1/files/fake_123/versions/fake_version_123",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_get_file_version_details_fails_with_404_exception(self) -> None:
        """Test get file version details raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.GET,
                url,
                status=404,
                body="""{"message": "The requested asset does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested asset does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_file_version_details_fails_with_400_exception(self) -> None:
        """Test get file version details raises 400 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body="""{"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "Your request contains invalid fileId parameter.", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)


class TestDeleteFileVersion(ClientTestCase):
    version_id = "fake_123_version_id"
    file_id = "fax_abx1223"

    @responses.activate
    def test_delete_file_version_fails_with_404_exception(self) -> None:
        """Test delete_file_version raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.DELETE,
                url,
                status=404,
                body="""{"message": "The requested file version does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.delete_file_version(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file version does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_delete_file_version_succeeds(self) -> None:
        """Test delete_file_version succeeds with file and version Id"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.DELETE, url, status=204, headers=headers, body="{}")
        resp = self.client.delete_file_version(self.file_id, self.version_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/fax_abx1223/versions/fake_123_version_id",
            responses.calls[0].request.url,
        )


class TestCopyFile(ClientTestCase):
    source_file_path = "/source_file.jpg"

    destination_path = "/destination_path"

    @responses.activate
    def test_copy_file_fails_with_404(self) -> None:
        """Test copy_file raises 404"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=404,
            headers=headers,
            body="""{
                "message": "No file found with filePath /source_file.jpg",
                "help": "For support kindly contact us at support@imagekit.io .",
                "reason": "SOURCE_FILE_MISSING"
            }""",
        )
        try:
            self.client.copy_file(
                options=CopyFileRequestOptions(
                    source_file_path=self.source_file_path,
                    destination_path=self.destination_path,
                    include_file_versions=False,
                )
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No file found with filePath /source_file.jpg", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_copy_file_succeeds(self) -> None:
        """Test copy_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.POST, url, status=204, headers=headers, body="{}")

        resp = self.client.copy_file(
            options=CopyFileRequestOptions(
                source_file_path=self.source_file_path,
                destination_path=self.destination_path,
                include_file_versions=True,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        request_body = json.dumps(
            json.loads(
                """{
                "sourceFilePath": "/source_file.jpg",
                "destinationPath": "/destination_path",
                "includeFileVersions": true
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/copy", responses.calls[0].request.url
        )

    @responses.activate
    def test_copy_file_succeeds_without_include_file_versions(self) -> None:
        """Test copy_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.POST, url, status=204, headers=headers, body="{}")

        resp = self.client.copy_file(
            options=CopyFileRequestOptions(
                source_file_path=self.source_file_path,
                destination_path=self.destination_path,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        request_body = json.dumps(
            json.loads(
                """{
                "sourceFilePath": "/source_file.jpg",
                "destinationPath": "/destination_path"
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/copy", responses.calls[0].request.url
        )


class TestMoveFile(ClientTestCase):
    source_file_path = "/source_file.jpg"

    destination_path = "/destination_path"

    @responses.activate
    def test_move_file_fails_with_404(self) -> None:
        """Test move_file raises 404"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/move".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=404,
            headers=headers,
            body="""{
                "message": "No file found with filePath /source_file.jpg",
                "help": "For support kindly contact us at support@imagekit.io .",
                "reason": "SOURCE_FILE_MISSING"
            }""",
        )
        try:
            self.client.move_file(
                options=MoveFileRequestOptions(
                    source_file_path=self.source_file_path,
                    destination_path=self.destination_path,
                )
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No file found with filePath /source_file.jpg", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_move_file_succeeds(self) -> None:
        """Test move_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/move".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.POST, url, status=204, headers=headers, body="{}")

        resp = self.client.move_file(
            options=MoveFileRequestOptions(
                source_file_path=self.source_file_path,
                destination_path=self.destination_path,
            )
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 204,
            "raw": None,
        }

        request_body = json.dumps(
            json.loads(
                """{
                "sourceFilePath": "/source_file.jpg",
                "destinationPath": "/destination_path"
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/files/move", responses.calls[0].request.url
        )


class TestRenameFile(ClientTestCase):
    file_path = "/file_path.jpg"

    new_file_name = "new_file.jpg"

    @responses.activate
    def test_rename_file_fails_with_409(self) -> None:
        """Test rename_file raises 409"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        try:
            responses.add(
                responses.PUT,
                url,
                status=409,
                headers=headers,
                body="""{
                    "message": "File with name testing-binary.jpg already exists at the same location.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "reason": "FILE_ALREADY_EXISTS"
                }""",
            )
            self.client.rename_file(
                options=RenameFileRequestOptions(
                    file_path=self.file_path, new_file_name=self.new_file_name
                )
            )
            self.assertRaises(ConflictException)
        except ConflictException as e:
            self.assertEqual(
                "File with name testing-binary.jpg already exists at the same location.",
                e.message,
            )
            self.assertEqual(409, e.response_metadata.http_status_code)
            self.assertEqual("FILE_ALREADY_EXISTS", e.response_metadata.raw["reason"])

    @responses.activate
    def test_rename_file_succeeds_with_purge_cache_false(self) -> None:
        """Test rename_file succeeds with Purge cache"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body="{}",
        )
        resp = self.client.rename_file(
            options=RenameFileRequestOptions(
                file_path=self.file_path,
                new_file_name=self.new_file_name,
                purge_cache=False,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {},
        }

        request_body = json.dumps(
            json.loads(
                """{
                "filePath": "/file_path.jpg",
                "newFileName": "new_file.jpg",
                "purgeCache": false
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(None, resp.purge_request_id)
        self.assertEqual(
            "http://test.com/v1/files/rename", responses.calls[0].request.url
        )

    @responses.activate
    def test_rename_file_succeeds_with_purge_cache(self) -> None:
        """Test rename_file succeeds with Purge cache"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body='{"purgeRequestId": "62de3e986f68334a5a3339fb"}',
        )
        resp = self.client.rename_file(
            options=RenameFileRequestOptions(
                file_path=self.file_path,
                new_file_name=self.new_file_name,
                purge_cache=True,
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {"purgeRequestId": "62de3e986f68334a5a3339fb"},
        }

        request_body = json.dumps(
            json.loads(
                """{
                "filePath": "/file_path.jpg",
                "newFileName": "new_file.jpg",
                "purgeCache": true
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("62de3e986f68334a5a3339fb", resp.purge_request_id)
        self.assertEqual(
            "http://test.com/v1/files/rename", responses.calls[0].request.url
        )

    @responses.activate
    def test_rename_file_succeeds(self) -> None:
        """Test rename_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(responses.PUT, url, headers=headers, body="{}")
        resp = self.client.rename_file(
            options=RenameFileRequestOptions(
                file_path=self.file_path, new_file_name=self.new_file_name
            )
        )
        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 200,
            "raw": {},
        }

        request_body = json.dumps(
            json.loads(
                """{
                "filePath": "/file_path.jpg",
                "newFileName": "new_file.jpg"
            }"""
            )
        )

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(None, resp.purge_request_id)
        self.assertEqual(
            "http://test.com/v1/files/rename", responses.calls[0].request.url
        )


class TestRestoreFileVersion(ClientTestCase):
    version_id = "fake_123_version_id"
    file_id = "fax_abx1223"

    @responses.activate
    def test_restore_file_version_fails_with_404_exception(self) -> None:
        """Test restore_file_version raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}/restore".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        try:
            responses.add(
                responses.PUT,
                url,
                status=404,
                body="""{"message": "The requested file version does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.restore_file_version(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file version does not exist.", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_restore_file_version_succeeds(self) -> None:
        """Test restore_file_version succeeds with file and version Id"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}/restore".format(
            URL.API_BASE_URL, self.file_id, self.version_id
        )
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body="""{
                "fileId": "fileId",
                "type": "file",
                "name": "file1.jpg",
                "filePath": "/images/file.jpg",
                "tags": ["t-shirt", "round-neck", "sale2019"],
                "AITags": [
                    {
                        "confidence": 90.12,
                        "source": "google-auto-tagging"
                    }],
                "versionInfo": {
                    "id": "versionId",
                    "name": "Version 2"
                },
                "isPrivateFile": false,
                "customCoordinates": "",
                "url": "https://ik.imagekit.io/your_imagekit_id/images/products/file1.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-media_library_thumbnail/images/products/file1.jpg",
                "fileType": "image",
                "hasAlpha": false,
                "height": 100,
                "isPrivateFile": false,
                "mime": "image/jpeg",
                "name": "file1.jpg",
                "size": 100,
                "hasAlpha": false,
                "customMetadata": {
                    "brand": "Nike",
                    "color": "red"
                },
                "createdAt": "2019-08-24T06:14:41.313Z",
                "updatedAt": "2019-09-24T06:14:41.313Z"
            }""",
        )
        resp = self.client.restore_file_version(self.file_id, self.version_id)

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "http_status_code": 200,
            "raw": {
                "AITags": [{"confidence": 90.12, "source": "google-auto-tagging"}],
                "createdAt": "2019-08-24T06:14:41.313Z",
                "customCoordinates": "",
                "customMetadata": {"brand": "Nike", "color": "red"},
                "fileId": "fileId",
                "filePath": "/images/file.jpg",
                "fileType": "image",
                "hasAlpha": False,
                "height": 100,
                "isPrivateFile": False,
                "mime": "image/jpeg",
                "name": "file1.jpg",
                "size": 100,
                "tags": ["t-shirt", "round-neck", "sale2019"],
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-media_library_thumbnail/images/products/file1.jpg",
                "type": "file",
                "updatedAt": "2019-09-24T06:14:41.313Z",
                "url": "https://ik.imagekit.io/your_imagekit_id/images/products/file1.jpg",
                "versionInfo": {"id": "versionId", "name": "Version 2"},
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("fileId", resp.file_id)
        self.assertEqual("versionId", resp.version_info.id)
        self.assertEqual(
            "http://test.com/v1/files/fax_abx1223/versions/fake_123_version_id/restore",
            responses.calls[0].request.url,
        )
