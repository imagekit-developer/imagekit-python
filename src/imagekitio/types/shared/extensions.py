# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

__all__ = [
    "Extensions",
    "ExtensionItem",
    "ExtensionItemRemoveBg",
    "ExtensionItemRemoveBgOptions",
    "ExtensionItemAutoTaggingExtension",
    "ExtensionItemAIAutoDescription",
]


class ExtensionItemRemoveBgOptions(BaseModel):
    add_shadow: Optional[bool] = None
    """Whether to add an artificial shadow to the result.

    Default is false. Note: Adding shadows is currently only supported for car
    photos.
    """

    bg_color: Optional[str] = None
    """
    Specifies a solid color background using hex code (e.g., "81d4fa", "fff") or
    color name (e.g., "green"). If this parameter is set, `bg_image_url` must be
    empty.
    """

    bg_image_url: Optional[str] = None
    """Sets a background image from a URL.

    If this parameter is set, `bg_color` must be empty.
    """

    semitransparency: Optional[bool] = None
    """Allows semi-transparent regions in the result.

    Default is true. Note: Semitransparency is currently only supported for car
    windows.
    """


class ExtensionItemRemoveBg(BaseModel):
    name: Literal["remove-bg"]
    """Specifies the background removal extension."""

    options: Optional[ExtensionItemRemoveBgOptions] = None


class ExtensionItemAutoTaggingExtension(BaseModel):
    max_tags: int = FieldInfo(alias="maxTags")
    """Maximum number of tags to attach to the asset."""

    min_confidence: int = FieldInfo(alias="minConfidence")
    """Minimum confidence level for tags to be considered valid."""

    name: Literal["google-auto-tagging", "aws-auto-tagging"]
    """Specifies the auto-tagging extension used."""


class ExtensionItemAIAutoDescription(BaseModel):
    name: Literal["ai-auto-description"]
    """Specifies the auto description extension."""


ExtensionItem: TypeAlias = Annotated[
    Union[ExtensionItemRemoveBg, ExtensionItemAutoTaggingExtension, ExtensionItemAIAutoDescription],
    PropertyInfo(discriminator="name"),
]

Extensions: TypeAlias = List[ExtensionItem]
