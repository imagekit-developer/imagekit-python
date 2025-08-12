# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekit import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekit.types.files import PurgeStatusResponse, PurgeExecuteResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPurge:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_execute(self, client: ImageKit) -> None:
        purge = client.files.purge.execute(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )
        assert_matches_type(PurgeExecuteResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_execute(self, client: ImageKit) -> None:
        response = client.files.purge.with_raw_response.execute(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = response.parse()
        assert_matches_type(PurgeExecuteResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_execute(self, client: ImageKit) -> None:
        with client.files.purge.with_streaming_response.execute(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = response.parse()
            assert_matches_type(PurgeExecuteResponse, purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_status(self, client: ImageKit) -> None:
        purge = client.files.purge.status(
            "requestId",
        )
        assert_matches_type(PurgeStatusResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: ImageKit) -> None:
        response = client.files.purge.with_raw_response.status(
            "requestId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = response.parse()
        assert_matches_type(PurgeStatusResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: ImageKit) -> None:
        with client.files.purge.with_streaming_response.status(
            "requestId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = response.parse()
            assert_matches_type(PurgeStatusResponse, purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_status(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            client.files.purge.with_raw_response.status(
                "",
            )


class TestAsyncPurge:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_execute(self, async_client: AsyncImageKit) -> None:
        purge = await async_client.files.purge.execute(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )
        assert_matches_type(PurgeExecuteResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_execute(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.purge.with_raw_response.execute(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = await response.parse()
        assert_matches_type(PurgeExecuteResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_execute(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.purge.with_streaming_response.execute(
            url="https://ik.imagekit.io/your_imagekit_id/default-image.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = await response.parse()
            assert_matches_type(PurgeExecuteResponse, purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncImageKit) -> None:
        purge = await async_client.files.purge.status(
            "requestId",
        )
        assert_matches_type(PurgeStatusResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.purge.with_raw_response.status(
            "requestId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        purge = await response.parse()
        assert_matches_type(PurgeStatusResponse, purge, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.purge.with_streaming_response.status(
            "requestId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            purge = await response.parse()
            assert_matches_type(PurgeStatusResponse, purge, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_status(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `request_id` but received ''"):
            await async_client.files.purge.with_raw_response.status(
                "",
            )
