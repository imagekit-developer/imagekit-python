# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "UploadPostTransformErrorEvent",
    "UploadPostTransformErrorEventData",
    "UploadPostTransformErrorEventDataTransformation",
    "UploadPostTransformErrorEventDataTransformationError",
    "UploadPostTransformErrorEventRequest",
    "UploadPostTransformErrorEventRequestTransformation",
]


class UploadPostTransformErrorEventDataTransformationError(BaseModel):
    reason: str
    """Reason for the post-transformation failure."""


class UploadPostTransformErrorEventDataTransformation(BaseModel):
    error: UploadPostTransformErrorEventDataTransformationError


class UploadPostTransformErrorEventData(BaseModel):
    file_id: str = FieldInfo(alias="fileId")
    """Unique identifier of the originally uploaded file."""

    name: str
    """Name of the file."""

    path: str
    """Path of the file."""

    transformation: UploadPostTransformErrorEventDataTransformation

    url: str
    """URL of the attempted post-transformation."""


class UploadPostTransformErrorEventRequestTransformation(BaseModel):
    type: Literal["transformation", "abs", "gif-to-video", "thumbnail"]
    """Type of the requested post-transformation."""

    protocol: Optional[Literal["hls", "dash"]] = None
    """Only applicable if transformation type is 'abs'. Streaming protocol used."""

    value: Optional[str] = None
    """Value for the requested transformation type."""


class UploadPostTransformErrorEventRequest(BaseModel):
    transformation: UploadPostTransformErrorEventRequestTransformation

    x_request_id: str
    """Unique identifier for the originating request."""


class UploadPostTransformErrorEvent(BaseWebhookEvent):
    """Triggered when a post-transformation fails.

    The original file remains available, but the requested transformation could not be generated.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: UploadPostTransformErrorEventData

    request: UploadPostTransformErrorEventRequest

    type: Literal["upload.post-transform.error"]  # type: ignore
