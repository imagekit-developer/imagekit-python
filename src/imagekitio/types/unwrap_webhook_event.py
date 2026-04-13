# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import Annotated, TypeAlias

from .._utils import PropertyInfo
from .file_create_event import FileCreateEvent
from .file_delete_event import FileDeleteEvent
from .file_update_event import FileUpdateEvent
from .file_version_create_event import FileVersionCreateEvent
from .file_version_delete_event import FileVersionDeleteEvent
from .upload_pre_transform_error_event import UploadPreTransformErrorEvent
from .video_transformation_error_event import VideoTransformationErrorEvent
from .video_transformation_ready_event import VideoTransformationReadyEvent
from .upload_post_transform_error_event import UploadPostTransformErrorEvent
from .upload_pre_transform_success_event import UploadPreTransformSuccessEvent
from .upload_post_transform_success_event import UploadPostTransformSuccessEvent
from .video_transformation_accepted_event import VideoTransformationAcceptedEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Annotated[
    Union[
        VideoTransformationAcceptedEvent,
        VideoTransformationReadyEvent,
        VideoTransformationErrorEvent,
        UploadPreTransformSuccessEvent,
        UploadPreTransformErrorEvent,
        UploadPostTransformSuccessEvent,
        UploadPostTransformErrorEvent,
        FileCreateEvent,
        FileUpdateEvent,
        FileDeleteEvent,
        FileVersionCreateEvent,
        FileVersionDeleteEvent,
    ],
    PropertyInfo(discriminator="type"),
]
