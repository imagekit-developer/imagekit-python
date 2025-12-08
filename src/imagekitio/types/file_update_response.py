# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .file import File
from .._models import BaseModel

__all__ = ["FileUpdateResponse", "FileUpdateResponseExtensionStatus"]


class FileUpdateResponseExtensionStatus(BaseModel):
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


class FileUpdateResponse(File):
    """Object containing details of a file or file version."""

    extension_status: Optional[FileUpdateResponseExtensionStatus] = FieldInfo(alias="extensionStatus", default=None)
