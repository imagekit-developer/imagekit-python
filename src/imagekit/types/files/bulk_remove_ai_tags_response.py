# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BulkRemoveAITagsResponse"]


class BulkRemoveAITagsResponse(BaseModel):
    successfully_updated_file_ids: Optional[List[str]] = FieldInfo(alias="successfullyUpdatedFileIds", default=None)
    """An array of fileIds that in which AITags were successfully removed."""
