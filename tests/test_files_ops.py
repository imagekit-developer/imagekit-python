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
from tests.helpers import (
    ClientTestCase,
    create_headers_for_test, get_auth_headers_for_test,
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
            self.client.upload_file(file=self.image, file_name=self.filename,
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

        resp = self.client.upload_file(file=open("sample.jpg", "rb"),
                                       file_name="file_name.jpg",
                                       options={
                                           "use_unique_file_name": 'false',
                                           "response_fields": ["is_private_file", "tags"],
                                           "is_private_file": True,
                                           "folder": "/testing-python-folder/",
                                           "tags": ["abc", "def"],
                                           "extensions": json.dumps(
                                               ({"name": "remove-bg",
                                                 "options": {"add_shadow": True, "bg_color": "pink"}},
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
            self.client.upload_file(file=open("sample.jpg", "rb"))
        except TypeError as e:
            self.assertEqual({'message': 'Missing fileName parameter for upload', 'help': ''}, e.args[0])

    def test_upload_fails_without_file(self) -> None:
        """Test upload raises error on missing required params
        """
        try:
            self.client.upload_file(file_name="file_name.jpg")
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
            self.client.upload_file(file=self.image, file_name=self.filename,
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

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)
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

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files".format(URL.API_BASE_URL)

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
            "http://test.com/v1/files?type=file&sort=ASC_CREATED&path=%2F&searchQuery=createdAt+%3E%3D+%272d%27+OR+size"
            "+%3C+%272mb%27+OR+format%3D%27png%27&fileType=all&limit=1&skip=0&tags=Tag-1%2C+Tag-2%2C+Tag-3",
            responses.calls[0].request.url)
        self.assertEqual(mock_resp, resp)

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

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)
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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, self.file_id)

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

        self.assertEqual("http://test.com/v1/files/fake_file_id1234/details", responses.calls[0].request.url)
        self.assertEqual(mock_resp, resp)

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

        URL.API_BASE_URL = "http://test.com"
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
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
        self.assertEqual(json.dumps({"fileIds": ["fake_123", "fake_222"]}), responses.calls[0].request.body)
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/batch/deleteByFileIds", responses.calls[0].request.url)

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

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}".format(URL.API_BASE_URL, self.file_id)
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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}".format(URL.API_BASE_URL, self.file_id)
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
        self.assertEqual("http://test.com/v1/files/fax_abx1223", responses.calls[0].request.url)


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
                body=json.dumps({'message': 'Your account cannot be authenticated.'
                                    , 'help': 'For support kindly contact us at support@imagekit.io .'}),
            )
            self.client.purge_file_cache(self.fake_image_url)
            self.assertRaises(ForbiddenException)
        except ForbiddenException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(e.response_metadata['httpStatusCode'], 403)

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
                body=json.dumps({"message": "Invalid url"}),
            )
            self.client.purge_file_cache("url")
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Invalid url", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])

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
            body=json.dumps({"requestId": "62df7d671b02a58936e7c732"}),
        )
        resp = self.client.purge_file_cache(self.fake_image_url)
        mock_resp = {
            'error': None,
            'response': {
                'request_id': '62df7d671b02a58936e7c732',
                '_response_metadata': {
                    'raw': {
                        'requestId': '62df7d671b02a58936e7c732'
                    },
                    'httpStatusCode': 201,
                    'headers': {
                        'Content-Type': 'text/plain'
                    }
                }
            }
        }
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/purge", responses.calls[0].request.url)
        self.assertEqual(json.dumps({"url": "https://example.com/fakeid/fakeimage.jpg"}),
                         responses.calls[0].request.body)


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
                body=json.dumps({"message": "No request found for this requestId.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )
            self.client.get_purge_file_cache_status(self.cache_request_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("No request found for this requestId.", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])

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
            body=json.dumps({"status": "Completed"}),
        )
        resp = self.client.get_purge_file_cache_status(self.cache_request_id)
        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain'
                    },
                    'httpStatusCode': 200,
                    'raw': {
                        'status': 'Completed'
                    }
                },
                'status': 'Completed'
            }
        }
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/purge/fake1234", responses.calls[0].request.url)


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
                body=json.dumps({"message": "Your request contains invalid fileId parameter.",
                                 "help": "For support kindly contact us at support@imagekit.io .",
                                 "type": "INVALID_PARAM_ERROR"}),
            )
            self.client.get_file_metadata(self.file_id)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Your request contains invalid fileId parameter.", e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])
            self.assertEqual("INVALID_PARAM_ERROR", e.response_metadata['raw']['type'])

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
            body=json.dumps({
                "height": 354,
                "width": 236,
                "size": 7390,
                "format": "jpg",
                "hasColorProfile": False,
                "quality": 0,
                "density": 250,
                "hasTransparency": False,
                "exif": {},
                "pHash": "2e0ed1f12eda9525"
            }),
        )
        resp = self.client.get_file_metadata(self.file_id)
        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain'
                    },
                    'httpStatusCode': 200,
                    'raw': {
                        'density': 250,
                        'exif': {},
                        'format': 'jpg',
                        'hasColorProfile': False,
                        'hasTransparency': False,
                        'height': 354,
                        'pHash': '2e0ed1f12eda9525',
                        'quality': 0,
                        'size': 7390,
                        'width': 236
                    }
                },
                'density': 250,
                'exif': {},
                'format': 'jpg',
                'has_color_profile': False,
                'has_transparency': False,
                'height': 354,
                'p_hash': '2e0ed1f12eda9525',
                'quality': 0,
                'size': 7390,
                'width': 236
            }
        }
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/fake_file_xbc/metadata", responses.calls[0].request.url)

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
                body=json.dumps({
                    "message": "https://example.com/fakeid/fakeimage.jpg should be accessible using your ImageKit.io account.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }),
                match=[matchers.query_string_matcher("url=https://example.com/fakeid/fakeimage.jpg")]
            )
            self.client.get_remote_file_url_metadata(self.fake_image_url)
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "https://example.com/fakeid/fakeimage.jpg should be accessible using your ImageKit.io account.",
                e.message)
            self.assertEqual(400, e.response_metadata['httpStatusCode'])

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
            body=json.dumps({
                "height": 354,
                "width": 236,
                "size": 7390,
                "format": "jpg",
                "hasColorProfile": False,
                "quality": 0,
                "density": 250,
                "hasTransparency": False,
                "exif": {},
                "pHash": "2e0ed1f12eda9525"
            }),
            match=[matchers.query_string_matcher("url=https://example.com/fakeid/fakeimage.jpg")]
        )
        resp = self.client.get_remote_file_url_metadata(self.fake_image_url)
        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain'
                    },
                    'httpStatusCode': 200,
                    'raw': {
                        'density': 250,
                        'exif': {},
                        'format': 'jpg',
                        'hasColorProfile': False,
                        'hasTransparency': False,
                        'height': 354,
                        'pHash': '2e0ed1f12eda9525',
                        'quality': 0,
                        'size': 7390,
                        'width': 236
                    }
                },
                'density': 250,
                'exif': {},
                'format': 'jpg',
                'has_color_profile': False,
                'has_transparency': False,
                'height': 354,
                'p_hash': '2e0ed1f12eda9525',
                'quality': 0,
                'size': 7390,
                'width': 236
            }
        }
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/metadata?url=https%3A%2F%2Fexample.com%2Ffakeid%2Ffakeimage.jpg",
                         responses.calls[0].request.url)


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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, self.file_id)
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
        self.assertEqual("http://test.com/v1/files/fake_123/details/", responses.calls[0].request.url)

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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)
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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, self.file_id)

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
        self.assertEqual("http://test.com/v1/files/fake_123/versions", responses.calls[0].request.url)

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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, self.file_id, self.version_id)
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
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, self.file_id, self.version_id)

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
        self.assertEqual("http://test.com/v1/files/fake_123/versions/fake_version_123", responses.calls[0].request.url)

    @responses.activate
    def test_get_file_version_details_fails_with_404_exception(self) -> None:
        """Test get file version details raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, self.file_id, self.version_id)
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

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, self.file_id, self.version_id)
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


class TestDeleteFileVersion(ClientTestCase):
    version_id = "fake_123_version_id"
    file_id = "fax_abx1223"

    @responses.activate
    def test_delete_file_version_fails_with_404_exception(self) -> None:
        """Test delete_file_version raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, self.file_id, self.version_id)
        try:
            responses.add(
                responses.DELETE,
                url,
                status=404,
                body=json.dumps({"message": "The requested file version does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )
            self.client.delete_file_version(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file version does not exist.", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])

    @responses.activate
    def test_delete_file_version_succeeds(self) -> None:
        """Test delete_file_version succeeds with file and version Id"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, self.file_id, self.version_id)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.DELETE,
            url,
            status=204,
            headers=headers
        )
        resp = self.client.delete_file_version(self.file_id, self.version_id)

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 204,
                    'raw': None
                }
            }
        }

        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/fax_abx1223/versions/fake_123_version_id",
                         responses.calls[0].request.url)


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
            body=json.dumps({
                "message": "No file found with filePath /source_file.jpg",
                "help": "For support kindly contact us at support@imagekit.io .",
                "reason": "SOURCE_FILE_MISSING"
            })
        )
        try:
            self.client.copy_file({"source_file_path": self.source_file_path,
                                   "destination_path": self.destination_path,
                                   "include_file_versions": False})
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No file found with filePath /source_file.jpg", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])

    @responses.activate
    def test_copy_file_succeeds(self) -> None:
        """Test copy_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=204,
            headers=headers
        )
        resp = self.client.copy_file({"source_file_path": self.source_file_path,
                                      "destination_path": self.destination_path,
                                      "include_file_versions": True})

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 204,
                    'raw': None
                }
            }
        }

        request_body = json.dumps({
            "sourceFilePath": "/source_file.jpg",
            "destinationPath": "/destination_path",
            "includeFileVersions": True
        })

        self.assertEqual(request_body, responses.calls[0].request.body)

        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/copy", responses.calls[0].request.url)


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
            body=json.dumps({
                "message": "No file found with filePath /source_file.jpg",
                "help": "For support kindly contact us at support@imagekit.io .",
                "reason": "SOURCE_FILE_MISSING"
            })
        )
        try:
            self.client.move_file({"source_file_path": self.source_file_path,
                                   "destination_path": self.destination_path})
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No file found with filePath /source_file.jpg", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])

    @responses.activate
    def test_move_file_succeeds(self) -> None:
        """Test move_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/move".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=204,
            headers=headers
        )
        resp = self.client.move_file({"source_file_path": self.source_file_path,
                                      "destination_path": self.destination_path})

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 204,
                    'raw': None
                }
            }
        }

        request_body = json.dumps({
            "sourceFilePath": "/source_file.jpg",
            "destinationPath": "/destination_path",
        })

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/move", responses.calls[0].request.url)


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
                body=json.dumps({
                    "message": "File with name testing-binary.jpg already exists at the same location.",
                    "help": "For support kindly contact us at support@imagekit.io .",
                    "reason": "FILE_ALREADY_EXISTS"
                })
            )
            self.client.rename_file({"file_path": self.file_path,
                                     "new_file_name": self.new_file_name})
            self.assertRaises(ConflictException)
        except ConflictException as e:
            self.assertEqual("File with name testing-binary.jpg already exists at the same location.", e.message)
            self.assertEqual(409, e.response_metadata['httpStatusCode'])
            self.assertEqual("FILE_ALREADY_EXISTS", e.response_metadata['raw']['reason'])

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
            body=json.dumps({"purgeRequestId": "62de3e986f68334a5a3339fb"})
        )
        resp = self.client.rename_file({"file_path": self.file_path,
                                        "new_file_name": self.new_file_name,
                                        "purge_cache": True})

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 200,
                    'raw': {
                        'purgeRequestId': '62de3e986f68334a5a3339fb'
                    }
                },
                'purge_request_id': '62de3e986f68334a5a3339fb'
            }
        }

        request_body = json.dumps({
            "filePath": "/file_path.jpg",
            "newFileName": "new_file.jpg",
            "purgeCache": True
        })

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/rename", responses.calls[0].request.url)

    @responses.activate
    def test_rename_file_succeeds(self) -> None:
        """Test rename_file succeeds"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body=json.dumps({})
        )
        resp = self.client.rename_file({"file_path": self.file_path,
                                        "new_file_name": self.new_file_name})

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 200,
                    'raw': None
                }
            }
        }

        request_body = json.dumps({
            "filePath": "/file_path.jpg",
            "newFileName": "new_file.jpg"
        })

        self.assertEqual(request_body, responses.calls[0].request.body)
        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/rename", responses.calls[0].request.url)


