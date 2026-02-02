# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Folder"]


class Folder(BaseModel):
    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """Date and time when the folder was created.

    The date and time is in ISO8601 format.
    """

    custom_metadata: Optional[Dict[str, object]] = FieldInfo(alias="customMetadata", default=None)
    """An object with custom metadata for the folder.

    Returns empty object if no custom metadata is set.
    """

    folder_id: Optional[str] = FieldInfo(alias="folderId", default=None)
    """Unique identifier of the asset."""

    folder_path: Optional[str] = FieldInfo(alias="folderPath", default=None)
    """Path of the folder.

    This is the path you would use in the URL to access the folder. For example, if
    the folder is at the root of the media library, the path will be /folder. If the
    folder is inside another folder named images, the path will be /images/folder.
    """

    name: Optional[str] = None
    """Name of the asset."""

    type: Optional[Literal["folder"]] = None
    """Type of the asset."""

    updated_at: Optional[datetime] = FieldInfo(alias="updatedAt", default=None)
    """Date and time when the folder was last updated.

    The date and time is in ISO8601 format.
    """
