# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import bulk_job_copy_folder_params, bulk_job_move_folder_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.bulk_job_copy_folder_response import BulkJobCopyFolderResponse
from ..types.bulk_job_move_folder_response import BulkJobMoveFolderResponse
from ..types.bulk_job_retrieve_status_response import BulkJobRetrieveStatusResponse

__all__ = ["BulkJobsResource", "AsyncBulkJobsResource"]


class BulkJobsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return BulkJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return BulkJobsResourceWithStreamingResponse(self)

    def copy_folder(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        include_versions: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkJobCopyFolderResponse:
        """This will copy one folder into another.

        The selected folder, its nested folders,
        files, and their versions (in `includeVersions` is set to true) are copied in
        this operation. Note: If any file at the destination has the same name as the
        source file, then the source file and its versions will be appended to the
        destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to copy the source folder
              into.

          source_folder_path: The full path to the source folder you want to copy.

          include_versions: Option to copy all versions of files that are nested inside the selected folder.
              By default, only the current version of each file will be copied. When set to
              true, all versions of each file will be copied. Default value - `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/bulkJobs/copyFolder",
            body=maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                    "include_versions": include_versions,
                },
                bulk_job_copy_folder_params.BulkJobCopyFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkJobCopyFolderResponse,
        )

    def move_folder(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkJobMoveFolderResponse:
        """This will move one folder into another.

        The selected folder, its nested folders,
        files, and their versions are moved in this operation. Note: If any file at the
        destination has the same name as the source file, then the source file and its
        versions will be appended to the destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to move the source folder
              into.

          source_folder_path: The full path to the source folder you want to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/bulkJobs/moveFolder",
            body=maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                },
                bulk_job_move_folder_params.BulkJobMoveFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkJobMoveFolderResponse,
        )

    def retrieve_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkJobRetrieveStatusResponse:
        """
        This API returns the status of a bulk job like copy and move folder operations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return self._get(
            f"/v1/bulkJobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkJobRetrieveStatusResponse,
        )


class AsyncBulkJobsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkJobsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkJobsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkJobsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return AsyncBulkJobsResourceWithStreamingResponse(self)

    async def copy_folder(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        include_versions: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkJobCopyFolderResponse:
        """This will copy one folder into another.

        The selected folder, its nested folders,
        files, and their versions (in `includeVersions` is set to true) are copied in
        this operation. Note: If any file at the destination has the same name as the
        source file, then the source file and its versions will be appended to the
        destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to copy the source folder
              into.

          source_folder_path: The full path to the source folder you want to copy.

          include_versions: Option to copy all versions of files that are nested inside the selected folder.
              By default, only the current version of each file will be copied. When set to
              true, all versions of each file will be copied. Default value - `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/bulkJobs/copyFolder",
            body=await async_maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                    "include_versions": include_versions,
                },
                bulk_job_copy_folder_params.BulkJobCopyFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkJobCopyFolderResponse,
        )

    async def move_folder(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkJobMoveFolderResponse:
        """This will move one folder into another.

        The selected folder, its nested folders,
        files, and their versions are moved in this operation. Note: If any file at the
        destination has the same name as the source file, then the source file and its
        versions will be appended to the destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to move the source folder
              into.

          source_folder_path: The full path to the source folder you want to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/bulkJobs/moveFolder",
            body=await async_maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                },
                bulk_job_move_folder_params.BulkJobMoveFolderParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkJobMoveFolderResponse,
        )

    async def retrieve_status(
        self,
        job_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> BulkJobRetrieveStatusResponse:
        """
        This API returns the status of a bulk job like copy and move folder operations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not job_id:
            raise ValueError(f"Expected a non-empty value for `job_id` but received {job_id!r}")
        return await self._get(
            f"/v1/bulkJobs/{job_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkJobRetrieveStatusResponse,
        )


class BulkJobsResourceWithRawResponse:
    def __init__(self, bulk_jobs: BulkJobsResource) -> None:
        self._bulk_jobs = bulk_jobs

        self.copy_folder = to_raw_response_wrapper(
            bulk_jobs.copy_folder,
        )
        self.move_folder = to_raw_response_wrapper(
            bulk_jobs.move_folder,
        )
        self.retrieve_status = to_raw_response_wrapper(
            bulk_jobs.retrieve_status,
        )


class AsyncBulkJobsResourceWithRawResponse:
    def __init__(self, bulk_jobs: AsyncBulkJobsResource) -> None:
        self._bulk_jobs = bulk_jobs

        self.copy_folder = async_to_raw_response_wrapper(
            bulk_jobs.copy_folder,
        )
        self.move_folder = async_to_raw_response_wrapper(
            bulk_jobs.move_folder,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            bulk_jobs.retrieve_status,
        )


class BulkJobsResourceWithStreamingResponse:
    def __init__(self, bulk_jobs: BulkJobsResource) -> None:
        self._bulk_jobs = bulk_jobs

        self.copy_folder = to_streamed_response_wrapper(
            bulk_jobs.copy_folder,
        )
        self.move_folder = to_streamed_response_wrapper(
            bulk_jobs.move_folder,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            bulk_jobs.retrieve_status,
        )


class AsyncBulkJobsResourceWithStreamingResponse:
    def __init__(self, bulk_jobs: AsyncBulkJobsResource) -> None:
        self._bulk_jobs = bulk_jobs

        self.copy_folder = async_to_streamed_response_wrapper(
            bulk_jobs.copy_folder,
        )
        self.move_folder = async_to_streamed_response_wrapper(
            bulk_jobs.move_folder,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            bulk_jobs.retrieve_status,
        )
