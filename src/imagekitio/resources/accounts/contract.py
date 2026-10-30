# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts.contract_get_response import ContractGetResponse

__all__ = ["ContractResource", "AsyncContractResource"]


class ContractResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return ContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return ContractResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractGetResponse:
        """
        Get the account's contract terms and the usage consumed against them in the
        current contract term. Bandwidth is in bytes; video processing units, extension
        units and purge cache requests are counts.

        For an agency account, consumption includes the child accounts billed to it. A
        child account billed to its parent cannot call this endpoint; call it with the
        parent account's credentials instead.

        Contract terms are read live; consumption is refreshed periodically, not on
        every request. Use `asOf` to check how fresh it is. Contracts of one month or
        less are reported as `hasContract: false`. The response is cached for 5 minutes
        per account.

        Requires an API key with account management access.
        """
        return self._get(
            "/v1/accounts/contract",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractGetResponse,
        )


class AsyncContractResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncContractResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncContractResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncContractResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncContractResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ContractGetResponse:
        """
        Get the account's contract terms and the usage consumed against them in the
        current contract term. Bandwidth is in bytes; video processing units, extension
        units and purge cache requests are counts.

        For an agency account, consumption includes the child accounts billed to it. A
        child account billed to its parent cannot call this endpoint; call it with the
        parent account's credentials instead.

        Contract terms are read live; consumption is refreshed periodically, not on
        every request. Use `asOf` to check how fresh it is. Contracts of one month or
        less are reported as `hasContract: false`. The response is cached for 5 minutes
        per account.

        Requires an API key with account management access.
        """
        return await self._get(
            "/v1/accounts/contract",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ContractGetResponse,
        )


class ContractResourceWithRawResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.get = to_raw_response_wrapper(
            contract.get,
        )


class AsyncContractResourceWithRawResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.get = async_to_raw_response_wrapper(
            contract.get,
        )


class ContractResourceWithStreamingResponse:
    def __init__(self, contract: ContractResource) -> None:
        self._contract = contract

        self.get = to_streamed_response_wrapper(
            contract.get,
        )


class AsyncContractResourceWithStreamingResponse:
    def __init__(self, contract: AsyncContractResource) -> None:
        self._contract = contract

        self.get = async_to_streamed_response_wrapper(
            contract.get,
        )
