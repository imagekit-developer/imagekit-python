# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types import (
    SavedExtensionListResponse,
)
from imagekitio.types.shared import SavedExtension

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSavedExtensions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        saved_extension = client.saved_extensions.create(
            config={"name": "remove-bg"},
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ImageKit) -> None:
        saved_extension = client.saved_extensions.create(
            config={
                "name": "remove-bg",
                "options": {
                    "add_shadow": True,
                    "bg_color": "bg_color",
                    "bg_image_url": "bg_image_url",
                    "semitransparency": True,
                },
            },
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.saved_extensions.with_raw_response.create(
            config={"name": "remove-bg"},
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = response.parse()
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.saved_extensions.with_streaming_response.create(
            config={"name": "remove-bg"},
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = response.parse()
            assert_matches_type(SavedExtension, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: ImageKit) -> None:
        saved_extension = client.saved_extensions.update(
            id="id",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ImageKit) -> None:
        saved_extension = client.saved_extensions.update(
            id="id",
            config={
                "name": "remove-bg",
                "options": {
                    "add_shadow": True,
                    "bg_color": "bg_color",
                    "bg_image_url": "bg_image_url",
                    "semitransparency": True,
                },
            },
            description="x",
            name="x",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ImageKit) -> None:
        response = client.saved_extensions.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = response.parse()
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ImageKit) -> None:
        with client.saved_extensions.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = response.parse()
            assert_matches_type(SavedExtension, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.saved_extensions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        saved_extension = client.saved_extensions.list()
        assert_matches_type(SavedExtensionListResponse, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.saved_extensions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = response.parse()
        assert_matches_type(SavedExtensionListResponse, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.saved_extensions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = response.parse()
            assert_matches_type(SavedExtensionListResponse, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        saved_extension = client.saved_extensions.delete(
            "id",
        )
        assert saved_extension is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.saved_extensions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = response.parse()
        assert saved_extension is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.saved_extensions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = response.parse()
            assert saved_extension is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.saved_extensions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        saved_extension = client.saved_extensions.get(
            "id",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.saved_extensions.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = response.parse()
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.saved_extensions.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = response.parse()
            assert_matches_type(SavedExtension, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.saved_extensions.with_raw_response.get(
                "",
            )


class TestAsyncSavedExtensions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        saved_extension = await async_client.saved_extensions.create(
            config={"name": "remove-bg"},
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncImageKit) -> None:
        saved_extension = await async_client.saved_extensions.create(
            config={
                "name": "remove-bg",
                "options": {
                    "add_shadow": True,
                    "bg_color": "bg_color",
                    "bg_image_url": "bg_image_url",
                    "semitransparency": True,
                },
            },
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.saved_extensions.with_raw_response.create(
            config={"name": "remove-bg"},
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = await response.parse()
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.saved_extensions.with_streaming_response.create(
            config={"name": "remove-bg"},
            description="Analyzes vehicle images for type, condition, and quality assessment",
            name="Car Quality Analysis",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = await response.parse()
            assert_matches_type(SavedExtension, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncImageKit) -> None:
        saved_extension = await async_client.saved_extensions.update(
            id="id",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncImageKit) -> None:
        saved_extension = await async_client.saved_extensions.update(
            id="id",
            config={
                "name": "remove-bg",
                "options": {
                    "add_shadow": True,
                    "bg_color": "bg_color",
                    "bg_image_url": "bg_image_url",
                    "semitransparency": True,
                },
            },
            description="x",
            name="x",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncImageKit) -> None:
        response = await async_client.saved_extensions.with_raw_response.update(
            id="id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = await response.parse()
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncImageKit) -> None:
        async with async_client.saved_extensions.with_streaming_response.update(
            id="id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = await response.parse()
            assert_matches_type(SavedExtension, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.saved_extensions.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        saved_extension = await async_client.saved_extensions.list()
        assert_matches_type(SavedExtensionListResponse, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.saved_extensions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = await response.parse()
        assert_matches_type(SavedExtensionListResponse, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.saved_extensions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = await response.parse()
            assert_matches_type(SavedExtensionListResponse, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        saved_extension = await async_client.saved_extensions.delete(
            "id",
        )
        assert saved_extension is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.saved_extensions.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = await response.parse()
        assert saved_extension is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.saved_extensions.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = await response.parse()
            assert saved_extension is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.saved_extensions.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        saved_extension = await async_client.saved_extensions.get(
            "id",
        )
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.saved_extensions.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        saved_extension = await response.parse()
        assert_matches_type(SavedExtension, saved_extension, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.saved_extensions.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            saved_extension = await response.parse()
            assert_matches_type(SavedExtension, saved_extension, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.saved_extensions.with_raw_response.get(
                "",
            )
