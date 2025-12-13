# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, SequenceNotStr, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.files import bulk_delete_params, bulk_add_tags_params, bulk_remove_tags_params, bulk_remove_ai_tags_params
from ..._base_client import make_request_options
from ...types.files.bulk_delete_response import BulkDeleteResponse
from ...types.files.bulk_add_tags_response import BulkAddTagsResponse
from ...types.files.bulk_remove_tags_response import BulkRemoveTagsResponse
from ...types.files.bulk_remove_ai_tags_response import BulkRemoveAITagsResponse

__all__ = ["BulkResource", "AsyncBulkResource"]


class BulkResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return BulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return BulkResourceWithStreamingResponse(self)

    def delete(
        self,
        *,
        file_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkDeleteResponse:
        """
        This API deletes multiple files and all their file versions permanently.

        Note: If a file or specific transformation has been requested in the past, then
        the response is cached. Deleting a file does not purge the cache. You can purge
        the cache using purge cache API.

        A maximum of 100 files can be deleted at a time.

        Args:
          file_ids: An array of fileIds which you want to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/batch/deleteByFileIds",
            body=maybe_transform({"file_ids": file_ids}, bulk_delete_params.BulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkDeleteResponse,
        )

    def add_tags(
        self,
        *,
        file_ids: SequenceNotStr[str],
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkAddTagsResponse:
        """This API adds tags to multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds to which you want to add tags.

          tags: An array of tags that you want to add to the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/addTags",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                bulk_add_tags_params.BulkAddTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkAddTagsResponse,
        )

    def remove_ai_tags(
        self,
        *,
        ai_tags: SequenceNotStr[str],
        file_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkRemoveAITagsResponse:
        """This API removes AITags from multiple files in bulk.

        A maximum of 50 files can
        be specified at a time.

        Args:
          ai_tags: An array of AITags that you want to remove from the files.

          file_ids: An array of fileIds from which you want to remove AITags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/removeAITags",
            body=maybe_transform(
                {
                    "ai_tags": ai_tags,
                    "file_ids": file_ids,
                },
                bulk_remove_ai_tags_params.BulkRemoveAITagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRemoveAITagsResponse,
        )

    def remove_tags(
        self,
        *,
        file_ids: SequenceNotStr[str],
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkRemoveTagsResponse:
        """This API removes tags from multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds from which you want to remove tags.

          tags: An array of tags that you want to remove from the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/removeTags",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                bulk_remove_tags_params.BulkRemoveTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRemoveTagsResponse,
        )


class AsyncBulkResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBulkResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBulkResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBulkResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncBulkResourceWithStreamingResponse(self)

    async def delete(
        self,
        *,
        file_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkDeleteResponse:
        """
        This API deletes multiple files and all their file versions permanently.

        Note: If a file or specific transformation has been requested in the past, then
        the response is cached. Deleting a file does not purge the cache. You can purge
        the cache using purge cache API.

        A maximum of 100 files can be deleted at a time.

        Args:
          file_ids: An array of fileIds which you want to delete.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/batch/deleteByFileIds",
            body=await async_maybe_transform({"file_ids": file_ids}, bulk_delete_params.BulkDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkDeleteResponse,
        )

    async def add_tags(
        self,
        *,
        file_ids: SequenceNotStr[str],
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkAddTagsResponse:
        """This API adds tags to multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds to which you want to add tags.

          tags: An array of tags that you want to add to the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/addTags",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                bulk_add_tags_params.BulkAddTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkAddTagsResponse,
        )

    async def remove_ai_tags(
        self,
        *,
        ai_tags: SequenceNotStr[str],
        file_ids: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkRemoveAITagsResponse:
        """This API removes AITags from multiple files in bulk.

        A maximum of 50 files can
        be specified at a time.

        Args:
          ai_tags: An array of AITags that you want to remove from the files.

          file_ids: An array of fileIds from which you want to remove AITags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/removeAITags",
            body=await async_maybe_transform(
                {
                    "ai_tags": ai_tags,
                    "file_ids": file_ids,
                },
                bulk_remove_ai_tags_params.BulkRemoveAITagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRemoveAITagsResponse,
        )

    async def remove_tags(
        self,
        *,
        file_ids: SequenceNotStr[str],
        tags: SequenceNotStr[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BulkRemoveTagsResponse:
        """This API removes tags from multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds from which you want to remove tags.

          tags: An array of tags that you want to remove from the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/removeTags",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                bulk_remove_tags_params.BulkRemoveTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BulkRemoveTagsResponse,
        )


class BulkResourceWithRawResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.delete = to_raw_response_wrapper(
            bulk.delete,
        )
        self.add_tags = to_raw_response_wrapper(
            bulk.add_tags,
        )
        self.remove_ai_tags = to_raw_response_wrapper(
            bulk.remove_ai_tags,
        )
        self.remove_tags = to_raw_response_wrapper(
            bulk.remove_tags,
        )


class AsyncBulkResourceWithRawResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.delete = async_to_raw_response_wrapper(
            bulk.delete,
        )
        self.add_tags = async_to_raw_response_wrapper(
            bulk.add_tags,
        )
        self.remove_ai_tags = async_to_raw_response_wrapper(
            bulk.remove_ai_tags,
        )
        self.remove_tags = async_to_raw_response_wrapper(
            bulk.remove_tags,
        )


class BulkResourceWithStreamingResponse:
    def __init__(self, bulk: BulkResource) -> None:
        self._bulk = bulk

        self.delete = to_streamed_response_wrapper(
            bulk.delete,
        )
        self.add_tags = to_streamed_response_wrapper(
            bulk.add_tags,
        )
        self.remove_ai_tags = to_streamed_response_wrapper(
            bulk.remove_ai_tags,
        )
        self.remove_tags = to_streamed_response_wrapper(
            bulk.remove_tags,
        )


class AsyncBulkResourceWithStreamingResponse:
    def __init__(self, bulk: AsyncBulkResource) -> None:
        self._bulk = bulk

        self.delete = async_to_streamed_response_wrapper(
            bulk.delete,
        )
        self.add_tags = async_to_streamed_response_wrapper(
            bulk.add_tags,
        )
        self.remove_ai_tags = async_to_streamed_response_wrapper(
            bulk.remove_ai_tags,
        )
        self.remove_tags = async_to_streamed_response_wrapper(
            bulk.remove_tags,
        )
