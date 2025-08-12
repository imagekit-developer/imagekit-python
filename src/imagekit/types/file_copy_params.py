# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileCopyParams"]


class FileCopyParams(TypedDict, total=False):
    destination_path: Required[Annotated[str, PropertyInfo(alias="destinationPath")]]
    """Full path to the folder you want to copy the above file into."""

    source_file_path: Required[Annotated[str, PropertyInfo(alias="sourceFilePath")]]
    """The full path of the file you want to copy."""

    include_file_versions: Annotated[bool, PropertyInfo(alias="includeFileVersions")]
    """Option to copy all versions of a file.

    By default, only the current version of the file is copied. When set to true,
    all versions of the file will be copied. Default value - `false`.
    """
