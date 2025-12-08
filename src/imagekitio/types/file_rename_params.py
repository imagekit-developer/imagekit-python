# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileRenameParams"]


class FileRenameParams(TypedDict, total=False):
    file_path: Required[Annotated[str, PropertyInfo(alias="filePath")]]
    """The full path of the file you want to rename."""

    new_file_name: Required[Annotated[str, PropertyInfo(alias="newFileName")]]
    """The new name of the file. A filename can contain:

    Alphanumeric Characters: `a-z`, `A-Z`, `0-9` (including Unicode letters, marks,
    and numerals in other languages). Special Characters: `.`, `_`, and `-`.

    Any other character, including space, will be replaced by `_`.
    """

    purge_cache: Annotated[bool, PropertyInfo(alias="purgeCache")]
    """Option to purge cache for the old file and its versions' URLs.

    When set to true, it will internally issue a purge cache request on CDN to
    remove cached content of old file and its versions. This purge request is
    counted against your monthly purge quota.

    Note: If the old file were accessible at
    `https://ik.imagekit.io/demo/old-filename.jpg`, a purge cache request would be
    issued against `https://ik.imagekit.io/demo/old-filename.jpg*` (with a wildcard
    at the end). It will remove the file and its versions' URLs and any
    transformations made using query parameters on this file or its versions.
    However, the cache for file transformations made using path parameters will
    persist. You can purge them using the purge API. For more details, refer to the
    purge API documentation.

    Default value - `false`
    """
