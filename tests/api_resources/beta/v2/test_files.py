# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekit import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekit.types.beta.v2 import FileUploadResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: ImageKit) -> None:
        file = client.beta.v2.files.upload(
            file=b"raw file contents",
            file_name="fileName",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: ImageKit) -> None:
        file = client.beta.v2.files.upload(
            file=b"raw file contents",
            file_name="fileName",
            token="token",
            checks='"request.folder" : "marketing/"\n',
            custom_coordinates="customCoordinates",
            custom_metadata={
                "brand": "bar",
                "color": "bar",
            },
            description="Running shoes",
            extensions=[
                {
                    "name": "remove-bg",
                    "options": {
                        "add_shadow": True,
                        "bg_color": "bg_color",
                        "bg_image_url": "bg_image_url",
                        "semitransparency": True,
                    },
                },
                {
                    "max_tags": 5,
                    "min_confidence": 95,
                    "name": "google-auto-tagging",
                },
            ],
            folder="folder",
            is_private_file=True,
            is_published=True,
            overwrite_ai_tags=True,
            overwrite_custom_metadata=True,
            overwrite_file=True,
            overwrite_tags=True,
            response_fields=["tags", "customCoordinates", "isPrivateFile"],
            tags=["t-shirt", "round-neck", "men"],
            transformation={
                "post": [
                    {
                        "type": "thumbnail",
                        "value": "w-150,h-150",
                    },
                    {
                        "protocol": "dash",
                        "type": "abs",
                        "value": "sr-240_360_480_720_1080",
                    },
                ],
                "pre": "w-300,h-300,q-80",
            },
            use_unique_file_name=True,
            webhook_url="https://example.com",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload(self, client: ImageKit) -> None:
        response = client.beta.v2.files.with_raw_response.upload(
            file=b"raw file contents",
            file_name="fileName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload(self, client: ImageKit) -> None:
        with client.beta.v2.files.with_streaming_response.upload(
            file=b"raw file contents",
            file_name="fileName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncImageKit) -> None:
        file = await async_client.beta.v2.files.upload(
            file=b"raw file contents",
            file_name="fileName",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.beta.v2.files.upload(
            file=b"raw file contents",
            file_name="fileName",
            token="token",
            checks='"request.folder" : "marketing/"\n',
            custom_coordinates="customCoordinates",
            custom_metadata={
                "brand": "bar",
                "color": "bar",
            },
            description="Running shoes",
            extensions=[
                {
                    "name": "remove-bg",
                    "options": {
                        "add_shadow": True,
                        "bg_color": "bg_color",
                        "bg_image_url": "bg_image_url",
                        "semitransparency": True,
                    },
                },
                {
                    "max_tags": 5,
                    "min_confidence": 95,
                    "name": "google-auto-tagging",
                },
            ],
            folder="folder",
            is_private_file=True,
            is_published=True,
            overwrite_ai_tags=True,
            overwrite_custom_metadata=True,
            overwrite_file=True,
            overwrite_tags=True,
            response_fields=["tags", "customCoordinates", "isPrivateFile"],
            tags=["t-shirt", "round-neck", "men"],
            transformation={
                "post": [
                    {
                        "type": "thumbnail",
                        "value": "w-150,h-150",
                    },
                    {
                        "protocol": "dash",
                        "type": "abs",
                        "value": "sr-240_360_480_720_1080",
                    },
                ],
                "pre": "w-300,h-300,q-80",
            },
            use_unique_file_name=True,
            webhook_url="https://example.com",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload(self, async_client: AsyncImageKit) -> None:
        response = await async_client.beta.v2.files.with_raw_response.upload(
            file=b"raw file contents",
            file_name="fileName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload(self, async_client: AsyncImageKit) -> None:
        async with async_client.beta.v2.files.with_streaming_response.upload(
            file=b"raw file contents",
            file_name="fileName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
