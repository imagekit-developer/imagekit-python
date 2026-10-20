# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .folder import Folder
from .base_webhook_event import BaseWebhookEvent

__all__ = ["FolderCreateEvent"]


class FolderCreateEvent(BaseWebhookEvent):
    """
    Triggered when a folder is created, whether explicitly, by copying or moving a folder, or implicitly when an upload creates missing parent folders. Copying or moving a folder tree sends one event per folder in the tree.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: Folder

    type: Literal["folder.created"]  # type: ignore
    """Type of the webhook event."""
