# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .shared_params.extension_config import ExtensionConfig

__all__ = ["SavedExtensionCreateParams"]


class SavedExtensionCreateParams(TypedDict, total=False):
    config: Required[ExtensionConfig]
    """
    Configuration object for an extension (base extensions only, not saved extension
    references).
    """

    description: Required[str]
    """Description of what the saved extension does."""

    name: Required[str]
    """Name of the saved extension."""
