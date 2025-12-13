# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

from .overlay_timing import OverlayTiming
from .overlay_position import OverlayPosition

__all__ = ["BaseOverlay"]


class BaseOverlay(TypedDict, total=False):
    position: OverlayPosition

    timing: OverlayTiming
