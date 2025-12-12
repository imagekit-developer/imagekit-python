# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "VideoTransformationAcceptedEvent",
    "VideoTransformationAcceptedEventData",
    "VideoTransformationAcceptedEventDataAsset",
    "VideoTransformationAcceptedEventDataTransformation",
    "VideoTransformationAcceptedEventDataTransformationOptions",
    "VideoTransformationAcceptedEventRequest",
]


class VideoTransformationAcceptedEventDataAsset(BaseModel):
    """Information about the source video asset being transformed."""

    url: str
    """URL to download or access the source video file."""


class VideoTransformationAcceptedEventDataTransformationOptions(BaseModel):
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


class VideoTransformationAcceptedEventDataTransformation(BaseModel):
    """Base information about a video transformation request."""

    type: Literal["video-transformation", "gif-to-video", "video-thumbnail"]
    """Type of video transformation:

    - `video-transformation`: Standard video processing (resize, format conversion,
      etc.)
    - `gif-to-video`: Convert animated GIF to video format
    - `video-thumbnail`: Generate thumbnail image from video
    """

    options: Optional[VideoTransformationAcceptedEventDataTransformationOptions] = None
    """Configuration options for video transformations."""


class VideoTransformationAcceptedEventData(BaseModel):
    asset: VideoTransformationAcceptedEventDataAsset
    """Information about the source video asset being transformed."""

    transformation: VideoTransformationAcceptedEventDataTransformation
    """Base information about a video transformation request."""


class VideoTransformationAcceptedEventRequest(BaseModel):
    """Information about the original request that triggered the video transformation."""

    url: str
    """Full URL of the transformation request that was submitted."""

    x_request_id: str
    """Unique identifier for the originating transformation request."""

    user_agent: Optional[str] = None
    """User-Agent header from the original request that triggered the transformation."""


class VideoTransformationAcceptedEvent(BaseWebhookEvent):
    """Triggered when a new video transformation request is accepted for processing.

    This event confirms that ImageKit has received and queued your transformation request. Use this for debugging and tracking transformation lifecycle.
    """

    created_at: datetime
    """Timestamp when the event was created in ISO8601 format."""

    data: VideoTransformationAcceptedEventData

    request: VideoTransformationAcceptedEventRequest
    """Information about the original request that triggered the video transformation."""

    type: Literal["video.transformation.accepted"]  # type: ignore
