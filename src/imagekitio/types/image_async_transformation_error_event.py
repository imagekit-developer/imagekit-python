# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "ImageAsyncTransformationErrorEvent",
    "ImageAsyncTransformationErrorEventData",
    "ImageAsyncTransformationErrorEventDataAsset",
    "ImageAsyncTransformationErrorEventDataTransformation",
    "ImageAsyncTransformationErrorEventDataTransformationError",
    "ImageAsyncTransformationErrorEventDataTransformationOptions",
    "ImageAsyncTransformationErrorEventRequest",
]


class ImageAsyncTransformationErrorEventDataAsset(BaseModel):
    """Information about the source image asset being transformed."""

    url: str
    """URL of the source image, without the transformation."""


class ImageAsyncTransformationErrorEventDataTransformationError(BaseModel):
    """Details about the transformation error."""

    reason: Literal["download_failed", "invalid_transformation", "limit_exceeded", "internal_server_error"]
    """Specific reason for the transformation failure:

    - `download_failed`: Could not download the source image
    - `invalid_transformation`: The requested transformation is invalid
    - `limit_exceeded`: The source image or transformation exceeds a limit
    - `internal_server_error`: Unexpected server error
    """

    message: Optional[str] = None
    """A description of the error, when available."""


class ImageAsyncTransformationErrorEventDataTransformationOptions(BaseModel):
    """Options of the requested transformation."""

    transformation: Optional[str] = None
    """The transformation string from the request URL, for example `e-removedotbg`.

    Not present if the URL has no transformation.
    """


class ImageAsyncTransformationErrorEventDataTransformation(BaseModel):
    type: Literal["image-transformation"]
    """Type of transformation. Always `image-transformation`."""

    error: Optional[ImageAsyncTransformationErrorEventDataTransformationError] = None
    """Details about the transformation error."""

    options: Optional[ImageAsyncTransformationErrorEventDataTransformationOptions] = None
    """Options of the requested transformation."""


class ImageAsyncTransformationErrorEventData(BaseModel):
    asset: ImageAsyncTransformationErrorEventDataAsset
    """Information about the source image asset being transformed."""

    transformation: ImageAsyncTransformationErrorEventDataTransformation


class ImageAsyncTransformationErrorEventRequest(BaseModel):
    """Information about the original request that triggered the image transformation."""

    url: str
    """Full URL of the transformation request that was submitted."""

    x_request_id: str
    """Unique identifier for the originating transformation request."""

    user_agent: Optional[str] = None
    """User-Agent header from the original request that triggered the transformation."""


class ImageAsyncTransformationErrorEvent(BaseWebhookEvent):
    """Triggered when an asynchronous image transformation fails.

    Listen to this webhook to log error reasons and debug issues. Check your origin and URL endpoint settings if the reason is related to download failure. For other errors, contact ImageKit support.
    """

    created_at: datetime
    """Timestamp when the event was created in ISO8601 format."""

    data: ImageAsyncTransformationErrorEventData

    request: ImageAsyncTransformationErrorEventRequest
    """Information about the original request that triggered the image transformation."""

    type: Literal["image.async-transformation.error"]  # type: ignore
