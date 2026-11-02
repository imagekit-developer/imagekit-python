# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..types import tag_list_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..types.tag import Tag
from ..pagination import SyncTagCursor, AsyncTagCursor
from .._base_client import AsyncPaginator, make_request_options

__all__ = ["TagsResource", "AsyncTagsResource"]


class TagsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> TagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return TagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> TagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return TagsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        file_type: Literal["image", "video", "static", "all"] | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["ASC_NAME", "DESC_NAME", "ASC_LAST_USED", "DESC_LAST_USED"] | Omit = omit,
        tag_source: Literal["user", "ai", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SyncTagCursor[Tag]:
        """
        This API lists the distinct tags in use across your media library, with the
        number of assets each tag is applied to and when it was last used. Tags are
        matched case-insensitively, so `Summer` and `summer` are one entry: `name` is
        the lowercased form and `label` is the spelling that was used most recently.

        Use `tagSource` and `fileType` to list only the tags in use on matching assets.
        `lastUsedAt` and the `ASC_LAST_USED` / `DESC_LAST_USED` sorts follow those
        filters, while `assetCount` always counts every asset carrying the tag. Use
        `search` or `prefix` to narrow the listing and `cursor` to page through it.

        Tag counts are updated asynchronously. Changes to a file's tags usually appear
        in this list within about a minute, but can take longer during heavy tagging
        activity, so a tag you just added or removed may not be reflected immediately.

        Args:
          cursor: The `nextCursor` value from the previous response, to fetch the next page. A
              cursor is bound to the `tagSource`, `fileType`, `sort`, `search` and `prefix` it
              was issued with; sending it with different values returns a 400.

          file_type: Filter tags by the type of asset they are applied to.

              - `image` — tags in use on images
              - `video` — tags in use on videos
              - `static` — tags in use on any other file, such as documents, scripts and
                stylesheets
              - `all` — tags in use on any asset

          limit: The maximum number of tags to return in response.

          prefix: Only return tags that begin with this value. Matching is case-insensitive.

          search: Only return tags that contain this text. Every word in the value must appear in
              the tag and the last word may be incomplete, which suits search-as-you-type.
              Matching is case-insensitive.

          sort: Sort the results.

              - `ASC_NAME` / `DESC_NAME` — by `name`
              - `ASC_LAST_USED` / `DESC_LAST_USED` — by `lastUsedAt` within the requested
                `tagSource` and `fileType`, ties broken by `name`

          tag_source: Filter tags by who added them.

              - `user` — tags added by users through the dashboard or the API
              - `ai` — tags added by AI auto-tagging extensions
              - `all` — both

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tags",
            page=SyncTagCursor[Tag],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "file_type": file_type,
                        "limit": limit,
                        "prefix": prefix,
                        "search": search,
                        "sort": sort,
                        "tag_source": tag_source,
                    },
                    tag_list_params.TagListParams,
                ),
            ),
            model=Tag,
        )


class AsyncTagsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncTagsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncTagsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncTagsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncTagsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        cursor: str | Omit = omit,
        file_type: Literal["image", "video", "static", "all"] | Omit = omit,
        limit: int | Omit = omit,
        prefix: str | Omit = omit,
        search: str | Omit = omit,
        sort: Literal["ASC_NAME", "DESC_NAME", "ASC_LAST_USED", "DESC_LAST_USED"] | Omit = omit,
        tag_source: Literal["user", "ai", "all"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncPaginator[Tag, AsyncTagCursor[Tag]]:
        """
        This API lists the distinct tags in use across your media library, with the
        number of assets each tag is applied to and when it was last used. Tags are
        matched case-insensitively, so `Summer` and `summer` are one entry: `name` is
        the lowercased form and `label` is the spelling that was used most recently.

        Use `tagSource` and `fileType` to list only the tags in use on matching assets.
        `lastUsedAt` and the `ASC_LAST_USED` / `DESC_LAST_USED` sorts follow those
        filters, while `assetCount` always counts every asset carrying the tag. Use
        `search` or `prefix` to narrow the listing and `cursor` to page through it.

        Tag counts are updated asynchronously. Changes to a file's tags usually appear
        in this list within about a minute, but can take longer during heavy tagging
        activity, so a tag you just added or removed may not be reflected immediately.

        Args:
          cursor: The `nextCursor` value from the previous response, to fetch the next page. A
              cursor is bound to the `tagSource`, `fileType`, `sort`, `search` and `prefix` it
              was issued with; sending it with different values returns a 400.

          file_type: Filter tags by the type of asset they are applied to.

              - `image` — tags in use on images
              - `video` — tags in use on videos
              - `static` — tags in use on any other file, such as documents, scripts and
                stylesheets
              - `all` — tags in use on any asset

          limit: The maximum number of tags to return in response.

          prefix: Only return tags that begin with this value. Matching is case-insensitive.

          search: Only return tags that contain this text. Every word in the value must appear in
              the tag and the last word may be incomplete, which suits search-as-you-type.
              Matching is case-insensitive.

          sort: Sort the results.

              - `ASC_NAME` / `DESC_NAME` — by `name`
              - `ASC_LAST_USED` / `DESC_LAST_USED` — by `lastUsedAt` within the requested
                `tagSource` and `fileType`, ties broken by `name`

          tag_source: Filter tags by who added them.

              - `user` — tags added by users through the dashboard or the API
              - `ai` — tags added by AI auto-tagging extensions
              - `all` — both

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get_api_list(
            "/v1/tags",
            page=AsyncTagCursor[Tag],
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "cursor": cursor,
                        "file_type": file_type,
                        "limit": limit,
                        "prefix": prefix,
                        "search": search,
                        "sort": sort,
                        "tag_source": tag_source,
                    },
                    tag_list_params.TagListParams,
                ),
            ),
            model=Tag,
        )


class TagsResourceWithRawResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.list = to_raw_response_wrapper(
            tags.list,
        )


class AsyncTagsResourceWithRawResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.list = async_to_raw_response_wrapper(
            tags.list,
        )


class TagsResourceWithStreamingResponse:
    def __init__(self, tags: TagsResource) -> None:
        self._tags = tags

        self.list = to_streamed_response_wrapper(
            tags.list,
        )


class AsyncTagsResourceWithStreamingResponse:
    def __init__(self, tags: AsyncTagsResource) -> None:
        self._tags = tags

        self.list = async_to_streamed_response_wrapper(
            tags.list,
        )
