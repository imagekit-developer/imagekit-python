# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import TypedDict

from .webhook_event_type import WebhookEventType

__all__ = ["WebhookUpdateParams"]


class WebhookUpdateParams(TypedDict, total=False):
    enabled: bool
    """Whether the webhook is enabled. Omit to leave the current value unchanged."""

    endpoint: str
    """The URL where ImageKit sends webhook events as `POST` requests.

    Must use the `http` or `https` protocol, and must be unique across all webhooks
    for your account.
    """

    events: List[WebhookEventType]
    """The event types this webhook is subscribed to.

    Replaces the existing list. Omit to leave the current value unchanged.
    """
