# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekit import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekit.types.files import DetailUpdateResponse, DetailRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDetails:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: ImageKit) -> None:
        detail = client.files.details.retrieve(
            "fileId",
        )
        assert_matches_type(DetailRetrieveResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: ImageKit) -> None:
        response = client.files.details.with_raw_response.retrieve(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailRetrieveResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: ImageKit) -> None:
        with client.files.details.with_streaming_response.retrieve(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailRetrieveResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.details.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: ImageKit) -> None:
        detail = client.files.details.update(
            file_id="fileId",
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: ImageKit) -> None:
        detail = client.files.details.update(
            file_id="fileId",
            custom_coordinates="customCoordinates",
            custom_metadata={},
            extensions=[
                {
                    "name": "remove-bg",
                    "options": {
                        "add_shadow": True,
                        "bg_color": "bg_color",
                        "bg_image_url": "bg_image_url",
                        "semitransparency": True,
                    },
                }
            ],
            remove_ai_tags=["string"],
            tags=["tag1", "tag2"],
            webhook_url="webhookUrl",
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: ImageKit) -> None:
        response = client.files.details.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: ImageKit) -> None:
        with client.files.details.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailUpdateResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.details.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: ImageKit) -> None:
        detail = client.files.details.update(
            file_id="fileId",
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: ImageKit) -> None:
        detail = client.files.details.update(
            file_id="fileId",
            publish={
                "is_published": True,
                "include_file_versions": True,
            },
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: ImageKit) -> None:
        response = client.files.details.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = response.parse()
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: ImageKit) -> None:
        with client.files.details.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = response.parse()
            assert_matches_type(DetailUpdateResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.details.with_raw_response.update(
                file_id="",
            )


class TestAsyncDetails:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncImageKit) -> None:
        detail = await async_client.files.details.retrieve(
            "fileId",
        )
        assert_matches_type(DetailRetrieveResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.details.with_raw_response.retrieve(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailRetrieveResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.details.with_streaming_response.retrieve(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailRetrieveResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.details.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncImageKit) -> None:
        detail = await async_client.files.details.update(
            file_id="fileId",
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncImageKit) -> None:
        detail = await async_client.files.details.update(
            file_id="fileId",
            custom_coordinates="customCoordinates",
            custom_metadata={},
            extensions=[
                {
                    "name": "remove-bg",
                    "options": {
                        "add_shadow": True,
                        "bg_color": "bg_color",
                        "bg_image_url": "bg_image_url",
                        "semitransparency": True,
                    },
                }
            ],
            remove_ai_tags=["string"],
            tags=["tag1", "tag2"],
            webhook_url="webhookUrl",
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.details.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.details.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailUpdateResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.details.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncImageKit) -> None:
        detail = await async_client.files.details.update(
            file_id="fileId",
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncImageKit) -> None:
        detail = await async_client.files.details.update(
            file_id="fileId",
            publish={
                "is_published": True,
                "include_file_versions": True,
            },
        )
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.details.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        detail = await response.parse()
        assert_matches_type(DetailUpdateResponse, detail, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.details.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            detail = await response.parse()
            assert_matches_type(DetailUpdateResponse, detail, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.details.with_raw_response.update(
                file_id="",
            )
