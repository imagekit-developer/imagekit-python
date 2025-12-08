# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["JobGetResponse"]


class JobGetResponse(BaseModel):
    job_id: Optional[str] = FieldInfo(alias="jobId", default=None)
    """Unique identifier of the bulk job."""

    purge_request_id: Optional[str] = FieldInfo(alias="purgeRequestId", default=None)
    """Unique identifier of the purge request.

    This will be present only if `purgeCache` is set to `true` in the rename folder
    API request.
    """

    status: Optional[Literal["Pending", "Completed"]] = None
    """Status of the bulk job."""

    type: Optional[Literal["COPY_FOLDER", "MOVE_FOLDER", "RENAME_FOLDER"]] = None
    """Type of the bulk job."""
