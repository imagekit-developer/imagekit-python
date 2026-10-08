# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Required, TypedDict

from .webhook_event_type import WebhookEventType

__all__ = ["WebhookCreateParams"]


class WebhookCreateParams(TypedDict, total=False):
    endpoint: Required[str]
    """The URL where ImageKit sends webhook events as `POST` requests.

    Must use the `http` or `https` protocol, and must be unique across all webhooks
    for your account.
    """

    events: Required[List[WebhookEventType]]
    """The event types this webhook is subscribed to.

    ImageKit sends a request to the `endpoint` only for these events.
    """

    enabled: bool
    """Whether the webhook is enabled.

    When `false`, ImageKit doesn't send any events to the `endpoint`.
    """
