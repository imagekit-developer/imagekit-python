# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FolderMoveParams"]


class FolderMoveParams(TypedDict, total=False):
    destination_path: Required[Annotated[str, PropertyInfo(alias="destinationPath")]]
    """
    Full path to the destination folder where you want to move the source folder
    into.
    """

    source_folder_path: Required[Annotated[str, PropertyInfo(alias="sourceFolderPath")]]
    """The full path to the source folder you want to move."""
