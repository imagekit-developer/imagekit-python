import json
import os

import responses
from responses import matchers

from imagekitio.client import ImageKit
from imagekitio.constants.url import URL
from imagekitio.exceptions.BadRequestException import BadRequestException
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.exceptions.UnknownException import UnknownException
from tests.dummy_data.file import (
    SUCCESS_PURGE_CACHE_MSG,
    SUCCESS_PURGE_CACHE_STATUS_MSG,
)
from tests.helpers import (
    ClientTestCase,
    get_mocked_failed_resp,
    get_mocked_success_resp, create_headers_for_test, get_auth_headers_for_test,
)

imagekit_obj = ImageKit(
    private_key="private_fake:", public_key="public_fake123:", url_endpoint="fake.com",
)


class TestUpload(ClientTestCase):
    """
    TestUpload class used to test upload method
    """

    image = os.path.join(
        os.path.dirname(os.path.realpath(__file__)), "dummy_data/image.png"
    )
    filename = "test"

    @responses.activate
    def test_upload_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "api/v1/files/upload")
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.upload(file=self.image, file_name=self.filename,
                               options={
                                   "use_unique_file_name": 'false',
                                   "response_fields": ["is_private_file", "tags"],
                                   "is_private_file": True,
                                   "folder": "/testing-python-folder/",
                                   "tags": ["abc", "def"],
                                   "extensions": json.dumps(
                                       ({"name": "remove-bg", "options": {"add_shadow": True, "bg_color": "pink"}},
                                        {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10})
                                   ),
                                   "webhook_url": "https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
                                   "overwrite_file": True,
                                   "overwrite_a_i_tags": False,
                                   "overwrite_tags": False,
                                   "overwrite_custom_metadata": True,
                                   "custom_metadata": json.dumps({"test100": 11})
                               })
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

    @responses.activate
    def test_binary_upload_succeeds(self):
        """
        Tests if  upload succeeds
        """
        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "api/v1/files/upload")
        headers = create_headers_for_test()
        responses.add(
            responses.POST,
            url,
            body=json.dumps({
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
                "thumbnailUrl": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder"
                                "/file_name.jpg",
                "tags": ["abc", "def"],
                "AITags": [{
                    "name": "Computer",
                    "confidence": 97.66,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Personal computer",
                    "confidence": 94.96,
                    "source": "google-auto-tagging"
                }],
                "isPrivateFile": True,
                "extensionStatus": {
                    "remove-bg": "pending",
                    "google-auto-tagging": "success"
                }
            }),
            headers=headers
        )

        resp = self.client.upload(file=open("sample.jpg", "rb"),
                                  file_name="file_name.jpg",
                                  options={
                                      "use_unique_file_name": 'false',
                                      "response_fields": ["is_private_file", "tags"],
                                      "is_private_file": True,
                                      "folder": "/testing-python-folder/",
                                      "tags": ["abc", "def"],
                                      "extensions": json.dumps(
                                          ({"name": "remove-bg", "options": {"add_shadow": True, "bg_color": "pink"}},
                                           {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10})
                                      ),
                                      "webhook_url": "url",
                                      "overwrite_file": True,
                                      "overwrite_a_i_tags": False,
                                      "overwrite_tags": False,
                                      "overwrite_custom_metadata": True,
                                      "custom_metadata": json.dumps({"test100": 11})
                                  })
        mock_resp = {
            'error': None,
            'response': {
                'file_id': 'fake_file_id1234',
                'name': 'file_name.jpg',
                'url': 'https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg',
                'thumbnail_url': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg',
                'height': 700,
                'width': 1050,
                'size': 102117,
                'file_path': '/testing-python-folder/file_name.jpg',
                'tags': ['abc', 'def'],
                'ai_tags': [{
                    'name': 'Computer',
                    'confidence': 97.66,
                    'source': 'google-auto-tagging'
                }, {
                    'name': 'Personal computer',
                    'confidence': 94.96,
                    'source': 'google-auto-tagging'
                }],
                'version_info': {
                    'id': '62d670648cdb697522602b45',
                    'name': 'Version 11'
                },
                'is_private_file': True,
                'custom_coordinates': None,
                'custom_metadata': None,
                'embedded_metadata': None,
                'extension_status': {
                    'remove-bg': 'pending',
                    'google-auto-tagging': 'success'
                },
                'file_type': 'image',
                '_response_metadata': {
                    'raw': {
                        'fileId': 'fake_file_id1234',
                        'name': 'file_name.jpg',
                        'size': 102117,
                        'versionInfo': {
                            'id': '62d670648cdb697522602b45',
                            'name': 'Version 11'
                        },
                        'filePath': '/testing-python-folder/file_name.jpg',
                        'url': 'https://ik.imagekit.io/your_imagekit_id/testing-python-folder/file_name.jpg',
                        'fileType': 'image',
                        'height': 700,
                        'width': 1050,
                        'thumbnailUrl': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/testing-python-folder/file_name.jpg',
                        'tags': ['abc', 'def'],
                        'AITags': [{
                            'name': 'Computer',
                            'confidence': 97.66,
                            'source': 'google-auto-tagging'
                        }, {
                            'name': 'Personal computer',
                            'confidence': 94.96,
                            'source': 'google-auto-tagging'
                        }],
                        'isPrivateFile': True,
                        'extensionStatus': {
                            'remove-bg': 'pending',
                            'google-auto-tagging': 'success'
                        }
                    },
                    'httpStatusCode': 200,
                    'headers': {
                        'Content-Type': 'text/plain',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    }
                }
            }
        }
        request_body = json.loads(json.dumps({
            'file': "<_io.BufferedReader name='sample.jpg'>",
            'fileName': 'file_name.jpg',
            'useUniqueFileName': 'false',
            'responseFields': 'isPrivateFile,tags',
            'isPrivateFile': 'true',
            'folder': '/testing-python-folder/',
            'tags': 'abc,def',
            'extensions': '[{"name": "remove-bg", "options": {"add_shadow": true, "bg_color": "pink"}}, {"name": '
                          '"google-auto-tagging", "minConfidence": 80, "maxTags": 10}]',
            'webhookUrl': 'url',
            'overwriteFile': 'true',
            'overwriteAITags': 'false',
            'overwriteTags': 'false',
            'overwriteCustomMetadata': 'true',
            'customMetadata': '{"test100": 11}'
        }))
        actual_body = responses.calls[0].request.body.__dict__.__getitem__("fields")
        actual_body['file'] = "<_io.BufferedReader name='sample.jpg'>"
        self.assertEqual(request_body, actual_body)
        self.assertEqual(mock_resp, resp)
        self.assertEqual(url, responses.calls[0].request.url)

    def test_upload_fails_without_file_name(self) -> None:
        """Test upload raises error on missing required params
        """
        try:
            self.client.upload(file=open("sample.jpg", "rb"))
        except TypeError as e:
            self.assertEqual({'message': 'Missing fileName parameter for upload', 'help': ''}, e.args[0])

    def test_upload_fails_without_file(self) -> None:
        """Test upload raises error on missing required params
        """
        try:
            self.client.upload(file_name="file_name.jpg")
        except TypeError as e:
            self.assertEqual({'message': 'Missing file parameter for upload', 'help': ''}, e.args[0])

    @responses.activate
    def test_upload_fails_with_400_exception(self) -> None:
        """Test upload raises 400 error"""

        URL.UPLOAD_BASE_URL = "http://test.com"
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "api/v1/files/upload")
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body=json.dumps({
                    'message': 'A file with the same name already exists at the exact location. We '
                               'could not overwrite it because both overwriteFile and '
                               'useUniqueFileName are set to false.'
                }),
            )
            self.client.upload(file=self.image, file_name=self.filename,
                               options={
                                   "use_unique_file_name": 'false',
                                   "response_fields": ["is_private_file", "tags"],
                                   "is_private_file": True,
                                   "folder": "/testing-python-folder/",
                                   "tags": ["abc", "def"],
                                   "extensions": json.dumps(
                                       ({"name": "remove-bg", "options": {"add_shadow": True, "bg_color": "pink"}},
                                        {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10})
                                   ),
                                   "webhook_url": "https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
                                   "overwrite_file": False,
                                   "overwrite_a_i_tags": False,
                                   "overwrite_tags": False,
                                   "overwrite_custom_metadata": True,
                                   "custom_metadata": json.dumps({"test100": 11})
                               })
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("A file with the same name already exists at the exact location. We could not overwrite "
                             "it because both overwriteFile and useUniqueFileName are set to false.", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])


