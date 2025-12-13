# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FolderCopyParams"]


class FolderCopyParams(TypedDict, total=False):
    destination_path: Required[Annotated[str, PropertyInfo(alias="destinationPath")]]
    """
    Full path to the destination folder where you want to copy the source folder
    into.
    """

    source_folder_path: Required[Annotated[str, PropertyInfo(alias="sourceFolderPath")]]
    """The full path to the source folder you want to copy."""

    include_versions: Annotated[bool, PropertyInfo(alias="includeVersions")]
    """Option to copy all versions of files that are nested inside the selected folder.

    By default, only the current version of each file will be copied. When set to
    true, all versions of each file will be copied. Default value - `false`.
    """
