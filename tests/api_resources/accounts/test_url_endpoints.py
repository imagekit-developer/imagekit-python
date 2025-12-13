# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types.accounts import (
    URLEndpointResponse,
    URLEndpointListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestURLEndpoints:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        url_endpoint = client.accounts.url_endpoints.create(
            description="My custom URL endpoint",
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ImageKit) -> None:
        url_endpoint = client.accounts.url_endpoints.create(
            description="My custom URL endpoint",
            origins=["origin-id-1"],
            url_prefix="product-images",
            url_rewriter={
                "type": "CLOUDINARY",
                "preserve_asset_delivery_types": True,
            },
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.accounts.url_endpoints.with_raw_response.create(
            description="My custom URL endpoint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = response.parse()
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.accounts.url_endpoints.with_streaming_response.create(
            description="My custom URL endpoint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = response.parse()
            assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: ImageKit) -> None:
        url_endpoint = client.accounts.url_endpoints.update(
            id="id",
            description="My custom URL endpoint",
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ImageKit) -> None:
        url_endpoint = client.accounts.url_endpoints.update(
            id="id",
            description="My custom URL endpoint",
            origins=["origin-id-1"],
            url_prefix="product-images",
            url_rewriter={
                "type": "CLOUDINARY",
                "preserve_asset_delivery_types": True,
            },
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ImageKit) -> None:
        response = client.accounts.url_endpoints.with_raw_response.update(
            id="id",
            description="My custom URL endpoint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = response.parse()
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ImageKit) -> None:
        with client.accounts.url_endpoints.with_streaming_response.update(
            id="id",
            description="My custom URL endpoint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = response.parse()
            assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.url_endpoints.with_raw_response.update(
                id="",
                description="My custom URL endpoint",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        url_endpoint = client.accounts.url_endpoints.list()
        assert_matches_type(URLEndpointListResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.accounts.url_endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = response.parse()
        assert_matches_type(URLEndpointListResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.accounts.url_endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = response.parse()
            assert_matches_type(URLEndpointListResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        url_endpoint = client.accounts.url_endpoints.delete(
            "id",
        )
        assert url_endpoint is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.accounts.url_endpoints.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = response.parse()
        assert url_endpoint is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.accounts.url_endpoints.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = response.parse()
            assert url_endpoint is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.url_endpoints.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        url_endpoint = client.accounts.url_endpoints.get(
            "id",
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.accounts.url_endpoints.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = response.parse()
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.accounts.url_endpoints.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = response.parse()
            assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.url_endpoints.with_raw_response.get(
                "",
            )


class TestAsyncURLEndpoints:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        url_endpoint = await async_client.accounts.url_endpoints.create(
            description="My custom URL endpoint",
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncImageKit) -> None:
        url_endpoint = await async_client.accounts.url_endpoints.create(
            description="My custom URL endpoint",
            origins=["origin-id-1"],
            url_prefix="product-images",
            url_rewriter={
                "type": "CLOUDINARY",
                "preserve_asset_delivery_types": True,
            },
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.url_endpoints.with_raw_response.create(
            description="My custom URL endpoint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = await response.parse()
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.url_endpoints.with_streaming_response.create(
            description="My custom URL endpoint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = await response.parse()
            assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncImageKit) -> None:
        url_endpoint = await async_client.accounts.url_endpoints.update(
            id="id",
            description="My custom URL endpoint",
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncImageKit) -> None:
        url_endpoint = await async_client.accounts.url_endpoints.update(
            id="id",
            description="My custom URL endpoint",
            origins=["origin-id-1"],
            url_prefix="product-images",
            url_rewriter={
                "type": "CLOUDINARY",
                "preserve_asset_delivery_types": True,
            },
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.url_endpoints.with_raw_response.update(
            id="id",
            description="My custom URL endpoint",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = await response.parse()
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.url_endpoints.with_streaming_response.update(
            id="id",
            description="My custom URL endpoint",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = await response.parse()
            assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.url_endpoints.with_raw_response.update(
                id="",
                description="My custom URL endpoint",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        url_endpoint = await async_client.accounts.url_endpoints.list()
        assert_matches_type(URLEndpointListResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.url_endpoints.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = await response.parse()
        assert_matches_type(URLEndpointListResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.url_endpoints.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = await response.parse()
            assert_matches_type(URLEndpointListResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        url_endpoint = await async_client.accounts.url_endpoints.delete(
            "id",
        )
        assert url_endpoint is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.url_endpoints.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = await response.parse()
        assert url_endpoint is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.url_endpoints.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = await response.parse()
            assert url_endpoint is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.url_endpoints.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        url_endpoint = await async_client.accounts.url_endpoints.get(
            "id",
        )
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.url_endpoints.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        url_endpoint = await response.parse()
        assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.url_endpoints.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            url_endpoint = await response.parse()
            assert_matches_type(URLEndpointResponse, url_endpoint, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.url_endpoints.with_raw_response.get(
                "",
            )
