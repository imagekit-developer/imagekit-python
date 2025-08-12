# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekit import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekit.types import (
    BulkJobCopyFolderResponse,
    BulkJobMoveFolderResponse,
    BulkJobRetrieveStatusResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBulkJobs:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy_folder(self, client: ImageKit) -> None:
        bulk_job = client.bulk_jobs.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_copy_folder_with_all_params(self, client: ImageKit) -> None:
        bulk_job = client.bulk_jobs.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
            include_versions=True,
        )
        assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_copy_folder(self, client: ImageKit) -> None:
        response = client.bulk_jobs.with_raw_response.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_job = response.parse()
        assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_copy_folder(self, client: ImageKit) -> None:
        with client.bulk_jobs.with_streaming_response.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_job = response.parse()
            assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_move_folder(self, client: ImageKit) -> None:
        bulk_job = client.bulk_jobs.move_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(BulkJobMoveFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_move_folder(self, client: ImageKit) -> None:
        response = client.bulk_jobs.with_raw_response.move_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_job = response.parse()
        assert_matches_type(BulkJobMoveFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_move_folder(self, client: ImageKit) -> None:
        with client.bulk_jobs.with_streaming_response.move_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_job = response.parse()
            assert_matches_type(BulkJobMoveFolderResponse, bulk_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: ImageKit) -> None:
        bulk_job = client.bulk_jobs.retrieve_status(
            "jobId",
        )
        assert_matches_type(BulkJobRetrieveStatusResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: ImageKit) -> None:
        response = client.bulk_jobs.with_raw_response.retrieve_status(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_job = response.parse()
        assert_matches_type(BulkJobRetrieveStatusResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: ImageKit) -> None:
        with client.bulk_jobs.with_streaming_response.retrieve_status(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_job = response.parse()
            assert_matches_type(BulkJobRetrieveStatusResponse, bulk_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            client.bulk_jobs.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncBulkJobs:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy_folder(self, async_client: AsyncImageKit) -> None:
        bulk_job = await async_client.bulk_jobs.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_copy_folder_with_all_params(self, async_client: AsyncImageKit) -> None:
        bulk_job = await async_client.bulk_jobs.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
            include_versions=True,
        )
        assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_copy_folder(self, async_client: AsyncImageKit) -> None:
        response = await async_client.bulk_jobs.with_raw_response.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_job = await response.parse()
        assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_copy_folder(self, async_client: AsyncImageKit) -> None:
        async with async_client.bulk_jobs.with_streaming_response.copy_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_job = await response.parse()
            assert_matches_type(BulkJobCopyFolderResponse, bulk_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_move_folder(self, async_client: AsyncImageKit) -> None:
        bulk_job = await async_client.bulk_jobs.move_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )
        assert_matches_type(BulkJobMoveFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_move_folder(self, async_client: AsyncImageKit) -> None:
        response = await async_client.bulk_jobs.with_raw_response.move_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_job = await response.parse()
        assert_matches_type(BulkJobMoveFolderResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_move_folder(self, async_client: AsyncImageKit) -> None:
        async with async_client.bulk_jobs.with_streaming_response.move_folder(
            destination_path="/path/of/destination/folder",
            source_folder_path="/path/of/source/folder",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_job = await response.parse()
            assert_matches_type(BulkJobMoveFolderResponse, bulk_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncImageKit) -> None:
        bulk_job = await async_client.bulk_jobs.retrieve_status(
            "jobId",
        )
        assert_matches_type(BulkJobRetrieveStatusResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncImageKit) -> None:
        response = await async_client.bulk_jobs.with_raw_response.retrieve_status(
            "jobId",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        bulk_job = await response.parse()
        assert_matches_type(BulkJobRetrieveStatusResponse, bulk_job, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncImageKit) -> None:
        async with async_client.bulk_jobs.with_streaming_response.retrieve_status(
            "jobId",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            bulk_job = await response.parse()
            assert_matches_type(BulkJobRetrieveStatusResponse, bulk_job, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `job_id` but received ''"):
            await async_client.bulk_jobs.with_raw_response.retrieve_status(
                "",
            )
