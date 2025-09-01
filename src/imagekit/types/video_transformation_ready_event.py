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
    """URL to download or access the source video file."""


class DataTransformationOptions(BaseModel):
    audio_codec: Optional[Literal["aac", "opus"]] = None
    """Audio codec used for encoding (aac or opus)."""

    auto_rotate: Optional[bool] = None
    """Whether to automatically rotate the video based on metadata."""

    format: Optional[Literal["mp4", "webm", "jpg", "png", "webp"]] = None
    """Output format for the transformed video or thumbnail."""

    quality: Optional[int] = None
    """Quality setting for the output video."""

    stream_protocol: Optional[Literal["HLS", "DASH"]] = None
    """Streaming protocol for adaptive bitrate streaming."""

    variants: Optional[List[str]] = None
    """Array of quality representations for adaptive bitrate streaming."""

    video_codec: Optional[Literal["h264", "vp9", "av1"]] = None
    """Video codec used for encoding (h264, vp9, or av1)."""


class DataTransformationOutputVideoMetadata(BaseModel):
    bitrate: int
    """Bitrate of the output video in bits per second."""

    duration: float
    """Duration of the output video in seconds."""

    height: int
    """Height of the output video in pixels."""

    width: int
    """Width of the output video in pixels."""


class DataTransformationOutput(BaseModel):
    url: str
    """URL to access the transformed video."""

    video_metadata: Optional[DataTransformationOutputVideoMetadata] = None
    """Metadata of the output video file."""


class DataTransformation(BaseModel):
    type: Literal["video-transformation", "gif-to-video", "video-thumbnail"]
    """Type of video transformation:

    - `video-transformation`: Standard video processing (resize, format conversion,
      etc.)
    - `gif-to-video`: Convert animated GIF to video format
    - `video-thumbnail`: Generate thumbnail image from video
    """

    options: Optional[DataTransformationOptions] = None
    """Configuration options for video transformations."""

    output: Optional[DataTransformationOutput] = None
    """Information about the transformed output video."""


class Data(BaseModel):
    asset: DataAsset
    """Information about the source video asset being transformed."""

    transformation: DataTransformation


class Request(BaseModel):
    url: str
    """Full URL of the transformation request that was submitted."""

    x_request_id: str
    """Unique identifier for the originating transformation request."""

    user_agent: Optional[str] = None
    """User-Agent header from the original request that triggered the transformation."""


class Timings(BaseModel):
    download_duration: Optional[int] = None
    """
    Time spent downloading the source video from your origin or media library, in
    milliseconds.
    """

    encoding_duration: Optional[int] = None
    """Time spent encoding the video, in milliseconds."""


class VideoTransformationReadyEvent(BaseModel):
    id: str
    """Unique identifier for the event."""

    created_at: datetime
    """Timestamp when the event was created in ISO8601 format."""

    data: Data

    request: Request
    """Information about the original request that triggered the video transformation."""

    type: Literal["video.transformation.ready"]

    timings: Optional[Timings] = None
    """Performance metrics for the transformation process."""