class TestListFiles(ClientTestCase):
    """
    TestListFiles class used to test list_files method
    """

    @responses.activate
    def test_list_files_fails_on_unauthenticated_request(self) -> None:
        """ Tests unauthenticated request restricted for list_files method
        """

        URL.BASE_URL = "http://test.com"
        url = URL.BASE_URL
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.list_files(self.options)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

    @responses.activate
    def test_list_files_succeeds_with_basic_request(self) -> None:
        """
        Tests if list_files work with options which contains type, sort, path, searchQuery, fileType, limit, skip and tags
        """

        URL.BASE_URL = "http://test.com/files"
        url = URL.BASE_URL

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body=json.dumps([{
                "type": "file",
                "name": "sample-cat-image_gr64HPlJS.jpg",
                "createdAt": "2022-06-15T08:19:00.843Z",
                "updatedAt": "2022-06-15T08:19:45.169Z",
                "fileId": "62a995f4d875ec08dc587b72",
                "tags": ["{Tag_1", " Tag_2", " Tag_3}", "tag-to-add-2"],
                "AITags": None,
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
                "isPrivateFile": False,
                "url": "https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg",
                "fileType": "image",
                "filePath": "/sample-cat-image_gr64HPlJS.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": False,
                "mime": "image/jpeg"
            }]),
            headers=headers,
            match=[matchers.query_string_matcher(
                "type=file&sort=ASC_CREATED&path=%2F&searchQuery=createdAt+%3E%3D+%272d%27+OR+size+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3")],
        )

        resp = self.client.list_files(self.options)

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 200,
                    'raw': [{
                        'AITags': None,
                        'createdAt': '2022-06-15T08:19:00.843Z',
                        'customCoordinates': '10,10,20,20',
                        'customMetadata': {
                            'test100': 10
                        },
                        'embeddedMetadata': {
                            'DateCreated': '2022-06-15T08:19:01.523Z',
                            'DateTimeCreated': '2022-06-15T08:19:01.524Z',
                            'XResolution': 250,
                            'YResolution': 250
                        },
                        'fileId': '62a995f4d875ec08dc587b72',
                        'filePath': '/sample-cat-image_gr64HPlJS.jpg',
                        'fileType': 'image',
                        'hasAlpha': False,
                        'height': 354,
                        'isPrivateFile': False,
                        'mime': 'image/jpeg',
                        'name': 'sample-cat-image_gr64HPlJS.jpg',
                        'size': 23023,
                        'tags': ['{Tag_1',
                                 ' Tag_2',
                                 ' Tag_3}',
                                 'tag-to-add-2'
                                 ],
                        'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg',
                        'type': 'file',
                        'updatedAt': '2022-06-15T08:19:45.169Z',
                        'url': 'https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg',
                        'versionInfo': {
                            'id': '62a995f4d875ec08dc587b72',
                            'name': 'Version '
                                    '1'
                        },
                        'width': 236
                    }]
                },
                'list': [{
                    '_response_metadata': {},
                    'ai_tags': None,
                    'created_at': '2022-06-15T08:19:00.843Z',
                    'custom_coordinates': '10,10,20,20',
                    'custom_metadata': {
                        'test100': 10
                    },
                    'embedded_metadata': {
                        'DateCreated': '2022-06-15T08:19:01.523Z',
                        'DateTimeCreated': '2022-06-15T08:19:01.524Z',
                        'XResolution': 250,
                        'YResolution': 250
                    },
                    'extension_status': {},
                    'file_id': '62a995f4d875ec08dc587b72',
                    'file_path': '/sample-cat-image_gr64HPlJS.jpg',
                    'file_type': 'image',
                    'has_alpha': False,
                    'height': 354,
                    'is_private_file': False,
                    'mime': 'image/jpeg',
                    'name': 'sample-cat-image_gr64HPlJS.jpg',
                    'size': 23023,
                    'tags': ['{Tag_1', ' Tag_2', ' Tag_3}', 'tag-to-add-2'],
                    'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/sample-cat-image_gr64HPlJS.jpg',
                    'type': 'file',
                    'updated_at': '2022-06-15T08:19:45.169Z',
                    'url': 'https://ik.imagekit.io/your_imagekit_id/sample-cat-image_gr64HPlJS.jpg',
                    'version_info': {
                        'id': '62a995f4d875ec08dc587b72',
                        'name': 'Version 1'
                    },
                    'width': 236
                }]
            }
        }

        self.assertEqual(
            "http://test.com/files?type=file&sort=ASC_CREATED&path=%2F&searchQuery=createdAt+%3E%3D+%272d%27+OR+size"
            "+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3",
            responses.calls[0].request.url)
        self.assertEqual(mock_resp, resp)

    @responses.activate
    def test_list_files_fails_with_400_exception(self) -> None:
        """Test get list of files raises 400 error"""

        URL.BASE_URL = "http://test.com/files"
        url = URL.BASE_URL
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body=json.dumps({"message": "Invalid search query - createdAt field must have a valid date value. Make "
                                            "sure the value is enclosed within quotes. Please refer to the "
                                            "documentation for syntax specification.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
                match=[matchers.query_string_matcher("type=file&sort=ASC_CREATED&path=%2F&searchQuery=createdAt+%3E"
                                                     "%3D+%272date%27+OR+size+%3C+%272mb%27+OR+format%3D%27png%27"
                                                     "&fileType=all&limit=1&skip=0&tags=Tag_1%2C+Tag_2%2C"
                                                     "+Tag_3")],
            )
            self.client.list_files({"type": "file", "sort": "ASC_CREATED", "path": "/",
                                    "searchQuery": "createdAt >= '2date' OR size < '2mb' OR format='png'",
                                    "fileType": "all", "limit": 1, "skip": 0,
                                    "tags": "Tag_1, Tag_2, Tag_3"})
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Invalid search query - createdAt field must have a valid date value. Make "
                             "sure the value is enclosed within quotes. Please refer to the "
                             "documentation for syntax specification.", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])


