# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from .._utils import PropertyInfo

__all__ = [
    "FileUpdateParams",
    "UpdateFileDetails",
    "UpdateFileDetailsExtension",
    "UpdateFileDetailsExtensionRemovedotBgExtension",
    "UpdateFileDetailsExtensionRemovedotBgExtensionOptions",
    "UpdateFileDetailsExtensionAutoTaggingExtension",
    "UpdateFileDetailsExtensionAutoDescriptionExtension",
    "ChangePublicationStatus",
    "ChangePublicationStatusPublish",
]


class UpdateFileDetails(TypedDict, total=False):
    custom_coordinates: Annotated[Optional[str], PropertyInfo(alias="customCoordinates")]
    """Define an important area in the image in the format `x,y,width,height` e.g.

    `10,10,100,100`. Send `null` to unset this value.
    """

    custom_metadata: Annotated[object, PropertyInfo(alias="customMetadata")]
    """A key-value data to be associated with the asset.

    To unset a key, send `null` value for that key. Before setting any custom
    metadata on an asset you have to create the field using custom metadata fields
    API.
    """

    description: str
    """Optional text to describe the contents of the file."""

    extensions: Iterable[UpdateFileDetailsExtension]
    """Array of extensions to be applied to the asset.

    Each extension can be configured with specific parameters based on the extension
    type.
    """

    remove_ai_tags: Annotated[Union[List[str], Literal["all"]], PropertyInfo(alias="removeAITags")]
    """An array of AITags associated with the file that you want to remove, e.g.

    `["car", "vehicle", "motorsports"]`.

    If you want to remove all AITags associated with the file, send a string -
    "all".

    Note: The remove operation for `AITags` executes before any of the `extensions`
    are processed.
    """

    tags: Optional[List[str]]
    """An array of tags associated with the file, such as `["tag1", "tag2"]`.

    Send `null` to unset all tags associated with the file.
    """

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """
    The final status of extensions after they have completed execution will be
    delivered to this endpoint as a POST request.
    [Learn more](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#webhook-payload-structure)
    about the webhook payload structure.
    """


class UpdateFileDetailsExtensionRemovedotBgExtensionOptions(TypedDict, total=False):
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


class UpdateFileDetailsExtensionRemovedotBgExtension(TypedDict, total=False):
    name: Required[Literal["remove-bg"]]
    """Specifies the background removal extension."""

    options: UpdateFileDetailsExtensionRemovedotBgExtensionOptions


class UpdateFileDetailsExtensionAutoTaggingExtension(TypedDict, total=False):
    max_tags: Required[Annotated[int, PropertyInfo(alias="maxTags")]]
    """Maximum number of tags to attach to the asset."""

    min_confidence: Required[Annotated[int, PropertyInfo(alias="minConfidence")]]
    """Minimum confidence level for tags to be considered valid."""

    name: Required[Literal["google-auto-tagging", "aws-auto-tagging"]]
    """Specifies the auto-tagging extension used."""


class UpdateFileDetailsExtensionAutoDescriptionExtension(TypedDict, total=False):
    name: Required[Literal["ai-auto-description"]]
    """Specifies the auto description extension."""


UpdateFileDetailsExtension: TypeAlias = Union[
    UpdateFileDetailsExtensionRemovedotBgExtension,
    UpdateFileDetailsExtensionAutoTaggingExtension,
    UpdateFileDetailsExtensionAutoDescriptionExtension,
]


class ChangePublicationStatus(TypedDict, total=False):
    publish: ChangePublicationStatusPublish
    """Configure the publication status of a file and its versions."""


class ChangePublicationStatusPublish(TypedDict, total=False):
    is_published: Required[Annotated[bool, PropertyInfo(alias="isPublished")]]
    """Set to `true` to publish the file. Set to `false` to unpublish the file."""

    include_file_versions: Annotated[bool, PropertyInfo(alias="includeFileVersions")]
    """Set to `true` to publish/unpublish all versions of the file.

    Set to `false` to publish/unpublish only the current version of the file.
    """


FileUpdateParams: TypeAlias = Union[UpdateFileDetails, ChangePublicationStatus]
