# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = [
    "ExtensionConfig",
    "RemoveBg",
    "RemoveBgOptions",
    "AutoTaggingExtension",
    "AIAutoDescription",
    "AITasks",
    "AITasksTask",
    "AITasksTaskSelectTags",
    "AITasksTaskSelectMetadata",
    "AITasksTaskYesNo",
    "AITasksTaskYesNoOnNo",
    "AITasksTaskYesNoOnNoSetMetadata",
    "AITasksTaskYesNoOnNoUnsetMetadata",
    "AITasksTaskYesNoOnUnknown",
    "AITasksTaskYesNoOnUnknownSetMetadata",
    "AITasksTaskYesNoOnUnknownUnsetMetadata",
    "AITasksTaskYesNoOnYes",
    "AITasksTaskYesNoOnYesSetMetadata",
    "AITasksTaskYesNoOnYesUnsetMetadata",
]


class RemoveBgOptions(TypedDict, total=False):
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


class RemoveBg(TypedDict, total=False):
    name: Required[Literal["remove-bg"]]
    """Specifies the background removal extension."""

    options: RemoveBgOptions


class AutoTaggingExtension(TypedDict, total=False):
    max_tags: Required[Annotated[int, PropertyInfo(alias="maxTags")]]
    """Maximum number of tags to attach to the asset."""

    min_confidence: Required[Annotated[int, PropertyInfo(alias="minConfidence")]]
    """Minimum confidence level for tags to be considered valid."""

    name: Required[Literal["google-auto-tagging", "aws-auto-tagging"]]
    """Specifies the auto-tagging extension used."""


class AIAutoDescription(TypedDict, total=False):
    name: Required[Literal["ai-auto-description"]]
    """Specifies the auto description extension."""


class AITasksTaskSelectTags(TypedDict, total=False):
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


class AITasksTaskSelectMetadata(TypedDict, total=False):
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


class AITasksTaskYesNoOnNoSetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to set."""

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float, bool]]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class AITasksTaskYesNoOnNoUnsetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to remove."""


class AITasksTaskYesNoOnNo(TypedDict, total=False):
    """Actions to execute if the AI answers no."""

    add_tags: SequenceNotStr[str]
    """Array of tag strings to add to the asset."""

    remove_tags: SequenceNotStr[str]
    """Array of tag strings to remove from the asset."""

    set_metadata: Iterable[AITasksTaskYesNoOnNoSetMetadata]
    """Array of custom metadata field updates."""

    unset_metadata: Iterable[AITasksTaskYesNoOnNoUnsetMetadata]
    """Array of custom metadata fields to remove."""


class AITasksTaskYesNoOnUnknownSetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to set."""

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float, bool]]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class AITasksTaskYesNoOnUnknownUnsetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to remove."""


class AITasksTaskYesNoOnUnknown(TypedDict, total=False):
    """Actions to execute if the AI cannot determine the answer."""

    add_tags: SequenceNotStr[str]
    """Array of tag strings to add to the asset."""

    remove_tags: SequenceNotStr[str]
    """Array of tag strings to remove from the asset."""

    set_metadata: Iterable[AITasksTaskYesNoOnUnknownSetMetadata]
    """Array of custom metadata field updates."""

    unset_metadata: Iterable[AITasksTaskYesNoOnUnknownUnsetMetadata]
    """Array of custom metadata fields to remove."""


class AITasksTaskYesNoOnYesSetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to set."""

    value: Required[Union[str, float, bool, SequenceNotStr[Union[str, float, bool]]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class AITasksTaskYesNoOnYesUnsetMetadata(TypedDict, total=False):
    field: Required[str]
    """Name of the custom metadata field to remove."""


class AITasksTaskYesNoOnYes(TypedDict, total=False):
    """Actions to execute if the AI answers yes."""

    add_tags: SequenceNotStr[str]
    """Array of tag strings to add to the asset."""

    remove_tags: SequenceNotStr[str]
    """Array of tag strings to remove from the asset."""

    set_metadata: Iterable[AITasksTaskYesNoOnYesSetMetadata]
    """Array of custom metadata field updates."""

    unset_metadata: Iterable[AITasksTaskYesNoOnYesUnsetMetadata]
    """Array of custom metadata fields to remove."""


class AITasksTaskYesNo(TypedDict, total=False):
    instruction: Required[str]
    """The yes/no question for the AI to answer about the image."""

    type: Required[Literal["yes_no"]]
    """Task type that asks a yes/no question and executes actions based on the answer."""

    on_no: AITasksTaskYesNoOnNo
    """Actions to execute if the AI answers no."""

    on_unknown: AITasksTaskYesNoOnUnknown
    """Actions to execute if the AI cannot determine the answer."""

    on_yes: AITasksTaskYesNoOnYes
    """Actions to execute if the AI answers yes."""


AITasksTask: TypeAlias = Union[AITasksTaskSelectTags, AITasksTaskSelectMetadata, AITasksTaskYesNo]


class AITasks(TypedDict, total=False):
    name: Required[Literal["ai-tasks"]]
    """Specifies the AI tasks extension for automated image analysis using AI models."""

    tasks: Required[Iterable[AITasksTask]]
    """Array of task objects defining AI operations to perform on the asset."""


ExtensionConfig: TypeAlias = Union[RemoveBg, AutoTaggingExtension, AIAutoDescription, AITasks]
