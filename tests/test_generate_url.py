import unittest

from imagekitio.client import ImageKit
from imagekitio.constants.defaults import Default


class TestGenerateURL(unittest.TestCase):
    def setUp(self) -> None:
        self.client = ImageKit(
            private_key="private_key_test",
            public_key="public_key_test",
            url_endpoint="https://test-domain.com/test-endpoint",
        )

    def test_generate_url_with_path(self):
        options = {
            "path": "/default-image.jpg",
            "transformation": [{"height": "300", "width": "400"}],
        }
        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://test-domain.com/test-endpoint/tr:h-300,w-400/default-image.jpg?ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_url_contains_ik_sdk_version(self):
        options = {
            "path": "/default-image.jpg",
            "transformation": [{"height": "300", "width": "400"}],
        }
        url = self.client.url(options)
        self.assertIn("ik-sdk-version", url)
        self.assertEqual(
            url,
            "https://test-domain.com/test-endpoint/tr:h-300,w-400/default-image.jpg?ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_generate_url_without_leading_slash_in_path(self):
        options = {
            "path": "default-image.jpg",
            "transformation": [{"height": "300", "width": "400"}],
        }
        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://test-domain.com/test-endpoint/tr:h-300,w-400/default-image.jpg?ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_overriding_url_endpoint_generation_consists_new_url(self):
        """
        Overriding urlEndpoint parameter. Passing a urlEndpoint value which is
        different from what I've used during SDK initialization and see if the url
        returned is using this new parameter
        """
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/new/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
        }

        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/new/endpoint/tr:h-300,w-400/default-image.jpg?ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_overriding_url_endpoint_without_slash_generation_consists_new_url(self):
        """
        Overriding urlEndpoint parameter. Passing a urlEndpoint value without slash
        """
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/new/endpoint",
            "transformation": [{"height": "300", "width": "400"}],
        }

        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/new/endpoint/tr:h-300,w-400/default-image.jpg?ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_generate_url_query_parameters(self):
        options = {
            "path": "/default-image.jpg",
            "query_parameters": {
                "param1": "value1",
                "param2": "value2"
            },
            "transformation": [
                {
                    "height": "300",
                    "width": "400"
                }
            ],
        }
        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://test-domain.com/test-endpoint/tr:h-300,w-400/default-image.jpg?param1=value1&param2=value2&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_generate_url_with_src(self):
        options = {
            "src": "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg",
            "transformation": [
                {
                    "height": "300",
                    "width": "400",
                    "format": "jpg",
                    "progressive": "true",
                    "effect_contrast": "1",
                },
                {"rotation": 90},
            ],
        }
        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg?tr=h-300%2Cw-400%2Cf-jpg%2Cpr-true%2Ce-contrast-1%3Art-90&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_generate_url_with_src_with_query_params_double(self):
        options = {
            "src": "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg?queryparam1=value1",
            "query_parameters": {
                "param1": "value1"
            },
            "transformation": [
                {
                    "height": "300",
                    "width": "400",
                    "format": "jpg",
                    "progressive": "true",
                    "effect_contrast": "1",
                },
                {"rotation": 90},
            ],
        }
        url = self.client.url(options)
        # @TODO - adjust value of param1=value1 in test case but it should be there
        self.assertEqual(
            url,
            "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg?queryparam1=value1&param1=value1&tr=h-300%2Cw-400%2Cf-jpg%2Cpr-true%2Ce-contrast-1%3Art-90&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            )
        )

    def test_generate_url_with_path_and_signed(self):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
            "signed": True,
        }

        url = self.client.url(options)
        self.assertIsNot(url, "")
        self.assertIn(options["url_endpoint"], url)
        self.assertIn("300", url)
        self.assertIn("300", url)

        self.assertNotIn("&&", url)
        self.assertNotIn("??", url)

        url = self.client.url(options)
        self.assertEqual(url.split("default-image.jpg")[1][:1], "?")
        self.assertNotEqual(url.split("default-image.jpg")[0][-2:], "//")

    def test_generate_url_with_path_and_signed_in_proper_form(self):
        """
        Check path param url generation doesn't contain double slash
        """
        options = {
            "path": "/test-signed-url.jpg",
            "signed": True,
            "transformation": [{"width": 100}],
        }

        url = self.client.url(options)
        self.assertIn("ik-s", url)

    def test_url_with_new_transformation_returns_as_it_is(self):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "fake_xxxx": "400"}],
            "transformation_position": "query",
        }

        url = self.client.url(options)
        self.assertIn("fake_xxxx", url)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300%2Cfake_xxxx-400&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_query_url_generation_transformation_as_query_and_transformations_in_url(
        self,
    ):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300"}],
            "transformation_position": "query",
        }

        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_generate_url_with_chained_transformations(self):
        options = {
            "src": "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg",
            "transformation": [
                {
                    "height": "300",
                    "width": "400",
                    "format": "jpg",
                    "progressive": "true",
                    "effect_contrast": "1",
                },
                {"rotation": 90},
            ],
        }
        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg?tr=h-300%2Cw-400%2Cf-jpg%2Cpr-true%2Ce-contrast-1%3Art-90&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_url_check_query_param_are_added_correctly(self):
        options = {
            "path": "/default-image.jpg?client=123&user=5",
            "transformation": [{"height": "300", "width": "400"}],
            "transformation_position": "query",
        }
        url = self.client.url(options)
        self.assertEqual(url,
                         "https://test-domain.com/test-endpoint/default-image.jpg?client=123&user=5&tr=h-300%2Cw-400&ik-sdk-version={}".format(
                             Default.SDK_VERSION.value))

    def test_generate_url_with_src_query_parameters_merge_correctly(self):
        options = {
            "src": "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg?client=123&ab=c",
            "transformation": [
                {
                    "height": "300",
                    "width": "400",
                    "format": "jpg",
                    "progressive": "true",
                    "effect_contrast": "1",
                },
                {"rotation": 90},
            ],
        }
        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg?client=123&ab=c&tr=h-300%2Cw-400%2Cf-jpg%2Cpr-true%2Ce-contrast-1%3Art-90&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_generate_url_with_src_and_transformation_position_path(self):
        options = {
            "src": "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg",
            "transformation": [
                {
                    "height": "300",
                    "width": "400",
                    "format": "jpg",
                    "progressive": "true",
                    "effect_contrast": "1",
                },
                {"rotation": 90},
            ],
            "transformation_position": "path",
        }
        url = self.client.url(options)
        self.assertEqual(
            url,
            "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg?tr=h-300%2Cw-400%2Cf-jpg%2Cpr-true%2Ce-contrast-1%3Art-90&ik-sdk-version={}".format(
                Default.SDK_VERSION.value
            ),
        )

    def test_url_with_invalid_trans_pos(self):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
            "signed": True,
            "transformation_position": "fake",
        }
        self.assertRaises((KeyError, ValueError), self.client.url, options)

    def test_url_without_path_and_src(self):
        options = {
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
            "signed": True,
        }
        self.assertEqual(self.client.url(options), "")

    def test_url_contains_sdk_version(self):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
            "signed": True,
            "transformation_position": "query",
        }

        self.assertIn("ik-sdk-version", self.client.url(options))

    def test_url_contains_slash_if_transformation_position_is_path(self):
        options = {
            "path": "/default-image.jpg",
            "transformation": [
                {
                    "height": "300",
                    "width": "400",
                    "format": "jpg",
                    "progressive": "true",
                    "effect_sharpen": "-",
                    "effect_contrast": "1",
                },
                {"rotation": 90},
            ],
            "transformation_position": "path",
        }
        url = self.client.url(options)
        self.assertEqual(url.split("tr:h-300")[0][-1], "/")
        self.assertNotEqual(url.split("default-image.jpg")[0][-2:], "//")

    def test_url_signed_with_expire_in_seconds(self):
        options = {
            "path": "/default-image.jpg",
            "transformation": [
                {
                    "width": "400",
                },
            ],
            "signed": True,
            "expire_seconds": 100,
        }
        url = self.client.url(options)
        self.assertIn("ik-t", url)

    def test_get_signature_with_100_expire_seconds(self):
        url = "https://test-domain.com/test-endpoint/tr:w-100/test-signed-url.png"
        signature = self.client.url_obj.get_signature(
            "private_key_test", url, "https://test-domain.com/test-endpoint/", 100)
        self.assertEqual(signature, "5e5037a31a7121cbe2964e220b4338cc6e1ba66d")

    def test_get_signature_without_expire_seconds(self):
        url = "https://test-domain.com/test-endpoint/tr:w-100/test-signed-url.png"
        signature = self.client.url_obj.get_signature(
            "private_key_test", url, "https://test-domain.com/test-endpoint/", 0)
        self.assertEqual(signature, "41b3075c40bc84147eb71b8b49ae7fbf349d0f00")

    def test_get_signature_without_expire_seconds_without_slash(self):
        url = "https://test-domain.com/test-endpoint/tr:w-100/test-signed-url.png"
        signature = self.client.url_obj.get_signature(
            "private_key_test", url, "https://test-domain.com/test-endpoint", 0)
        self.assertEqual(signature, "41b3075c40bc84147eb71b8b49ae7fbf349d0f00")
