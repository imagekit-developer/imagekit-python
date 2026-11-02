# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TagListParams"]


class TagListParams(TypedDict, total=False):
    cursor: str
    """The `nextCursor` value from the previous response, to fetch the next page.

    A cursor is bound to the `tagSource`, `fileType`, `sort`, `search` and `prefix`
    it was issued with; sending it with different values returns a 400.
    """

    file_type: Annotated[Literal["image", "video", "static", "all"], PropertyInfo(alias="fileType")]
    """Filter tags by the type of asset they are applied to.

    - `image` — tags in use on images
    - `video` — tags in use on videos
    - `static` — tags in use on any other file, such as documents, scripts and
      stylesheets
    - `all` — tags in use on any asset
    """

    limit: int
    """The maximum number of tags to return in response."""

    prefix: str
    """Only return tags that begin with this value. Matching is case-insensitive."""

    search: str
    """Only return tags that contain this text.

    Every word in the value must appear in the tag and the last word may be
    incomplete, which suits search-as-you-type. Matching is case-insensitive.
    """

    sort: Literal["ASC_NAME", "DESC_NAME", "ASC_LAST_USED", "DESC_LAST_USED"]
    """Sort the results.

    - `ASC_NAME` / `DESC_NAME` — by `name`
    - `ASC_LAST_USED` / `DESC_LAST_USED` — by `lastUsedAt` within the requested
      `tagSource` and `fileType`, ties broken by `name`
    """

    tag_source: Annotated[Literal["user", "ai", "all"], PropertyInfo(alias="tagSource")]
    """Filter tags by who added them.

    - `user` — tags added by users through the dashboard or the API
    - `ai` — tags added by AI auto-tagging extensions
    - `all` — both
    """
