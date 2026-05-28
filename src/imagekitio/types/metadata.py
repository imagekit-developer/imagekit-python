# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Metadata", "Exif", "ExifExif", "ExifGps", "ExifImage", "ExifInteroperability", "ExifThumbnail"]


class ExifExif(BaseModel):
    """Object containing Exif details."""

    aperture_value: Optional[float] = FieldInfo(alias="ApertureValue", default=None)

    brightness_value: Optional[float] = FieldInfo(alias="BrightnessValue", default=None)

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

    focal_length: Optional[float] = FieldInfo(alias="FocalLength", default=None)

    focal_length_in35mm_format: Optional[int] = FieldInfo(alias="FocalLengthIn35mmFormat", default=None)

    focal_plane_resolution_unit: Optional[int] = FieldInfo(alias="FocalPlaneResolutionUnit", default=None)

    focal_plane_x_resolution: Optional[float] = FieldInfo(alias="FocalPlaneXResolution", default=None)

    focal_plane_y_resolution: Optional[float] = FieldInfo(alias="FocalPlaneYResolution", default=None)

    interop_offset: Optional[int] = FieldInfo(alias="InteropOffset", default=None)

    iso: Optional[int] = FieldInfo(alias="ISO", default=None)

    lens_model: Optional[str] = FieldInfo(alias="LensModel", default=None)

    light_source: Optional[int] = FieldInfo(alias="LightSource", default=None)

    max_aperture_value: Optional[float] = FieldInfo(alias="MaxApertureValue", default=None)

    metering_mode: Optional[int] = FieldInfo(alias="MeteringMode", default=None)

    scene_capture_type: Optional[int] = FieldInfo(alias="SceneCaptureType", default=None)

    scene_type: Optional[str] = FieldInfo(alias="SceneType", default=None)

    sensing_method: Optional[int] = FieldInfo(alias="SensingMethod", default=None)

    shutter_speed_value: Optional[float] = FieldInfo(alias="ShutterSpeedValue", default=None)

    sub_sec_time: Optional[str] = FieldInfo(alias="SubSecTime", default=None)

    user_comment: Optional[str] = FieldInfo(alias="UserComment", default=None)

    white_balance: Optional[int] = FieldInfo(alias="WhiteBalance", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ExifGps(BaseModel):
    """Object containing GPS information."""

    gps_altitude: Optional[float] = FieldInfo(alias="GPSAltitude", default=None)

    gps_altitude_ref: Optional[int] = FieldInfo(alias="GPSAltitudeRef", default=None)

    gps_date_stamp: Optional[str] = FieldInfo(alias="GPSDateStamp", default=None)

    gps_img_direction: Optional[float] = FieldInfo(alias="GPSImgDirection", default=None)

    gps_img_direction_ref: Optional[str] = FieldInfo(alias="GPSImgDirectionRef", default=None)

    gps_latitude: Optional[List[float]] = FieldInfo(alias="GPSLatitude", default=None)

    gps_latitude_ref: Optional[str] = FieldInfo(alias="GPSLatitudeRef", default=None)

    gps_longitude: Optional[List[float]] = FieldInfo(alias="GPSLongitude", default=None)

    gps_longitude_ref: Optional[str] = FieldInfo(alias="GPSLongitudeRef", default=None)

    gps_time_stamp: Optional[List[float]] = FieldInfo(alias="GPSTimeStamp", default=None)

    gps_version_id: Optional[List[int]] = FieldInfo(alias="GPSVersionID", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ExifImage(BaseModel):
    """Object containing EXIF image information."""

    artist: Optional[str] = FieldInfo(alias="Artist", default=None)

    copyright: Optional[str] = FieldInfo(alias="Copyright", default=None)

    exif_offset: Optional[int] = FieldInfo(alias="ExifOffset", default=None)

    gps_info: Optional[int] = FieldInfo(alias="GPSInfo", default=None)

    image_description: Optional[str] = FieldInfo(alias="ImageDescription", default=None)

    make: Optional[str] = FieldInfo(alias="Make", default=None)

    model: Optional[str] = FieldInfo(alias="Model", default=None)

    modify_date: Optional[str] = FieldInfo(alias="ModifyDate", default=None)

    orientation: Optional[int] = FieldInfo(alias="Orientation", default=None)

    resolution_unit: Optional[int] = FieldInfo(alias="ResolutionUnit", default=None)

    software: Optional[str] = FieldInfo(alias="Software", default=None)

    x_resolution: Optional[float] = FieldInfo(alias="XResolution", default=None)

    y_cb_cr_positioning: Optional[int] = FieldInfo(alias="YCbCrPositioning", default=None)

    y_resolution: Optional[float] = FieldInfo(alias="YResolution", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ExifInteroperability(BaseModel):
    """JSON object."""

    interop_index: Optional[str] = FieldInfo(alias="InteropIndex", default=None)

    interop_version: Optional[str] = FieldInfo(alias="InteropVersion", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class ExifThumbnail(BaseModel):
    """Object containing Thumbnail information."""

    compression: Optional[int] = FieldInfo(alias="Compression", default=None)

    resolution_unit: Optional[int] = FieldInfo(alias="ResolutionUnit", default=None)

    thumbnail_length: Optional[int] = FieldInfo(alias="ThumbnailLength", default=None)

    thumbnail_offset: Optional[int] = FieldInfo(alias="ThumbnailOffset", default=None)

    x_resolution: Optional[float] = FieldInfo(alias="XResolution", default=None)

    y_resolution: Optional[float] = FieldInfo(alias="YResolution", default=None)

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Exif(BaseModel):
    exif: Optional[ExifExif] = None
    """Object containing Exif details."""

    gps: Optional[ExifGps] = None
    """Object containing GPS information."""

    image: Optional[ExifImage] = None
    """Object containing EXIF image information."""

    interoperability: Optional[ExifInteroperability] = None
    """JSON object."""

    makernote: Optional[Dict[str, object]] = None

    thumbnail: Optional[ExifThumbnail] = None
    """Object containing Thumbnail information."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]


class Metadata(BaseModel):
    """JSON object containing metadata."""

    audio_codec: Optional[str] = FieldInfo(alias="audioCodec", default=None)
    """The audio codec used in the video (only for video)."""

    bit_rate: Optional[int] = FieldInfo(alias="bitRate", default=None)
    """The bit rate of the video in kbps (only for video)."""

    density: Optional[int] = None
    """The density of the image in DPI."""

    duration: Optional[int] = None
    """The duration of the video in seconds (only for video)."""

    exif: Optional[Exif] = None

    format: Optional[str] = None
    """The format of the file (e.g., 'jpg', 'mp4')."""

    has_color_profile: Optional[bool] = FieldInfo(alias="hasColorProfile", default=None)
    """Indicates if the image has a color profile."""

    has_transparency: Optional[bool] = FieldInfo(alias="hasTransparency", default=None)
    """Indicates if the image contains transparent areas."""

    height: Optional[int] = None
    """The height of the image or video in pixels."""

    p_hash: Optional[str] = FieldInfo(alias="pHash", default=None)
    """Perceptual hash of the image."""

    quality: Optional[int] = None
    """The quality indicator of the image."""

    size: Optional[int] = None
    """The file size in bytes."""

    video_codec: Optional[str] = FieldInfo(alias="videoCodec", default=None)
    """The video codec used in the video (only for video)."""

    width: Optional[int] = None
    """The width of the image or video in pixels."""

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
