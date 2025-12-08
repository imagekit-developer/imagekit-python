# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["UsageGetResponse"]


class UsageGetResponse(BaseModel):
    bandwidth_bytes: Optional[int] = FieldInfo(alias="bandwidthBytes", default=None)
    """Amount of bandwidth used in bytes."""

    extension_units_count: Optional[int] = FieldInfo(alias="extensionUnitsCount", default=None)
    """Number of extension units used."""

    media_library_storage_bytes: Optional[int] = FieldInfo(alias="mediaLibraryStorageBytes", default=None)
    """Storage used by media library in bytes."""

    original_cache_storage_bytes: Optional[int] = FieldInfo(alias="originalCacheStorageBytes", default=None)
    """Storage used by the original cache in bytes."""

    video_processing_units_count: Optional[int] = FieldInfo(alias="videoProcessingUnitsCount", default=None)
    """Number of video processing units used."""
