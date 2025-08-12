# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["BulkJobRetrieveStatusResponse"]


class BulkJobRetrieveStatusResponse(BaseModel):
    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)
    """Unique identifier of the bulk job."""

    status: Optional[str] = None
    """Status of the bulk job. Possible values - `Pending`, `Completed`."""

    type: Optional[str] = None
    """Type of the bulk job. Possible values - `COPY_FOLDER`, `MOVE_FOLDER`."""
