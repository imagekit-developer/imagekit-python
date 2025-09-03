# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BulkAddTagsParams"]


class BulkAddTagsParams(TypedDict, total=False):
    file_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="fileIds")]]
    """An array of fileIds to which you want to add tags."""

    tags: Required[SequenceNotStr[str]]
    """An array of tags that you want to add to the files."""
