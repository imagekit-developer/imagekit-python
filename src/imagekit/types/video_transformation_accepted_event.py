# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = [
    "VideoTransformationAcceptedEvent",
    "Data",
    "DataAsset",
    "DataTransformation",
    "DataTransformationOptions",
    "Request",
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


class DataTransformation(BaseModel):
    type: Literal["video-transformation", "gif-to-video", "video-thumbnail"]

    options: Optional[DataTransformationOptions] = None


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


class VideoTransformationAcceptedEvent(BaseModel):
    id: str
    """Unique identifier for the event."""

    created_at: datetime

    data: Data

    request: Request

    type: Literal["video.transformation.accepted"]
