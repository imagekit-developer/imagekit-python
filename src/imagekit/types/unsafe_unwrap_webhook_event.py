# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .video_transformation_error_event import VideoTransformationErrorEvent
from .video_transformation_ready_event import VideoTransformationReadyEvent
from .video_transformation_accepted_event import VideoTransformationAcceptedEvent

__all__ = ["UnsafeUnwrapWebhookEvent"]

UnsafeUnwrapWebhookEvent: TypeAlias = Union[
    VideoTransformationAcceptedEvent, VideoTransformationReadyEvent, VideoTransformationErrorEvent
]
