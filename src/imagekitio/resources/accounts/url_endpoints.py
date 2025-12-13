# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.accounts import url_endpoint_create_params, url_endpoint_update_params
from ...types.accounts.url_endpoint_response import URLEndpointResponse
from ...types.accounts.url_endpoint_list_response import URLEndpointListResponse

__all__ = ["URLEndpointsResource", "AsyncURLEndpointsResource"]


class URLEndpointsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> URLEndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return URLEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> URLEndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return URLEndpointsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        description: str,
        origins: SequenceNotStr[str] | Omit = omit,
        url_prefix: str | Omit = omit,
        url_rewriter: url_endpoint_create_params.URLRewriter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointResponse:
        """**Note:** This API is currently in beta.


        Creates a new URL‑endpoint and returns the resulting object.

        Args:
          description: Description of the URL endpoint.

          origins: Ordered list of origin IDs to try when the file isn’t in the Media Library;
              ImageKit checks them in the sequence provided. Origin must be created before it
              can be used in a URL endpoint.

          url_prefix: Path segment appended to your base URL to form the endpoint (letters, digits,
              and hyphens only — or empty for the default endpoint).

          url_rewriter: Configuration for third-party URL rewriting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/accounts/url-endpoints",
            body=maybe_transform(
                {
                    "description": description,
                    "origins": origins,
                    "url_prefix": url_prefix,
                    "url_rewriter": url_rewriter,
                },
                url_endpoint_create_params.URLEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointResponse,
        )

    def update(
        self,
        id: str,
        *,
        description: str,
        origins: SequenceNotStr[str] | Omit = omit,
        url_prefix: str | Omit = omit,
        url_rewriter: url_endpoint_update_params.URLRewriter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointResponse:
        """**Note:** This API is currently in beta.


        Updates the URL‑endpoint identified by `id` and returns the updated object.

        Args:
          id: Unique identifier for the URL-endpoint. This is generated by ImageKit when you
              create a new URL-endpoint. For the default URL-endpoint, this is always
              `default`.

          description: Description of the URL endpoint.

          origins: Ordered list of origin IDs to try when the file isn’t in the Media Library;
              ImageKit checks them in the sequence provided. Origin must be created before it
              can be used in a URL endpoint.

          url_prefix: Path segment appended to your base URL to form the endpoint (letters, digits,
              and hyphens only — or empty for the default endpoint).

          url_rewriter: Configuration for third-party URL rewriting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._put(
            f"/v1/accounts/url-endpoints/{id}",
            body=maybe_transform(
                {
                    "description": description,
                    "origins": origins,
                    "url_prefix": url_prefix,
                    "url_rewriter": url_rewriter,
                },
                url_endpoint_update_params.URLEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointResponse,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointListResponse:
        """**Note:** This API is currently in beta.


        Returns an array of all URL‑endpoints configured including the default
        URL-endpoint generated by ImageKit during account creation.
        """
        return self._get(
            "/v1/accounts/url-endpoints",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Note:** This API is currently in beta.


        Deletes the URL‑endpoint identified by `id`. You cannot delete the default
        URL‑endpoint created by ImageKit during account creation.

        Args:
          id: Unique identifier for the URL-endpoint. This is generated by ImageKit when you
              create a new URL-endpoint. For the default URL-endpoint, this is always
              `default`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/accounts/url-endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointResponse:
        """**Note:** This API is currently in beta.


        Retrieves the URL‑endpoint identified by `id`.

        Args:
          id: Unique identifier for the URL-endpoint. This is generated by ImageKit when you
              create a new URL-endpoint. For the default URL-endpoint, this is always
              `default`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/accounts/url-endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointResponse,
        )


class AsyncURLEndpointsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncURLEndpointsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncURLEndpointsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncURLEndpointsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncURLEndpointsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        description: str,
        origins: SequenceNotStr[str] | Omit = omit,
        url_prefix: str | Omit = omit,
        url_rewriter: url_endpoint_create_params.URLRewriter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointResponse:
        """**Note:** This API is currently in beta.


        Creates a new URL‑endpoint and returns the resulting object.

        Args:
          description: Description of the URL endpoint.

          origins: Ordered list of origin IDs to try when the file isn’t in the Media Library;
              ImageKit checks them in the sequence provided. Origin must be created before it
              can be used in a URL endpoint.

          url_prefix: Path segment appended to your base URL to form the endpoint (letters, digits,
              and hyphens only — or empty for the default endpoint).

          url_rewriter: Configuration for third-party URL rewriting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/accounts/url-endpoints",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "origins": origins,
                    "url_prefix": url_prefix,
                    "url_rewriter": url_rewriter,
                },
                url_endpoint_create_params.URLEndpointCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointResponse,
        )

    async def update(
        self,
        id: str,
        *,
        description: str,
        origins: SequenceNotStr[str] | Omit = omit,
        url_prefix: str | Omit = omit,
        url_rewriter: url_endpoint_update_params.URLRewriter | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointResponse:
        """**Note:** This API is currently in beta.


        Updates the URL‑endpoint identified by `id` and returns the updated object.

        Args:
          id: Unique identifier for the URL-endpoint. This is generated by ImageKit when you
              create a new URL-endpoint. For the default URL-endpoint, this is always
              `default`.

          description: Description of the URL endpoint.

          origins: Ordered list of origin IDs to try when the file isn’t in the Media Library;
              ImageKit checks them in the sequence provided. Origin must be created before it
              can be used in a URL endpoint.

          url_prefix: Path segment appended to your base URL to form the endpoint (letters, digits,
              and hyphens only — or empty for the default endpoint).

          url_rewriter: Configuration for third-party URL rewriting.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._put(
            f"/v1/accounts/url-endpoints/{id}",
            body=await async_maybe_transform(
                {
                    "description": description,
                    "origins": origins,
                    "url_prefix": url_prefix,
                    "url_rewriter": url_rewriter,
                },
                url_endpoint_update_params.URLEndpointUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointResponse,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointListResponse:
        """**Note:** This API is currently in beta.


        Returns an array of all URL‑endpoints configured including the default
        URL-endpoint generated by ImageKit during account creation.
        """
        return await self._get(
            "/v1/accounts/url-endpoints",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Note:** This API is currently in beta.


        Deletes the URL‑endpoint identified by `id`. You cannot delete the default
        URL‑endpoint created by ImageKit during account creation.

        Args:
          id: Unique identifier for the URL-endpoint. This is generated by ImageKit when you
              create a new URL-endpoint. For the default URL-endpoint, this is always
              `default`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/accounts/url-endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> URLEndpointResponse:
        """**Note:** This API is currently in beta.


        Retrieves the URL‑endpoint identified by `id`.

        Args:
          id: Unique identifier for the URL-endpoint. This is generated by ImageKit when you
              create a new URL-endpoint. For the default URL-endpoint, this is always
              `default`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/accounts/url-endpoints/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=URLEndpointResponse,
        )


class URLEndpointsResourceWithRawResponse:
    def __init__(self, url_endpoints: URLEndpointsResource) -> None:
        self._url_endpoints = url_endpoints

        self.create = to_raw_response_wrapper(
            url_endpoints.create,
        )
        self.update = to_raw_response_wrapper(
            url_endpoints.update,
        )
        self.list = to_raw_response_wrapper(
            url_endpoints.list,
        )
        self.delete = to_raw_response_wrapper(
            url_endpoints.delete,
        )
        self.get = to_raw_response_wrapper(
            url_endpoints.get,
        )


class AsyncURLEndpointsResourceWithRawResponse:
    def __init__(self, url_endpoints: AsyncURLEndpointsResource) -> None:
        self._url_endpoints = url_endpoints

        self.create = async_to_raw_response_wrapper(
            url_endpoints.create,
        )
        self.update = async_to_raw_response_wrapper(
            url_endpoints.update,
        )
        self.list = async_to_raw_response_wrapper(
            url_endpoints.list,
        )
        self.delete = async_to_raw_response_wrapper(
            url_endpoints.delete,
        )
        self.get = async_to_raw_response_wrapper(
            url_endpoints.get,
        )


class URLEndpointsResourceWithStreamingResponse:
    def __init__(self, url_endpoints: URLEndpointsResource) -> None:
        self._url_endpoints = url_endpoints

        self.create = to_streamed_response_wrapper(
            url_endpoints.create,
        )
        self.update = to_streamed_response_wrapper(
            url_endpoints.update,
        )
        self.list = to_streamed_response_wrapper(
            url_endpoints.list,
        )
        self.delete = to_streamed_response_wrapper(
            url_endpoints.delete,
        )
        self.get = to_streamed_response_wrapper(
            url_endpoints.get,
        )


class AsyncURLEndpointsResourceWithStreamingResponse:
    def __init__(self, url_endpoints: AsyncURLEndpointsResource) -> None:
        self._url_endpoints = url_endpoints

        self.create = async_to_streamed_response_wrapper(
            url_endpoints.create,
        )
        self.update = async_to_streamed_response_wrapper(
            url_endpoints.update,
        )
        self.list = async_to_streamed_response_wrapper(
            url_endpoints.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            url_endpoints.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            url_endpoints.get,
        )
