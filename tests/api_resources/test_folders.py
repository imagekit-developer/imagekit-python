# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types import (
    FolderCopyResponse,
    FolderMoveResponse,
    FolderCreateResponse,
    FolderDeleteResponse,
    FolderRenameResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFolders:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        folder = client.folders.create(
            folder_name="summer",
            parent_folder_path="/product/images/",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.folders.with_raw_response.create(
            folder_name="summer",
            parent_folder_path="/product/images/",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.folders.with_streaming_response.create(
            folder_name="summer",
            parent_folder_path="/product/images/",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        folder = client.folders.delete(
            folder_path="/folder/to/delete/",
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.folders.with_raw_response.delete(
            folder_path="/folder/to/delete/",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.folders.with_streaming_response.delete(
            folder_path="/folder/to/delete/",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderDeleteResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy(self, client: ImageKit) -> None:
        folder = client.folders.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(FolderCopyResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy_with_all_params(self, client: ImageKit) -> None:
        folder = client.folders.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
            include_versions=True,
        )
        assert_matches_type(FolderCopyResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_copy(self, client: ImageKit) -> None:
        response = client.folders.with_raw_response.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderCopyResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_copy(self, client: ImageKit) -> None:
        with client.folders.with_streaming_response.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderCopyResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move(self, client: ImageKit) -> None:
        folder = client.folders.move(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_move(self, client: ImageKit) -> None:
        response = client.folders.with_raw_response.move(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_move(self, client: ImageKit) -> None:
        with client.folders.with_streaming_response.move(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderMoveResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rename(self, client: ImageKit) -> None:
        folder = client.folders.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
        )
        assert_matches_type(FolderRenameResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rename_with_all_params(self, client: ImageKit) -> None:
        folder = client.folders.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
            purge_cache=True,
        )
        assert_matches_type(FolderRenameResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rename(self, client: ImageKit) -> None:
        response = client.folders.with_raw_response.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = response.parse()
        assert_matches_type(FolderRenameResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rename(self, client: ImageKit) -> None:
        with client.folders.with_streaming_response.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = response.parse()
            assert_matches_type(FolderRenameResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFolders:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        folder = await async_client.folders.create(
            folder_name="summer",
            parent_folder_path="/product/images/",
        )
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.folders.with_raw_response.create(
            folder_name="summer",
            parent_folder_path="/product/images/",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderCreateResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.folders.with_streaming_response.create(
            folder_name="summer",
            parent_folder_path="/product/images/",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderCreateResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        folder = await async_client.folders.delete(
            folder_path="/folder/to/delete/",
        )
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.folders.with_raw_response.delete(
            folder_path="/folder/to/delete/",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderDeleteResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.folders.with_streaming_response.delete(
            folder_path="/folder/to/delete/",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderDeleteResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy(self, async_client: AsyncImageKit) -> None:
        folder = await async_client.folders.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(FolderCopyResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy_with_all_params(self, async_client: AsyncImageKit) -> None:
        folder = await async_client.folders.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
            include_versions=True,
        )
        assert_matches_type(FolderCopyResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_copy(self, async_client: AsyncImageKit) -> None:
        response = await async_client.folders.with_raw_response.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderCopyResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_copy(self, async_client: AsyncImageKit) -> None:
        async with async_client.folders.with_streaming_response.copy(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderCopyResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move(self, async_client: AsyncImageKit) -> None:
        folder = await async_client.folders.move(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_move(self, async_client: AsyncImageKit) -> None:
        response = await async_client.folders.with_raw_response.move(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderMoveResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_move(self, async_client: AsyncImageKit) -> None:
        async with async_client.folders.with_streaming_response.move(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderMoveResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rename(self, async_client: AsyncImageKit) -> None:
        folder = await async_client.folders.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
        )
        assert_matches_type(FolderRenameResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rename_with_all_params(self, async_client: AsyncImageKit) -> None:
        folder = await async_client.folders.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
            purge_cache=True,
        )
        assert_matches_type(FolderRenameResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rename(self, async_client: AsyncImageKit) -> None:
        response = await async_client.folders.with_raw_response.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        folder = await response.parse()
        assert_matches_type(FolderRenameResponse, folder, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rename(self, async_client: AsyncImageKit) -> None:
        async with async_client.folders.with_streaming_response.rename(
            folder_path="/path/of/folder",
            new_folder_name="new-folder-name",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            folder = await response.parse()
            assert_matches_type(FolderRenameResponse, folder, path=["response"])

        assert cast(Any, response.is_closed) is True
