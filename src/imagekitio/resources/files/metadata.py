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
from ...types.files import metadata_get_from_url_params
from ..._base_client import make_request_options
from ...types.metadata import Metadata

__all__ = ["MetadataResource", "AsyncMetadataResource"]


class MetadataResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> MetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return MetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return MetadataResourceWithStreamingResponse(self)

    def get(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Metadata:
        """
        You can programmatically get image EXIF, pHash, and other metadata for uploaded
        files in the ImageKit.io media library using this API.

        You can also get the metadata in upload API response by passing `metadata` in
        `responseFields` parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/files/{file_id}/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metadata,
        )

    def get_from_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Metadata:
        """
        Get image EXIF, pHash, and other metadata from ImageKit.io powered remote URL
        using this API.

        Args:
          url: Should be a valid file URL. It should be accessible using your ImageKit.io
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/files/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"url": url}, metadata_get_from_url_params.MetadataGetFromURLParams),
            ),
            cast_to=Metadata,
        )


class AsyncMetadataResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncMetadataResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMetadataResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMetadataResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncMetadataResourceWithStreamingResponse(self)

    async def get(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Metadata:
        """
        You can programmatically get image EXIF, pHash, and other metadata for uploaded
        files in the ImageKit.io media library using this API.

        You can also get the metadata in upload API response by passing `metadata` in
        `responseFields` parameter.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/files/{file_id}/metadata",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Metadata,
        )

    async def get_from_url(
        self,
        *,
        url: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Metadata:
        """
        Get image EXIF, pHash, and other metadata from ImageKit.io powered remote URL
        using this API.

        Args:
          url: Should be a valid file URL. It should be accessible using your ImageKit.io
              account.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/files/metadata",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"url": url}, metadata_get_from_url_params.MetadataGetFromURLParams),
            ),
            cast_to=Metadata,
        )


class MetadataResourceWithRawResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.get = to_raw_response_wrapper(
            metadata.get,
        )
        self.get_from_url = to_raw_response_wrapper(
            metadata.get_from_url,
        )


class AsyncMetadataResourceWithRawResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.get = async_to_raw_response_wrapper(
            metadata.get,
        )
        self.get_from_url = async_to_raw_response_wrapper(
            metadata.get_from_url,
        )


class MetadataResourceWithStreamingResponse:
    def __init__(self, metadata: MetadataResource) -> None:
        self._metadata = metadata

        self.get = to_streamed_response_wrapper(
            metadata.get,
        )
        self.get_from_url = to_streamed_response_wrapper(
            metadata.get_from_url,
        )


class AsyncMetadataResourceWithStreamingResponse:
    def __init__(self, metadata: AsyncMetadataResource) -> None:
        self._metadata = metadata

        self.get = async_to_streamed_response_wrapper(
            metadata.get,
        )
        self.get_from_url = async_to_streamed_response_wrapper(
            metadata.get_from_url,
        )
