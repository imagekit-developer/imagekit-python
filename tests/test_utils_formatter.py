import unittest

from imagekitio.utils.formatter import camel_to_snake, request_formatter


class TestFormatterClass(unittest.TestCase):
    """
    TestFormatterClass tests if functions on formatter is working properly
    """

    def test_camel_to_snake(self) -> None:
        """
        Test if CamelCase to snake_case is being converted
        properly by camel_to_snake utility function
        """
        self.assertEqual("abc", camel_to_snake("abc"))
        self.assertEqual("_abc", camel_to_snake("_abc"))
        self.assertEqual("", camel_to_snake(""))
        self.assertEqual("my_name", camel_to_snake("myName"))
        self.assertEqual("my_name_", camel_to_snake("myName_"))
        self.assertEqual("url_endpoint", camel_to_snake("urlEndpoint"))
