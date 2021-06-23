import base64
import json
import os
from unittest.mock import MagicMock

from imagekitio.client import ImageKit
from imagekitio.constants.url import URL
from tests.dummy_data.file import (
    FAILED_DELETE_RESP,
    SUCCESS_DETAIL_MSG,
    SUCCESS_LIST_RESP_MESSAGE,
    SUCCESS_PURGE_CACHE_MSG,
    SUCCESS_PURGE_CACHE_STATUS_MSG,
)
from tests.helpers import (
    ClientTestCase,
    get_mocked_failed_resp,
    get_mocked_failed_resp_text,
    get_mocked_success_resp,
)
from imagekitio.utils.formatter import request_formatter


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

    def test_upload_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted

        """

        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.upload(file=self.image, file_name=self.filename)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_binary_upload_succeeds(self):
        """
        Tests if  upload succeeds
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        file = open(self.image, "rb")
        file.close()
        resp = self.client.upload(file=file, file_name=self.filename)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_base64_upload_succeeds(self):
        """
        Tests if  upload succeeds
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        with open(self.image, mode="rb") as img:
            imgstr = base64.b64encode(img.read())

        resp = self.client.upload(file=imgstr, file_name=self.filename)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_url_upload_succeeds(self):
        """
        Tests if  url upload succeeds
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.upload(file="example.com/abc.jpg", file_name=self.filename)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_file_upload_succeeds(self):
        """
        Tests if  file upload succeeds
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )

        # generate expected encoded private key for the auth headers
        private_key_file_upload = ClientTestCase.private_key
        if private_key_file_upload != ":":
            private_key_file_upload += ":"
        encoded_private_key = base64.b64encode(private_key_file_upload.encode()).decode(
            "utf-8"
        )

        resp = self.client.upload_file(file=self.image, file_name=self.filename)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])
        self.client.ik_request.request.assert_called_once_with(
            "Post", 
            url=URL.UPLOAD_URL.value,
            files={
                'file': (None, self.image), 
                'fileName': (None, self.filename)
                },
            data={},
            headers={'Accept-Encoding': 'gzip, deflate', 'Authorization': "Basic {}".format(encoded_private_key)}
        )


    def test_upload_fails_without_file_or_file_name(self) -> None:
        """Test upload raises error on missing required params
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(TypeError, self.client.upload, file_name=self.filename)
        self.assertRaises(TypeError, self.client.upload, file=self.image)

    def test_absence_of_params_gives_proper_resp(self) -> None:
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.upload(
            file=self.image,
            file_name="x",
            options={
                "is_private_file": "",
                "tags": None,
                "custom_coordinates": None,
                "use_unique_file_name": None,
                "folder": None

            }
        )
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_all_params_being_passed_on_upload(self) -> None:
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.upload(
            file=self.image,
            file_name="fileabc",
            options={
                "is_private_file": True,
                "tags": ["abc"],
                "response_fields": ["is_private_file", "tags"],
                "custom_coordinates": "10,10,100,100",
                "use_unique_file_name": True,
                "folder": "abc"
            }
        )
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_upload_file_fails_without_file_or_file_name(self) -> None:
        """Test upload raises error on missing required params
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        self.assertRaises(TypeError, self.client.upload_file, file_name=self.filename)
        self.assertRaises(TypeError, self.client.upload_file, file=self.image)

    def test_upload_file_fails_without_json_response_from_server(self) -> None:
        """Test upload raises error on non json response
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp_text()
        )
        resp = self.client.upload(
            file=self.image,
            file_name="fileabc",
            options={
                "is_private_file": True,
                "tags": ["abc"],
                "response_fields": ["is_private_file", "tags"],
                "custom_coordinates": "10,10,100,100",
                "use_unique_file_name": True,
                "folder": "abc"
            }
        )
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])


