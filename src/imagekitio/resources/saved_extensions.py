# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import saved_extension_create_params, saved_extension_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.shared.saved_extension import SavedExtension
from ..types.saved_extension_list_response import SavedExtensionListResponse
from ..types.shared_params.extension_config import ExtensionConfig

__all__ = ["SavedExtensionsResource", "AsyncSavedExtensionsResource"]


class SavedExtensionsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SavedExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return SavedExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SavedExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return SavedExtensionsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        config: ExtensionConfig,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedExtension:
        """This API creates a new saved extension.

        Saved extensions allow you to save
        complex extension configurations (like AI tasks) and reuse them by referencing
        the ID in upload or update file APIs.

        **Saved extension limit** \\
        You can create a maximum of 100 saved extensions per account.

        Args:
          config: Configuration object for an extension (base extensions only, not saved extension
              references).

          description: Description of what the saved extension does.

          name: Name of the saved extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/saved-extensions",
            body=maybe_transform(
                {
                    "config": config,
                    "description": description,
                    "name": name,
                },
                saved_extension_create_params.SavedExtensionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtension,
        )

    def update(
        self,
        id: str,
        *,
        config: ExtensionConfig | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedExtension:
        """This API updates an existing saved extension.

        You can update the name,
        description, or config.

        Args:
          config: Configuration object for an extension (base extensions only, not saved extension
              references).

          description: Updated description of the saved extension.

          name: Updated name of the saved extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v1/saved-extensions/{id}",
            body=maybe_transform(
                {
                    "config": config,
                    "description": description,
                    "name": name,
                },
                saved_extension_update_params.SavedExtensionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtension,
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
    ) -> SavedExtensionListResponse:
        """This API returns an array of all saved extensions for your account.

        Saved
        extensions allow you to save complex extension configurations and reuse them by
        referencing them by ID in upload or update file APIs.
        """
        return self._get(
            "/v1/saved-extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtensionListResponse,
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
        """
        This API deletes a saved extension permanently.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/saved-extensions/{id}",
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
    ) -> SavedExtension:
        """
        This API returns details of a specific saved extension by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            f"/v1/saved-extensions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtension,
        )


class AsyncSavedExtensionsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSavedExtensionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSavedExtensionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSavedExtensionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncSavedExtensionsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        config: ExtensionConfig,
        description: str,
        name: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedExtension:
        """This API creates a new saved extension.

        Saved extensions allow you to save
        complex extension configurations (like AI tasks) and reuse them by referencing
        the ID in upload or update file APIs.

        **Saved extension limit** \\
        You can create a maximum of 100 saved extensions per account.

        Args:
          config: Configuration object for an extension (base extensions only, not saved extension
              references).

          description: Description of what the saved extension does.

          name: Name of the saved extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/saved-extensions",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "description": description,
                    "name": name,
                },
                saved_extension_create_params.SavedExtensionCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtension,
        )

    async def update(
        self,
        id: str,
        *,
        config: ExtensionConfig | Omit = omit,
        description: str | Omit = omit,
        name: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SavedExtension:
        """This API updates an existing saved extension.

        You can update the name,
        description, or config.

        Args:
          config: Configuration object for an extension (base extensions only, not saved extension
              references).

          description: Updated description of the saved extension.

          name: Updated name of the saved extension.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v1/saved-extensions/{id}",
            body=await async_maybe_transform(
                {
                    "config": config,
                    "description": description,
                    "name": name,
                },
                saved_extension_update_params.SavedExtensionUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtension,
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
    ) -> SavedExtensionListResponse:
        """This API returns an array of all saved extensions for your account.

        Saved
        extensions allow you to save complex extension configurations and reuse them by
        referencing them by ID in upload or update file APIs.
        """
        return await self._get(
            "/v1/saved-extensions",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtensionListResponse,
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
        """
        This API deletes a saved extension permanently.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/saved-extensions/{id}",
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
    ) -> SavedExtension:
        """
        This API returns details of a specific saved extension by ID.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            f"/v1/saved-extensions/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SavedExtension,
        )


class SavedExtensionsResourceWithRawResponse:
    def __init__(self, saved_extensions: SavedExtensionsResource) -> None:
        self._saved_extensions = saved_extensions

        self.create = to_raw_response_wrapper(
            saved_extensions.create,
        )
        self.update = to_raw_response_wrapper(
            saved_extensions.update,
        )
        self.list = to_raw_response_wrapper(
            saved_extensions.list,
        )
        self.delete = to_raw_response_wrapper(
            saved_extensions.delete,
        )
        self.get = to_raw_response_wrapper(
            saved_extensions.get,
        )


class AsyncSavedExtensionsResourceWithRawResponse:
    def __init__(self, saved_extensions: AsyncSavedExtensionsResource) -> None:
        self._saved_extensions = saved_extensions

        self.create = async_to_raw_response_wrapper(
            saved_extensions.create,
        )
        self.update = async_to_raw_response_wrapper(
            saved_extensions.update,
        )
        self.list = async_to_raw_response_wrapper(
            saved_extensions.list,
        )
        self.delete = async_to_raw_response_wrapper(
            saved_extensions.delete,
        )
        self.get = async_to_raw_response_wrapper(
            saved_extensions.get,
        )


class SavedExtensionsResourceWithStreamingResponse:
    def __init__(self, saved_extensions: SavedExtensionsResource) -> None:
        self._saved_extensions = saved_extensions

        self.create = to_streamed_response_wrapper(
            saved_extensions.create,
        )
        self.update = to_streamed_response_wrapper(
            saved_extensions.update,
        )
        self.list = to_streamed_response_wrapper(
            saved_extensions.list,
        )
        self.delete = to_streamed_response_wrapper(
            saved_extensions.delete,
        )
        self.get = to_streamed_response_wrapper(
            saved_extensions.get,
        )


class AsyncSavedExtensionsResourceWithStreamingResponse:
    def __init__(self, saved_extensions: AsyncSavedExtensionsResource) -> None:
        self._saved_extensions = saved_extensions

        self.create = async_to_streamed_response_wrapper(
            saved_extensions.create,
        )
        self.update = async_to_streamed_response_wrapper(
            saved_extensions.update,
        )
        self.list = async_to_streamed_response_wrapper(
            saved_extensions.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            saved_extensions.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            saved_extensions.get,
        )
