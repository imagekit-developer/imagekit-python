# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["OverlayPosition"]


class OverlayPosition(TypedDict, total=False):
    focus: Literal["center", "top", "left", "bottom", "right", "top_left", "top_right", "bottom_left", "bottom_right"]
    """
    Specifies the position of the overlay relative to the parent image or video.
    Maps to `lfo` in the URL.
    """

    x: Union[float, str]
    """
    Specifies the x-coordinate of the top-left corner of the base asset where the
    overlay's top-left corner will be positioned. It also accepts arithmetic
    expressions such as `bw_mul_0.4` or `bw_sub_cw`. Maps to `lx` in the URL. Learn
    about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """

    y: Union[float, str]
    """
    Specifies the y-coordinate of the top-left corner of the base asset where the
    overlay's top-left corner will be positioned. It also accepts arithmetic
    expressions such as `bh_mul_0.4` or `bh_sub_ch`. Maps to `ly` in the URL. Learn
    about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
