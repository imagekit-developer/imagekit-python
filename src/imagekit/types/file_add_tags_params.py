# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileAddTagsParams"]


class FileAddTagsParams(TypedDict, total=False):
    file_ids: Required[Annotated[List[str], PropertyInfo(alias="fileIds")]]
    """An array of fileIds to which you want to add tags."""

    tags: Required[List[str]]
    """An array of tags that you want to add to the files."""
