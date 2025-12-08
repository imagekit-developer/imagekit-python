# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FolderDeleteParams"]


class FolderDeleteParams(TypedDict, total=False):
    folder_path: Required[Annotated[str, PropertyInfo(alias="folderPath")]]
    """Full path to the folder you want to delete. For example `/folder/to/delete/`."""
