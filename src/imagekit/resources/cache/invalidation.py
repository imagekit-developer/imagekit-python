# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.cache import invalidation_create_params
from ..._base_client import make_request_options
from ...types.cache.invalidation_get_response import InvalidationGetResponse
from ...types.cache.invalidation_create_response import InvalidationCreateResponse

__all__ = ["InvalidationResource", "AsyncInvalidationResource"]


class InvalidationResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InvalidationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return InvalidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InvalidationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return InvalidationResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvalidationCreateResponse:
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
            body=maybe_transform({"url": url}, invalidation_create_params.InvalidationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvalidationCreateResponse,
        )

    def get(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvalidationGetResponse:
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
            cast_to=InvalidationGetResponse,
        )


class AsyncInvalidationResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInvalidationResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInvalidationResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInvalidationResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncInvalidationResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvalidationCreateResponse:
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
            body=await async_maybe_transform({"url": url}, invalidation_create_params.InvalidationCreateParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvalidationCreateResponse,
        )

    async def get(
        self,
        request_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvalidationGetResponse:
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
            cast_to=InvalidationGetResponse,
        )


class InvalidationResourceWithRawResponse:
    def __init__(self, invalidation: InvalidationResource) -> None:
        self._invalidation = invalidation

        self.create = to_raw_response_wrapper(
            invalidation.create,
        )
        self.get = to_raw_response_wrapper(
            invalidation.get,
        )


class AsyncInvalidationResourceWithRawResponse:
    def __init__(self, invalidation: AsyncInvalidationResource) -> None:
        self._invalidation = invalidation

        self.create = async_to_raw_response_wrapper(
            invalidation.create,
        )
        self.get = async_to_raw_response_wrapper(
            invalidation.get,
        )


class InvalidationResourceWithStreamingResponse:
    def __init__(self, invalidation: InvalidationResource) -> None:
        self._invalidation = invalidation

        self.create = to_streamed_response_wrapper(
            invalidation.create,
        )
        self.get = to_streamed_response_wrapper(
            invalidation.get,
        )


class AsyncInvalidationResourceWithStreamingResponse:
    def __init__(self, invalidation: AsyncInvalidationResource) -> None:
        self._invalidation = invalidation

        self.create = async_to_streamed_response_wrapper(
            invalidation.create,
        )
        self.get = async_to_streamed_response_wrapper(
            invalidation.get,
        )
