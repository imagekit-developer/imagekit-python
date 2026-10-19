# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .folder import Folder
from .base_webhook_event import BaseWebhookEvent

__all__ = ["FolderUpdateEvent"]


class FolderUpdateEvent(BaseWebhookEvent):
    """
    Triggered when a folder is updated, for example when its custom metadata changes or it is renamed. Renaming a folder sends one event per folder in the tree, each with its new `folderPath`.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: Folder

    type: Literal["folder.updated"]  # type: ignore
    """Type of the webhook event."""
