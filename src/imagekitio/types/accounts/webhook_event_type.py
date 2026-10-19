# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal, TypeAlias

__all__ = ["WebhookEventType"]

WebhookEventType: TypeAlias = Literal[
    "video.transformation.accepted",
    "video.transformation.ready",
    "video.transformation.error",
    "upload.pre-transform.success",
    "upload.pre-transform.error",
    "upload.post-transform.success",
    "upload.post-transform.error",
    "file.created",
    "file.updated",
    "file.deleted",
    "file-version.created",
    "file-version.deleted",
    "folder.created",
    "folder.updated",
    "folder.deleted",
]
