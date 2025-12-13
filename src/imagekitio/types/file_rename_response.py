# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FileRenameResponse"]


class FileRenameResponse(BaseModel):
    purge_request_id: Optional[str] = FieldInfo(alias="purgeRequestId", default=None)
    """Unique identifier of the purge request.

    This can be used to check the status of the purge request.
    """
