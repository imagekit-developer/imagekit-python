# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.files import purge_execute_params
from ..._base_client import make_request_options
from ...types.files.purge_status_response import PurgeStatusResponse
from ...types.files.purge_execute_response import PurgeExecuteResponse

__all__ = ["PurgeResource", "AsyncPurgeResource"]


class PurgeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PurgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return PurgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PurgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return PurgeResourceWithStreamingResponse(self)

    def execute(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurgeExecuteResponse:
        """This API will purge CDN cache and ImageKit.io's internal cache for a file.

        Note:
        Purge cache is an asynchronous process and it may take some time to reflect the
        changes.

        Args:
          url: The full URL of the file to be purged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/purge",
            body=maybe_transform({"url": url}, purge_execute_params.PurgeExecuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurgeExecuteResponse,
        )

    def status(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurgeStatusResponse:
        """
        This API returns the status of a purge cache request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return self._get(
            f"/v1/files/purge/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurgeStatusResponse,
        )


class AsyncPurgeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPurgeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPurgeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPurgeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return AsyncPurgeResourceWithStreamingResponse(self)

    async def execute(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurgeExecuteResponse:
        """This API will purge CDN cache and ImageKit.io's internal cache for a file.

        Note:
        Purge cache is an asynchronous process and it may take some time to reflect the
        changes.

        Args:
          url: The full URL of the file to be purged.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/purge",
            body=await async_maybe_transform({"url": url}, purge_execute_params.PurgeExecuteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurgeExecuteResponse,
        )

    async def status(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> PurgeStatusResponse:
        """
        This API returns the status of a purge cache request.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not request_id:
            raise ValueError(f"Expected a non-empty value for `request_id` but received {request_id!r}")
        return await self._get(
            f"/v1/files/purge/{request_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PurgeStatusResponse,
        )


class PurgeResourceWithRawResponse:
    def __init__(self, purge: PurgeResource) -> None:
        self._purge = purge

        self.execute = to_raw_response_wrapper(
            purge.execute,
        )
        self.status = to_raw_response_wrapper(
            purge.status,
        )


class AsyncPurgeResourceWithRawResponse:
    def __init__(self, purge: AsyncPurgeResource) -> None:
        self._purge = purge

        self.execute = async_to_raw_response_wrapper(
            purge.execute,
        )
        self.status = async_to_raw_response_wrapper(
            purge.status,
        )


class PurgeResourceWithStreamingResponse:
    def __init__(self, purge: PurgeResource) -> None:
        self._purge = purge

        self.execute = to_streamed_response_wrapper(
            purge.execute,
        )
        self.status = to_streamed_response_wrapper(
            purge.status,
        )


class AsyncPurgeResourceWithStreamingResponse:
    def __init__(self, purge: AsyncPurgeResource) -> None:
        self._purge = purge

        self.execute = async_to_streamed_response_wrapper(
            purge.execute,
        )
        self.status = async_to_streamed_response_wrapper(
            purge.status,
        )
