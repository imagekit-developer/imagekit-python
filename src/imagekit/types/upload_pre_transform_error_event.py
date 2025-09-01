# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel

__all__ = ["UploadPreTransformErrorEvent", "Data", "DataTransformation", "DataTransformationError", "Request"]


class DataTransformationError(BaseModel):
    reason: str
    """Reason for the pre-transformation failure."""


class DataTransformation(BaseModel):
    error: DataTransformationError


class Data(BaseModel):
    name: str
    """Name of the file."""

    path: str
    """Path of the file."""

    transformation: DataTransformation


class Request(BaseModel):
    transformation: str
    """The requested pre-transformation string."""

    x_request_id: str
    """Unique identifier for the originating request."""


class UploadPreTransformErrorEvent(BaseModel):
    id: str
    """Unique identifier for the event."""

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: Data

    request: Request

    type: Literal["upload.pre-transform.error"]
