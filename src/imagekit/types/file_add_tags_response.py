# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileAddTagsResponse"]


class FileAddTagsResponse(BaseModel):
    successfully_updated_file_ids: Optional[List[str]] = FieldInfo(alias="successfullyUpdatedFileIds", default=None)
    """An array of fileIds that in which tags were successfully added."""
