# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileMoveParams"]


class FileMoveParams(TypedDict, total=False):
    destination_path: Required[Annotated[str, PropertyInfo(alias="destinationPath")]]
    """Full path to the folder you want to move the above file into."""

    source_file_path: Required[Annotated[str, PropertyInfo(alias="sourceFilePath")]]
    """The full path of the file you want to move."""
