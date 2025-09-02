# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "UploadPreTransformErrorEvent",
    "UploadPreTransformErrorEventData",
    "UploadPreTransformErrorEventDataTransformation",
    "UploadPreTransformErrorEventDataTransformationError",
    "UploadPreTransformErrorEventRequest",
]


class UploadPreTransformErrorEventDataTransformationError(BaseModel):
    reason: str
    """Reason for the pre-transformation failure."""


class UploadPreTransformErrorEventDataTransformation(BaseModel):
    error: UploadPreTransformErrorEventDataTransformationError


class UploadPreTransformErrorEventData(BaseModel):
    name: str
    """Name of the file."""

    path: str
    """Path of the file."""

    transformation: UploadPreTransformErrorEventDataTransformation


class UploadPreTransformErrorEventRequest(BaseModel):
    transformation: str
    """The requested pre-transformation string."""

    x_request_id: str
    """Unique identifier for the originating request."""


class UploadPreTransformErrorEvent(BaseWebhookEvent):
    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: UploadPreTransformErrorEventData

    request: UploadPreTransformErrorEventRequest

    type: Literal["upload.pre-transform.error"]  # type: ignore
