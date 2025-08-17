# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .shared.gps import Gps
from .shared.thumbnail import Thumbnail
from .shared.exif_image import ExifImage
from .shared.exif_details import ExifDetails
from .shared.interoperability import Interoperability

__all__ = ["FileUploadResponse", "AITag", "ExtensionStatus", "Metadata", "MetadataExif", "VersionInfo"]


class AITag(BaseModel):
    confidence: Optional[float] = None
    """Confidence score of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    source: Optional[str] = None
    """Array of `AITags` associated with the image.

    If no `AITags` are set, it will be null. These tags can be added using the
    `google-auto-tagging` or `aws-auto-tagging` extensions.
    """


class ExtensionStatus(BaseModel):
    aws_auto_tagging: Optional[Literal["success", "pending", "failed"]] = FieldInfo(
        alias="aws-auto-tagging", default=None
    )

    google_auto_tagging: Optional[Literal["success", "pending", "failed"]] = FieldInfo(
        alias="google-auto-tagging", default=None
    )

    remove_bg: Optional[Literal["success", "pending", "failed"]] = FieldInfo(alias="remove-bg", default=None)


class MetadataExif(BaseModel):
    exif: Optional[ExifDetails] = None
    """Object containing Exif details."""

    gps: Optional[Gps] = None
    """Object containing GPS information."""

    image: Optional[ExifImage] = None
    """Object containing EXIF image information."""

    interoperability: Optional[Interoperability] = None
    """JSON object."""

    makernote: Optional[Dict[str, object]] = None

    thumbnail: Optional[Thumbnail] = None
    """Object containing Thumbnail information."""


class Metadata(BaseModel):
    audio_codec: Optional[str] = FieldInfo(alias="audioCodec", default=None)
    """The audio codec used in the video (only for video)."""

    bit_rate: Optional[int] = FieldInfo(alias="bitRate", default=None)
    """The bit rate of the video in kbps (only for video)."""

    density: Optional[int] = None
    """The density of the image in DPI."""

    duration: Optional[int] = None
    """The duration of the video in seconds (only for video)."""

    exif: Optional[MetadataExif] = None

    format: Optional[str] = None
    """The format of the file (e.g., 'jpg', 'mp4')."""

    has_color_profile: Optional[bool] = FieldInfo(alias="hasColorProfile", default=None)
    """Indicates if the image has a color profile."""

    has_transparency: Optional[bool] = FieldInfo(alias="hasTransparency", default=None)
    """Indicates if the image contains transparent areas."""

    height: Optional[int] = None
    """The height of the image or video in pixels."""

    p_hash: Optional[str] = FieldInfo(alias="pHash", default=None)
    """Perceptual hash of the image."""

    quality: Optional[int] = None
    """The quality indicator of the image."""

    size: Optional[int] = None
    """The file size in bytes."""

    video_codec: Optional[str] = FieldInfo(alias="videoCodec", default=None)
    """The video codec used in the video (only for video)."""

    width: Optional[int] = None
    """The width of the image or video in pixels."""


class VersionInfo(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the file version."""

    name: Optional[str] = None
    """Name of the file version."""


class FileUploadResponse(BaseModel):
    ai_tags: Optional[List[AITag]] = FieldInfo(alias="AITags", default=None)
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

    duration: Optional[int] = None
    """The duration of the video in seconds (only for video)."""

    embedded_metadata: Optional[Dict[str, object]] = FieldInfo(alias="embeddedMetadata", default=None)
    """Consolidated embedded metadata associated with the file.

    It includes exif, iptc, and xmp data. Send `embeddedMetadata` in
    `responseFields` in API request to get embeddedMetadata in the upload API
    response.
    """

    extension_status: Optional[ExtensionStatus] = FieldInfo(alias="extensionStatus", default=None)
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

    version_info: Optional[VersionInfo] = FieldInfo(alias="versionInfo", default=None)
    """An object containing the file or file version's `id` (versionId) and `name`."""

    video_codec: Optional[str] = FieldInfo(alias="videoCodec", default=None)
    """The video codec used in the video (only for video)."""

    width: Optional[float] = None
    """Width of the image in pixels (Only for Images)"""
