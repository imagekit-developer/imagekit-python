# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

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
from ..._base_client import make_request_options
from ...types.accounts import usage_analytics_get_params
from ...types.accounts.usage_analytics_response import UsageAnalyticsResponse

__all__ = ["UsageAnalyticsResource", "AsyncUsageAnalyticsResource"]


class UsageAnalyticsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> UsageAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return UsageAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> UsageAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return UsageAnalyticsResourceWithStreamingResponse(self)

    def get(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageAnalyticsResponse:
        """
        **Note:** This API is currently in beta.

        Get the account analytics data between two dates. The response covers the period
        from the start date to the end date, both dates inclusive. Both dates are
        interpreted as UTC calendar days.

        The returned data is scoped to the requesting account only. Unlike
        `/v1/accounts/usage`, an agency account's analytics are not aggregated across
        its child accounts.

        The response is cached for 5 minutes per account and date range. Use
        `generatedAt` to check how fresh the returned data is.

        Args:
          end_date: Specify an `endDate` in `YYYY-MM-DD` format, interpreted as a UTC calendar day.
              It should be after the `startDate`. The difference between `startDate` and
              `endDate` should be less than 90 days.

          start_date: Specify a `startDate` in `YYYY-MM-DD` format, interpreted as a UTC calendar day.
              It should be before the `endDate`. The difference between `startDate` and
              `endDate` should be less than 90 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/accounts/usage-analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    usage_analytics_get_params.UsageAnalyticsGetParams,
                ),
            ),
            cast_to=UsageAnalyticsResponse,
        )


class AsyncUsageAnalyticsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncUsageAnalyticsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncUsageAnalyticsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncUsageAnalyticsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncUsageAnalyticsResourceWithStreamingResponse(self)

    async def get(
        self,
        *,
        end_date: Union[str, date],
        start_date: Union[str, date],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UsageAnalyticsResponse:
        """
        **Note:** This API is currently in beta.

        Get the account analytics data between two dates. The response covers the period
        from the start date to the end date, both dates inclusive. Both dates are
        interpreted as UTC calendar days.

        The returned data is scoped to the requesting account only. Unlike
        `/v1/accounts/usage`, an agency account's analytics are not aggregated across
        its child accounts.

        The response is cached for 5 minutes per account and date range. Use
        `generatedAt` to check how fresh the returned data is.

        Args:
          end_date: Specify an `endDate` in `YYYY-MM-DD` format, interpreted as a UTC calendar day.
              It should be after the `startDate`. The difference between `startDate` and
              `endDate` should be less than 90 days.

          start_date: Specify a `startDate` in `YYYY-MM-DD` format, interpreted as a UTC calendar day.
              It should be before the `endDate`. The difference between `startDate` and
              `endDate` should be less than 90 days.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/accounts/usage-analytics",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    usage_analytics_get_params.UsageAnalyticsGetParams,
                ),
            ),
            cast_to=UsageAnalyticsResponse,
        )


class UsageAnalyticsResourceWithRawResponse:
    def __init__(self, usage_analytics: UsageAnalyticsResource) -> None:
        self._usage_analytics = usage_analytics

        self.get = to_raw_response_wrapper(
            usage_analytics.get,
        )


class AsyncUsageAnalyticsResourceWithRawResponse:
    def __init__(self, usage_analytics: AsyncUsageAnalyticsResource) -> None:
        self._usage_analytics = usage_analytics

        self.get = async_to_raw_response_wrapper(
            usage_analytics.get,
        )


class UsageAnalyticsResourceWithStreamingResponse:
    def __init__(self, usage_analytics: UsageAnalyticsResource) -> None:
        self._usage_analytics = usage_analytics

        self.get = to_streamed_response_wrapper(
            usage_analytics.get,
        )


class AsyncUsageAnalyticsResourceWithStreamingResponse:
    def __init__(self, usage_analytics: AsyncUsageAnalyticsResource) -> None:
        self._usage_analytics = usage_analytics

        self.get = async_to_streamed_response_wrapper(
            usage_analytics.get,
        )
