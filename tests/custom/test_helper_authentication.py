"""Helper authentication tests - converted from Ruby SDK."""

import re

import pytest

from imagekitio import ImageKit, ImageKitError


class TestHelperAuthentication:
    """Test helper authentication parameter generation."""

    def test_should_return_correct_authentication_parameters_with_provided_token_and_expire(self) -> None:
        """Should return correct authentication parameters with provided token and expire."""
        private_key = "private_key_test"
        client = ImageKit(private_key=private_key)

        token = "your_token"
        expire = 1582269249

        params = client.helper.get_authentication_parameters(token=token, expire=expire)

        # Expected exact match with Node.js output
        expected_signature = "e71bcd6031016b060d349d212e23e85c791decdd"

        assert params["token"] == token
        assert params["expire"] == expire
        assert params["signature"] == expected_signature

    def test_should_return_authentication_parameters_with_required_properties_when_no_params_provided(self) -> None:
        """Should return authentication parameters with required properties when no params provided."""
        private_key = "private_key_test"
        client = ImageKit(private_key=private_key)

        params = client.helper.get_authentication_parameters()

        # Check that all required properties exist
        assert "token" in params, "Expected token parameter"
        assert "expire" in params, "Expected expire parameter"
        assert "signature" in params, "Expected signature parameter"

        # Token should be a UUID v4 format (36 characters with dashes)
        token = params["token"]
        assert isinstance(token, str)
        assert re.match(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", token, re.IGNORECASE
        ), "Expected token to be UUID v4 format"

        # Expire should be a number greater than current time
        expire = params["expire"]
        assert isinstance(expire, int)
        import time

        current_time = int(time.time())
        assert expire > current_time, f"Expected expire {expire} to be greater than current time {current_time}"

        # Signature should be a hex string (40 characters for HMAC-SHA1)
        signature = params["signature"]
        assert isinstance(signature, str)
        assert re.match(r"^[a-f0-9]{40}$", signature), "Expected signature to be 40 character hex string"

    def test_should_handle_edge_case_with_expire_time_0(self) -> None:
        """Should handle edge case with expire time 0."""
        private_key = "private_key_test"
        client = ImageKit(private_key=private_key)

        token = "test_token"
        expire = 0

        params = client.helper.get_authentication_parameters(token=token, expire=expire)

        assert params["token"] == token
        assert params["expire"] == expire
        assert "signature" in params
        # Signature should still be generated even with expire = 0
        assert isinstance(params["signature"], str)
        assert len(params["signature"]) == 40

    def test_should_handle_empty_string_token(self) -> None:
        """Should handle empty string token."""
        private_key = "private_key_test"
        client = ImageKit(private_key=private_key)

        token = ""  # Empty string is falsy
        expire = 1582269249

        params = client.helper.get_authentication_parameters(token=token, expire=expire)

        # Since empty string is falsy, it should generate a token
        token_result = params["token"]
        assert isinstance(token_result, str)
        assert len(token_result) > 0, "Expected token to be generated when empty string is provided"
        assert re.match(
            r"^[0-9a-f]{8}-[0-9a-f]{4}-4[0-9a-f]{3}-[89ab][0-9a-f]{3}-[0-9a-f]{12}$", token_result, re.IGNORECASE
        ), "Expected generated token to be UUID v4 format"

        assert params["expire"] == expire

        # Signature should be a hex string (40 characters for HMAC-SHA1)
        signature = params["signature"]
        assert isinstance(signature, str)
        assert re.match(r"^[a-f0-9]{40}$", signature), "Expected signature to be 40 character hex string"

    def test_should_raise_error_when_private_key_is_not_provided(self) -> None:
        """Should raise error when private key is empty."""
        with pytest.raises(ValueError, match="Private key is required"):
            client = ImageKit(private_key="")
            client.helper.get_authentication_parameters(token="test", expire=123)

    def test_should_raise_error_when_private_key_is_nil(self) -> None:
        """Should raise error when private key is None."""
        with pytest.raises(ImageKitError, match="private_key client option must be set"):
            client = ImageKit(private_key=None)  # type: ignore
            client.helper.get_authentication_parameters(token="test", expire=123)
