# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["InvalidationGetResponse"]


class InvalidationGetResponse(BaseModel):
    status: Optional[Literal["Pending", "Completed"]] = None
    """Status of the purge request."""
