# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = [
    "UploadPostTransformErrorWebhookEvent",
    "Data",
    "DataTransformation",
    "DataTransformationError",
    "Request",
    "RequestTransformation",
]


class DataTransformationError(BaseModel):
    reason: str
    """Reason for the post-transformation failure."""


class DataTransformation(BaseModel):
    error: DataTransformationError


class Data(BaseModel):
    file_id: str = FieldInfo(alias="fileId")
    """Unique identifier of the originally uploaded file."""

    name: str
    """Name of the file."""

    path: str
    """Path of the file."""

    transformation: DataTransformation

    url: str
    """URL of the attempted post-transformation."""


class RequestTransformation(BaseModel):
    type: Literal["transformation", "abs", "gif-to-video", "thumbnail"]
    """Type of the requested post-transformation."""

    protocol: Optional[Literal["hls", "dash"]] = None
    """Only applicable if transformation type is 'abs'. Streaming protocol used."""

    value: Optional[str] = None
    """Value for the requested transformation type."""


class Request(BaseModel):
    transformation: RequestTransformation

    x_request_id: str
    """Unique identifier for the originating request."""


class UploadPostTransformErrorWebhookEvent(BaseModel):
    id: str
    """Unique identifier for the event."""

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: Data

    request: Request

    type: Literal["upload.post-transform.error"]
