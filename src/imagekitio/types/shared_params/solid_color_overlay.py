# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, Required

from .base_overlay import BaseOverlay
from .solid_color_overlay_transformation import SolidColorOverlayTransformation

__all__ = ["SolidColorOverlay"]


class SolidColorOverlay(BaseOverlay, total=False):
    color: Required[str]
    """
    Specifies the color of the block using an RGB hex code (e.g., `FF0000`), an RGBA
    code (e.g., `FFAABB50`), or a color name (e.g., `red`). If an 8-character value
    is provided, the last two characters represent the opacity level (from `00` for
    0.00 to `99` for 0.99).
    """

    type: Required[Literal["solidColor"]]

    transformation: Iterable[SolidColorOverlayTransformation]
    """Control width and height of the solid color overlay.

    Supported transformations depend on the base/parent asset. See overlays on
    [Images](https://imagekit.io/docs/add-overlays-on-images#apply-transformation-on-solid-color-overlay)
    and
    [Videos](https://imagekit.io/docs/add-overlays-on-videos#apply-transformations-on-solid-color-block-overlay).
    """