class TestListFiles(ClientTestCase):
    """
    TestListFiles class used to test list_files method
    """

    def test_list_files_fails_on_unauthenticated_request(self) -> None:
        """ Tests unauthenticated request restricted for list_files method
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.list_files(self.options)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_list_files_succeeds_with_basic_request(self) -> None:
        """
        Tests if list_files work with skip and limit
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp(message=SUCCESS_LIST_RESP_MESSAGE)
        )

        resp = self.client.list_files(self.options)

        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_list_accepting_all_parameter(self):
        """
        checking if list accept all parameter
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )
        resp = self.client.list_files(
            options={
                "file_type": "image",
                "tags": ["tag1", "tag2"],
                "include_folder": True,
                "name": "new-dir",
                "limit": "1",
                "skip": "1",
            },
        )

        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])


class TestGetFileDetails(ClientTestCase):
    """
    TestGetFileDetails class used to test get_file_details method
    """

    file_id = "fake_file_id1234"
    file_url = "https://example.com/default.jpg"

    def test_get_file_details_fails_on_unauthenticated_request(self) -> None:
        """Tests if get_file_details raise error on unauthenticated request
        """

        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.get_file_details(self.file_id)
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_file_details_succeeds_with_id(self) -> None:
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp(message=SUCCESS_DETAIL_MSG)
        )
        resp = self.client.get_file_details(self.file_id)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])

    def test_file_details_succeeds_with_url(self) -> None:
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp(message=SUCCESS_DETAIL_MSG)
        )
        resp = self.client.get_file_details(self.file_url)
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])


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

    def test_bulk_file_delete_fails_on_unauthenticated_request(self) -> None:
        """Test bulk_file_delete on unauthenticated request
        this function checks if raises error on unauthenticated request
        to check if bulk_delete is only restricted to authenticated
        requests
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.bulk_file_delete(self.bulk_delete_ids)

        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_file_delete_fails_on_item_not_found(self):
        """Test delete_file on unavailable content
        this function raising expected error if the file
        is not available
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp(message=FAILED_DELETE_RESP)
        )
        resp = self.client.delete_file(self.file_id)

        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_file_delete_succeeds(self):
        """Test delete file on authenticated request
        this function tests if delete_file working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp({"error": None, "response": None})
        )
        resp = self.client.delete_file(self.file_id)

        self.assertIsNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_bulk_file_delete_succeeds(self):
        """Test bulk_delete  on authenticated request
        this function tests if bulk_file_delete working properly
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp({"error": None, "response": {'successfullyDeletedFileIds': ['5e785a03ed03082733b979ec', '5e787c4427dd2a6c2fc564a5']}})
        )
        resp = self.client.bulk_file_delete(self.bulk_delete_ids)

        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])


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

    def test_update_file_details_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted

        """

        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_failed_resp()
        )
        resp = self.client.update_file_details(
            file_id=self.file_id, options=self.valid_options
        )
        self.assertIsNotNone(resp["error"])
        self.assertIsNone(resp["response"])

    def test_update_file_details_succeeds_with_id(self):
        """
        Tests if  update_file_details succeeds with file_url
        """
        self.client.ik_request.request = MagicMock(
            return_value=get_mocked_success_resp()
        )

        # generate expected encoded private key for the auth headers
        private_key_file_upload = ClientTestCase.private_key
        if private_key_file_upload != ":":
            private_key_file_upload += ":"
        encoded_private_key = base64.b64encode(private_key_file_upload.encode()).decode(
            "utf-8"
        )

        resp = self.client.update_file_details(
            file_id=self.file_id, options=self.valid_options
        )
        self.assertIsNone(resp["error"])
        self.assertIsNotNone(resp["response"])
        self.client.ik_request.request.assert_called_once_with(
            method="Patch", 
            url="{}/{}/details/".format(URL.BASE_URL.value, self.file_id),
            headers={'Content-Type': 'application/json', 'Authorization': "Basic {}".format(encoded_private_key)},
            data=json.dumps(request_formatter(self.valid_options))
        )

    def test_file_details_succeeds_with_url(self):
        self.client.ik_request = MagicMock(return_value=get_mocked_success_resp())
