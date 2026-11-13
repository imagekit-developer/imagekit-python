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
    """Values the folder had before this update.

    Present only when the folder was renamed or its parent folder was renamed.
    """

    folder_path: Optional[str] = FieldInfo(alias="folderPath", default=None)
    """Path of the folder before it was renamed."""


class FolderUpdateEvent(BaseWebhookEvent):
    """
    Triggered when a folder is updated, for example when its custom metadata changes or it is renamed. Renaming a folder sends one event per folder in the tree, each with its new `folderPath` in `data` and its old `folderPath` in `previous`.
    """

    created_at: datetime
    """Timestamp of when the event occurred in ISO8601 format."""

    data: Folder

    type: Literal["folder.updated"]  # type: ignore
    """Type of the webhook event."""

    previous: Optional[FolderUpdateEventPrevious] = None
    """Values the folder had before this update.

    Present only when the folder was renamed or its parent folder was renamed.
    """
