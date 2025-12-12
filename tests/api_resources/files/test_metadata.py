# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types import Metadata

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestMetadata:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        metadata = client.files.metadata.get(
            "fileId",
        )
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.files.metadata.with_raw_response.get(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.files.metadata.with_streaming_response.get(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(Metadata, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.metadata.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get_from_url(self, client: ImageKit) -> None:
        metadata = client.files.metadata.get_from_url(
            url="https://example.com",
        )
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get_from_url(self, client: ImageKit) -> None:
        response = client.files.metadata.with_raw_response.get_from_url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = response.parse()
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get_from_url(self, client: ImageKit) -> None:
        with client.files.metadata.with_streaming_response.get_from_url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = response.parse()
            assert_matches_type(Metadata, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncMetadata:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        metadata = await async_client.files.metadata.get(
            "fileId",
        )
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.metadata.with_raw_response.get(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.metadata.with_streaming_response.get(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(Metadata, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.metadata.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get_from_url(self, async_client: AsyncImageKit) -> None:
        metadata = await async_client.files.metadata.get_from_url(
            url="https://example.com",
        )
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get_from_url(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.metadata.with_raw_response.get_from_url(
            url="https://example.com",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        metadata = await response.parse()
        assert_matches_type(Metadata, metadata, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get_from_url(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.metadata.with_streaming_response.get_from_url(
            url="https://example.com",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            metadata = await response.parse()
            assert_matches_type(Metadata, metadata, path=["response"])

        assert cast(Any, response.is_closed) is True
