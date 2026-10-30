# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContractUnits"]


class ContractUnits(BaseModel):
    bandwidth_bytes: int = FieldInfo(alias="bandwidthBytes")
    """Bandwidth in bytes."""

    extension_units_count: int = FieldInfo(alias="extensionUnitsCount")
    """Number of extension units."""

    purge_cache_requests: int = FieldInfo(alias="purgeCacheRequests")
    """Number of purge cache requests."""

    video_processing_units_count: int = FieldInfo(alias="videoProcessingUnitsCount")
    """Number of video processing units."""
