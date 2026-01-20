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
    "ExtensionItemAITasks",
    "ExtensionItemAITasksTask",
    "ExtensionItemAITasksTaskSelectTags",
    "ExtensionItemAITasksTaskSelectMetadata",
    "ExtensionItemAITasksTaskYesNo",
    "ExtensionItemAITasksTaskYesNoOnNo",
    "ExtensionItemAITasksTaskYesNoOnNoSetMetadata",
    "ExtensionItemAITasksTaskYesNoOnNoUnsetMetadata",
    "ExtensionItemAITasksTaskYesNoOnUnknown",
    "ExtensionItemAITasksTaskYesNoOnUnknownSetMetadata",
    "ExtensionItemAITasksTaskYesNoOnUnknownUnsetMetadata",
    "ExtensionItemAITasksTaskYesNoOnYes",
    "ExtensionItemAITasksTaskYesNoOnYesSetMetadata",
    "ExtensionItemAITasksTaskYesNoOnYesUnsetMetadata",
    "ExtensionItemSavedExtension",
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


class ExtensionItemAITasksTaskSelectTags(BaseModel):
    instruction: str
    """The question or instruction for the AI to analyze the image."""

    type: Literal["select_tags"]
    """Task type that analyzes the image and adds matching tags from a vocabulary."""

    max_selections: Optional[int] = None
    """Maximum number of tags to select from the vocabulary."""

    min_selections: Optional[int] = None
    """Minimum number of tags to select from the vocabulary."""

    vocabulary: Optional[List[str]] = None
    """Array of possible tag values.

    Combined length of all strings must not exceed 500 characters. Cannot contain
    the `%` character.
    """


class ExtensionItemAITasksTaskSelectMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to set. The field must exist in your account."""

    instruction: str
    """The question or instruction for the AI to analyze the image."""

    type: Literal["select_metadata"]
    """
    Task type that analyzes the image and sets a custom metadata field value from a
    vocabulary.
    """

    max_selections: Optional[int] = None
    """Maximum number of values to select from the vocabulary."""

    min_selections: Optional[int] = None
    """Minimum number of values to select from the vocabulary."""

    vocabulary: Optional[List[Union[str, float, bool]]] = None
    """Array of possible values matching the custom metadata field type."""


class ExtensionItemAITasksTaskYesNoOnNoSetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to set."""

    value: Union[str, float, bool, List[Union[str, float, bool]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class ExtensionItemAITasksTaskYesNoOnNoUnsetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to remove."""


class ExtensionItemAITasksTaskYesNoOnNo(BaseModel):
    """Actions to execute if the AI answers no."""

    add_tags: Optional[List[str]] = None
    """Array of tag strings to add to the asset."""

    remove_tags: Optional[List[str]] = None
    """Array of tag strings to remove from the asset."""

    set_metadata: Optional[List[ExtensionItemAITasksTaskYesNoOnNoSetMetadata]] = None
    """Array of custom metadata field updates."""

    unset_metadata: Optional[List[ExtensionItemAITasksTaskYesNoOnNoUnsetMetadata]] = None
    """Array of custom metadata fields to remove."""


class ExtensionItemAITasksTaskYesNoOnUnknownSetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to set."""

    value: Union[str, float, bool, List[Union[str, float, bool]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class ExtensionItemAITasksTaskYesNoOnUnknownUnsetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to remove."""


class ExtensionItemAITasksTaskYesNoOnUnknown(BaseModel):
    """Actions to execute if the AI cannot determine the answer."""

    add_tags: Optional[List[str]] = None
    """Array of tag strings to add to the asset."""

    remove_tags: Optional[List[str]] = None
    """Array of tag strings to remove from the asset."""

    set_metadata: Optional[List[ExtensionItemAITasksTaskYesNoOnUnknownSetMetadata]] = None
    """Array of custom metadata field updates."""

    unset_metadata: Optional[List[ExtensionItemAITasksTaskYesNoOnUnknownUnsetMetadata]] = None
    """Array of custom metadata fields to remove."""


class ExtensionItemAITasksTaskYesNoOnYesSetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to set."""

    value: Union[str, float, bool, List[Union[str, float, bool]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class ExtensionItemAITasksTaskYesNoOnYesUnsetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to remove."""


class ExtensionItemAITasksTaskYesNoOnYes(BaseModel):
    """Actions to execute if the AI answers yes."""

    add_tags: Optional[List[str]] = None
    """Array of tag strings to add to the asset."""

    remove_tags: Optional[List[str]] = None
    """Array of tag strings to remove from the asset."""

    set_metadata: Optional[List[ExtensionItemAITasksTaskYesNoOnYesSetMetadata]] = None
    """Array of custom metadata field updates."""

    unset_metadata: Optional[List[ExtensionItemAITasksTaskYesNoOnYesUnsetMetadata]] = None
    """Array of custom metadata fields to remove."""


class ExtensionItemAITasksTaskYesNo(BaseModel):
    instruction: str
    """The yes/no question for the AI to answer about the image."""

    type: Literal["yes_no"]
    """Task type that asks a yes/no question and executes actions based on the answer."""

    on_no: Optional[ExtensionItemAITasksTaskYesNoOnNo] = None
    """Actions to execute if the AI answers no."""

    on_unknown: Optional[ExtensionItemAITasksTaskYesNoOnUnknown] = None
    """Actions to execute if the AI cannot determine the answer."""

    on_yes: Optional[ExtensionItemAITasksTaskYesNoOnYes] = None
    """Actions to execute if the AI answers yes."""


ExtensionItemAITasksTask: TypeAlias = Annotated[
    Union[ExtensionItemAITasksTaskSelectTags, ExtensionItemAITasksTaskSelectMetadata, ExtensionItemAITasksTaskYesNo],
    PropertyInfo(discriminator="type"),
]


class ExtensionItemAITasks(BaseModel):
    name: Literal["ai-tasks"]
    """Specifies the AI tasks extension for automated image analysis using AI models."""

    tasks: List[ExtensionItemAITasksTask]
    """Array of task objects defining AI operations to perform on the asset."""


class ExtensionItemSavedExtension(BaseModel):
    id: str
    """The unique ID of the saved extension to apply."""

    name: Literal["saved-extension"]
    """Indicates this is a reference to a saved extension."""


ExtensionItem: TypeAlias = Annotated[
    Union[
        ExtensionItemRemoveBg,
        ExtensionItemAutoTaggingExtension,
        ExtensionItemAIAutoDescription,
        ExtensionItemAITasks,
        ExtensionItemSavedExtension,
    ],
    PropertyInfo(discriminator="name"),
]

Extensions: TypeAlias = List[ExtensionItem]
