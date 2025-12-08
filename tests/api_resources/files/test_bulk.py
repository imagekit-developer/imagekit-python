# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types.files import (
    BulkDeleteResponse,
    BulkAddTagsResponse,
    BulkRemoveTagsResponse,
    BulkRemoveAITagsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulk:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        bulk = client.files.bulk.delete(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.files.bulk.with_raw_response.delete(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.files.bulk.with_streaming_response.delete(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_add_tags(self, client: ImageKit) -> None:
        bulk = client.files.bulk.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(BulkAddTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_tags(self, client: ImageKit) -> None:
        response = client.files.bulk.with_raw_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkAddTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_tags(self, client: ImageKit) -> None:
        with client.files.bulk.with_streaming_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkAddTagsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_ai_tags(self, client: ImageKit) -> None:
        bulk = client.files.bulk.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )
        assert_matches_type(BulkRemoveAITagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_ai_tags(self, client: ImageKit) -> None:
        response = client.files.bulk.with_raw_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkRemoveAITagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_ai_tags(self, client: ImageKit) -> None:
        with client.files.bulk.with_streaming_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkRemoveAITagsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_tags(self, client: ImageKit) -> None:
        bulk = client.files.bulk.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(BulkRemoveTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_tags(self, client: ImageKit) -> None:
        response = client.files.bulk.with_raw_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = response.parse()
        assert_matches_type(BulkRemoveTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_tags(self, client: ImageKit) -> None:
        with client.files.bulk.with_streaming_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = response.parse()
            assert_matches_type(BulkRemoveTagsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBulk:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        bulk = await async_client.files.bulk.delete(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.bulk.with_raw_response.delete(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.bulk.with_streaming_response.delete(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkDeleteResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_add_tags(self, async_client: AsyncImageKit) -> None:
        bulk = await async_client.files.bulk.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(BulkAddTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_tags(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.bulk.with_raw_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkAddTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_tags(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.bulk.with_streaming_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkAddTagsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_ai_tags(self, async_client: AsyncImageKit) -> None:
        bulk = await async_client.files.bulk.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )
        assert_matches_type(BulkRemoveAITagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_ai_tags(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.bulk.with_raw_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkRemoveAITagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_ai_tags(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.bulk.with_streaming_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkRemoveAITagsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_tags(self, async_client: AsyncImageKit) -> None:
        bulk = await async_client.files.bulk.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(BulkRemoveTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_tags(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.bulk.with_raw_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk = await response.parse()
        assert_matches_type(BulkRemoveTagsResponse, bulk, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_tags(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.bulk.with_streaming_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk = await response.parse()
            assert_matches_type(BulkRemoveTagsResponse, bulk, path=["response"])

        assert cast(Any, response.is_closed) is True
