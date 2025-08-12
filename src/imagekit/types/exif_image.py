# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["ExifImage"]


class ExifImage(BaseModel):
    exif_offset: Optional[int] = FieldInfo(alias="ExifOffset", default=None)

    gps_info: Optional[int] = FieldInfo(alias="GPSInfo", default=None)

    make: Optional[str] = FieldInfo(alias="Make", default=None)

    model: Optional[str] = FieldInfo(alias="Model", default=None)

    modify_date: Optional[str] = FieldInfo(alias="ModifyDate", default=None)

    orientation: Optional[int] = FieldInfo(alias="Orientation", default=None)

    resolution_unit: Optional[int] = FieldInfo(alias="ResolutionUnit", default=None)

    software: Optional[str] = FieldInfo(alias="Software", default=None)

    x_resolution: Optional[int] = FieldInfo(alias="XResolution", default=None)

    y_cb_cr_positioning: Optional[int] = FieldInfo(alias="YCbCrPositioning", default=None)

    y_resolution: Optional[int] = FieldInfo(alias="YResolution", default=None)
