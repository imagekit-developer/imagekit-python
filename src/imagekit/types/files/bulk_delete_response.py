# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["BulkDeleteResponse"]


class BulkDeleteResponse(BaseModel):
    successfully_deleted_file_ids: Optional[List[str]] = FieldInfo(alias="successfullyDeletedFileIds", default=None)
    """An array of fileIds that were successfully deleted."""
