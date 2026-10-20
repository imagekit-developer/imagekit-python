# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "VideoTransformationReadyEvent",
    "VideoTransformationReadyEventData",
    "VideoTransformationReadyEventDataAsset",
    "VideoTransformationReadyEventDataTransformation",
    "VideoTransformationReadyEventDataTransformationOptions",
    "VideoTransformationReadyEventDataTransformationOutput",
    "VideoTransformationReadyEventDataTransformationOutputVideoMetadata",
    "VideoTransformationReadyEventRequest",
    "VideoTransformationReadyEventTimings",
]


class VideoTransformationReadyEventDataAsset(BaseModel):
    """Information about the source video asset being transformed."""

    url: str
    """URL to download or access the source video file."""


class VideoTransformationReadyEventDataTransformationOptions(BaseModel):
    """Configuration options for video transformations."""

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


class VideoTransformationReadyEventDataTransformationOutputVideoMetadata(BaseModel):
    """Metadata of the output video file."""

    bitrate: int
    """Bitrate of the output video in bits per second."""

    duration: float
    """Duration of the output video in seconds."""

    height: int
    """Height of the output video in pixels."""

    width: int
    """Width of the output video in pixels."""


class VideoTransformationReadyEventDataTransformationOutput(BaseModel):
    """Information about the transformed output video."""

    url: str
    """URL to access the transformed video."""

    video_metadata: Optional[VideoTransformationReadyEventDataTransformationOutputVideoMetadata] = None
    """Metadata of the output video file."""


class VideoTransformationReadyEventDataTransformation(BaseModel):
    type: Literal["video-transformation", "gif-to-video", "video-thumbnail"]
    """Type of video transformation:

    - `video-transformation`: Standard video processing (resize, format conversion,
      etc.)
    - `gif-to-video`: Convert animated GIF to video format
    - `video-thumbnail`: Generate thumbnail image from video
    """

    options: Optional[VideoTransformationReadyEventDataTransformationOptions] = None
    """Configuration options for video transformations."""

    output: Optional[VideoTransformationReadyEventDataTransformationOutput] = None
    """Information about the transformed output video."""


class VideoTransformationReadyEventData(BaseModel):
    asset: VideoTransformationReadyEventDataAsset
    """Information about the source video asset being transformed."""

    transformation: VideoTransformationReadyEventDataTransformation


class VideoTransformationReadyEventRequest(BaseModel):
    """Information about the original request that triggered the video transformation."""

    url: str
    """Full URL of the transformation request that was submitted."""

    x_request_id: str
    """Unique identifier for the originating transformation request."""

    user_agent: Optional[str] = None
    """User-Agent header from the original request that triggered the transformation."""


class VideoTransformationReadyEventTimings(BaseModel):
    """Performance metrics for the transformation process."""

    download_duration: Optional[int] = None
    """
    Time spent downloading the source video from your origin or media library, in
    milliseconds.
    """

    encoding_duration: Optional[int] = None
    """Time spent encoding the video, in milliseconds."""


class VideoTransformationReadyEvent(BaseWebhookEvent):
    """
    Triggered when video encoding is finished and the transformed resource is ready to be served. This is the key event to listen for - update your database or CMS flags when you receive this so your application can start showing the transformed video to users.
    """

    created_at: datetime
    """Timestamp when the event was created in ISO8601 format."""

    data: VideoTransformationReadyEventData

    request: VideoTransformationReadyEventRequest
    """Information about the original request that triggered the video transformation."""

    type: Literal["video.transformation.ready"]  # type: ignore

    timings: Optional[VideoTransformationReadyEventTimings] = None
    """Performance metrics for the transformation process."""
