# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types import (
    File,
    FileCopyResponse,
    FileMoveResponse,
    FileRenameResponse,
    FileUpdateResponse,
    FileUploadResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: ImageKit) -> None:
        file = client.files.update(
            file_id="fileId",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: ImageKit) -> None:
        file = client.files.update(
            file_id="fileId",
            custom_coordinates="customCoordinates",
            custom_metadata={"foo": "bar"},
            description="description",
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
                {"name": "ai-auto-description"},
                {
                    "name": "ai-tasks",
                    "tasks": [
                        {
                            "instruction": "What types of clothing items are visible in this image?",
                            "type": "select_tags",
                            "max_selections": 1,
                            "min_selections": 0,
                            "vocabulary": ["shirt", "tshirt", "dress", "trousers", "jacket"],
                        },
                        {
                            "instruction": "Is this a luxury or high-end fashion item?",
                            "type": "yes_no",
                            "on_no": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_unknown": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_yes": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                        },
                    ],
                },
                {
                    "id": "ext_abc123",
                    "name": "saved-extension",
                },
            ],
            remove_ai_tags=["string"],
            tags=["tag1", "tag2"],
            webhook_url="https://example.com",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: ImageKit) -> None:
        file = client.files.update(
            file_id="fileId",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: ImageKit) -> None:
        file = client.files.update(
            file_id="fileId",
            publish={
                "is_published": True,
                "include_file_versions": True,
            },
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        file = client.files.delete(
            "fileId",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.delete(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.delete(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy(self, client: ImageKit) -> None:
        file = client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(FileCopyResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy_with_all_params(self, client: ImageKit) -> None:
        file = client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
            include_file_versions=False,
        )
        assert_matches_type(FileCopyResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_copy(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileCopyResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_copy(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileCopyResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        file = client.files.get(
            "fileId",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.get(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.get(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            client.files.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move(self, client: ImageKit) -> None:
        file = client.files.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(FileMoveResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_move(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileMoveResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_move(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileMoveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rename(self, client: ImageKit) -> None:
        file = client.files.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
        )
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rename_with_all_params(self, client: ImageKit) -> None:
        file = client.files.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
            purge_cache=True,
        )
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rename(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rename(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileRenameResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload(self, client: ImageKit) -> None:
        file = client.files.upload(
            file=b"raw file contents",
            file_name="fileName",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_with_all_params(self, client: ImageKit) -> None:
        file = client.files.upload(
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
            expire=0,
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
                {"name": "ai-auto-description"},
                {
                    "name": "ai-tasks",
                    "tasks": [
                        {
                            "instruction": "What types of clothing items are visible in this image?",
                            "type": "select_tags",
                            "max_selections": 1,
                            "min_selections": 0,
                            "vocabulary": ["shirt", "tshirt", "dress", "trousers", "jacket"],
                        },
                        {
                            "instruction": "Is this a luxury or high-end fashion item?",
                            "type": "yes_no",
                            "on_no": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_unknown": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_yes": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                        },
                    ],
                },
                {
                    "id": "ext_abc123",
                    "name": "saved-extension",
                },
            ],
            folder="folder",
            is_private_file=True,
            is_published=True,
            overwrite_ai_tags=True,
            overwrite_custom_metadata=True,
            overwrite_file=True,
            overwrite_tags=True,
            public_key="publicKey",
            response_fields=["tags", "customCoordinates", "isPrivateFile"],
            signature="signature",
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
        response = client.files.with_raw_response.upload(
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
        with client.files.with_streaming_response.upload(
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
    async def test_method_update_overload_1(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.update(
            file_id="fileId",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.update(
            file_id="fileId",
            custom_coordinates="customCoordinates",
            custom_metadata={"foo": "bar"},
            description="description",
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
                {"name": "ai-auto-description"},
                {
                    "name": "ai-tasks",
                    "tasks": [
                        {
                            "instruction": "What types of clothing items are visible in this image?",
                            "type": "select_tags",
                            "max_selections": 1,
                            "min_selections": 0,
                            "vocabulary": ["shirt", "tshirt", "dress", "trousers", "jacket"],
                        },
                        {
                            "instruction": "Is this a luxury or high-end fashion item?",
                            "type": "yes_no",
                            "on_no": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_unknown": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_yes": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                        },
                    ],
                },
                {
                    "id": "ext_abc123",
                    "name": "saved-extension",
                },
            ],
            remove_ai_tags=["string"],
            tags=["tag1", "tag2"],
            webhook_url="https://example.com",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.update(
            file_id="fileId",
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.update(
            file_id="fileId",
            publish={
                "is_published": True,
                "include_file_versions": True,
            },
        )
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.update(
            file_id="fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUpdateResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.update(
            file_id="fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUpdateResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.update(
                file_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.delete(
            "fileId",
        )
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.delete(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert file is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.delete(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert file is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(FileCopyResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
            include_file_versions=False,
        )
        assert_matches_type(FileCopyResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileCopyResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileCopyResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.get(
            "fileId",
        )
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.get(
            "fileId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(File, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.get(
            "fileId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(File, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `file_id` but received ''"):
            await async_client.files.with_raw_response.get(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(FileMoveResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileMoveResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileMoveResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rename(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
        )
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rename_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
            purge_cache=True,
        )
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rename(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileRenameResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rename(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.rename(
            file_path="/path/to/file.jpg",
            new_file_name="newFileName.jpg",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileRenameResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.upload(
            file=b"raw file contents",
            file_name="fileName",
        )
        assert_matches_type(FileUploadResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.upload(
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
            expire=0,
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
                {"name": "ai-auto-description"},
                {
                    "name": "ai-tasks",
                    "tasks": [
                        {
                            "instruction": "What types of clothing items are visible in this image?",
                            "type": "select_tags",
                            "max_selections": 1,
                            "min_selections": 0,
                            "vocabulary": ["shirt", "tshirt", "dress", "trousers", "jacket"],
                        },
                        {
                            "instruction": "Is this a luxury or high-end fashion item?",
                            "type": "yes_no",
                            "on_no": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_unknown": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                            "on_yes": {
                                "add_tags": ["luxury", "premium"],
                                "remove_tags": ["budget", "affordable"],
                                "set_metadata": [
                                    {
                                        "field": "price_range",
                                        "value": "premium",
                                    }
                                ],
                                "unset_metadata": [{"field": "price_range"}],
                            },
                        },
                    ],
                },
                {
                    "id": "ext_abc123",
                    "name": "saved-extension",
                },
            ],
            folder="folder",
            is_private_file=True,
            is_published=True,
            overwrite_ai_tags=True,
            overwrite_custom_metadata=True,
            overwrite_file=True,
            overwrite_tags=True,
            public_key="publicKey",
            response_fields=["tags", "customCoordinates", "isPrivateFile"],
            signature="signature",
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
        response = await async_client.files.with_raw_response.upload(
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
        async with async_client.files.with_streaming_response.upload(
            file=b"raw file contents",
            file_name="fileName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True
