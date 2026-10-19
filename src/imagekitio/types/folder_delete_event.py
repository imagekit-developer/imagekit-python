# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["FolderDeleteEvent", "FolderDeleteEventData"]


class FolderDeleteEventData(BaseModel):
    folder_id: str = FieldInfo(alias="folderId")
    """The unique `folderId` of the deleted folder."""


class FolderDeleteEvent(BaseWebhookEvent):
    """Triggered when a folder is deleted.

    Deleting a folder tree sends one event per folder in the tree; the files inside it send `file.deleted` events and their versions send `file-version.deleted` events. Moving a folder sends this event for the old `folderId` and `folder.created` for the new one.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: FolderDeleteEventData

    type: Literal["folder.deleted"]  # type: ignore
    """Type of the webhook event."""
