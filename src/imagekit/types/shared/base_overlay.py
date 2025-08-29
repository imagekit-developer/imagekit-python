# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .overlay_timing import OverlayTiming
from .overlay_position import OverlayPosition

__all__ = ["BaseOverlay"]


class BaseOverlay(BaseModel):
    position: Optional[OverlayPosition] = None

    timing: Optional[OverlayTiming] = None

    __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
