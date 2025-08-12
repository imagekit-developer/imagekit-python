# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileRemoveAITagsParams"]


class FileRemoveAITagsParams(TypedDict, total=False):
    ai_tags: Required[Annotated[List[str], PropertyInfo(alias="AITags")]]
    """An array of AITags that you want to remove from the files."""

    file_ids: Required[Annotated[List[str], PropertyInfo(alias="fileIds")]]
    """An array of fileIds from which you want to remove AITags."""
