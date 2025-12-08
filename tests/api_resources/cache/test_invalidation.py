# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types.cache import InvalidationGetResponse, InvalidationCreateResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInvalidation:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        invalidation = client.cache.invalidation.create(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )
        assert_matches_type(InvalidationCreateResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.cache.invalidation.with_raw_response.create(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invalidation = response.parse()
        assert_matches_type(InvalidationCreateResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.cache.invalidation.with_streaming_response.create(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invalidation = response.parse()
            assert_matches_type(InvalidationCreateResponse, invalidation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        invalidation = client.cache.invalidation.get(
            "requestId",
        )
        assert_matches_type(InvalidationGetResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.cache.invalidation.with_raw_response.get(
            "requestId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invalidation = response.parse()
        assert_matches_type(InvalidationGetResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.cache.invalidation.with_streaming_response.get(
            "requestId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invalidation = response.parse()
            assert_matches_type(InvalidationGetResponse, invalidation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.cache.invalidation.with_raw_response.get(
                "",
            )


class TestAsyncInvalidation:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        invalidation = await async_client.cache.invalidation.create(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )
        assert_matches_type(InvalidationCreateResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.cache.invalidation.with_raw_response.create(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invalidation = await response.parse()
        assert_matches_type(InvalidationCreateResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.cache.invalidation.with_streaming_response.create(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invalidation = await response.parse()
            assert_matches_type(InvalidationCreateResponse, invalidation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        invalidation = await async_client.cache.invalidation.get(
            "requestId",
        )
        assert_matches_type(InvalidationGetResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.cache.invalidation.with_raw_response.get(
            "requestId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        invalidation = await response.parse()
        assert_matches_type(InvalidationGetResponse, invalidation, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.cache.invalidation.with_streaming_response.get(
            "requestId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            invalidation = await response.parse()
            assert_matches_type(InvalidationGetResponse, invalidation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.cache.invalidation.with_raw_response.get(
                "",
            )
