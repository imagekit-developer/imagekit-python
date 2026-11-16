# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .folder import Folder
from .._models import BaseModel
from .base_webhook_event import BaseWebhookEvent

__all__ = ["FolderUpdateEvent", "FolderUpdateEventPrevious"]


class FolderUpdateEventPrevious(BaseModel):
    """Present only when the folder or one of its parent folders was renamed.

    Contains the folder's path before the rename.
    """

    folder_path: str = FieldInfo(alias="folderPath")
    """Path of the folder before it was renamed."""


class FolderUpdateEvent(BaseWebhookEvent):
    """
    Triggered when a folder is updated, for example when its custom metadata changes or it is renamed. Renaming a folder sends one event per folder in the tree. In each of these events, `data.folderPath` is the folder's new path and `previous.folderPath` is its path before the rename.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: Folder

    type: Literal["folder.updated"]  # type: ignore
    """Type of the webhook event."""

    previous: Optional[FolderUpdateEventPrevious] = None
    """Present only when the folder or one of its parent folders was renamed.

    Contains the folder's path before the rename.
    """
