# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "Extensions",
    "ExtensionItem",
    "ExtensionItemRemoveBg",
    "ExtensionItemRemoveBgOptions",
    "ExtensionItemAutoTaggingExtension",
    "ExtensionItemAIAutoDescription",
]


class ExtensionItemRemoveBgOptions(TypedDict, total=False):
    add_shadow: bool
    """Whether to add an artificial shadow to the result.

    Default is false. Note: Adding shadows is currently only supported for car
    photos.
    """

    bg_color: str
    """
    Specifies a solid color background using hex code (e.g., "81d4fa", "fff") or
    color name (e.g., "green"). If this parameter is set, `bg_image_url` must be
    empty.
    """

    bg_image_url: str
    """Sets a background image from a URL.

    If this parameter is set, `bg_color` must be empty.
    """

    semitransparency: bool
    """Allows semi-transparent regions in the result.

    Default is true. Note: Semitransparency is currently only supported for car
    windows.
    """


class ExtensionItemRemoveBg(TypedDict, total=False):
    name: Required[Literal["remove-bg"]]
    """Specifies the background removal extension."""

    options: ExtensionItemRemoveBgOptions


class ExtensionItemAutoTaggingExtension(TypedDict, total=False):
    max_tags: Required[Annotated[int, PropertyInfo(alias="maxTags")]]
    """Maximum number of tags to attach to the asset."""

    min_confidence: Required[Annotated[int, PropertyInfo(alias="minConfidence")]]
    """Minimum confidence level for tags to be considered valid."""

    name: Required[Literal["google-auto-tagging", "aws-auto-tagging"]]
    """Specifies the auto-tagging extension used."""


class ExtensionItemAIAutoDescription(TypedDict, total=False):
    name: Required[Literal["ai-auto-description"]]
    """Specifies the auto description extension."""


ExtensionItem: TypeAlias = Union[
    ExtensionItemRemoveBg, ExtensionItemAutoTaggingExtension, ExtensionItemAIAutoDescription
]

Extensions: TypeAlias = List[ExtensionItem]
