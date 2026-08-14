# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types import (
    NamedTransformationListResponse,
)
from imagekitio.types.shared import NamedTransformation

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNamedTransformations:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        named_transformation = client.named_transformations.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ImageKit) -> None:
        named_transformation = client.named_transformations.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
            enabled=True,
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.named_transformations.with_raw_response.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = response.parse()
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.named_transformations.with_streaming_response.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = response.parse()
            assert_matches_type(NamedTransformation, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: ImageKit) -> None:
        named_transformation = client.named_transformations.update(
            id="6bZ9x2ZUx",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ImageKit) -> None:
        named_transformation = client.named_transformations.update(
            id="6bZ9x2ZUx",
            enabled=False,
            name="small_thumbnail",
            transformation="w-200,h-200,fo-center,cm-pad_resize",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ImageKit) -> None:
        response = client.named_transformations.with_raw_response.update(
            id="6bZ9x2ZUx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = response.parse()
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ImageKit) -> None:
        with client.named_transformations.with_streaming_response.update(
            id="6bZ9x2ZUx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = response.parse()
            assert_matches_type(NamedTransformation, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.named_transformations.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        named_transformation = client.named_transformations.list()
        assert_matches_type(NamedTransformationListResponse, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.named_transformations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = response.parse()
        assert_matches_type(NamedTransformationListResponse, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.named_transformations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = response.parse()
            assert_matches_type(NamedTransformationListResponse, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        named_transformation = client.named_transformations.delete(
            "6bZ9x2ZUx",
        )
        assert named_transformation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.named_transformations.with_raw_response.delete(
            "6bZ9x2ZUx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = response.parse()
        assert named_transformation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.named_transformations.with_streaming_response.delete(
            "6bZ9x2ZUx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = response.parse()
            assert named_transformation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.named_transformations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        named_transformation = client.named_transformations.get(
            "6bZ9x2ZUx",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.named_transformations.with_raw_response.get(
            "6bZ9x2ZUx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = response.parse()
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.named_transformations.with_streaming_response.get(
            "6bZ9x2ZUx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = response.parse()
            assert_matches_type(NamedTransformation, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.named_transformations.with_raw_response.get(
                "",
            )


class TestAsyncNamedTransformations:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        named_transformation = await async_client.named_transformations.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncImageKit) -> None:
        named_transformation = await async_client.named_transformations.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
            enabled=True,
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.named_transformations.with_raw_response.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = await response.parse()
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.named_transformations.with_streaming_response.create(
            name="small_thumbnail",
            transformation="w-150,h-150,fo-center,cm-pad_resize",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = await response.parse()
            assert_matches_type(NamedTransformation, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncImageKit) -> None:
        named_transformation = await async_client.named_transformations.update(
            id="6bZ9x2ZUx",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncImageKit) -> None:
        named_transformation = await async_client.named_transformations.update(
            id="6bZ9x2ZUx",
            enabled=False,
            name="small_thumbnail",
            transformation="w-200,h-200,fo-center,cm-pad_resize",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncImageKit) -> None:
        response = await async_client.named_transformations.with_raw_response.update(
            id="6bZ9x2ZUx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = await response.parse()
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncImageKit) -> None:
        async with async_client.named_transformations.with_streaming_response.update(
            id="6bZ9x2ZUx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = await response.parse()
            assert_matches_type(NamedTransformation, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.named_transformations.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        named_transformation = await async_client.named_transformations.list()
        assert_matches_type(NamedTransformationListResponse, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.named_transformations.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = await response.parse()
        assert_matches_type(NamedTransformationListResponse, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.named_transformations.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = await response.parse()
            assert_matches_type(NamedTransformationListResponse, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        named_transformation = await async_client.named_transformations.delete(
            "6bZ9x2ZUx",
        )
        assert named_transformation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.named_transformations.with_raw_response.delete(
            "6bZ9x2ZUx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = await response.parse()
        assert named_transformation is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.named_transformations.with_streaming_response.delete(
            "6bZ9x2ZUx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = await response.parse()
            assert named_transformation is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.named_transformations.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        named_transformation = await async_client.named_transformations.get(
            "6bZ9x2ZUx",
        )
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.named_transformations.with_raw_response.get(
            "6bZ9x2ZUx",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        named_transformation = await response.parse()
        assert_matches_type(NamedTransformation, named_transformation, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.named_transformations.with_streaming_response.get(
            "6bZ9x2ZUx",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            named_transformation = await response.parse()
            assert_matches_type(NamedTransformation, named_transformation, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.named_transformations.with_raw_response.get(
                "",
            )
