# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["BulkRemoveAITagsParams"]


class BulkRemoveAITagsParams(TypedDict, total=False):
    ai_tags: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="AITags")]]
    """An array of AITags that you want to remove from the files."""

    file_ids: Required[Annotated[SequenceNotStr[str], PropertyInfo(alias="fileIds")]]
    """An array of fileIds from which you want to remove AITags."""
