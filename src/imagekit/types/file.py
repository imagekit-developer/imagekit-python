# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["File", "AITag", "VersionInfo"]


class AITag(BaseModel):
    confidence: Optional[float] = None
    """Confidence score of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    source: Optional[str] = None
    """Source of the tag.

    Possible values are `google-auto-tagging` and `aws-auto-tagging`.
    """


class VersionInfo(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the file version."""

    name: Optional[str] = None
    """Name of the file version."""


class File(BaseModel):
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
