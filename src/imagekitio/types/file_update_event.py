# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .file import File
from .base_webhook_event import BaseWebhookEvent

__all__ = ["FileUpdateEvent"]


class FileUpdateEvent(BaseWebhookEvent):
    """Triggered when a file is updated."""

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: File
    """Object containing details of a file or file version."""

    type: Literal["file.updated"]  # type: ignore
    """Type of the webhook event."""
