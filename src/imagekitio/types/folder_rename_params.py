# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FolderRenameParams"]


class FolderRenameParams(TypedDict, total=False):
    folder_path: Required[Annotated[str, PropertyInfo(alias="folderPath")]]
    """The full path to the folder you want to rename."""

    new_folder_name: Required[Annotated[str, PropertyInfo(alias="newFolderName")]]
    """The new name for the folder.

    All characters except alphabets and numbers (inclusive of unicode letters,
    marks, and numerals in other languages) and `-` will be replaced by an
    underscore i.e. `_`.
    """

    purge_cache: Annotated[bool, PropertyInfo(alias="purgeCache")]
    """Option to purge cache for the old nested files and their versions' URLs.

    When set to true, it will internally issue a purge cache request on CDN to
    remove the cached content of the old nested files and their versions. There will
    only be one purge request for all the nested files, which will be counted
    against your monthly purge quota.

    Note: A purge cache request will be issued against
    `https://ik.imagekit.io/old/folder/path*` (with a wildcard at the end). This
    will remove all nested files, their versions' URLs, and any transformations made
    using query parameters on these files or their versions. However, the cache for
    file transformations made using path parameters will persist. You can purge them
    using the purge API. For more details, refer to the purge API documentation.

    Default value - `false`
    """
