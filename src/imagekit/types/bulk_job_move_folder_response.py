# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BulkJobMoveFolderResponse"]


class BulkJobMoveFolderResponse(BaseModel):
    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)
    """Unique identifier of the bulk job.

    This can be used to check the status of the bulk job.
    """
