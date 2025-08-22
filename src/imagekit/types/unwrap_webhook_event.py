# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .video_transformation_error_webhook_event import VideoTransformationErrorWebhookEvent
from .video_transformation_ready_webhook_event import VideoTransformationReadyWebhookEvent
from .video_transformation_accepted_webhook_event import VideoTransformationAcceptedWebhookEvent

__all__ = ["UnwrapWebhookEvent"]

UnwrapWebhookEvent: TypeAlias = Union[
    VideoTransformationAcceptedWebhookEvent, VideoTransformationReadyWebhookEvent, VideoTransformationErrorWebhookEvent
]
