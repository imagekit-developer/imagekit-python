# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekit import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekit.types import (
    FileListResponse,
    FileRenameResponse,
    FileAddTagsResponse,
    FileUploadV1Response,
    FileUploadV2Response,
    FileRemoveTagsResponse,
    FileRemoveAITagsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFiles:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        file = client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: ImageKit) -> None:
        file = client.files.list(
            file_type="fileType",
            limit="limit",
            path="path",
            search_query="searchQuery",
            skip="skip",
            sort="sort",
            type="file",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    def test_method_add_tags(self, client: ImageKit) -> None:
        file = client.files.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(FileAddTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_add_tags(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileAddTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_add_tags(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileAddTagsResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy(self, client: ImageKit) -> None:
        file = client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy_with_all_params(self, client: ImageKit) -> None:
        file = client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
            include_file_versions=False,
        )
        assert_matches_type(object, file, path=["response"])

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
        assert_matches_type(object, file, path=["response"])

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
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move(self, client: ImageKit) -> None:
        file = client.files.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(object, file, path=["response"])

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
        assert_matches_type(object, file, path=["response"])

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
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_ai_tags(self, client: ImageKit) -> None:
        file = client.files.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )
        assert_matches_type(FileRemoveAITagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_ai_tags(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileRemoveAITagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_ai_tags(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileRemoveAITagsResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_remove_tags(self, client: ImageKit) -> None:
        file = client.files.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(FileRemoveTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_remove_tags(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileRemoveTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_remove_tags(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileRemoveTagsResponse, file, path=["response"])

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
    def test_method_upload_v1(self, client: ImageKit) -> None:
        file = client.files.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )
        assert_matches_type(FileUploadV1Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_v1_with_all_params(self, client: ImageKit) -> None:
        file = client.files.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
            token="token",
            checks='"request.folder" : "marketing/"\n',
            custom_coordinates="customCoordinates",
            custom_metadata='"\n  {\n    "brand": "Nike",\n    "color":"red"\n  }\n"\n',
            expire="expire",
            extensions='"\n[\n  {"name":"remove-bg","options":{"add_shadow":true,"bg_colour":"green"}},\n  {"name":"google-auto-tagging","maxTags":5,"minConfidence":95}\n]\n"\n',
            folder="folder",
            is_private_file="true",
            is_published="true",
            overwrite_ai_tags="true",
            overwrite_custom_metadata="true",
            overwrite_file="overwriteFile",
            overwrite_tags="true",
            public_key="publicKey",
            response_fields="responseFields",
            signature="signature",
            tags="t-shirt,round-neck,men",
            transformation='\'{"pre":"width:300,height:300,quality:80","post":[{"type":"thumbnail","value":"width:100,height:100"}]}\'\n',
            use_unique_file_name="true",
            webhook_url="webhookUrl",
        )
        assert_matches_type(FileUploadV1Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_v1(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadV1Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_v1(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadV1Response, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_v2(self, client: ImageKit) -> None:
        file = client.files.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )
        assert_matches_type(FileUploadV2Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_upload_v2_with_all_params(self, client: ImageKit) -> None:
        file = client.files.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
            token="token",
            checks='"request.folder" : "marketing/"\n',
            custom_coordinates="customCoordinates",
            custom_metadata='"\n  {\n    "brand": "Nike",\n    "color":"red"\n  }\n"\n',
            extensions='"\n[\n  {"name":"remove-bg","options":{"add_shadow":true,"bg_colour":"green"}},\n  {"name":"google-auto-tagging","maxTags":5,"minConfidence":95}\n]\n"\n',
            folder="folder",
            is_private_file="true",
            is_published="true",
            overwrite_ai_tags="true",
            overwrite_custom_metadata="true",
            overwrite_file="overwriteFile",
            overwrite_tags="true",
            response_fields="responseFields",
            tags="t-shirt,round-neck,men",
            transformation='\'{"pre":"width:300,height:300,quality:80","post":[{"type":"thumbnail","value":"width:100,height:100"}]}\'\n',
            use_unique_file_name="true",
            webhook_url="webhookUrl",
        )
        assert_matches_type(FileUploadV2Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_upload_v2(self, client: ImageKit) -> None:
        response = client.files.with_raw_response.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = response.parse()
        assert_matches_type(FileUploadV2Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_upload_v2(self, client: ImageKit) -> None:
        with client.files.with_streaming_response.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = response.parse()
            assert_matches_type(FileUploadV2Response, file, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFiles:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.list()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.list(
            file_type="fileType",
            limit="limit",
            path="path",
            search_query="searchQuery",
            skip="skip",
            sort="sort",
            type="file",
        )
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileListResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileListResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

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
    async def test_method_add_tags(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(FileAddTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_add_tags(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileAddTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_add_tags(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.add_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileAddTagsResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(object, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.copy(
            destination_path="/folder/to/copy/into/",
            source_file_path="/path/to/file.jpg",
            include_file_versions=False,
        )
        assert_matches_type(object, file, path=["response"])

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
        assert_matches_type(object, file, path=["response"])

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
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.move(
            destination_path="/folder/to/move/into/",
            source_file_path="/path/to/file.jpg",
        )
        assert_matches_type(object, file, path=["response"])

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
        assert_matches_type(object, file, path=["response"])

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
            assert_matches_type(object, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_ai_tags(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )
        assert_matches_type(FileRemoveAITagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_ai_tags(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileRemoveAITagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_ai_tags(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.remove_ai_tags(
            ai_tags=["t-shirt", "round-neck", "sale2019"],
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileRemoveAITagsResponse, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_remove_tags(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )
        assert_matches_type(FileRemoveTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_remove_tags(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileRemoveTagsResponse, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_remove_tags(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.remove_tags(
            file_ids=["598821f949c0a938d57563bd", "598821f949c0a938d57563be"],
            tags=["t-shirt", "round-neck", "sale2019"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileRemoveTagsResponse, file, path=["response"])

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
    async def test_method_upload_v1(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )
        assert_matches_type(FileUploadV1Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_v1_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
            token="token",
            checks='"request.folder" : "marketing/"\n',
            custom_coordinates="customCoordinates",
            custom_metadata='"\n  {\n    "brand": "Nike",\n    "color":"red"\n  }\n"\n',
            expire="expire",
            extensions='"\n[\n  {"name":"remove-bg","options":{"add_shadow":true,"bg_colour":"green"}},\n  {"name":"google-auto-tagging","maxTags":5,"minConfidence":95}\n]\n"\n',
            folder="folder",
            is_private_file="true",
            is_published="true",
            overwrite_ai_tags="true",
            overwrite_custom_metadata="true",
            overwrite_file="overwriteFile",
            overwrite_tags="true",
            public_key="publicKey",
            response_fields="responseFields",
            signature="signature",
            tags="t-shirt,round-neck,men",
            transformation='\'{"pre":"width:300,height:300,quality:80","post":[{"type":"thumbnail","value":"width:100,height:100"}]}\'\n',
            use_unique_file_name="true",
            webhook_url="webhookUrl",
        )
        assert_matches_type(FileUploadV1Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_v1(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadV1Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_v1(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.upload_v1(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadV1Response, file, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_v2(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )
        assert_matches_type(FileUploadV2Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_upload_v2_with_all_params(self, async_client: AsyncImageKit) -> None:
        file = await async_client.files.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
            token="token",
            checks='"request.folder" : "marketing/"\n',
            custom_coordinates="customCoordinates",
            custom_metadata='"\n  {\n    "brand": "Nike",\n    "color":"red"\n  }\n"\n',
            extensions='"\n[\n  {"name":"remove-bg","options":{"add_shadow":true,"bg_colour":"green"}},\n  {"name":"google-auto-tagging","maxTags":5,"minConfidence":95}\n]\n"\n',
            folder="folder",
            is_private_file="true",
            is_published="true",
            overwrite_ai_tags="true",
            overwrite_custom_metadata="true",
            overwrite_file="overwriteFile",
            overwrite_tags="true",
            response_fields="responseFields",
            tags="t-shirt,round-neck,men",
            transformation='\'{"pre":"width:300,height:300,quality:80","post":[{"type":"thumbnail","value":"width:100,height:100"}]}\'\n',
            use_unique_file_name="true",
            webhook_url="webhookUrl",
        )
        assert_matches_type(FileUploadV2Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_upload_v2(self, async_client: AsyncImageKit) -> None:
        response = await async_client.files.with_raw_response.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        file = await response.parse()
        assert_matches_type(FileUploadV2Response, file, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_upload_v2(self, async_client: AsyncImageKit) -> None:
        async with async_client.files.with_streaming_response.upload_v2(
            file="https://www.example.com/rest-of-the-image-path.jpg",
            file_name="fileName",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            file = await response.parse()
            assert_matches_type(FileUploadV2Response, file, path=["response"])

        assert cast(Any, response.is_closed) is True
