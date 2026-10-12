# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["FolderDeleteEvent", "FolderDeleteEventData"]


class FolderDeleteEventData(BaseModel):
    id: str
    """The unique identifier of the deleted folder."""


class FolderDeleteEvent(BaseWebhookEvent):
    """Triggered when a folder is deleted."""

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: FolderDeleteEventData

    type: Literal["folder.deleted"]  # type: ignore
    """Type of the webhook event."""
