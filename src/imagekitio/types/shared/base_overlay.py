# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from ..._models import BaseModel
from .overlay_timing import OverlayTiming
from .overlay_position import OverlayPosition

__all__ = ["BaseOverlay"]


class BaseOverlay(BaseModel):
    position: Optional[OverlayPosition] = None

    timing: Optional[OverlayTiming] = None
