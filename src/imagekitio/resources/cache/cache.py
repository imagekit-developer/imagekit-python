# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .invalidation import (
    InvalidationResource,
    AsyncInvalidationResource,
    InvalidationResourceWithRawResponse,
    AsyncInvalidationResourceWithRawResponse,
    InvalidationResourceWithStreamingResponse,
    AsyncInvalidationResourceWithStreamingResponse,
)

__all__ = ["CacheResource", "AsyncCacheResource"]


class CacheResource(SyncAPIResource):
    @cached_property
    def invalidation(self) -> InvalidationResource:
        return InvalidationResource(self._client)

    @cached_property
    def with_raw_response(self) -> CacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return CacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return CacheResourceWithStreamingResponse(self)


class AsyncCacheResource(AsyncAPIResource):
    @cached_property
    def invalidation(self) -> AsyncInvalidationResource:
        return AsyncInvalidationResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCacheResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCacheResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCacheResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncCacheResourceWithStreamingResponse(self)


class CacheResourceWithRawResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

    @cached_property
    def invalidation(self) -> InvalidationResourceWithRawResponse:
        return InvalidationResourceWithRawResponse(self._cache.invalidation)


class AsyncCacheResourceWithRawResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

    @cached_property
    def invalidation(self) -> AsyncInvalidationResourceWithRawResponse:
        return AsyncInvalidationResourceWithRawResponse(self._cache.invalidation)


class CacheResourceWithStreamingResponse:
    def __init__(self, cache: CacheResource) -> None:
        self._cache = cache

    @cached_property
    def invalidation(self) -> InvalidationResourceWithStreamingResponse:
        return InvalidationResourceWithStreamingResponse(self._cache.invalidation)


class AsyncCacheResourceWithStreamingResponse:
    def __init__(self, cache: AsyncCacheResource) -> None:
        self._cache = cache

    @cached_property
    def invalidation(self) -> AsyncInvalidationResourceWithStreamingResponse:
        return AsyncInvalidationResourceWithStreamingResponse(self._cache.invalidation)
