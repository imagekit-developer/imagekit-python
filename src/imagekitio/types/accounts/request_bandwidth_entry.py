# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RequestBandwidthEntry"]


class RequestBandwidthEntry(BaseModel):
    bandwidth_bytes: float = FieldInfo(alias="bandwidthBytes")
    """Total bandwidth used in bytes."""

    request_count: float = FieldInfo(alias="requestCount")
    """Number of requests."""
