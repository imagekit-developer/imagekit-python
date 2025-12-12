# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .usage import (
    UsageResource,
    AsyncUsageResource,
    UsageResourceWithRawResponse,
    AsyncUsageResourceWithRawResponse,
    UsageResourceWithStreamingResponse,
    AsyncUsageResourceWithStreamingResponse,
)
from .origins import (
    OriginsResource,
    AsyncOriginsResource,
    OriginsResourceWithRawResponse,
    AsyncOriginsResourceWithRawResponse,
    OriginsResourceWithStreamingResponse,
    AsyncOriginsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .url_endpoints import (
    URLEndpointsResource,
    AsyncURLEndpointsResource,
    URLEndpointsResourceWithRawResponse,
    AsyncURLEndpointsResourceWithRawResponse,
    URLEndpointsResourceWithStreamingResponse,
    AsyncURLEndpointsResourceWithStreamingResponse,
)

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def usage(self) -> UsageResource:
        return UsageResource(self._client)

    @cached_property
    def origins(self) -> OriginsResource:
        return OriginsResource(self._client)

    @cached_property
    def url_endpoints(self) -> URLEndpointsResource:
        return URLEndpointsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def usage(self) -> AsyncUsageResource:
        return AsyncUsageResource(self._client)

    @cached_property
    def origins(self) -> AsyncOriginsResource:
        return AsyncOriginsResource(self._client)

    @cached_property
    def url_endpoints(self) -> AsyncURLEndpointsResource:
        return AsyncURLEndpointsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def usage(self) -> UsageResourceWithRawResponse:
        return UsageResourceWithRawResponse(self._accounts.usage)

    @cached_property
    def origins(self) -> OriginsResourceWithRawResponse:
        return OriginsResourceWithRawResponse(self._accounts.origins)

    @cached_property
    def url_endpoints(self) -> URLEndpointsResourceWithRawResponse:
        return URLEndpointsResourceWithRawResponse(self._accounts.url_endpoints)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def usage(self) -> AsyncUsageResourceWithRawResponse:
        return AsyncUsageResourceWithRawResponse(self._accounts.usage)

    @cached_property
    def origins(self) -> AsyncOriginsResourceWithRawResponse:
        return AsyncOriginsResourceWithRawResponse(self._accounts.origins)

    @cached_property
    def url_endpoints(self) -> AsyncURLEndpointsResourceWithRawResponse:
        return AsyncURLEndpointsResourceWithRawResponse(self._accounts.url_endpoints)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def usage(self) -> UsageResourceWithStreamingResponse:
        return UsageResourceWithStreamingResponse(self._accounts.usage)

    @cached_property
    def origins(self) -> OriginsResourceWithStreamingResponse:
        return OriginsResourceWithStreamingResponse(self._accounts.origins)

    @cached_property
    def url_endpoints(self) -> URLEndpointsResourceWithStreamingResponse:
        return URLEndpointsResourceWithStreamingResponse(self._accounts.url_endpoints)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

    @cached_property
    def usage(self) -> AsyncUsageResourceWithStreamingResponse:
        return AsyncUsageResourceWithStreamingResponse(self._accounts.usage)

    @cached_property
    def origins(self) -> AsyncOriginsResourceWithStreamingResponse:
        return AsyncOriginsResourceWithStreamingResponse(self._accounts.origins)

    @cached_property
    def url_endpoints(self) -> AsyncURLEndpointsResourceWithStreamingResponse:
        return AsyncURLEndpointsResourceWithStreamingResponse(self._accounts.url_endpoints)
