# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OverlayPosition"]


class OverlayPosition(BaseModel):
    anchor_point: Optional[
        Literal["top", "left", "right", "bottom", "top_left", "top_right", "bottom_left", "bottom_right", "center"]
    ] = FieldInfo(alias="anchorPoint", default=None)
    """
    Sets the anchor point on the base asset from which the overlay offset is
    calculated. The default value is `top_left`. Maps to `lap` in the URL. Can only
    be used with one or more of `x`, `y`, `xCenter`, or `yCenter`.
    """

    focus: Optional[
        Literal["center", "top", "left", "bottom", "right", "top_left", "top_right", "bottom_left", "bottom_right"]
    ] = None
    """
    Specifies the position of the overlay relative to the parent image or video. If
    one or more of `x`, `y`, `xCenter`, or `yCenter` parameters are specified, this
    parameter is ignored. Maps to `lfo` in the URL.
    """

    x: Union[float, str, None] = None
    """
    Specifies the x-coordinate of the top-left corner of the base asset where the
    overlay's top-left corner will be positioned. It also accepts arithmetic
    expressions such as `bw_mul_0.4` or `bw_sub_cw`. Maps to `lx` in the URL. Learn
    about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """

    x_center: Union[float, str, None] = FieldInfo(alias="xCenter", default=None)
    """
    Specifies the x-coordinate on the base asset where the overlay's center will be
    positioned. It also accepts arithmetic expressions such as `bw_mul_0.4` or
    `bw_sub_cw`. Maps to `lxc` in the URL. Cannot be used together with `x`, but can
    be used with `y`. Learn about
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

    y_center: Union[float, str, None] = FieldInfo(alias="yCenter", default=None)
    """
    Specifies the y-coordinate on the base asset where the overlay's center will be
    positioned. It also accepts arithmetic expressions such as `bh_mul_0.4` or
    `bh_sub_ch`. Maps to `lyc` in the URL. Cannot be used together with `y`, but can
    be used with `x`. Learn about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
