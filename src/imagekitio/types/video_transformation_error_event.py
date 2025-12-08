# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "VideoTransformationErrorEvent",
    "VideoTransformationErrorEventData",
    "VideoTransformationErrorEventDataAsset",
    "VideoTransformationErrorEventDataTransformation",
    "VideoTransformationErrorEventDataTransformationError",
    "VideoTransformationErrorEventDataTransformationOptions",
    "VideoTransformationErrorEventRequest",
]


class VideoTransformationErrorEventDataAsset(BaseModel):
    """Information about the source video asset being transformed."""

    url: str
    """URL to download or access the source video file."""


class VideoTransformationErrorEventDataTransformationError(BaseModel):
    """Details about the transformation error."""

    reason: Literal["encoding_failed", "download_failed", "internal_server_error"]
    """Specific reason for the transformation failure:

    - `encoding_failed`: Error during video encoding process
    - `download_failed`: Could not download source video
    - `internal_server_error`: Unexpected server error
    """


class VideoTransformationErrorEventDataTransformationOptions(BaseModel):
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


class VideoTransformationErrorEventDataTransformation(BaseModel):
    type: Literal["video-transformation", "gif-to-video", "video-thumbnail"]
    """Type of video transformation:

    - `video-transformation`: Standard video processing (resize, format conversion,
      etc.)
    - `gif-to-video`: Convert animated GIF to video format
    - `video-thumbnail`: Generate thumbnail image from video
    """

    error: Optional[VideoTransformationErrorEventDataTransformationError] = None
    """Details about the transformation error."""

    options: Optional[VideoTransformationErrorEventDataTransformationOptions] = None
    """Configuration options for video transformations."""


class VideoTransformationErrorEventData(BaseModel):
    asset: VideoTransformationErrorEventDataAsset
    """Information about the source video asset being transformed."""

    transformation: VideoTransformationErrorEventDataTransformation


class VideoTransformationErrorEventRequest(BaseModel):
    """Information about the original request that triggered the video transformation."""

    url: str
    """Full URL of the transformation request that was submitted."""

    x_request_id: str
    """Unique identifier for the originating transformation request."""

    user_agent: Optional[str] = None
    """User-Agent header from the original request that triggered the transformation."""


class VideoTransformationErrorEvent(BaseWebhookEvent):
    """Triggered when an error occurs during video encoding.

    Listen to this webhook to log error reasons and debug issues. Check your origin and URL endpoint settings if the reason is related to download failure. For other errors, contact ImageKit support.
    """

    created_at: datetime
    """Timestamp when the event was created in ISO8601 format."""

    data: VideoTransformationErrorEventData

    request: VideoTransformationErrorEventRequest
    """Information about the original request that triggered the video transformation."""

    type: Literal["video.transformation.error"]  # type: ignore
