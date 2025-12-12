# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .base_overlay import BaseOverlay
from .subtitle_overlay_transformation import SubtitleOverlayTransformation

__all__ = ["SubtitleOverlay"]


class SubtitleOverlay(BaseOverlay):
    input: str
    """Specifies the relative path to the subtitle file used as an overlay."""

    type: Literal["subtitle"]

    encoding: Optional[Literal["auto", "plain", "base64"]] = None
    """
    The input path can be included in the layer as either `i-{input}` or
    `ie-{base64_encoded_input}`. By default, the SDK determines the appropriate
    format automatically. To always use base64 encoding (`ie-{base64}`), set this
    parameter to `base64`. To always use plain text (`i-{input}`), set it to
    `plain`.
    """

    transformation: Optional[List[SubtitleOverlayTransformation]] = None
    """Control styling of the subtitle.

    See
    [Styling subtitles](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer).
    """
