# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .extension_config import ExtensionConfig

__all__ = ["SavedExtension"]


class SavedExtension(BaseModel):
    """Saved extension object containing extension configuration."""

    id: Optional[str] = None
    """Unique identifier of the saved extension."""

    config: Optional[ExtensionConfig] = None
    """
    Configuration object for an extension (base extensions only, not saved extension
    references).
    """

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Timestamp when the saved extension was created."""

    description: Optional[str] = None
    """Description of the saved extension."""

    name: Optional[str] = None
    """Name of the saved extension."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Timestamp when the saved extension was last updated."""
