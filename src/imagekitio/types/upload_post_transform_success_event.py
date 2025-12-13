# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "UploadPostTransformSuccessEvent",
    "UploadPostTransformSuccessEventData",
    "UploadPostTransformSuccessEventRequest",
    "UploadPostTransformSuccessEventRequestTransformation",
]


class UploadPostTransformSuccessEventData(BaseModel):
    file_id: str = FieldInfo(alias="fileId")
    """Unique identifier of the originally uploaded file."""

    name: str
    """Name of the file."""

    url: str
    """URL of the generated post-transformation."""


class UploadPostTransformSuccessEventRequestTransformation(BaseModel):
    type: Literal["transformation", "abs", "gif-to-video", "thumbnail"]
    """Type of the requested post-transformation."""

    protocol: Optional[Literal["hls", "dash"]] = None
    """Only applicable if transformation type is 'abs'. Streaming protocol used."""

    value: Optional[str] = None
    """Value for the requested transformation type."""


class UploadPostTransformSuccessEventRequest(BaseModel):
    transformation: UploadPostTransformSuccessEventRequestTransformation

    x_request_id: str
    """Unique identifier for the originating request."""


class UploadPostTransformSuccessEvent(BaseWebhookEvent):
    """Triggered when a post-transformation completes successfully.

    The transformed version of the file is now ready and can be accessed via the provided URL. Note that each post-transformation generates a separate webhook event.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: UploadPostTransformSuccessEventData

    request: UploadPostTransformSuccessEventRequest

    type: Literal["upload.post-transform.success"]  # type: ignore
