# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .shared_params.extension_config import ExtensionConfig

__all__ = ["SavedExtensionUpdateParams"]


class SavedExtensionUpdateParams(TypedDict, total=False):
    config: ExtensionConfig
    """
    Configuration object for an extension (base extensions only, not saved extension
    references).
    """

    description: str
    """Updated description of the saved extension."""

    name: str
    """Updated name of the saved extension."""
