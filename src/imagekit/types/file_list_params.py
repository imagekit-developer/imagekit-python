# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileListParams"]


class FileListParams(TypedDict, total=False):
    file_type: Annotated[str, PropertyInfo(alias="fileType")]
    """Type of files to include in the result set. Accepts three values:

    `all` - include all types of files in the result set. `image` - only search in
    image type files. `non-image` - only search in files that are not images, e.g.,
    JS or CSS or video files.

    Default value - `all`
    """

    limit: str
    """The maximum number of results to return in response:

    Minimum value - 1

    Maximum value - 1000

    Default value - 1000
    """

    path: str
    """Folder path if you want to limit the search within a specific folder.

    For example, `/sales-banner/` will only search in folder sales-banner.
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

    skip: str
    """The number of results to skip before returning results:

    Minimum value - 0

    Default value - 0
    """

    sort: str
    """You can sort based on the following fields:

    1. name - `ASC_NAME` or `DESC_NAME`
    2. createdAt - `ASC_CREATED` or `DESC_CREATED`
    3. updatedAt - `ASC_UPDATED` or `DESC_UPDATED`
    4. height - `ASC_HEIGHT` or `DESC_HEIGHT`
    5. width - `ASC_WIDTH` or `DESC_WIDTH`
    6. size - `ASC_SIZE` or `DESC_SIZE`

    Default value - `ASC_CREATED`
    """

    type: Literal["file", "file-version", "folder", "all"]
    """Limit search to one of `file`, `file-version`, or `folder`.

    Pass `all` to include `files` and `folders` in search results (`file-version`
    will not be included in this case).

    Default value - `file`
    """
