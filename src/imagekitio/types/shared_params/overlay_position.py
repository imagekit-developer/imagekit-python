# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["OverlayPosition"]


class OverlayPosition(TypedDict, total=False):
    anchor_point: Annotated[
        Literal["top", "left", "right", "bottom", "top_left", "top_right", "bottom_left", "bottom_right", "center"],
        PropertyInfo(alias="anchorPoint"),
    ]
    """
    Sets the anchor point on the base asset from which the overlay offset is
    calculated. The default value is `top_left`. Maps to `lap` in the URL. Can only
    be used with one or more of `x`, `y`, `xCenter`, or `yCenter`.
    """

    focus: Literal["center", "top", "left", "bottom", "right", "top_left", "top_right", "bottom_left", "bottom_right"]
    """
    Specifies the position of the overlay relative to the parent image or video. If
    one or more of `x`, `y`, `xCenter`, or `yCenter` parameters are specified, this
    parameter is ignored. Maps to `lfo` in the URL.
    """

    x: Union[float, str]
    """
    Specifies the x-coordinate of the top-left corner of the base asset where the
    overlay's top-left corner will be positioned. It also accepts arithmetic
    expressions such as `bw_mul_0.4` or `bw_sub_cw`. Maps to `lx` in the URL. Learn
    about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """

    x_center: Annotated[Union[float, str], PropertyInfo(alias="xCenter")]
    """
    Specifies the x-coordinate on the base asset where the overlay's center will be
    positioned. It also accepts arithmetic expressions such as `bw_mul_0.4` or
    `bw_sub_cw`. Maps to `lxc` in the URL. Cannot be used together with `x`, but can
    be used with `y`. Learn about
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

    y_center: Annotated[Union[float, str], PropertyInfo(alias="yCenter")]
    """
    Specifies the y-coordinate on the base asset where the overlay's center will be
    positioned. It also accepts arithmetic expressions such as `bh_mul_0.4` or
    `bh_sub_ch`. Maps to `lyc` in the URL. Cannot be used together with `y`, but can
    be used with `x`. Learn about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
