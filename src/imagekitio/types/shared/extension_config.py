# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal, Annotated, TypeAlias

from pydantic import Field as FieldInfo

from ..._utils import PropertyInfo
from ..._models import BaseModel

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


class RemoveBgOptions(BaseModel):
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


class RemoveBg(BaseModel):
    name: Literal["remove-bg"]
    """Specifies the background removal extension."""

    options: Optional[RemoveBgOptions] = None


class AutoTaggingExtension(BaseModel):
    max_tags: int = FieldInfo(alias="maxTags")
    """Maximum number of tags to attach to the asset."""

    min_confidence: int = FieldInfo(alias="minConfidence")
    """Minimum confidence level for tags to be considered valid."""

    name: Literal["google-auto-tagging", "aws-auto-tagging"]
    """Specifies the auto-tagging extension used."""


class AIAutoDescription(BaseModel):
    name: Literal["ai-auto-description"]
    """Specifies the auto description extension."""


class AITasksTaskSelectTags(BaseModel):
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


class AITasksTaskSelectMetadata(BaseModel):
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


class AITasksTaskYesNoOnNoSetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to set."""

    value: Union[str, float, bool, List[Union[str, float, bool]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class AITasksTaskYesNoOnNoUnsetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to remove."""


class AITasksTaskYesNoOnNo(BaseModel):
    """Actions to execute if the AI answers no."""

    add_tags: Optional[List[str]] = None
    """Array of tag strings to add to the asset."""

    remove_tags: Optional[List[str]] = None
    """Array of tag strings to remove from the asset."""

    set_metadata: Optional[List[AITasksTaskYesNoOnNoSetMetadata]] = None
    """Array of custom metadata field updates."""

    unset_metadata: Optional[List[AITasksTaskYesNoOnNoUnsetMetadata]] = None
    """Array of custom metadata fields to remove."""


class AITasksTaskYesNoOnUnknownSetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to set."""

    value: Union[str, float, bool, List[Union[str, float, bool]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class AITasksTaskYesNoOnUnknownUnsetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to remove."""


class AITasksTaskYesNoOnUnknown(BaseModel):
    """Actions to execute if the AI cannot determine the answer."""

    add_tags: Optional[List[str]] = None
    """Array of tag strings to add to the asset."""

    remove_tags: Optional[List[str]] = None
    """Array of tag strings to remove from the asset."""

    set_metadata: Optional[List[AITasksTaskYesNoOnUnknownSetMetadata]] = None
    """Array of custom metadata field updates."""

    unset_metadata: Optional[List[AITasksTaskYesNoOnUnknownUnsetMetadata]] = None
    """Array of custom metadata fields to remove."""


class AITasksTaskYesNoOnYesSetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to set."""

    value: Union[str, float, bool, List[Union[str, float, bool]]]
    """Value to set for the custom metadata field.

    The value type should match the custom metadata field type.
    """


class AITasksTaskYesNoOnYesUnsetMetadata(BaseModel):
    field: str
    """Name of the custom metadata field to remove."""


class AITasksTaskYesNoOnYes(BaseModel):
    """Actions to execute if the AI answers yes."""

    add_tags: Optional[List[str]] = None
    """Array of tag strings to add to the asset."""

    remove_tags: Optional[List[str]] = None
    """Array of tag strings to remove from the asset."""

    set_metadata: Optional[List[AITasksTaskYesNoOnYesSetMetadata]] = None
    """Array of custom metadata field updates."""

    unset_metadata: Optional[List[AITasksTaskYesNoOnYesUnsetMetadata]] = None
    """Array of custom metadata fields to remove."""


class AITasksTaskYesNo(BaseModel):
    instruction: str
    """The yes/no question for the AI to answer about the image."""

    type: Literal["yes_no"]
    """Task type that asks a yes/no question and executes actions based on the answer."""

    on_no: Optional[AITasksTaskYesNoOnNo] = None
    """Actions to execute if the AI answers no."""

    on_unknown: Optional[AITasksTaskYesNoOnUnknown] = None
    """Actions to execute if the AI cannot determine the answer."""

    on_yes: Optional[AITasksTaskYesNoOnYes] = None
    """Actions to execute if the AI answers yes."""


AITasksTask: TypeAlias = Annotated[
    Union[AITasksTaskSelectTags, AITasksTaskSelectMetadata, AITasksTaskYesNo], PropertyInfo(discriminator="type")
]


class AITasks(BaseModel):
    name: Literal["ai-tasks"]
    """Specifies the AI tasks extension for automated image analysis using AI models."""

    tasks: List[AITasksTask]
    """Array of task objects defining AI operations to perform on the asset."""


ExtensionConfig: TypeAlias = Annotated[
    Union[RemoveBg, AutoTaggingExtension, AIAutoDescription, AITasks], PropertyInfo(discriminator="name")
]
