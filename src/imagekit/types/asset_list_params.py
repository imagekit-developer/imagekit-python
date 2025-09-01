# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["AssetListParams"]


class AssetListParams(TypedDict, total=False):
    file_type: Annotated[Literal["all", "image", "non-image"], PropertyInfo(alias="fileType")]
    """Filter results by file type.

    - `all` — include all file types
    - `image` — include only image files
    - `non-image` — include only non-image files (e.g., JS, CSS, video)
    """

    limit: int
    """The maximum number of results to return in response."""

    path: str
    """Folder path if you want to limit the search within a specific folder.

    For example, `/sales-banner/` will only search in folder sales-banner.

    Note : If your use case involves searching within a folder as well as its
    subfolders, you can use `path` parameter in `searchQuery` with appropriate
    operator. Checkout
    [Supported parameters](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#supported-parameters)
    for more information.
    """

    search_query: Annotated[str, PropertyInfo(alias="searchQuery")]
    """Query string in a Lucene-like query language e.g. `createdAt > "7d"`.

    Note : When the searchQuery parameter is present, the following query parameters
    will have no effect on the result:

    1. `tags`
    2. `type`
    3. `name`

    [Learn more](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#advanced-search-queries)
    from examples.
    """

    skip: int
    """The number of results to skip before returning results."""

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
    """
    Sort the results by one of the supported fields in ascending or descending
    order.
    """

    type: Literal["file", "file-version", "folder", "all"]
    """Filter results by asset type.

    - `file` — returns only files
    - `file-version` — returns specific file versions
    - `folder` — returns only folders
    - `all` — returns both files and folders (excludes `file-version`)
    """
