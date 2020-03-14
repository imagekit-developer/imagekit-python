import unittest

from imagekitio.client import ImageKit


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
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
        }

        url = self.client.url(options)
        self.assertIsNot(url, "")
        self.assertIn(options["url_endpoint"], url)
        self.assertIn("300", url)
        self.assertIn("300", url)
        self.assertIn(
            "https://ik.imagekit.io/your_imagekit_id/endpoint/tr:h-300,w-400/default-image.jpg",
            url,
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
        self.assertIsNot(url, "")
        self.assertIn(options["url_endpoint"], url)
        self.assertIn("300", url)
        self.assertIn("300", url)
        self.assertIn("new/endpoint", url)
        self.assertNotEqual(url[:-1], "/")

    def test_generate_url_with_src(self):
        options = {
            "src": "https://ik.imagekit.io/ldt7znpgpjs/test_YhNhoRxWt.jpg",
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
            "transformation_position": "query",
            "signed": True,
            "expire_seconds": 30,
        }
        url = self.client.url(options)
        self.assertIn("300", url)
        self.assertIn("?", url)
        self.assertNotIn("&&", url)
        self.assertNotIn("??", url)

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
        # options = {
        #     "path": "/default-image.jpg",
        #     "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
        #     "transformation": [{"height": "300", "width": "400"}],
        #     "signed": True,
        # }

        options = {
            "path": "/test-signed-url.jpg",
            "signed": True,
            "transformation": [{"width": 100}],
        }

        url = self.client.url(options)
        self.assertIn('ik-s', url)

    def test_url_with_invalid_transformation_returns_as_it_is(self):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "fake_xxxx": "400"}],
            "transformation_position": "query",
        }

        url = self.client.url(options)
        self.assertIn("fake_xxxx", url)

    def test_query_url_generation_transformation_as_query_and_transformations_in_url(self):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300"}],
            "transformation_position": "query",
        }

        url = self.client.url(options)
        # check if query url
        self.assertEqual(url.split("/default-image.jpg")[1][0], "?")
        # query parameter being added to url
        self.assertEqual(url.split("?tr=")[1][0], "h")

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

    def test_url_with_signed_without_seconds(self):
        options = {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
            "signed": True,
            "transformation_position": "query",
        }

        self.assertIsNot(self.client.url(options), "")

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
