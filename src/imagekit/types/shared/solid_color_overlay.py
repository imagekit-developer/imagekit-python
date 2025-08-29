# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal, override

from pydantic import Field as FieldInfo

from .base_overlay import BaseOverlay
from .solid_color_overlay_transformation import SolidColorOverlayTransformation

__all__ = ["SolidColorOverlay"]


class SolidColorOverlay(BaseOverlay):
    color: str
    """
    Specifies the color of the block using an RGB hex code (e.g., `FF0000`), an RGBA
    code (e.g., `FFAABB50`), or a color name (e.g., `red`). If an 8-character value
    is provided, the last two characters represent the opacity level (from `00` for
    0.00 to `99` for 0.99).
    """

    type: Literal["solidColor"]

    transformation: Optional[List[SolidColorOverlayTransformation]] = None
    """Control width and height of the solid color overlay.

    Supported transformations depend on the base/parent asset.
    """

    __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        @override
        def __getattr__(self, attr: str) -> str: ...
