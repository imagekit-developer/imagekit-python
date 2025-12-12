# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required

from .base_overlay import BaseOverlay
from .subtitle_overlay_transformation import SubtitleOverlayTransformation

__all__ = ["SubtitleOverlay"]


class SubtitleOverlay(BaseOverlay, total=False):
    input: Required[str]
    """Specifies the relative path to the subtitle file used as an overlay."""

    type: Required[Literal["subtitle"]]

    encoding: Literal["auto", "plain", "base64"]
    """
    The input path can be included in the layer as either `i-{input}` or
    `ie-{base64_encoded_input}`. By default, the SDK determines the appropriate
    format automatically. To always use base64 encoding (`ie-{base64}`), set this
    parameter to `base64`. To always use plain text (`i-{input}`), set it to
    `plain`.
    """

    transformation: Iterable[SubtitleOverlayTransformation]
    """Control styling of the subtitle.

    See
    [Styling subtitles](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer).
    """
