import unittest
from imagekitio.client import ImageKit
from imagekitio.utils.calculation import get_authenticated_params


class TestUtilCalculation(unittest.TestCase):

    def test_get_authenticated_params(self):
        """Test authenticated_params returning proper value
        :return: param dict
        """
        result = get_authenticated_params(token='your_token', expire="1582269249", private_key="private_key_test")
        self.assertEqual(result['token'], 'your_token')
        self.assertEqual(result['expire'], '1582269249')
        self.assertEqual(result['signature'], 'e71bcd6031016b060d349d212e23e85c791decdd')
