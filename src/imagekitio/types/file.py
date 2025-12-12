# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["File", "AITag", "SelectedFieldsSchema", "VersionInfo"]


class AITag(BaseModel):
    confidence: Optional[float] = None
    """Confidence score of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    source: Optional[str] = None
    """Source of the tag.

    Possible values are `google-auto-tagging` and `aws-auto-tagging`.
    """


class SelectedFieldsSchema(BaseModel):
    type: Literal["Text", "Textarea", "Number", "Date", "Boolean", "SingleSelect", "MultiSelect"]
    """Type of the custom metadata field."""

    default_value: Union[str, float, bool, List[Union[str, float, bool]], None] = FieldInfo(
        alias="defaultValue", default=None
    )
    """The default value for this custom metadata field.

    The value should match the `type` of custom metadata field.
    """

    is_value_required: Optional[bool] = FieldInfo(alias="isValueRequired", default=None)
    """Specifies if the custom metadata field is required or not."""

    max_length: Optional[float] = FieldInfo(alias="maxLength", default=None)
    """Maximum length of string. Only set if `type` is set to `Text` or `Textarea`."""

    max_value: Union[str, float, None] = FieldInfo(alias="maxValue", default=None)
    """Maximum value of the field.

    Only set if field type is `Date` or `Number`. For `Date` type field, the value
    will be in ISO8601 string format. For `Number` type field, it will be a numeric
    value.
    """

    min_length: Optional[float] = FieldInfo(alias="minLength", default=None)
    """Minimum length of string. Only set if `type` is set to `Text` or `Textarea`."""

    min_value: Union[str, float, None] = FieldInfo(alias="minValue", default=None)
    """Minimum value of the field.

    Only set if field type is `Date` or `Number`. For `Date` type field, the value
    will be in ISO8601 string format. For `Number` type field, it will be a numeric
    value.
    """

    read_only: Optional[bool] = FieldInfo(alias="readOnly", default=None)
    """Indicates whether the custom metadata field is read only.

    A read only field cannot be modified after being set. This field is configurable
    only via the **Path policy** feature.
    """

    select_options: Optional[List[Union[str, float, bool]]] = FieldInfo(alias="selectOptions", default=None)
    """An array of allowed values when field type is `SingleSelect` or `MultiSelect`."""

    select_options_truncated: Optional[bool] = FieldInfo(alias="selectOptionsTruncated", default=None)
    """Specifies if the selectOptions array is truncated.

    It is truncated when number of options are > 100.
    """


class VersionInfo(BaseModel):
    """An object with details of the file version."""

    id: Optional[str] = None
    """Unique identifier of the file version."""

    name: Optional[str] = None
    """Name of the file version."""


class File(BaseModel):
    """Object containing details of a file or file version."""

    ai_tags: Optional[List[AITag]] = FieldInfo(alias="AITags", default=None)
    """An array of tags assigned to the file by auto tagging."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Date and time when the file was uploaded.

    The date and time is in ISO8601 format.
    """

    custom_coordinates: Optional[str] = FieldInfo(alias="customCoordinates", default=None)
    """An string with custom coordinates of the file."""

    custom_metadata: Optional[Dict[str, object]] = FieldInfo(alias="customMetadata", default=None)
    """An object with custom metadata for the file."""

    description: Optional[str] = None
    """Optional text to describe the contents of the file.

    Can be set by the user or the ai-auto-description extension.
    """

    file_id: Optional[str] = FieldInfo(alias="fileId", default=None)
    """Unique identifier of the asset."""

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)
    """Path of the file.

    This is the path you would use in the URL to access the file. For example, if
    the file is at the root of the media library, the path will be `/file.jpg`. If
    the file is inside a folder named `images`, the path will be `/images/file.jpg`.
    """

    file_type: Optional[str] = FieldInfo(alias="fileType", default=None)
    """Type of the file. Possible values are `image`, `non-image`."""

    has_alpha: Optional[bool] = FieldInfo(alias="hasAlpha", default=None)
    """Specifies if the image has an alpha channel."""

    height: Optional[float] = None
    """Height of the file."""

    is_private_file: Optional[bool] = FieldInfo(alias="isPrivateFile", default=None)
    """Specifies if the file is private or not."""

    is_published: Optional[bool] = FieldInfo(alias="isPublished", default=None)
    """Specifies if the file is published or not."""

    mime: Optional[str] = None
    """MIME type of the file."""

    name: Optional[str] = None
    """Name of the asset."""

    selected_fields_schema: Optional[Dict[str, SelectedFieldsSchema]] = FieldInfo(
        alias="selectedFieldsSchema", default=None
    )
    """
    This field is included in the response only if the Path policy feature is
    available in the plan. It contains schema definitions for the custom metadata
    fields selected for the specified file path. Field selection can only be done
    when the Path policy feature is enabled.

    Keys are the names of the custom metadata fields; the value object has details
    about the custom metadata schema.
    """

    size: Optional[float] = None
    """Size of the file in bytes."""

    tags: Optional[List[str]] = None
    """An array of tags assigned to the file.

    Tags are used to search files in the media library.
    """

    thumbnail: Optional[str] = None
    """URL of the thumbnail image.

    This URL is used to access the thumbnail image of the file in the media library.
    """

    type: Optional[Literal["file", "file-version"]] = None
    """Type of the asset."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Date and time when the file was last updated.

    The date and time is in ISO8601 format.
    """

    url: Optional[str] = None
    """URL of the file."""

    version_info: Optional[VersionInfo] = FieldInfo(alias="versionInfo", default=None)
    """An object with details of the file version."""

    width: Optional[float] = None
    """Width of the file."""
