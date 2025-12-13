# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Union, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .metadata import Metadata
from .base_webhook_event import BaseWebhookEvent

__all__ = [
    "UploadPreTransformSuccessEvent",
    "UploadPreTransformSuccessEventData",
    "UploadPreTransformSuccessEventDataAITag",
    "UploadPreTransformSuccessEventDataExtensionStatus",
    "UploadPreTransformSuccessEventDataSelectedFieldsSchema",
    "UploadPreTransformSuccessEventDataVersionInfo",
    "UploadPreTransformSuccessEventRequest",
]


class UploadPreTransformSuccessEventDataAITag(BaseModel):
    confidence: Optional[float] = None
    """Confidence score of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    source: Optional[str] = None
    """Array of `AITags` associated with the image.

    If no `AITags` are set, it will be null. These tags can be added using the
    `google-auto-tagging` or `aws-auto-tagging` extensions.
    """


class UploadPreTransformSuccessEventDataExtensionStatus(BaseModel):
    """
    Extension names with their processing status at the time of completion of the request. It could have one of the following status values:

    `success`: The extension has been successfully applied.
    `failed`: The extension has failed and will not be retried.
    `pending`: The extension will finish processing in some time. On completion, the final status (success / failed) will be sent to the `webhookUrl` provided.

    If no extension was requested, then this parameter is not returned.
    """

    ai_auto_description: Optional[Literal["success", "pending", "failed"]] = FieldInfo(
        alias="ai-auto-description", default=None
    )

    aws_auto_tagging: Optional[Literal["success", "pending", "failed"]] = FieldInfo(
        alias="aws-auto-tagging", default=None
    )

    google_auto_tagging: Optional[Literal["success", "pending", "failed"]] = FieldInfo(
        alias="google-auto-tagging", default=None
    )

    remove_bg: Optional[Literal["success", "pending", "failed"]] = FieldInfo(alias="remove-bg", default=None)


class UploadPreTransformSuccessEventDataSelectedFieldsSchema(BaseModel):
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


class UploadPreTransformSuccessEventDataVersionInfo(BaseModel):
    """An object containing the file or file version's `id` (versionId) and `name`."""

    id: Optional[str] = None
    """Unique identifier of the file version."""

    name: Optional[str] = None
    """Name of the file version."""


class UploadPreTransformSuccessEventData(BaseModel):
    """Object containing details of a successful upload."""

    ai_tags: Optional[List[UploadPreTransformSuccessEventDataAITag]] = FieldInfo(alias="AITags", default=None)
    """An array of tags assigned to the uploaded file by auto tagging."""

    audio_codec: Optional[str] = FieldInfo(alias="audioCodec", default=None)
    """The audio codec used in the video (only for video)."""

    bit_rate: Optional[int] = FieldInfo(alias="bitRate", default=None)
    """The bit rate of the video in kbps (only for video)."""

    custom_coordinates: Optional[str] = FieldInfo(alias="customCoordinates", default=None)
    """
    Value of custom coordinates associated with the image in the format
    `x,y,width,height`. If `customCoordinates` are not defined, then it is `null`.
    Send `customCoordinates` in `responseFields` in API request to get the value of
    this field.
    """

    custom_metadata: Optional[Dict[str, object]] = FieldInfo(alias="customMetadata", default=None)
    """A key-value data associated with the asset.

    Use `responseField` in API request to get `customMetadata` in the upload API
    response. Before setting any custom metadata on an asset, you have to create the
    field using custom metadata fields API. Send `customMetadata` in
    `responseFields` in API request to get the value of this field.
    """

    description: Optional[str] = None
    """Optional text to describe the contents of the file.

    Can be set by the user or the ai-auto-description extension.
    """

    duration: Optional[int] = None
    """The duration of the video in seconds (only for video)."""

    embedded_metadata: Optional[Dict[str, object]] = FieldInfo(alias="embeddedMetadata", default=None)
    """Consolidated embedded metadata associated with the file.

    It includes exif, iptc, and xmp data. Send `embeddedMetadata` in
    `responseFields` in API request to get embeddedMetadata in the upload API
    response.
    """

    extension_status: Optional[UploadPreTransformSuccessEventDataExtensionStatus] = FieldInfo(
        alias="extensionStatus", default=None
    )
    """
    Extension names with their processing status at the time of completion of the
    request. It could have one of the following status values:

    `success`: The extension has been successfully applied. `failed`: The extension
    has failed and will not be retried. `pending`: The extension will finish
    processing in some time. On completion, the final status (success / failed) will
    be sent to the `webhookUrl` provided.

    If no extension was requested, then this parameter is not returned.
    """

    file_id: Optional[str] = FieldInfo(alias="fileId", default=None)
    """Unique fileId.

    Store this fileld in your database, as this will be used to perform update
    action on this file.
    """

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)
    """The relative path of the file in the media library e.g.

    `/marketing-assets/new-banner.jpg`.
    """

    file_type: Optional[str] = FieldInfo(alias="fileType", default=None)
    """Type of the uploaded file. Possible values are `image`, `non-image`."""

    height: Optional[float] = None
    """Height of the image in pixels (Only for images)"""

    is_private_file: Optional[bool] = FieldInfo(alias="isPrivateFile", default=None)
    """Is the file marked as private.

    It can be either `true` or `false`. Send `isPrivateFile` in `responseFields` in
    API request to get the value of this field.
    """

    is_published: Optional[bool] = FieldInfo(alias="isPublished", default=None)
    """Is the file published or in draft state.

    It can be either `true` or `false`. Send `isPublished` in `responseFields` in
    API request to get the value of this field.
    """

    metadata: Optional[Metadata] = None
    """Legacy metadata.

    Send `metadata` in `responseFields` in API request to get metadata in the upload
    API response.
    """

    name: Optional[str] = None
    """Name of the asset."""

    selected_fields_schema: Optional[Dict[str, UploadPreTransformSuccessEventDataSelectedFieldsSchema]] = FieldInfo(
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
    """Size of the image file in Bytes."""

    tags: Optional[List[str]] = None
    """The array of tags associated with the asset.

    If no tags are set, it will be `null`. Send `tags` in `responseFields` in API
    request to get the value of this field.
    """

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)
    """In the case of an image, a small thumbnail URL."""

    url: Optional[str] = None
    """A publicly accessible URL of the file."""

    version_info: Optional[UploadPreTransformSuccessEventDataVersionInfo] = FieldInfo(alias="versionInfo", default=None)
    """An object containing the file or file version's `id` (versionId) and `name`."""

    video_codec: Optional[str] = FieldInfo(alias="videoCodec", default=None)
    """The video codec used in the video (only for video)."""

    width: Optional[float] = None
    """Width of the image in pixels (Only for Images)"""


class UploadPreTransformSuccessEventRequest(BaseModel):
    transformation: str
    """The requested pre-transformation string."""

    x_request_id: str
    """Unique identifier for the originating request."""


class UploadPreTransformSuccessEvent(BaseWebhookEvent):
    """Triggered when a pre-transformation completes successfully.

    The file has been processed with the requested transformation and is now available in the Media Library.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: UploadPreTransformSuccessEventData
    """Object containing details of a successful upload."""

    request: UploadPreTransformSuccessEventRequest

    type: Literal["upload.pre-transform.success"]  # type: ignore
