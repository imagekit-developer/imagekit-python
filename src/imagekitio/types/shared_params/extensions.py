# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

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


class ExtensionItemAITasksTaskSelectTags(TypedDict, total=False):
    instruction: Required[str]
    """The question or instruction for the AI to analyze the image."""

    type: Required[Literal["select_tags"]]
    """Task type that analyzes the image and adds matching tags from a vocabulary."""

    max_selections: int
    """Maximum number of tags to select from the vocabulary."""

    min_selections: int
    """Minimum number of tags to select from the vocabulary."""

    vocabulary: SequenceNotStr[str]
    """Array of possible tag values.

    Combined length of all strings must not exceed 500 characters. Cannot contain
    the `%` character.
    """


class ExtensionItemAITasksTaskSelectMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to set. The field must exist in your account."""

    instruction: Required[str]
    """The question or instruction for the AI to analyze the image."""

    type: Required[Literal["select_metadata"]]
    """
    Task type that analyzes the image and sets a custom metadata field value from a
    vocabulary.
    """

    max_selections: int
    """Maximum number of values to select from the vocabulary."""

    min_selections: int
    """Minimum number of values to select from the vocabulary."""

    vocabulary: SequenceNotStr[Union[str, float, bool]]
    """Array of possible values matching the custom metadata field type."""


class ExtensionItemAITasksTaskYesNoOnNoSetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to set."""

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float, bool]]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class ExtensionItemAITasksTaskYesNoOnNoUnsetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to remove."""


class ExtensionItemAITasksTaskYesNoOnNo(TypedDict, total=False):
    """Actions to execute if the AI answers no."""

    add_tags: SequenceNotStr[str]
    """Array of tag strings to add to the asset."""

    remove_tags: SequenceNotStr[str]
    """Array of tag strings to remove from the asset."""

    set_metadata: Iterable[ExtensionItemAITasksTaskYesNoOnNoSetMetadata]
    """Array of custom metadata field updates."""

    unset_metadata: Iterable[ExtensionItemAITasksTaskYesNoOnNoUnsetMetadata]
    """Array of custom metadata fields to remove."""


class ExtensionItemAITasksTaskYesNoOnUnknownSetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to set."""

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float, bool]]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class ExtensionItemAITasksTaskYesNoOnUnknownUnsetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to remove."""


class ExtensionItemAITasksTaskYesNoOnUnknown(TypedDict, total=False):
    """Actions to execute if the AI cannot determine the answer."""

    add_tags: SequenceNotStr[str]
    """Array of tag strings to add to the asset."""

    remove_tags: SequenceNotStr[str]
    """Array of tag strings to remove from the asset."""

    set_metadata: Iterable[ExtensionItemAITasksTaskYesNoOnUnknownSetMetadata]
    """Array of custom metadata field updates."""

    unset_metadata: Iterable[ExtensionItemAITasksTaskYesNoOnUnknownUnsetMetadata]
    """Array of custom metadata fields to remove."""


class ExtensionItemAITasksTaskYesNoOnYesSetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to set."""

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float, bool]]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class ExtensionItemAITasksTaskYesNoOnYesUnsetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to remove."""


class ExtensionItemAITasksTaskYesNoOnYes(TypedDict, total=False):
    """Actions to execute if the AI answers yes."""

    add_tags: SequenceNotStr[str]
    """Array of tag strings to add to the asset."""

    remove_tags: SequenceNotStr[str]
    """Array of tag strings to remove from the asset."""

    set_metadata: Iterable[ExtensionItemAITasksTaskYesNoOnYesSetMetadata]
    """Array of custom metadata field updates."""

    unset_metadata: Iterable[ExtensionItemAITasksTaskYesNoOnYesUnsetMetadata]
    """Array of custom metadata fields to remove."""


class ExtensionItemAITasksTaskYesNo(TypedDict, total=False):
    instruction: Required[str]
    """The yes/no question for the AI to answer about the image."""

    type: Required[Literal["yes_no"]]
    """Task type that asks a yes/no question and executes actions based on the answer."""

    on_no: ExtensionItemAITasksTaskYesNoOnNo
    """Actions to execute if the AI answers no."""

    on_unknown: ExtensionItemAITasksTaskYesNoOnUnknown
    """Actions to execute if the AI cannot determine the answer."""

    on_yes: ExtensionItemAITasksTaskYesNoOnYes
    """Actions to execute if the AI answers yes."""


ExtensionItemAITasksTask: TypeAlias = Union[
    ExtensionItemAITasksTaskSelectTags, ExtensionItemAITasksTaskSelectMetadata, ExtensionItemAITasksTaskYesNo
]


class ExtensionItemAITasks(TypedDict, total=False):
    name: Required[Literal["ai-tasks"]]
    """Specifies the AI tasks extension for automated image analysis using AI models."""

    tasks: Required[Iterable[ExtensionItemAITasksTask]]
    """Array of task objects defining AI operations to perform on the asset."""


class ExtensionItemSavedExtension(TypedDict, total=False):
    id: Required[str]
    """The unique ID of the saved extension to apply."""

    name: Required[Literal["saved-extension"]]
    """Indicates this is a reference to a saved extension."""


ExtensionItem: TypeAlias = Union[
    ExtensionItemRemoveBg,
    ExtensionItemAutoTaggingExtension,
    ExtensionItemAIAutoDescription,
    ExtensionItemAITasks,
    ExtensionItemSavedExtension,
]

Extensions: TypeAlias = List[ExtensionItem]
