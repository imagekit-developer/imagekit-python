# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ExifDetails"]


class ExifDetails(BaseModel):
    aperture_value: Optional[float] = FieldInfo(alias="ApertureValue", default=None)

    color_space: Optional[int] = FieldInfo(alias="ColorSpace", default=None)

    create_date: Optional[str] = FieldInfo(alias="CreateDate", default=None)

    custom_rendered: Optional[int] = FieldInfo(alias="CustomRendered", default=None)

    date_time_original: Optional[str] = FieldInfo(alias="DateTimeOriginal", default=None)

    exif_image_height: Optional[int] = FieldInfo(alias="ExifImageHeight", default=None)

    exif_image_width: Optional[int] = FieldInfo(alias="ExifImageWidth", default=None)

    exif_version: Optional[str] = FieldInfo(alias="ExifVersion", default=None)

    exposure_compensation: Optional[float] = FieldInfo(alias="ExposureCompensation", default=None)

    exposure_mode: Optional[int] = FieldInfo(alias="ExposureMode", default=None)

    exposure_program: Optional[int] = FieldInfo(alias="ExposureProgram", default=None)

    exposure_time: Optional[float] = FieldInfo(alias="ExposureTime", default=None)

    flash: Optional[int] = FieldInfo(alias="Flash", default=None)

    flashpix_version: Optional[str] = FieldInfo(alias="FlashpixVersion", default=None)

    f_number: Optional[float] = FieldInfo(alias="FNumber", default=None)

    focal_length: Optional[int] = FieldInfo(alias="FocalLength", default=None)

    focal_plane_resolution_unit: Optional[int] = FieldInfo(alias="FocalPlaneResolutionUnit", default=None)

    focal_plane_x_resolution: Optional[float] = FieldInfo(alias="FocalPlaneXResolution", default=None)

    focal_plane_y_resolution: Optional[float] = FieldInfo(alias="FocalPlaneYResolution", default=None)

    interop_offset: Optional[int] = FieldInfo(alias="InteropOffset", default=None)

    iso: Optional[int] = FieldInfo(alias="ISO", default=None)

    metering_mode: Optional[int] = FieldInfo(alias="MeteringMode", default=None)

    scene_capture_type: Optional[int] = FieldInfo(alias="SceneCaptureType", default=None)

    shutter_speed_value: Optional[float] = FieldInfo(alias="ShutterSpeedValue", default=None)

    sub_sec_time: Optional[str] = FieldInfo(alias="SubSecTime", default=None)

    white_balance: Optional[int] = FieldInfo(alias="WhiteBalance", default=None)
