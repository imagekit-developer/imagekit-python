# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["FileDeleteEvent", "FileDeleteEventData"]


class FileDeleteEventData(BaseModel):
    file_id: str = FieldInfo(alias="fileId")
    """The unique `fileId` of the deleted file."""


class FileDeleteEvent(BaseWebhookEvent):
    """Triggered when a file is deleted."""

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: FileDeleteEventData

    type: Literal["file.deleted"]  # type: ignore
    """Type of the webhook event."""
