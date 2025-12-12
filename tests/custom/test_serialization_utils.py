"""Unit tests for serialization_utils module."""

import json
from typing import Any, Dict, List

from imagekitio.lib.serialization_utils import serialize_upload_options


class TestSerializeUploadOptions:
    """Test cases for serialize_upload_options function."""

    def test_should_convert_tags_array_to_comma_separated_string(self):
        """Test that tags array is converted to comma-separated string."""
        body = {"tags": ["tag1", "tag2", "tag3"]}
        result = serialize_upload_options(body)
        assert result["tags"] == "tag1,tag2,tag3"

    def test_should_convert_tags_tuple_to_comma_separated_string(self):
        """Test that tags tuple is converted to comma-separated string."""
        body = {"tags": ("tag1", "tag2", "tag3")}
        result = serialize_upload_options(body)
        assert result["tags"] == "tag1,tag2,tag3"

    def test_should_convert_response_fields_array_to_comma_separated_string(self):
        """Test that response_fields array is converted to comma-separated string."""
        body = {"response_fields": ["tags", "customCoordinates", "metadata"]}
        result = serialize_upload_options(body)
        assert result["response_fields"] == "tags,customCoordinates,metadata"

    def test_should_convert_response_fields_tuple_to_comma_separated_string(self):
        """Test that response_fields tuple is converted to comma-separated string."""
        body = {"response_fields": ("tags", "customCoordinates")}
        result = serialize_upload_options(body)
        assert result["response_fields"] == "tags,customCoordinates"

    def test_should_json_stringify_extensions_array(self):
        """Test that extensions array is JSON stringified."""
        body = {"extensions": [{"name": "remove-bg"}, {"name": "google-auto-tagging", "minConfidence": 80}]}
        result = serialize_upload_options(body)
        expected = json.dumps(body["extensions"])
        assert result["extensions"] == expected
        # Verify it's valid JSON
        assert json.loads(result["extensions"]) == body["extensions"]

    def test_should_json_stringify_custom_metadata_object(self):
        """Test that custom_metadata object is JSON stringified."""
        body = {"custom_metadata": {"key1": "value1", "key2": 123, "key3": True}}
        result = serialize_upload_options(body)
        expected = json.dumps(body["custom_metadata"])
        assert result["custom_metadata"] == expected
        # Verify it's valid JSON
        assert json.loads(result["custom_metadata"]) == body["custom_metadata"]

    def test_should_json_stringify_transformation_object(self):
        """Test that transformation object is JSON stringified."""
        body = {
            "transformation": {
                "pre": "l-image,i-logo.png,w-100,h-100",
                "post": [{"type": "thumbnail", "value": "h-300"}],
            }
        }
        result = serialize_upload_options(body)
        expected = json.dumps(body["transformation"])
        assert result["transformation"] == expected
        # Verify it's valid JSON
        assert json.loads(result["transformation"]) == body["transformation"]

    def test_should_handle_all_serializable_fields_together(self):
        """Test that all serializable fields are processed correctly together."""
        body = {
            "file": "test.jpg",
            "file_name": "test.jpg",
            "tags": ["tag1", "tag2"],
            "response_fields": ["tags", "metadata"],
            "extensions": [{"name": "remove-bg"}],
            "custom_metadata": {"key": "value"},
            "transformation": {"pre": "w-100"},
            "folder": "/images",
        }
        result = serialize_upload_options(body)

        assert result["tags"] == "tag1,tag2"
        assert result["response_fields"] == "tags,metadata"
        assert result["extensions"] == json.dumps([{"name": "remove-bg"}])
        assert result["custom_metadata"] == json.dumps({"key": "value"})
        assert result["transformation"] == json.dumps({"pre": "w-100"})
        # Non-serializable fields should remain unchanged
        assert result["file"] == "test.jpg"
        assert result["file_name"] == "test.jpg"
        assert result["folder"] == "/images"

    def test_should_not_modify_original_body(self):
        """Test that the original body is not modified."""
        body = {
            "tags": ["tag1", "tag2"],
            "response_fields": ["tags"],
            "extensions": [{"name": "ext1"}],
        }
        original_tags = body["tags"].copy()
        original_response_fields = body["response_fields"].copy()
        original_extensions = body["extensions"].copy()

        serialize_upload_options(body)

        # Original should remain unchanged
        assert body["tags"] == original_tags
        assert body["response_fields"] == original_response_fields
        assert body["extensions"] == original_extensions

    def test_should_handle_empty_arrays(self):
        """Test that empty arrays are converted to empty strings."""
        body: Dict[str, List[str]] = {"tags": [], "response_fields": []}
        result = serialize_upload_options(body)
        assert result["tags"] == ""
        assert result["response_fields"] == ""

    def test_should_handle_empty_extensions_array(self):
        """Test that empty extensions array is JSON stringified."""
        body: Dict[str, List[Any]] = {"extensions": []}
        result = serialize_upload_options(body)
        assert result["extensions"] == "[]"

    def test_should_handle_none_values(self):
        """Test that None values are not processed."""
        body = {
            "tags": None,
            "response_fields": None,
            "extensions": None,
            "custom_metadata": None,
            "transformation": None,
        }
        result = serialize_upload_options(body)
        # None values should remain None
        assert result["tags"] is None
        assert result["response_fields"] is None
        assert result["extensions"] is None
        assert result["custom_metadata"] is None
        assert result["transformation"] is None

    def test_should_handle_empty_object(self):
        """Test that an empty object is returned as is."""
        body: Dict[str, Any] = {}
        result = serialize_upload_options(body)
        assert result == {}

    def test_should_skip_non_matching_fields(self):
        """Test that fields not in the serialization list are left unchanged."""
        body = {
            "file_name": "test.jpg",
            "folder": "/images",
            "is_private_file": True,
            "use_unique_file_name": False,
        }
        result = serialize_upload_options(body)
        assert result == body

    def test_should_handle_single_tag(self):
        """Test that a single tag array is handled correctly."""
        body = {"tags": ["single-tag"]}
        result = serialize_upload_options(body)
        assert result["tags"] == "single-tag"

    def test_should_handle_tags_with_empty_strings(self):
        """Test that tags with empty strings are still joined."""
        body = {"tags": ["tag1", "", "tag2"]}
        result = serialize_upload_options(body)
        assert result["tags"] == "tag1,,tag2"

    def test_should_handle_complex_nested_extensions(self):
        """Test that complex nested extensions are properly JSON stringified."""
        body = {
            "extensions": [
                {
                    "name": "aws-auto-tagging",
                    "options": {"maxTags": 10, "minConfidence": 75},
                },
                {
                    "name": "remove-bg",
                    "options": {"add_shadow": True, "bg_color": "white"},
                },
            ]
        }
        result = serialize_upload_options(body)
        expected = json.dumps(body["extensions"])
        assert result["extensions"] == expected
        assert json.loads(result["extensions"]) == body["extensions"]

    def test_should_handle_nested_custom_metadata(self):
        """Test that nested custom metadata is properly JSON stringified."""
        body = {
            "custom_metadata": {
                "product": {"name": "Test Product", "price": 99.99, "inStock": True},
                "category": "electronics",
            }
        }
        result = serialize_upload_options(body)
        expected = json.dumps(body["custom_metadata"])
        assert result["custom_metadata"] == expected
        assert json.loads(result["custom_metadata"]) == body["custom_metadata"]

    def test_should_handle_transformation_with_both_pre_and_post(self):
        """Test that transformation with both pre and post is properly handled."""
        body = {
            "transformation": {
                "pre": "w-200,h-200",
                "post": [{"type": "transformation", "value": "w-100,h-100"}],
            }
        }
        result = serialize_upload_options(body)
        expected = json.dumps(body["transformation"])
        assert result["transformation"] == expected
        assert json.loads(result["transformation"]) == body["transformation"]

    def test_should_not_modify_non_dict_custom_metadata(self):
        """Test that custom_metadata is only serialized when it's a dict."""
        # This shouldn't happen in practice but testing edge case
        body = {"custom_metadata": "string_value"}
        result = serialize_upload_options(body)
        # String value should remain unchanged
        assert result["custom_metadata"] == "string_value"

    def test_should_not_modify_non_list_extensions(self):
        """Test that extensions is only serialized when it's a list."""
        # This shouldn't happen in practice but testing edge case
        body = {"extensions": "string_value"}
        result = serialize_upload_options(body)
        # String value should remain unchanged
        assert result["extensions"] == "string_value"
