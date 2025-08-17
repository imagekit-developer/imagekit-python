# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Thumbnail"]


class Thumbnail(BaseModel):
    compression: Optional[int] = FieldInfo(alias="Compression", default=None)

    resolution_unit: Optional[int] = FieldInfo(alias="ResolutionUnit", default=None)

    thumbnail_length: Optional[int] = FieldInfo(alias="ThumbnailLength", default=None)

    thumbnail_offset: Optional[int] = FieldInfo(alias="ThumbnailOffset", default=None)

    x_resolution: Optional[int] = FieldInfo(alias="XResolution", default=None)

    y_resolution: Optional[int] = FieldInfo(alias="YResolution", default=None)
