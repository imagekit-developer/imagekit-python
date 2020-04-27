import unittest
from unittest.mock import MagicMock

from imagekitio.client import ImageKit
from tests.dummy_data.file import SUCCESS_DETAIL_MSG
from tests.helpers import ClientTestCase, get_mocked_success_resp

imagekit_obj = ImageKit(
    private_key="private_fake:", public_key="public_fake123:", url_endpoint="fake.com",
)


class TestPHashDistance(unittest.TestCase):
    def test_phash_distance(self):
        """Tests if phash_distance working properly
        """
        a, b = ("33699c96619cc69e", "968e978414fe04ea")
        c, d = ("33699c96619cc69e", "33699c96619cc69e")
        e, f = ("a4a65595ac94518b", "7838873e791f8400")

        self.assertEqual(imagekit_obj.phash_distance(a, b), 30)
        self.assertEqual(imagekit_obj.phash_distance(c, d), 0)
        self.assertEqual(imagekit_obj.phash_distance(e, f), 37)
        self.assertRaises(TypeError, imagekit_obj.phash_distance, "", "dkf90")
        self.assertRaises(TypeError, imagekit_obj.phash_distance, 1234, 111)


class TestClientAndImageKitObjInit(ClientTestCase):
    """
    Tests client and Imagekit classes object initialization
    """

    def test_all_variable_is_being_set_to_obj(self) -> None:
        """
        Tests if variables are properly being set when creating
        an object from ImageKit class
        """
        self.assertIsNotNone(self.client.ik_request)
        self.assertIsNotNone(self.client.url_obj)
        self.assertIsNotNone(self.client.file)


class TestGetAuthenticationParameters(ClientTestCase):
    def test_get_authentication_parameters_without_token(self) -> None:
        result = self.client.get_authentication_parameters("", expire=444)
        self.assertIsNotNone(result)

    def test_get_authentication_param_with_token(self) -> None:
        result = self.client.get_authentication_parameters(
            "dc45da6e3286066265a09e", expire=4555
        )
        self.assertIsNotNone(result)
