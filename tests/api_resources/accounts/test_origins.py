# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekit import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekit.types.accounts import (
    OriginResponse,
    OriginListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrigins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
                "base_url_for_canonical_header": "https://cdn.example.com",
                "include_canonical_header": False,
                "prefix": "images",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
                "base_url_for_canonical_header": "https://cdn.example.com",
                "include_canonical_header": False,
                "prefix": "images",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                origin={
                    "access_key": "AKIATEST123",
                    "bucket": "test-bucket",
                    "name": "My S3 Origin",
                    "secret_key": "secrettest123",
                    "type": "S3",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        origin = client.accounts.origins.list()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginListResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        origin = client.accounts.origins.delete(
            "id",
        )
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert origin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        origin = client.accounts.origins.get(
            "id",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.get(
                "",
            )


class TestAsyncOrigins:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
                "base_url_for_canonical_header": "https://cdn.example.com",
                "include_canonical_header": False,
                "prefix": "images",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
                "base_url_for_canonical_header": "https://cdn.example.com",
                "include_canonical_header": False,
                "prefix": "images",
            },
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            origin={
                "access_key": "AKIATEST123",
                "bucket": "test-bucket",
                "name": "My S3 Origin",
                "secret_key": "secrettest123",
                "type": "S3",
            },
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                origin={
                    "access_key": "AKIATEST123",
                    "bucket": "test-bucket",
                    "name": "My S3 Origin",
                    "secret_key": "secrettest123",
                    "type": "S3",
                },
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.list()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginListResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.delete(
            "id",
        )
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert origin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.get(
            "id",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.get(
                "",
            )
