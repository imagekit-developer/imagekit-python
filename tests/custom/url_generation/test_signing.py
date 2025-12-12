"""Signing URL tests - converted from Ruby SDK."""

from typing import TYPE_CHECKING

import pytest

from imagekitio import ImageKit

if TYPE_CHECKING:
    from imagekitio._client import ImageKit as ImageKitType


class TestSigning:
    """Test URL signing functionality."""

    client: "ImageKitType"

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Set up test client."""
        self.client = ImageKit(private_key="dummy-key")

    def test_should_generate_a_signed_url_when_signed_is_true_without_expires_in(self) -> None:
        """Should generate a signed URL when signed is true without expires_in."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/future-search.png", url_endpoint="https://ik.imagekit.io/demo/", signed=True
        )

        expected = "https://ik.imagekit.io/demo/sdk-testing-files/future-search.png?ik-s=32dbbbfc5f945c0403c71b54c38e76896ef2d6b0"
        assert url == expected

    def test_should_generate_a_signed_url_when_signed_is_true_with_expires_in(self) -> None:
        """Should generate a signed URL when signed is true with expires_in."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/future-search.png",
            url_endpoint="https://ik.imagekit.io/demo/",
            signed=True,
            expires_in=3600,
        )

        # Expect ik-t exist in the URL. We don't assert signature because it will keep changing.
        assert "ik-t" in url

    def test_should_generate_a_signed_url_when_expires_in_is_above_0_and_even_if_signed_is_false(self) -> None:
        """Should generate a signed URL when expires_in is above 0 and even if signed is false."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/future-search.png",
            url_endpoint="https://ik.imagekit.io/demo/",
            signed=False,
            expires_in=3600,
        )

        # Expect ik-t exist in the URL. We don't assert signature because it will keep changing.
        assert "ik-t" in url

    def test_should_generate_signed_url_with_special_characters_in_filename(self) -> None:
        """Should generate signed URL with special characters in filename."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/हिन्दी.png", url_endpoint="https://ik.imagekit.io/demo/", signed=True
        )

        expected = "https://ik.imagekit.io/demo/sdk-testing-files/%E0%A4%B9%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A5%80.png?ik-s=3fff2f31da1f45e007adcdbe95f88c8c330e743c"
        assert url == expected

    def test_should_generate_signed_url_with_text_overlay_containing_special_characters(self) -> None:
        """Should generate signed URL with text overlay containing special characters."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/हिन्दी.png",
            url_endpoint="https://ik.imagekit.io/demo/",
            transformation=[
                {
                    "overlay": {
                        "type": "text",
                        "text": "हिन्दी",
                        "transformation": [
                            {
                                "font_color": "red",
                                "font_size": "32",
                                "font_family": "sdk-testing-files/Poppins-Regular_Q15GrYWmL.ttf",
                            }
                        ],
                    }
                }
            ],
            signed=True,
        )

        expected = "https://ik.imagekit.io/demo/sdk-testing-files/%E0%A4%B9%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A5%80.png?tr=l-text,ie-4KS54KS%2F4KSo4KWN4KSm4KWA,co-red,fs-32,ff-sdk-testing-files@@Poppins-Regular_Q15GrYWmL.ttf,l-end&ik-s=ac9f24a03080102555e492185533c1ae6bd93fa7"
        assert url == expected

    def test_should_generate_signed_url_with_text_overlay_and_special_characters_using_path_transformation_position(
        self,
    ) -> None:
        """Should generate signed URL with text overlay and special characters using path transformation position."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/हिन्दी.png",
            url_endpoint="https://ik.imagekit.io/demo/",
            transformation_position="path",
            transformation=[
                {
                    "overlay": {
                        "type": "text",
                        "text": "हिन्दी",
                        "transformation": [
                            {
                                "font_color": "red",
                                "font_size": "32",
                                "font_family": "sdk-testing-files/Poppins-Regular_Q15GrYWmL.ttf",
                            }
                        ],
                    }
                }
            ],
            signed=True,
        )

        expected = "https://ik.imagekit.io/demo/tr:l-text,ie-4KS54KS%2F4KSo4KWN4KSm4KWA,co-red,fs-32,ff-sdk-testing-files@@Poppins-Regular_Q15GrYWmL.ttf,l-end/sdk-testing-files/%E0%A4%B9%E0%A4%BF%E0%A4%A8%E0%A5%8D%E0%A4%A6%E0%A5%80.png?ik-s=69f2ecbb7364bbbad24616e1f7f1bac5a560fc71"
        assert url == expected

    def test_should_generate_signed_url_with_query_parameters(self) -> None:
        """Should generate signed URL with query parameters."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/future-search.png",
            url_endpoint="https://ik.imagekit.io/demo/",
            query_parameters={"version": "1.0", "cache": "false"},
            signed=True,
        )

        expected = "https://ik.imagekit.io/demo/sdk-testing-files/future-search.png?version=1.0&cache=false&ik-s=f2e5a1b8b6a0b03fd63789dfc6413a94acef9fd8"
        assert url == expected

    def test_should_generate_signed_url_with_transformations_and_query_parameters(self) -> None:
        """Should generate signed URL with transformations and query parameters."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/future-search.png",
            url_endpoint="https://ik.imagekit.io/demo/",
            transformation=[{"width": 300, "height": 200}],
            query_parameters={"version": "2.0"},
            signed=True,
        )

        expected = "https://ik.imagekit.io/demo/sdk-testing-files/future-search.png?version=2.0&tr=w-300,h-200&ik-s=601d97a7834b7554f4dabf0d3fc3a219ceeb6b31"
        assert url == expected

    def test_should_not_sign_url_when_signed_is_false(self) -> None:
        """Should not sign URL when signed is false."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/future-search.png", url_endpoint="https://ik.imagekit.io/demo/", signed=False
        )

        expected = "https://ik.imagekit.io/demo/sdk-testing-files/future-search.png"
        assert url == expected
        assert "ik-s=" not in url
        assert "ik-t=" not in url

    def test_should_generate_signed_url_with_transformations_in_path_position_and_query_parameters(self) -> None:
        """Should generate signed URL with transformations in path position and query parameters."""
        url = self.client.helper.build_url(
            src="sdk-testing-files/future-search.png",
            url_endpoint="https://ik.imagekit.io/demo/",
            transformation=[{"width": 300, "height": 200}],
            transformation_position="path",
            query_parameters={"version": "2.0"},
            signed=True,
        )

        expected = "https://ik.imagekit.io/demo/tr:w-300,h-200/sdk-testing-files/future-search.png?version=2.0&ik-s=dd1ee8f83d019bc59fd57a5fc4674a11eb8a3496"
        assert url == expected
