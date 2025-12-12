"""Basic URL generation tests - converted from Ruby SDK."""

from typing import TYPE_CHECKING

import pytest

from imagekitio import ImageKit

if TYPE_CHECKING:
    from imagekitio._client import ImageKit as ImageKitType


class TestBasicURLGeneration:
    """Test basic URL generation functionality."""

    client: "ImageKitType"

    @pytest.fixture(autouse=True)
    def setup(self) -> None:
        """Set up test client."""
        self.client = ImageKit(private_key="My Private API Key")

    def test_should_return_an_empty_string_when_src_is_not_provided(self) -> None:
        """Should return an empty string when src is not provided."""
        url = self.client.helper.build_url(
            src="", url_endpoint="https://ik.imagekit.io/test_url_endpoint", transformation_position="query"
        )

        assert url == ""

    def test_should_generate_a_valid_url_when_src_is_slash(self) -> None:
        """Should generate a valid URL when src is slash."""
        url = self.client.helper.build_url(
            src="/", url_endpoint="https://ik.imagekit.io/test_url_endpoint", transformation_position="query"
        )

        expected = "https://ik.imagekit.io/test_url_endpoint"
        assert url == expected

    def test_should_generate_a_valid_url_when_src_is_provided_with_transformation(self) -> None:
        """Should generate a valid URL when src is provided with transformation."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg"
        assert url == expected

    def test_should_generate_a_valid_url_when_a_src_is_provided_without_transformation(self) -> None:
        """Should generate a valid URL when a src is provided without transformation."""
        url = self.client.helper.build_url(
            src="https://ik.imagekit.io/test_url_endpoint/test_path_alt.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path_alt.jpg"
        assert url == expected

    def test_should_generate_a_valid_url_when_undefined_transformation_parameters_are_provided_with_path(self) -> None:
        """Should generate a valid URL when undefined transformation parameters are provided with path."""
        url = self.client.helper.build_url(
            src="/test_path_alt.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path_alt.jpg"
        assert url == expected

    def test_by_default_transformation_position_should_be_query(self) -> None:
        """By default transformation position should be query."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation=[{"height": 300, "width": 400}, {"rotation": 90}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400:rt-90"
        assert url == expected

    def test_should_generate_the_url_without_sdk_version(self) -> None:
        """Should generate the URL without SDK version."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation=[{"height": 300, "width": 400}],
            transformation_position="path",
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/tr:h-300,w-400/test_path.jpg"
        assert url == expected

    def test_should_generate_the_correct_url_with_a_valid_src_and_transformation(self) -> None:
        """Should generate the correct URL with a valid src and transformation."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400"
        assert url == expected

    def test_should_add_transformation_as_query_when_src_has_absolute_url_even_if_transformation_position_is_path(
        self,
    ) -> None:
        """Should add transformation as query when src has absolute URL even if transformation position is path."""
        url = self.client.helper.build_url(
            src="https://my.custom.domain.com/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://my.custom.domain.com/test_path.jpg?tr=h-300,w-400"
        assert url == expected

    def test_should_generate_correct_url_when_src_has_query_params(self) -> None:
        """Should generate correct URL when src has query params."""
        url = self.client.helper.build_url(
            src="https://ik.imagekit.io/imagekit_id/new-endpoint/test_path.jpg?t1=v1",
            url_endpoint="https://ik.imagekit.io/imagekit_id/new-endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://ik.imagekit.io/imagekit_id/new-endpoint/test_path.jpg?t1=v1&tr=h-300,w-400"
        assert url == expected

    def test_should_generate_the_correct_url_when_the_provided_path_contains_multiple_leading_slashes(self) -> None:
        """Should generate the correct URL when the provided path contains multiple leading slashes."""
        url = self.client.helper.build_url(
            src="///test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400"
        assert url == expected

    def test_should_generate_the_correct_url_when_the_url_endpoint_is_overridden(self) -> None:
        """Should generate the correct URL when the URL endpoint is overridden."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint_alt",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint_alt/test_path.jpg?tr=h-300,w-400"
        assert url == expected

    def test_should_generate_the_correct_url_with_transformation_position_as_query_parameter_when_src_is_provided(
        self,
    ) -> None:
        """Should generate the correct URL with transformation position as query parameter when src is provided."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400"
        assert url == expected

    def test_should_generate_the_correct_url_with_a_valid_src_parameter_and_transformation(self) -> None:
        """Should generate the correct URL with a valid src parameter and transformation."""
        url = self.client.helper.build_url(
            src="https://ik.imagekit.io/test_url_endpoint/test_path_alt.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path_alt.jpg?tr=h-300,w-400"
        assert url == expected

    def test_should_merge_query_parameters_correctly_in_the_generated_url(self) -> None:
        """Should merge query parameters correctly in the generated URL."""
        url = self.client.helper.build_url(
            src="https://ik.imagekit.io/test_url_endpoint/test_path_alt.jpg?t1=v1",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            query_parameters={"t2": "v2", "t3": "v3"},
            transformation=[{"height": 300, "width": 400}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path_alt.jpg?t1=v1&t2=v2&t3=v3&tr=h-300,w-400"
        assert url == expected

    def test_should_generate_the_correct_url_with_chained_transformations(self) -> None:
        """Should generate the correct URL with chained transformations."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}, {"rotation": 90}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400:rt-90"
        assert url == expected

    def test_should_generate_the_correct_url_with_chained_transformations_including_raw_transformation(self) -> None:
        """Should generate the correct URL with chained transformations including raw transformation."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400}, {"raw": "rndm_trnsf-abcd"}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400:rndm_trnsf-abcd"
        assert url == expected

    def test_should_generate_the_correct_url_when_border_transformation_is_applied(self) -> None:
        """Should generate the correct URL when border transformation is applied."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": 300, "width": 400, "border": "20_FF0000"}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400,b-20_FF0000"
        assert url == expected

    def test_should_generate_the_correct_url_when_transformation_has_empty_key_and_value(self) -> None:
        """Should generate the correct URL when transformation has empty key and value."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"raw": ""}],
        )

        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg"
        assert url == expected

    def test_should_generate_a_valid_url_when_cname_is_used(self) -> None:
        """Should generate a valid URL when CNAME is used."""
        url = self.client.helper.build_url(
            src="/test_path.jpg", url_endpoint="https://custom.domain.com", transformation_position="query"
        )

        expected = "https://custom.domain.com/test_path.jpg"
        assert url == expected

    def test_should_generate_a_valid_url_when_cname_with_path_is_used(self) -> None:
        """Should generate a valid URL when CNAME with path is used."""
        url = self.client.helper.build_url(
            src="/test_path.jpg", url_endpoint="https://custom.domain.com/url-pattern", transformation_position="query"
        )

        expected = "https://custom.domain.com/url-pattern/test_path.jpg"
        assert url == expected
