# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["OverlayPosition"]


class OverlayPosition(BaseModel):
    focus: Optional[
        Literal["center", "top", "left", "bottom", "right", "top_left", "top_right", "bottom_left", "bottom_right"]
    ] = None
    """
    Specifies the position of the overlay relative to the parent image or video.
    Maps to `lfo` in the URL.
    """

    x: Union[float, str, None] = None
    """
    Specifies the x-coordinate of the top-left corner of the base asset where the
    overlay's top-left corner will be positioned. It also accepts arithmetic
    expressions such as `bw_mul_0.4` or `bw_sub_cw`. Maps to `lx` in the URL. Learn
    about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """

    y: Union[float, str, None] = None
    """
    Specifies the y-coordinate of the top-left corner of the base asset where the
    overlay's top-left corner will be positioned. It also accepts arithmetic
    expressions such as `bh_mul_0.4` or `bh_sub_ch`. Maps to `ly` in the URL. Learn
    about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