class TestGetFileDetails(ClientTestCase):
    """
    TestGetFileDetails class used to test get_file_details method
    """

    file_id = "fake_file_id1234"
    file_url = "https://example.com/default.jpg"

    @responses.activate
    def test_get_file_details_fails_on_unauthenticated_request(self) -> None:
        """Tests of get_file_details raise error on unauthenticated request
        """

        URL.BASE_URL = "http://test.com"
        url = "{}/{}/details".format(URL.BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.get_file_details(self.file_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

    @responses.activate
    def test_file_details_succeeds_with_id(self) -> None:
        URL.BASE_URL = "http://test.com"
        url = "{}/{}/details".format(URL.BASE_URL, self.file_id)

        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body=json.dumps({
                "type": "file",
                "name": "new_car.jpg",
                "createdAt": "2022-06-15T11:34:36.294Z",
                "updatedAt": "2022-07-04T10:15:50.067Z",
                "fileId": "fake_file_id1234",
                "tags": ["Tag_1", "Tag_2", "Tag_3"],
                "AITags": [{
                    "name": "Clothing",
                    "confidence": 98.77,
                    "source": "google-auto-tagging"
                }, {
                    "name": "Smile",
                    "confidence": 95.31,
                    "source": "google-auto-tagging"
                }],
                "versionInfo": {
                    "id": "62b97749f63122840530fda9",
                    "name": "Version 4"
                },
                "embeddedMetadata": {
                    "DateCreated": "2022-07-04T10:15:50.066Z",
                    "DateTimeCreated": "2022-07-04T10:15:50.066Z"
                },
                "customCoordinates": "null",
                "customMetadata": {
                    "test100": 10,
                    "test10": 11
                },
                "isPrivateFile": False,
                "url": "https://ik.imagekit.io/your-imagekit-id/new_car.jpg",
                "thumbnail": "https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 7390,
                "hasAlpha": False,
                "mime": "image/jpeg"
            }),
            headers=headers
        )
        resp = self.client.get_file_details(self.file_id)

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 200,
                    'raw': {
                        'AITags': [{
                            'confidence': 98.77,
                            'name': 'Clothing',
                            'source': 'google-auto-tagging'
                        }, {
                            'confidence': 95.31,
                            'name': 'Smile',
                            'source': 'google-auto-tagging'
                        }],
                        'createdAt': '2022-06-15T11:34:36.294Z',
                        'customCoordinates': 'null',
                        'customMetadata': {
                            'test10': 11,
                            'test100': 10
                        },
                        'embeddedMetadata': {
                            'DateCreated': '2022-07-04T10:15:50.066Z',
                            'DateTimeCreated': '2022-07-04T10:15:50.066Z'
                        },
                        'fileId': 'fake_file_id1234',
                        'filePath': '/new_car.jpg',
                        'fileType': 'image',
                        'hasAlpha': False,
                        'height': 354,
                        'isPrivateFile': False,
                        'mime': 'image/jpeg',
                        'name': 'new_car.jpg',
                        'size': 7390,
                        'tags': ['Tag_1',
                                 'Tag_2',
                                 'Tag_3'
                                 ],
                        'thumbnail': 'https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg',
                        'type': 'file',
                        'updatedAt': '2022-07-04T10:15:50.067Z',
                        'url': 'https://ik.imagekit.io/your-imagekit-id/new_car.jpg',
                        'versionInfo': {
                            'id': '62b97749f63122840530fda9',
                            'name': 'Version '
                                    '4'
                        },
                        'width': 236
                    }
                },
                'ai_tags': [{
                    'confidence': 98.77,
                    'name': 'Clothing',
                    'source': 'google-auto-tagging'
                }, {
                    'confidence': 95.31,
                    'name': 'Smile',
                    'source': 'google-auto-tagging'
                }],
                'created_at': '2022-06-15T11:34:36.294Z',
                'custom_coordinates': 'null',
                'custom_metadata': {
                    'test10': 11,
                    'test100': 10
                },
                'embedded_metadata': {
                    'DateCreated': '2022-07-04T10:15:50.066Z',
                    'DateTimeCreated': '2022-07-04T10:15:50.066Z'
                },
                'extension_status': {},
                'file_id': 'fake_file_id1234',
                'file_path': '/new_car.jpg',
                'file_type': 'image',
                'has_alpha': False,
                'height': 354,
                'is_private_file': False,
                'mime': 'image/jpeg',
                'name': 'new_car.jpg',
                'size': 7390,
                'tags': ['Tag_1', 'Tag_2', 'Tag_3'],
                'thumbnail': 'https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg',
                'type': 'file',
                'updated_at': '2022-07-04T10:15:50.067Z',
                'url': 'https://ik.imagekit.io/your-imagekit-id/new_car.jpg',
                'version_info': {
                    'id': '62b97749f63122840530fda9',
                    'name': 'Version 4'
                },
                'width': 236
            }
        }

        self.assertEqual("http://test.com/fake_file_id1234/details", responses.calls[0].request.url)
        self.assertEqual(mock_resp, resp)

    @responses.activate
    def test_file_details_fails_with_400_exception(self) -> None:
        """Test get file details raises 400 error"""

        URL.BASE_URL = "http://test.com"
        url = "{}/{}/details".format(URL.BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body=json.dumps({"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )
            self.client.get_file_details(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Your request contains invalid fileId parameter.", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])


class TestDeleteFile(ClientTestCase):
    file_id = "fax_abx1223"

    bulk_delete_ids = ["fake_123", "fake_222"]

    def test_bulk_delete_fails_on_unauthenticated_request(self) -> None:
        """Test bulk_delete on unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if bulk_delete is only restricted to authenticated
        requests
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.bulk_delete(self.bulk_delete_ids)

        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    @responses.activate
    def test_bulk_file_delete_fails_on_unauthenticated_request(self) -> None:
        """Test bulk_file_delete on unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if bulk_delete is only restricted to authenticated
        requests
        """

        URL.BASE_URL = "http://test.com"
        url = URL.BASE_URL + URL.BULK_FILE_DELETE
        try:
            responses.add(
                responses.POST,
                url,
                status=403,
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.bulk_file_delete(self.bulk_delete_ids)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

    @responses.activate
    def test_bulk_file_delete_succeeds(self):
        """Test bulk_delete  on authenticated request
        this function tests if bulk_file_delete working properly
        """

        URL.BASE_URL = "http://test.com"
        url = URL.BASE_URL + URL.BULK_FILE_DELETE
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())

        responses.add(
            responses.POST,
            url,
            body=json.dumps({
                "successfullyDeletedFileIds": ["fake_123", "fake_222"]
            }),
            headers=headers
        )

        resp = self.client.bulk_file_delete(self.bulk_delete_ids)

        mock_resp = {
            'error': None,
            'response': {
                'successfully_deleted_file_ids': ['fake_123', 'fake_222'],
                '_response_metadata': {
                    'raw': {
                        'successfullyDeletedFileIds': ['fake_123', 'fake_222']
                    },
                    'httpStatusCode': 200,
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    }
                }
            }
        }
        self.assertEqual("fileIds=fake_123&fileIds=fake_222", responses.calls[0].request.body)
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/batch/deleteByFileIds", responses.calls[0].request.url)

    @responses.activate
    def test_bulk_file_delete_fails_with_404_exception(self) -> None:
        """Test bulk_file_delete raises 404 error"""

        URL.BASE_URL = "http://test.com"
        url = URL.BASE_URL + URL.BULK_FILE_DELETE
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.POST,
                url,
                status=404,
                body=json.dumps({
                    "message": "The requested file(s) does not exist.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "missingFileIds": ["fake_123", "fake_222"]
                }),
                headers=headers
            )
            self.client.bulk_file_delete(self.bulk_delete_ids)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file(s) does not exist.", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])
            self.assertEqual(["fake_123", "fake_222"], e.response_metadata['raw']['missingFileIds'])

    @responses.activate
    def test_file_delete_fails_with_400_exception(self):
        """Test delete_file on unavailable content
        this function raising 400 if the file
        is not available
        """

        URL.BASE_URL = "http://test.com"
        url = "{}/{}".format(URL.BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        try:
            responses.add(
                responses.DELETE,
                url,
                status=400,
                body=json.dumps({
                    "message": "Your request contains invalid fileId parameter.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }),
                headers=headers
            )
            self.client.delete_file(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Your request contains invalid fileId parameter.", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])

    @responses.activate
    def test_file_delete_succeeds(self):
        """Test delete file on authenticated request
        this function tests if delete_file working properly
        """
        URL.BASE_URL = "http://test.com"
        url = "{}/{}".format(URL.BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())

        responses.add(
            responses.DELETE,
            url,
            body=json.dumps({}),
            status=204,
            headers=headers
        )

        resp = self.client.delete_file(self.file_id)

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 204,
                    'raw': None
                }
            }
        }
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/fax_abx1223", responses.calls[0].request.url)


class TestPurgeCache(ClientTestCase):
    fake_image_url = "https://example.com/fakeid/fakeimage.jpg"

    def test_purge_cache_fails_on_unauthenticated_request(self) -> None:
        """Test purge_cache unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if purge_cache is only restricted to authenticated request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.purge_cache(self.fake_image_url)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_purge_file_cache_fails_on_unauthenticated_request(self) -> None:
        """Test purge_cache unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if purge_cache is only restricted to authenticated request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.purge_file_cache(self.fake_image_url)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_purge_cache_fails_without_passing_file_url(self) -> None:
        """Test purge_cache raises error on invalid_body request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(TypeError, self.client.purge_cache)

    def test_purge_file_cache_fails_without_passing_file_url(self) -> None:
        """Test purge_file_cache raises error on invalid_body request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(TypeError, self.client.purge_file_cache)

    def test_purge_cache_succeeds(self) -> None:
        """Test purge_cache working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp(message=SUCCESS_PURGE_CACHE_MSG)
        )
        resp = self.client.purge_cache(self.fake_image_url)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])
        self.assertIn("request_id", resp["response"])

    def test_purge_file_cache_succeeds(self) -> None:
        """Test purge_file_cache working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp(message=SUCCESS_PURGE_CACHE_MSG)
        )
        resp = self.client.purge_file_cache(self.fake_image_url)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])
        self.assertIn("request_id", resp["response"])


class TestPurgeCacheStatus(ClientTestCase):
    cache_request_id = "fake1234"

    def test_get_purge_cache_status_fails_on_unauthenticated_request(self) -> None:
        """Test get_purge_cache_status unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if get_purge_cache_status is only restricted to authenticated
        user
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.get_purge_cache_status(self.cache_request_id)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_get_purge_file_cache_status_fails_on_unauthenticated_request(self) -> None:
        """Test get_purge_file_cache_status unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if get_purge_cache_status is only restricted to authenticated
        user
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.get_purge_file_cache_status(self.cache_request_id)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_purge_cache_status_fails_without_passing_file_url(self) -> None:
        """Test purge_cache raises error on invalid_body request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(TypeError, self.client.get_purge_cache_status)

    def test_purge_file_cache_status_fails_without_passing_file_url(self) -> None:
        """Test purge_file_cache raises error on invalid_body request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(TypeError, self.client.get_purge_file_cache_status)

    def test_purge_cache_status_succeeds(self) -> None:
        """Test get_purge_cache_status working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp(message=SUCCESS_PURGE_CACHE_STATUS_MSG)
        )
        resp = self.client.get_purge_cache_status(self.cache_request_id)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_purge_cache_status_fails_without_passing_file_id(self) -> None:
        """Test purge_cache raises error on invalid_body request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(TypeError, self.client.get_metadata())

    def test_purge_file_cache_status_succeeds(self) -> None:
        """Test get_purge_file_cache_status working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp(message=SUCCESS_PURGE_CACHE_STATUS_MSG)
        )
        resp = self.client.get_purge_file_cache_status(self.cache_request_id)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])


