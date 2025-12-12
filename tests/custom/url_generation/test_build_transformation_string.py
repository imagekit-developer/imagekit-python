"""Build transformation string tests imported from Ruby SDK."""

import pytest

from imagekitio import ImageKit


class TestBuildTransformationString:
    """Test build_transformation_string matching Ruby SDK build_transformation_string_test.rb."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup client for each test."""
        self.client = ImageKit(private_key="test-key")

    def test_should_return_empty_string_for_empty_transformation_array(self):
        """Test empty transformation array returns empty string."""
        result = self.client.helper.build_transformation_string(None)
        assert result == ""

        result = self.client.helper.build_transformation_string([])
        assert result == ""

    def test_should_generate_transformation_string_for_width_only(self):
        """Test transformation string for width only."""
        result = self.client.helper.build_transformation_string([{"width": 300}])
        expected = "w-300"
        assert result == expected

    def test_should_generate_transformation_string_for_multiple_parameters(self):
        """Test transformation string for multiple parameters."""
        result = self.client.helper.build_transformation_string([{"width": 300, "height": 200}])
        expected = "w-300,h-200"
        assert result == expected

    def test_should_generate_transformation_string_for_chained_transformations(self):
        """Test transformation string for chained transformations."""
        result = self.client.helper.build_transformation_string([{"width": 300}, {"height": 200}])
        expected = "w-300:h-200"
        assert result == expected

    def test_should_handle_empty_transformation_object(self):
        """Test empty transformation object."""
        result = self.client.helper.build_transformation_string([{}])
        expected = ""
        assert result == expected

    def test_should_handle_transformation_with_overlay(self):
        """Test transformation with overlay."""
        result = self.client.helper.build_transformation_string([{"overlay": {"type": "text", "text": "Hello"}}])
        expected = "l-text,i-Hello,l-end"
        assert result == expected

    def test_should_handle_raw_transformation_parameter(self):
        """Test raw transformation parameter."""
        result = self.client.helper.build_transformation_string([{"raw": "custom-transform-123"}])
        expected = "custom-transform-123"
        assert result == expected

    def test_should_handle_mixed_parameters_with_raw(self):
        """Test mixed parameters with raw."""
        result = self.client.helper.build_transformation_string([{"width": 300, "raw": "custom-param-123"}])
        expected = "w-300,custom-param-123"
        assert result == expected

    def test_should_handle_quality_parameter(self):
        """Test quality parameter."""
        result = self.client.helper.build_transformation_string([{"quality": 80}])
        expected = "q-80"
        assert result == expected

    def test_should_handle_aspect_ratio_parameter(self):
        """Test aspect ratio parameter."""
        result = self.client.helper.build_transformation_string([{"aspect_ratio": "4:3"}])
        expected = "ar-4:3"
        assert result == expected
