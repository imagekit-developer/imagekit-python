# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import asset_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ..types.asset_list_response import AssetListResponse

__all__ = ["AssetsResource", "AsyncAssetsResource"]


class AssetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AssetsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        file_type: Literal["all", "image", "non-image"] | Omit = omit,
        limit: int | Omit = omit,
        path: str | Omit = omit,
        search_query: str | Omit = omit,
        skip: int | Omit = omit,
        sort: Literal[
            "ASC_NAME",
            "DESC_NAME",
            "ASC_CREATED",
            "DESC_CREATED",
            "ASC_UPDATED",
            "DESC_UPDATED",
            "ASC_HEIGHT",
            "DESC_HEIGHT",
            "ASC_WIDTH",
            "DESC_WIDTH",
            "ASC_SIZE",
            "DESC_SIZE",
            "ASC_RELEVANCE",
            "DESC_RELEVANCE",
        ]
        | Omit = omit,
        type: Literal["file", "file-version", "folder", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetListResponse:
        """
        This API can list all the uploaded files and folders in your ImageKit.io media
        library. In addition, you can fine-tune your query by specifying various filters
        by generating a query string in a Lucene-like syntax and provide this generated
        string as the value of the `searchQuery`.

        Args:
          file_type: Filter results by file type.

              - `all` — include all file types
              - `image` — include only image files
              - `non-image` — include only non-image files (e.g., JS, CSS, video)

          limit: The maximum number of results to return in response.

          path: Folder path if you want to limit the search within a specific folder. For
              example, `/sales-banner/` will only search in folder sales-banner.

              Note : If your use case involves searching within a folder as well as its
              subfolders, you can use `path` parameter in `searchQuery` with appropriate
              operator. Checkout
              [Supported parameters](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#supported-parameters)
              for more information.

          search_query: Query string in a Lucene-like query language e.g. `createdAt > "7d"`.

              Note : When the searchQuery parameter is present, the following query parameters
              will have no effect on the result:

              1. `tags`
              2. `type`
              3. `name`

              [Learn more](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#advanced-search-queries)
              from examples.

          skip: The number of results to skip before returning results.

          sort: Sort the results by one of the supported fields in ascending or descending
              order.

          type: Filter results by asset type.

              - `file` — returns only files
              - `file-version` — returns specific file versions
              - `folder` — returns only folders
              - `all` — returns both files and folders (excludes `file-version`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_type": file_type,
                        "limit": limit,
                        "path": path,
                        "search_query": search_query,
                        "skip": skip,
                        "sort": sort,
                        "type": type,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=AssetListResponse,
        )


class AsyncAssetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAssetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAssetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAssetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncAssetsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        file_type: Literal["all", "image", "non-image"] | Omit = omit,
        limit: int | Omit = omit,
        path: str | Omit = omit,
        search_query: str | Omit = omit,
        skip: int | Omit = omit,
        sort: Literal[
            "ASC_NAME",
            "DESC_NAME",
            "ASC_CREATED",
            "DESC_CREATED",
            "ASC_UPDATED",
            "DESC_UPDATED",
            "ASC_HEIGHT",
            "DESC_HEIGHT",
            "ASC_WIDTH",
            "DESC_WIDTH",
            "ASC_SIZE",
            "DESC_SIZE",
            "ASC_RELEVANCE",
            "DESC_RELEVANCE",
        ]
        | Omit = omit,
        type: Literal["file", "file-version", "folder", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AssetListResponse:
        """
        This API can list all the uploaded files and folders in your ImageKit.io media
        library. In addition, you can fine-tune your query by specifying various filters
        by generating a query string in a Lucene-like syntax and provide this generated
        string as the value of the `searchQuery`.

        Args:
          file_type: Filter results by file type.

              - `all` — include all file types
              - `image` — include only image files
              - `non-image` — include only non-image files (e.g., JS, CSS, video)

          limit: The maximum number of results to return in response.

          path: Folder path if you want to limit the search within a specific folder. For
              example, `/sales-banner/` will only search in folder sales-banner.

              Note : If your use case involves searching within a folder as well as its
              subfolders, you can use `path` parameter in `searchQuery` with appropriate
              operator. Checkout
              [Supported parameters](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#supported-parameters)
              for more information.

          search_query: Query string in a Lucene-like query language e.g. `createdAt > "7d"`.

              Note : When the searchQuery parameter is present, the following query parameters
              will have no effect on the result:

              1. `tags`
              2. `type`
              3. `name`

              [Learn more](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#advanced-search-queries)
              from examples.

          skip: The number of results to skip before returning results.

          sort: Sort the results by one of the supported fields in ascending or descending
              order.

          type: Filter results by asset type.

              - `file` — returns only files
              - `file-version` — returns specific file versions
              - `folder` — returns only folders
              - `all` — returns both files and folders (excludes `file-version`)

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "file_type": file_type,
                        "limit": limit,
                        "path": path,
                        "search_query": search_query,
                        "skip": skip,
                        "sort": sort,
                        "type": type,
                    },
                    asset_list_params.AssetListParams,
                ),
            ),
            cast_to=AssetListResponse,
        )


class AssetsResourceWithRawResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.list = to_raw_response_wrapper(
            assets.list,
        )


class AsyncAssetsResourceWithRawResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.list = async_to_raw_response_wrapper(
            assets.list,
        )


class AssetsResourceWithStreamingResponse:
    def __init__(self, assets: AssetsResource) -> None:
        self._assets = assets

        self.list = to_streamed_response_wrapper(
            assets.list,
        )


class AsyncAssetsResourceWithStreamingResponse:
    def __init__(self, assets: AsyncAssetsResource) -> None:
        self._assets = assets

        self.list = async_to_streamed_response_wrapper(
            assets.list,
        )
