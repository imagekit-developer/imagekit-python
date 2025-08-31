# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .video_transformation_error_event import VideoTransformationErrorEvent
from .video_transformation_ready_event import VideoTransformationReadyEvent
from .video_transformation_accepted_event import VideoTransformationAcceptedEvent
from .upload_pre_transform_error_webhook_event import UploadPreTransformErrorWebhookEvent
from .upload_post_transform_error_webhook_event import UploadPostTransformErrorWebhookEvent
from .upload_pre_transform_success_webhook_event import UploadPreTransformSuccessWebhookEvent
from .upload_post_transform_success_webhook_event import UploadPostTransformSuccessWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Union[
    VideoTransformationAcceptedEvent,
    VideoTransformationReadyEvent,
    VideoTransformationErrorEvent,
    UploadPreTransformSuccessWebhookEvent,
    UploadPreTransformErrorWebhookEvent,
    UploadPostTransformSuccessWebhookEvent,
    UploadPostTransformErrorWebhookEvent,
]
