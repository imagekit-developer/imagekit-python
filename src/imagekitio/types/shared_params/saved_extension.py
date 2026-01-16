# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import datetime
from typing_extensions import Annotated, TypedDict

from ..._utils import PropertyInfo
from .extension_config import ExtensionConfig

__all__ = ["SavedExtension"]


class SavedExtension(TypedDict, total=False):
    """Saved extension object containing extension configuration."""

    id: str
    """Unique identifier of the saved extension."""

    config: ExtensionConfig
    """
    Configuration object for an extension (base extensions only, not saved extension
    references).
    """

    created_at: Annotated[Union[str, datetime], PropertyInfo(alias="createdAt", format="iso8601")]
    """Timestamp when the saved extension was created."""

    description: str
    """Description of the saved extension."""

    name: str
    """Name of the saved extension."""

    updated_at: Annotated[Union[str, datetime], PropertyInfo(alias="updatedAt", format="iso8601")]
    """Timestamp when the saved extension was last updated."""
