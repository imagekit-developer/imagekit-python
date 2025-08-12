# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional

from pydantic import Field as FieldInfo

from ..gps import Gps
from ..._models import BaseModel
from ..thumbnail import Thumbnail
from ..exif_image import ExifImage
from ..exif_details import ExifDetails
from ..interoperability import Interoperability

__all__ = ["MetadataRetrieveResponse", "Exif"]


class Exif(BaseModel):
    exif: Optional[ExifDetails] = None
    """Object containing Exif details."""

    gps: Optional[Gps] = None
    """Object containing GPS information."""

    image: Optional[ExifImage] = None
    """Object containing EXIF image information."""

    interoperability: Optional[Interoperability] = None
    """JSON object."""

    makernote: Optional[Dict[str, object]] = None

    thumbnail: Optional[Thumbnail] = None
    """Object containing Thumbnail information."""


class MetadataRetrieveResponse(BaseModel):
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
