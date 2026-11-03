# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "ImageAsyncTransformationReadyEvent",
    "ImageAsyncTransformationReadyEventData",
    "ImageAsyncTransformationReadyEventDataAsset",
    "ImageAsyncTransformationReadyEventDataTransformation",
    "ImageAsyncTransformationReadyEventDataTransformationOptions",
    "ImageAsyncTransformationReadyEventDataTransformationOutput",
    "ImageAsyncTransformationReadyEventDataTransformationOutputImageMetadata",
    "ImageAsyncTransformationReadyEventRequest",
    "ImageAsyncTransformationReadyEventTimings",
]


class ImageAsyncTransformationReadyEventDataAsset(BaseModel):
    """Information about the source image asset being transformed."""

    url: str
    """URL of the source image, without the transformation."""


class ImageAsyncTransformationReadyEventDataTransformationOptions(BaseModel):
    """Options of the requested transformation."""

    transformation: Optional[str] = None
    """The transformation string from the request URL, for example `e-removedotbg`.

    Not present if the URL has no transformation.
    """


class ImageAsyncTransformationReadyEventDataTransformationOutputImageMetadata(BaseModel):
    """Metadata of the output image."""

    size: int
    """Size of the output image in bytes."""

    format: Optional[str] = None
    """Format of the output image, for example `webp` or `png`."""


class ImageAsyncTransformationReadyEventDataTransformationOutput(BaseModel):
    """Information about the transformed output image."""

    url: str
    """URL to access the transformed image."""

    image_metadata: Optional[ImageAsyncTransformationReadyEventDataTransformationOutputImageMetadata] = None
    """Metadata of the output image."""


class ImageAsyncTransformationReadyEventDataTransformation(BaseModel):
    type: Literal["image-transformation"]
    """Type of transformation. Always `image-transformation`."""

    options: Optional[ImageAsyncTransformationReadyEventDataTransformationOptions] = None
    """Options of the requested transformation."""

    output: Optional[ImageAsyncTransformationReadyEventDataTransformationOutput] = None
    """Information about the transformed output image."""


class ImageAsyncTransformationReadyEventData(BaseModel):
    asset: ImageAsyncTransformationReadyEventDataAsset
    """Information about the source image asset being transformed."""

    transformation: ImageAsyncTransformationReadyEventDataTransformation


class ImageAsyncTransformationReadyEventRequest(BaseModel):
    """Information about the original request that triggered the image transformation."""

    url: str
    """Full URL of the transformation request that was submitted."""

    x_request_id: str
    """Unique identifier for the originating transformation request."""

    user_agent: Optional[str] = None
    """User-Agent header from the original request that triggered the transformation."""


class ImageAsyncTransformationReadyEventTimings(BaseModel):
    """Performance metrics for the transformation process."""

    processing_duration: Optional[int] = None
    """Time spent processing the transformation, in milliseconds."""

    queue_duration: Optional[int] = None
    """
    Time the request waited in the queue before processing started, in milliseconds.
    """


class ImageAsyncTransformationReadyEvent(BaseWebhookEvent):
    """
    Triggered when an asynchronous image transformation is finished and the transformed image is ready to be served. Listen to this webhook and update any flags in your database or CMS so your application can start displaying the transformed image to users.
    """

    created_at: datetime
    """Timestamp when the event was created in ISO8601 format."""

    data: ImageAsyncTransformationReadyEventData

    request: ImageAsyncTransformationReadyEventRequest
    """Information about the original request that triggered the image transformation."""

    type: Literal["image.async-transformation.ready"]  # type: ignore

    timings: Optional[ImageAsyncTransformationReadyEventTimings] = None
    """Performance metrics for the transformation process."""
