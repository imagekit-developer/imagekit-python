# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime
from typing_extensions import Literal

from .base_webhook_event import BaseWebhookEvent

__all__ = ["DamFileVersionCreateEvent"]


class DamFileVersionCreateEvent(BaseWebhookEvent):
    """Triggered when a file version is created."""

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: object

    type: Literal["file-version.created"]  # type: ignore
    """Type of the webhook event."""
