# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FolderRenameResponse"]


class FolderRenameResponse(BaseModel):
    """Job submitted successfully. A `jobId` will be returned."""

    job_id: str = FieldInfo(alias="jobId")
    """Unique identifier of the bulk job.

    This can be used to check the status of the bulk job.
    """
