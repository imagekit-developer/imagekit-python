# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional

from pydantic import Field as FieldInfo

from .src_options import SrcOptions

__all__ = ["GetImageAttributesOptions"]


class GetImageAttributesOptions(SrcOptions):
    """
    Options for generating responsive image attributes including `src`, `srcSet`, and `sizes` for HTML `<img>` elements.
    This schema extends `SrcOptions` to add support for responsive image generation with breakpoints.
    """

    device_breakpoints: Optional[List[float]] = FieldInfo(alias="deviceBreakpoints", default=None)
    """
    Custom list of **device-width breakpoints** in pixels. These define common
    screen widths for responsive image generation.

    Defaults to `[640, 750, 828, 1080, 1200, 1920, 2048, 3840]`. Sorted
    automatically.
    """

    image_breakpoints: Optional[List[float]] = FieldInfo(alias="imageBreakpoints", default=None)
    """
    Custom list of **image-specific breakpoints** in pixels. Useful for generating
    small variants (e.g., placeholders or thumbnails).

    Merged with `deviceBreakpoints` before calculating `srcSet`. Defaults to
    `[16, 32, 48, 64, 96, 128, 256, 384]`. Sorted automatically.
    """

    sizes: Optional[str] = None
    """
    The value for the HTML `sizes` attribute (e.g., `"100vw"` or
    `"(min-width:768px) 50vw, 100vw"`).

    - If it includes one or more `vw` units, breakpoints smaller than the
      corresponding percentage of the smallest device width are excluded.
    - If it contains no `vw` units, the full breakpoint list is used.

    Enables a width-based strategy and generates `w` descriptors in `srcSet`.
    """

    width: Optional[float] = None
    """
    The intended display width of the image in pixels, used **only when the `sizes`
    attribute is not provided**.

    Triggers a DPR-based strategy (1x and 2x variants) and generates `x` descriptors
    in `srcSet`.

    Ignored if `sizes` is present.
    """
