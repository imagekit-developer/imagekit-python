# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "VideoTransformationReadyEvent",
    "Data",
    "DataAsset",
    "DataTransformation",
    "DataTransformationOptions",
    "DataTransformationOutput",
    "DataTransformationOutputVideoMetadata",
    "Request",
    "Timings",
]


class DataAsset(BaseModel):
    url: str
    """Source asset URL."""


class DataTransformationOptions(BaseModel):
    audio_codec: Optional[Literal["aac", "opus"]] = None

    auto_rotate: Optional[bool] = None

    format: Optional[Literal["mp4", "webm", "jpg", "png", "webp"]] = None

    quality: Optional[int] = None

    stream_protocol: Optional[Literal["HLS", "DASH"]] = None

    variants: Optional[List[str]] = None

    video_codec: Optional[Literal["h264", "vp9"]] = None


class DataTransformationOutputVideoMetadata(BaseModel):
    bitrate: int

    duration: float

    height: int

    width: int


class DataTransformationOutput(BaseModel):
    url: str

    video_metadata: Optional[DataTransformationOutputVideoMetadata] = None


class DataTransformation(BaseModel):
    type: Literal["video-transformation", "gif-to-video", "video-thumbnail"]

    options: Optional[DataTransformationOptions] = None

    output: Optional[DataTransformationOutput] = None


class Data(BaseModel):
    asset: DataAsset

    transformation: DataTransformation


class Request(BaseModel):
    url: str
    """URL of the submitted request."""

    x_request_id: str
    """Unique ID for the originating request."""

    user_agent: Optional[str] = None
    """User-Agent header of the originating request."""


class Timings(BaseModel):
    download_duration: Optional[int] = None
    """Milliseconds spent downloading the source."""

    encoding_duration: Optional[int] = None
    """Milliseconds spent encoding."""


class VideoTransformationReadyEvent(BaseModel):
    id: str
    """Unique identifier for the event."""

    created_at: datetime

    data: Data

    request: Request

    type: Literal["video.transformation.ready"]

    timings: Optional[Timings] = None
