# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "ImageAsyncTransformationAcceptedEvent",
    "ImageAsyncTransformationAcceptedEventData",
    "ImageAsyncTransformationAcceptedEventDataAsset",
    "ImageAsyncTransformationAcceptedEventDataTransformation",
    "ImageAsyncTransformationAcceptedEventDataTransformationOptions",
    "ImageAsyncTransformationAcceptedEventRequest",
]


class ImageAsyncTransformationAcceptedEventDataAsset(BaseModel):
    """Information about the source image asset being transformed."""

    url: str
    """URL of the source image, without the transformation."""


class ImageAsyncTransformationAcceptedEventDataTransformationOptions(BaseModel):
    """Options of the requested transformation."""

    transformation: Optional[str] = None
    """The transformation string from the request URL, for example `e-removedotbg`.

    Not present if the URL has no transformation.
    """


class ImageAsyncTransformationAcceptedEventDataTransformation(BaseModel):
    """Base information about an image transformation request."""

    type: Literal["image-transformation"]
    """Type of transformation. Always `image-transformation`."""

    options: Optional[ImageAsyncTransformationAcceptedEventDataTransformationOptions] = None
    """Options of the requested transformation."""


class ImageAsyncTransformationAcceptedEventData(BaseModel):
    asset: ImageAsyncTransformationAcceptedEventDataAsset
    """Information about the source image asset being transformed."""

    transformation: ImageAsyncTransformationAcceptedEventDataTransformation
    """Base information about an image transformation request."""


class ImageAsyncTransformationAcceptedEventRequest(BaseModel):
    """Information about the original request that triggered the image transformation."""

    url: str
    """Full URL of the transformation request that was submitted."""

    x_request_id: str
    """Unique identifier for the originating transformation request."""

    user_agent: Optional[str] = None
    """User-Agent header from the original request that triggered the transformation."""


class ImageAsyncTransformationAcceptedEvent(BaseWebhookEvent):
    """
    Triggered when a new asynchronous image transformation request is accepted for processing. This event confirms that ImageKit has received and queued your transformation request. Use this for debugging and tracking transformation lifecycle.
    """

    created_at: datetime
    """Timestamp when the event was created in ISO8601 format."""

    data: ImageAsyncTransformationAcceptedEventData

    request: ImageAsyncTransformationAcceptedEventRequest
    """Information about the original request that triggered the image transformation."""

    type: Literal["image.async-transformation.accepted"]  # type: ignore
