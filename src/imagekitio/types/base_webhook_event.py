# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from .._models import BaseModel

__all__ = ["BaseWebhookEvent"]


class BaseWebhookEvent(BaseModel):
    id: str
    """Unique identifier for the event."""

    type: str
    """The type of webhook event."""