class TestGetMetaData(ClientTestCase):
    file_id = "fake_file_xbc"

    def test_get_metadata_fails_on_unauthenticated_request(self) -> None:
        """Tests get_metadata raise error on unauthenticated request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.get_metadata(file_id=self.file_id)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_get_file_metadata_fails_on_unauthenticated_request(self) -> None:
        """Tests get_file_metadata raise error on unauthenticated request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.get_file_metadata(file_id=self.file_id)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_get_metadata_succeeds(self):
        """Tests if get_metadata working properly
        """

        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.get_metadata(file_id=self.file_id)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_get_file_metadata_succeeds(self):
        """Tests if get_file_metadata working properly
        """

        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.get_file_metadata(file_id=self.file_id)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_get_remote_url_metadata_file_url(self) -> None:
        """Test get_remote_url_metadata_ raises error on invalid_body request
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(ValueError, self.client.get_remote_url_metadata)

    def test_get_remote_url_metadata_succeeds(self):
        """Tests if get_remote_url_metadata working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.get_remote_url_metadata(
            remote_file_url="http://imagekit.io/default.jpg"
        )
        self.assertIsNone(resp["error"])
        self.assertIsNotNone("response")

        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.get_metadata(file_id=self.file_id)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_get_remote_file_url_metadata_succeeds(self):
        """Tests if get_remote_url_metadata working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.get_remote_file_url_metadata(
            remote_file_url="http://imagekit.io/default.jpg"
        )
        self.assertIsNone(resp["error"])
        self.assertIsNotNone("response")


class TestUpdateFileDetails(ClientTestCase):
    """
    TestUpdateFileDetails class used to update file details method
    """

    file_id = "fake_123"

    valid_options = {"tags": ["tag1", "tag2"], "custom_coordinates": "10,10,100,100"}

    @responses.activate
    def test_update_file_details_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.BASE_URL = "http://test.com"
        url = "{}/{}/details/".format(URL.BASE_URL, self.file_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=403,
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.update_file_details(
                file_id=self.file_id, options=self.valid_options
            )
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

    @responses.activate
    def test_update_file_details_succeeds_with_id(self):
        """
        Tests if  update file details succeeds with file id
        """
        URL.BASE_URL = "http://test.com"
        url = "{}/{}/details/".format(URL.BASE_URL, self.file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.PATCH,
            url,
            body=json.dumps({
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
                "isPrivateFile": False,
                "url": "https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/default-image.jpg",
                "fileType": "image",
                "filePath": "/default-image.jpg",
                "height": 1000,
                "width": 1000,
                "size": 184425,
                "hasAlpha": False,
                "mime": "image/jpeg",
                "extensionStatus": {
                    "remove-bg": "pending",
                    "google-auto-tagging": "success"
                }
            }),
            headers=headers
        )

        request_body = {
            "removeAITags": ["ai-tag1", "ai-tag2"],
            "webhookUrl": "url",
            "extensions": [{
                "name": "remove-bg",
                "options": {
                    "add_shadow": True,
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
        }
        resp = self.client.update_file_details(self.file_id, request_body)
        mock_resp = {
            'error': None,
            'response': {
                'type': 'file',
                'name': 'default-image.jpg',
                'created_at': '2022-07-21T10:31:22.529Z',
                'updated_at': '2022-07-21T10:37:11.848Z',
                'file_id': 'fake_123',
                'tags': ['tag1', 'tag2'],
                'ai_tags': [{
                    'name': 'Corridor',
                    'confidence': 99.39,
                    'source': 'aws-auto-tagging'
                }, {
                    'name': 'Floor',
                    'confidence': 97.59,
                    'source': 'aws-auto-tagging'
                }],
                'version_info': {
                    'id': 'versionId',
                    'name': 'Version 2'
                },
                'embedded_metadata': {
                    'XResolution': 1,
                    'YResolution': 1,
                    'DateCreated': '2022-07-21T10:35:34.497Z',
                    'DateTimeCreated': '2022-07-21T10:35:34.500Z'
                },
                'custom_coordinates': '10,10,100,100',
                'custom_metadata': {
                    'test': 11
                },
                'is_private_file': False,
                'url': 'https://ik.imagekit.io/your_imagekit_id/default-image.jpg',
                'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/default-image.jpg',
                'file_type': 'image',
                'file_path': '/default-image.jpg',
                'height': 1000,
                'width': 1000,
                'size': 184425,
                'has_alpha': False,
                'mime': 'image/jpeg',
                'extension_status': {
                    'remove-bg': 'pending',
                    'google-auto-tagging': 'success'
                },
                '_response_metadata': {
                    'raw': {
                        'type': 'file',
                        'name': 'default-image.jpg',
                        'createdAt': '2022-07-21T10:31:22.529Z',
                        'updatedAt': '2022-07-21T10:37:11.848Z',
                        'fileId': 'fake_123',
                        'tags': ['tag1', 'tag2'],
                        'AITags': [{
                            'name': 'Corridor',
                            'confidence': 99.39,
                            'source': 'aws-auto-tagging'
                        }, {
                            'name': 'Floor',
                            'confidence': 97.59,
                            'source': 'aws-auto-tagging'
                        }],
                        'versionInfo': {
                            'id': 'versionId',
                            'name': 'Version 2'
                        },
                        'embeddedMetadata': {
                            'XResolution': 1,
                            'YResolution': 1,
                            'DateCreated': '2022-07-21T10:35:34.497Z',
                            'DateTimeCreated': '2022-07-21T10:35:34.500Z'
                        },
                        'customCoordinates': '10,10,100,100',
                        'customMetadata': {
                            'test': 11
                        },
                        'isPrivateFile': False,
                        'url': 'https://ik.imagekit.io/your_imagekit_id/default-image.jpg',
                        'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/default-image.jpg',
                        'fileType': 'image',
                        'filePath': '/default-image.jpg',
                        'height': 1000,
                        'width': 1000,
                        'size': 184425,
                        'hasAlpha': False,
                        'mime': 'image/jpeg',
                        'extensionStatus': {
                            'remove-bg': 'pending',
                            'google-auto-tagging': 'success'
                        }
                    },
                    'httpStatusCode': 200,
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    }
                }
            }
        }
        self.assertEqual(json.dumps(request_body), responses.calls[0].request.body)
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/fake_123/details/", responses.calls[0].request.url)

    @responses.activate
    def test_update_file_details_fails_with_404_exception(self) -> None:
        """Test update file details raises 404 error"""

        URL.BASE_URL = "http://test.com"
        url = "{}/{}/details/".format(URL.BASE_URL, self.file_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=404,
                body=json.dumps({"message": "The requested file does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )

            request_body = {
                "removeAITags": ["ai-tag1", "ai-tag2"],
                "webhookUrl": "url",
                "extensions": [{
                    "name": "remove-bg",
                    "options": {
                        "add_shadow": True,
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
            }
            self.client.update_file_details(self.file_id, request_body)
            self.assertRaises(UnknownException)
        except UnknownException as e:
            self.assertEqual("The requested file does not exist.", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])


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
        URL.BASE_URL = "http://test.com"
        url = "{}/{}/versions".format(URL.BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.get_file_versions(self.file_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

    @responses.activate
    def test_get_file_versions_succeeds_with_id(self):
        """
        Tests if get file versions succeeds with file id
        """
        URL.BASE_URL = "http://test.com"
        url = "{}/{}/versions".format(URL.BASE_URL, self.file_id)

        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.GET,
            url,
            body=json.dumps([{
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
                "customCoordinates": None,
                "customMetadata": {
                    "test100": 10,
                    "test10": 11
                },
                "isPrivateFile": False,
                "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 7390,
                "hasAlpha": False,
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
                "isPrivateFile": False,
                "url": "https://ik.imagekit.io/your_imagekit_id/new_car.jpg?ik-obj-version"
                       "=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version"
                             "=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": False,
                "mime": "image/jpeg"
            }]),
            headers=headers
        )
        resp = self.client.get_file_versions(self.file_id)
        mock_resp = {
            'error': None,
            'response': {
                'list': [{
                    'type': 'file',
                    'name': 'new_car.jpg',
                    'created_at': '2022-06-15T11:34:36.294Z',
                    'updated_at': '2022-07-04T10:15:50.067Z',
                    'file_id': 'fake_123',
                    'tags': ['Tag_1', 'Tag_2', 'Tag_3'],
                    'ai_tags': [{
                        'name': 'Clothing',
                        'confidence': 98.77,
                        'source': 'google-auto-tagging'
                    }, {
                        'name': 'Smile',
                        'confidence': 95.31,
                        'source': 'google-auto-tagging'
                    }, {
                        'name': 'Shoe',
                        'confidence': 95.2,
                        'source': 'google-auto-tagging'
                    }],
                    'version_info': {
                        'id': 'versionId',
                        'name': 'Version 4'
                    },
                    'embedded_metadata': {
                        'DateCreated': '2022-07-04T10:15:50.066Z',
                        'DateTimeCreated': '2022-07-04T10:15:50.066Z'
                    },
                    'custom_coordinates': None,
                    'custom_metadata': {
                        'test100': 10,
                        'test10': 11
                    },
                    'is_private_file': False,
                    'url': 'https://ik.imagekit.io/your_imagekit_id/new_car.jpg',
                    'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg',
                    'file_type': 'image',
                    'file_path': '/new_car.jpg',
                    'height': 354,
                    'width': 236,
                    'size': 7390,
                    'has_alpha': False,
                    'mime': 'image/jpeg',
                    'extension_status': {},
                    '_response_metadata': {}
                }, {
                    'type': 'file-version',
                    'name': 'new_car.jpg',
                    'created_at': '2022-07-04T10:15:49.698Z',
                    'updated_at': '2022-07-04T10:15:49.734Z',
                    'file_id': 'fileId',
                    'tags': ['Tag_1', 'Tag_2', 'Tag_3'],
                    'ai_tags': [{
                        'name': 'Clothing',
                        'confidence': 98.77,
                        'source': 'google-auto-tagging'
                    }, {
                        'name': 'Smile',
                        'confidence': 95.31,
                        'source': 'google-auto-tagging'
                    }, {
                        'name': 'Shoe',
                        'confidence': 95.2,
                        'source': 'google-auto-tagging'
                    }, {
                        'name': 'Street light',
                        'confidence': 91.05,
                        'source': 'google-auto-tagging'
                    }],
                    'version_info': {
                        'id': '62c2bdd5872375c6b8f40fd4',
                        'name': 'Version 1'
                    },
                    'embedded_metadata': {
                        'XResolution': 250,
                        'YResolution': 250,
                        'DateCreated': '2022-06-15T11:34:36.702Z',
                        'DateTimeCreated': '2022-06-15T11:34:36.702Z'
                    },
                    'custom_coordinates': '10,10,40,40',
                    'custom_metadata': {
                        'test100': 10,
                        'test10': 11
                    },
                    'is_private_file': False,
                    'url': 'https://ik.imagekit.io/your_imagekit_id/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz',
                    'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz',
                    'file_type': 'image',
                    'file_path': '/new_car.jpg',
                    'height': 354,
                    'width': 236,
                    'size': 23023,
                    'has_alpha': False,
                    'mime': 'image/jpeg',
                    'extension_status': {},
                    '_response_metadata': {}
                }],
                '_response_metadata': {
                    'raw': [{
                        'type': 'file',
                        'name': 'new_car.jpg',
                        'createdAt': '2022-06-15T11:34:36.294Z',
                        'updatedAt': '2022-07-04T10:15:50.067Z',
                        'fileId': 'fake_123',
                        'tags': ['Tag_1', 'Tag_2', 'Tag_3'],
                        'AITags': [{
                            'name': 'Clothing',
                            'confidence': 98.77,
                            'source': 'google-auto-tagging'
                        }, {
                            'name': 'Smile',
                            'confidence': 95.31,
                            'source': 'google-auto-tagging'
                        }, {
                            'name': 'Shoe',
                            'confidence': 95.2,
                            'source': 'google-auto-tagging'
                        }],
                        'versionInfo': {
                            'id': 'versionId',
                            'name': 'Version 4'
                        },
                        'embeddedMetadata': {
                            'DateCreated': '2022-07-04T10:15:50.066Z',
                            'DateTimeCreated': '2022-07-04T10:15:50.066Z'
                        },
                        'customCoordinates': None,
                        'customMetadata': {
                            'test100': 10,
                            'test10': 11
                        },
                        'isPrivateFile': False,
                        'url': 'https://ik.imagekit.io/your_imagekit_id/new_car.jpg',
                        'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg',
                        'fileType': 'image',
                        'filePath': '/new_car.jpg',
                        'height': 354,
                        'width': 236,
                        'size': 7390,
                        'hasAlpha': False,
                        'mime': 'image/jpeg'
                    }, {
                        'type': 'file-version',
                        'name': 'new_car.jpg',
                        'createdAt': '2022-07-04T10:15:49.698Z',
                        'updatedAt': '2022-07-04T10:15:49.734Z',
                        'fileId': 'fileId',
                        'tags': ['Tag_1', 'Tag_2', 'Tag_3'],
                        'AITags': [{
                            'name': 'Clothing',
                            'confidence': 98.77,
                            'source': 'google-auto-tagging'
                        }, {
                            'name': 'Smile',
                            'confidence': 95.31,
                            'source': 'google-auto-tagging'
                        }, {
                            'name': 'Shoe',
                            'confidence': 95.2,
                            'source': 'google-auto-tagging'
                        }, {
                            'name': 'Street light',
                            'confidence': 91.05,
                            'source': 'google-auto-tagging'
                        }],
                        'versionInfo': {
                            'id': '62c2bdd5872375c6b8f40fd4',
                            'name': 'Version 1'
                        },
                        'embeddedMetadata': {
                            'XResolution': 250,
                            'YResolution': 250,
                            'DateCreated': '2022-06-15T11:34:36.702Z',
                            'DateTimeCreated': '2022-06-15T11:34:36.702Z'
                        },
                        'customCoordinates': '10,10,40,40',
                        'customMetadata': {
                            'test100': 10,
                            'test10': 11
                        },
                        'isPrivateFile': False,
                        'url': 'https://ik.imagekit.io/your_imagekit_id/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz',
                        'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=dlkUlhiJ7I8OTejhKG38GZJBrsvDBcnz',
                        'fileType': 'image',
                        'filePath': '/new_car.jpg',
                        'height': 354,
                        'width': 236,
                        'size': 23023,
                        'hasAlpha': False,
                        'mime': 'image/jpeg'
                    }],
                    'httpStatusCode': 200,
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    }
                }
            }
        }

        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/fake_123/versions", responses.calls[0].request.url)

    @responses.activate
    def test_get_file_versions_fails_with_404_exception(self) -> None:
        """Test get file versions raises 404 error"""

        URL.BASE_URL = "http://test.com"
        url = "{}/{}/versions".format(URL.BASE_URL, self.file_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=404,
                body=json.dumps({"message": "The requested asset does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )
            self.client.get_file_versions(self.file_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested asset does not exist.", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])

    @responses.activate
    def test_get_file_version_details_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.BASE_URL = "http://test.com"
        url = "{}/{}/versions/{}".format(URL.BASE_URL, self.file_id, self.version_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

    @responses.activate
    def test_get_file_version_details_succeeds_with_id(self):
        """
        Tests if get file version details succeeds with file id
        """
        URL.BASE_URL = "http://test.com"
        url = "{}/{}/versions/{}".format(URL.BASE_URL, self.file_id, self.version_id)

        headers = {"Content-Type": "application/json"}
        headers.update(get_auth_headers_for_test())
        responses.add(
            responses.GET,
            url,
            body=json.dumps({
                "type": "file-version",
                "name": "new_car.jpg",
                "createdAt": "2022-06-27T09:24:25.251Z",
                "updatedAt": "2022-06-27T12:11:11.247Z",
                "fileId": "fake_123",
                "tags": ["tagg", "tagg1"],
                "AITags": None,
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
                "isPrivateFile": False,
                "url": "https://ik.imagekit.io/your-imagekit-id/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                "thumbnail": "https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH",
                "fileType": "image",
                "filePath": "/new_car.jpg",
                "height": 354,
                "width": 236,
                "size": 23023,
                "hasAlpha": False,
                "mime": "image/jpeg"
            }),
            headers=headers
        )
        resp = self.client.get_file_version_details(self.file_id, self.version_id)
        mock_resp = {
            'error': None,
            'response': {
                'type': 'file-version',
                'name': 'new_car.jpg',
                'created_at': '2022-06-27T09:24:25.251Z',
                'updated_at': '2022-06-27T12:11:11.247Z',
                'file_id': 'fake_123',
                'tags': ['tagg', 'tagg1'],
                'ai_tags': None,
                'version_info': {
                    'id': 'fake_version_123',
                    'name': 'Version 1'
                },
                'embedded_metadata': {
                    'XResolution': 250,
                    'YResolution': 250,
                    'DateCreated': '2022-06-15T11:34:36.702Z',
                    'DateTimeCreated': '2022-06-15T11:34:36.702Z'
                },
                'custom_coordinates': '10,10,20,20',
                'custom_metadata': {
                    'test100': 10
                },
                'is_private_file': False,
                'url': 'https://ik.imagekit.io/your-imagekit-id/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH',
                'thumbnail': 'https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH',
                'file_type': 'image',
                'file_path': '/new_car.jpg',
                'height': 354,
                'width': 236,
                'size': 23023,
                'has_alpha': False,
                'mime': 'image/jpeg',
                'extension_status': {},
                '_response_metadata': {
                    'raw': {
                        'type': 'file-version',
                        'name': 'new_car.jpg',
                        'createdAt': '2022-06-27T09:24:25.251Z',
                        'updatedAt': '2022-06-27T12:11:11.247Z',
                        'fileId': 'fake_123',
                        'tags': ['tagg', 'tagg1'],
                        'AITags': None,
                        'versionInfo': {
                            'id': 'fake_version_123',
                            'name': 'Version 1'
                        },
                        'embeddedMetadata': {
                            'XResolution': 250,
                            'YResolution': 250,
                            'DateCreated': '2022-06-15T11:34:36.702Z',
                            'DateTimeCreated': '2022-06-15T11:34:36.702Z'
                        },
                        'customCoordinates': '10,10,20,20',
                        'customMetadata': {
                            'test100': 10
                        },
                        'isPrivateFile': False,
                        'url': 'https://ik.imagekit.io/your-imagekit-id/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH',
                        'thumbnail': 'https://ik.imagekit.io/your-imagekit-id/tr:n-ik_ml_thumbnail/new_car.jpg?ik-obj-version=hzBNRjaJhZYg.JNu75L2nMDfhjJP4tJH',
                        'fileType': 'image',
                        'filePath': '/new_car.jpg',
                        'height': 354,
                        'width': 236,
                        'size': 23023,
                        'hasAlpha': False,
                        'mime': 'image/jpeg'
                    },
                    'httpStatusCode': 200,
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    }
                }
            }
        }

        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/fake_123/versions/fake_version_123", responses.calls[0].request.url)

    @responses.activate
    def test_get_file_version_details_fails_with_404_exception(self) -> None:
        """Test get file version details raises 404 error"""

        URL.BASE_URL = "http://test.com"
        url = "{}/{}/versions/{}".format(URL.BASE_URL, self.file_id, self.version_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=404,
                body=json.dumps({"message": "The requested asset does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested asset does not exist.", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])

    @responses.activate
    def test_get_file_version_details_fails_with_400_exception(self) -> None:
        """Test get file version details raises 400 error"""

        URL.BASE_URL = "http://test.com"
        url = "{}/{}/versions/{}".format(URL.BASE_URL, self.file_id, self.version_id)
        try:
            responses.add(
                responses.GET,
                url,
                status=400,
                body=json.dumps({"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )
            self.client.get_file_version_details(self.file_id, self.version_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Your request contains invalid fileId parameter.", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])
