# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import folder_create_params, folder_delete_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
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

__all__ = ["FolderResource", "AsyncFolderResource"]


class FolderResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FolderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return FolderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FolderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return FolderResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        folder_name: str,
        parent_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """This will create a new folder.

        You can specify the folder name and location of
        the parent folder where this new folder should be created.

        Args:
          folder_name: The folder will be created with this name.

              All characters except alphabets and numbers (inclusive of unicode letters,
              marks, and numerals in other languages) will be replaced by an underscore i.e.
              `_`.

          parent_folder_path: The folder where the new folder should be created, for root use `/` else the
              path e.g. `containing/folder/`.

              Note: If any folder(s) is not present in the parentFolderPath parameter, it will
              be automatically created. For example, if you pass `/product/images/summer`,
              then `product`, `images`, and `summer` folders will be created if they don't
              already exist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/folder",
            body=maybe_transform(
                {
                    "folder_name": folder_name,
                    "parent_folder_path": parent_folder_path,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    def delete(
        self,
        *,
        folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """This will delete a folder and all its contents permanently.

        The API returns an
        empty response.

        Args:
          folder_path: Full path to the folder you want to delete. For example `/folder/to/delete/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/folder",
            body=maybe_transform({"folder_path": folder_path}, folder_delete_params.FolderDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class AsyncFolderResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFolderResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFolderResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFolderResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return AsyncFolderResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        folder_name: str,
        parent_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """This will create a new folder.

        You can specify the folder name and location of
        the parent folder where this new folder should be created.

        Args:
          folder_name: The folder will be created with this name.

              All characters except alphabets and numbers (inclusive of unicode letters,
              marks, and numerals in other languages) will be replaced by an underscore i.e.
              `_`.

          parent_folder_path: The folder where the new folder should be created, for root use `/` else the
              path e.g. `containing/folder/`.

              Note: If any folder(s) is not present in the parentFolderPath parameter, it will
              be automatically created. For example, if you pass `/product/images/summer`,
              then `product`, `images`, and `summer` folders will be created if they don't
              already exist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/folder",
            body=await async_maybe_transform(
                {
                    "folder_name": folder_name,
                    "parent_folder_path": parent_folder_path,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )

    async def delete(
        self,
        *,
        folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
        """This will delete a folder and all its contents permanently.

        The API returns an
        empty response.

        Args:
          folder_path: Full path to the folder you want to delete. For example `/folder/to/delete/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/folder",
            body=await async_maybe_transform({"folder_path": folder_path}, folder_delete_params.FolderDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=object,
        )


class FolderResourceWithRawResponse:
    def __init__(self, folder: FolderResource) -> None:
        self._folder = folder

        self.create = to_raw_response_wrapper(
            folder.create,
        )
        self.delete = to_raw_response_wrapper(
            folder.delete,
        )


class AsyncFolderResourceWithRawResponse:
    def __init__(self, folder: AsyncFolderResource) -> None:
        self._folder = folder

        self.create = async_to_raw_response_wrapper(
            folder.create,
        )
        self.delete = async_to_raw_response_wrapper(
            folder.delete,
        )


class FolderResourceWithStreamingResponse:
    def __init__(self, folder: FolderResource) -> None:
        self._folder = folder

        self.create = to_streamed_response_wrapper(
            folder.create,
        )
        self.delete = to_streamed_response_wrapper(
            folder.delete,
        )


class AsyncFolderResourceWithStreamingResponse:
    def __init__(self, folder: AsyncFolderResource) -> None:
        self._folder = folder

        self.create = async_to_streamed_response_wrapper(
            folder.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            folder.delete,
        )
