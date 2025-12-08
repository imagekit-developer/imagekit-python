# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types import (
    CustomMetadataField,
    CustomMetadataFieldListResponse,
    CustomMetadataFieldDeleteResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCustomMetadataFields:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        custom_metadata_field = client.custom_metadata_fields.create(
            label="price",
            name="price",
            schema={"type": "Number"},
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ImageKit) -> None:
        custom_metadata_field = client.custom_metadata_fields.create(
            label="price",
            name="price",
            schema={
                "type": "Number",
                "default_value": "string",
                "is_value_required": True,
                "max_length": 0,
                "max_value": 3000,
                "min_length": 0,
                "min_value": 1000,
                "select_options": ["small", "medium", "large", 30, 40, True],
            },
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.custom_metadata_fields.with_raw_response.create(
            label="price",
            name="price",
            schema={"type": "Number"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = response.parse()
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.custom_metadata_fields.with_streaming_response.create(
            label="price",
            name="price",
            schema={"type": "Number"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = response.parse()
            assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: ImageKit) -> None:
        custom_metadata_field = client.custom_metadata_fields.update(
            id="id",
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ImageKit) -> None:
        custom_metadata_field = client.custom_metadata_fields.update(
            id="id",
            label="price",
            schema={
                "default_value": "string",
                "is_value_required": True,
                "max_length": 0,
                "max_value": 3000,
                "min_length": 0,
                "min_value": 1000,
                "select_options": ["small", "medium", "large", 30, 40, True],
            },
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ImageKit) -> None:
        response = client.custom_metadata_fields.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = response.parse()
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ImageKit) -> None:
        with client.custom_metadata_fields.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = response.parse()
            assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.custom_metadata_fields.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        custom_metadata_field = client.custom_metadata_fields.list()
        assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ImageKit) -> None:
        custom_metadata_field = client.custom_metadata_fields.list(
            folder_path="folderPath",
            include_deleted=True,
        )
        assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.custom_metadata_fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = response.parse()
        assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.custom_metadata_fields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = response.parse()
            assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        custom_metadata_field = client.custom_metadata_fields.delete(
            "id",
        )
        assert_matches_type(CustomMetadataFieldDeleteResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.custom_metadata_fields.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = response.parse()
        assert_matches_type(CustomMetadataFieldDeleteResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.custom_metadata_fields.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = response.parse()
            assert_matches_type(CustomMetadataFieldDeleteResponse, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.custom_metadata_fields.with_raw_response.delete(
                "",
            )


class TestAsyncCustomMetadataFields:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        custom_metadata_field = await async_client.custom_metadata_fields.create(
            label="price",
            name="price",
            schema={"type": "Number"},
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncImageKit) -> None:
        custom_metadata_field = await async_client.custom_metadata_fields.create(
            label="price",
            name="price",
            schema={
                "type": "Number",
                "default_value": "string",
                "is_value_required": True,
                "max_length": 0,
                "max_value": 3000,
                "min_length": 0,
                "min_value": 1000,
                "select_options": ["small", "medium", "large", 30, 40, True],
            },
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.custom_metadata_fields.with_raw_response.create(
            label="price",
            name="price",
            schema={"type": "Number"},
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = await response.parse()
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.custom_metadata_fields.with_streaming_response.create(
            label="price",
            name="price",
            schema={"type": "Number"},
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = await response.parse()
            assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncImageKit) -> None:
        custom_metadata_field = await async_client.custom_metadata_fields.update(
            id="id",
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncImageKit) -> None:
        custom_metadata_field = await async_client.custom_metadata_fields.update(
            id="id",
            label="price",
            schema={
                "default_value": "string",
                "is_value_required": True,
                "max_length": 0,
                "max_value": 3000,
                "min_length": 0,
                "min_value": 1000,
                "select_options": ["small", "medium", "large", 30, 40, True],
            },
        )
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncImageKit) -> None:
        response = await async_client.custom_metadata_fields.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = await response.parse()
        assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncImageKit) -> None:
        async with async_client.custom_metadata_fields.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = await response.parse()
            assert_matches_type(CustomMetadataField, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.custom_metadata_fields.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        custom_metadata_field = await async_client.custom_metadata_fields.list()
        assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncImageKit) -> None:
        custom_metadata_field = await async_client.custom_metadata_fields.list(
            folder_path="folderPath",
            include_deleted=True,
        )
        assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.custom_metadata_fields.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = await response.parse()
        assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.custom_metadata_fields.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = await response.parse()
            assert_matches_type(CustomMetadataFieldListResponse, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        custom_metadata_field = await async_client.custom_metadata_fields.delete(
            "id",
        )
        assert_matches_type(CustomMetadataFieldDeleteResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.custom_metadata_fields.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        custom_metadata_field = await response.parse()
        assert_matches_type(CustomMetadataFieldDeleteResponse, custom_metadata_field, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.custom_metadata_fields.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            custom_metadata_field = await response.parse()
            assert_matches_type(CustomMetadataFieldDeleteResponse, custom_metadata_field, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.custom_metadata_fields.with_raw_response.delete(
                "",
            )