class TestRestoreFileVersion(ClientTestCase):
    version_id = "fake_123_version_id"
    file_id = "fax_abx1223"

    @responses.activate
    def test_restore_file_version_fails_with_404_exception(self) -> None:
        """Test restore_file_version raises 404 error"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}/restore".format(URL.API_BASE_URL, self.file_id, self.version_id)
        try:
            responses.add(
                responses.PUT,
                url,
                status=404,
                body=json.dumps({"message": "The requested file version does not exist.",
                                 "help": "For support kindly contact us at support@imagekit.io ."}),
            )
            self.client.restore_file_version(self.file_id, self.version_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("The requested file version does not exist.", e.message)
            self.assertEqual(404, e.response_metadata['httpStatusCode'])

    @responses.activate
    def test_restore_file_version_succeeds(self) -> None:
        """Test restore_file_version succeeds with file and version Id"""

        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/files/{}/versions/{}/restore".format(URL.API_BASE_URL, self.file_id, self.version_id)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PUT,
            url,
            headers=headers,
            body=json.dumps({
                "fileId": "fileId",
                "type": "file",
                "name": "file1.jpg",
                "filePath": "/images/file.jpg",
                "tags": ["t-shirt", "round-neck", "sale2019"],
                "AITags": [
                    {
                        "name": "Shirt",
                        "confidence": 90.12,
                        "source": "google-auto-tagging"
                    },
                ],
                "versionInfo": {
                    "id": "versionId",
                    "name": "Version 2"
                },
                "isPrivateFile": False,
                "customCoordinates": None,
                "url": "https://ik.imagekit.io/your_imagekit_id/images/products/file1.jpg",
                "thumbnail": "https://ik.imagekit.io/your_imagekit_id/tr:n-media_library_thumbnail/images/products/file1.jpg",
                "fileType": "image",
                "mime": "image/jpeg",
                "width": 100,
                "height": 100,
                "size": 100,
                "hasAlpha": False,
                "customMetadata": {
                    "brand": "Nike",
                    "color": "red"
                },
                "createdAt": "2019-08-24T06:14:41.313Z",
                "updatedAt": "2019-09-24T06:14:41.313Z"
            })
        )
        resp = self.client.restore_file_version(self.file_id, self.version_id)

        mock_resp = {
            'error': None,
            'response': {
                '_response_metadata': {
                    'headers': {
                        'Content-Type': 'text/plain, application/json',
                        'Accept-Encoding': 'gzip, deflate',
                        'Authorization': 'Basic ZmFrZTEyMjo='
                    },
                    'httpStatusCode': 200,
                    'raw': {
                        'AITags': [{
                            'confidence': 90.12,
                            'name': 'Shirt',
                            'source': 'google-auto-tagging'
                        }],
                        'createdAt': '2019-08-24T06:14:41.313Z',
                        'customCoordinates': None,
                        'customMetadata': {
                            'brand': 'Nike',
                            'color': 'red'
                        },
                        'fileId': 'fileId',
                        'filePath': '/images/file.jpg',
                        'fileType': 'image',
                        'hasAlpha': False,
                        'height': 100,
                        'isPrivateFile': False,
                        'mime': 'image/jpeg',
                        'name': 'file1.jpg',
                        'size': 100,
                        'tags': ['t-shirt',
                                 'round-neck',
                                 'sale2019'
                                 ],
                        'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-media_library_thumbnail/images/products/file1.jpg',
                        'type': 'file',
                        'updatedAt': '2019-09-24T06:14:41.313Z',
                        'url': 'https://ik.imagekit.io/your_imagekit_id/images/products/file1.jpg',
                        'versionInfo': {
                            'id': 'versionId',
                            'name': 'Version '
                                    '2'
                        },
                        'width': 100
                    }
                },
                'ai_tags': [{
                    'confidence': 90.12,
                    'name': 'Shirt',
                    'source': 'google-auto-tagging'
                }],
                'created_at': '2019-08-24T06:14:41.313Z',
                'custom_coordinates': None,
                'custom_metadata': {
                    'brand': 'Nike',
                    'color': 'red'
                },
                'embedded_metadata': {},
                'extension_status': {},
                'file_id': 'fileId',
                'file_path': '/images/file.jpg',
                'file_type': 'image',
                'has_alpha': False,
                'height': 100,
                'is_private_file': False,
                'mime': 'image/jpeg',
                'name': 'file1.jpg',
                'size': 100,
                'tags': ['t-shirt', 'round-neck', 'sale2019'],
                'thumbnail': 'https://ik.imagekit.io/your_imagekit_id/tr:n-media_library_thumbnail/images/products/file1.jpg',
                'type': 'file',
                'updated_at': '2019-09-24T06:14:41.313Z',
                'url': 'https://ik.imagekit.io/your_imagekit_id/images/products/file1.jpg',
                'version_info': {
                    'id': 'versionId',
                    'name': 'Version 2'
                },
                'width': 100
            }
        }

        self.assertEqual(mock_resp, resp)
        self.assertEqual("http://test.com/v1/files/fax_abx1223/versions/fake_123_version_id/restore",
                         responses.calls[0].request.url)
