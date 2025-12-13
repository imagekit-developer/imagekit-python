# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required

from .base_overlay import BaseOverlay

__all__ = ["VideoOverlay"]


class VideoOverlay(BaseOverlay, total=False):
    input: Required[str]
    """Specifies the relative path to the video used as an overlay."""

    type: Required[Literal["video"]]

    encoding: Literal["auto", "plain", "base64"]
    """
    The input path can be included in the layer as either `i-{input}` or
    `ie-{base64_encoded_input}`. By default, the SDK determines the appropriate
    format automatically. To always use base64 encoding (`ie-{base64}`), set this
    parameter to `base64`. To always use plain text (`i-{input}`), set it to
    `plain`.
    """

    transformation: Iterable["Transformation"]
    """Array of transformation to be applied to the overlay video.

    Except `streamingResolutions`, all other video transformations are supported.
    See [Video transformations](https://imagekit.io/docs/video-transformation).
    """


from .transformation import Transformation
