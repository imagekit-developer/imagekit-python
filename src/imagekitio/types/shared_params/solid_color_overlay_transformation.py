# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, TypedDict

__all__ = ["SolidColorOverlayTransformation"]


class SolidColorOverlayTransformation(TypedDict, total=False):
    alpha: float
    """Specifies the transparency level of the solid color overlay.

    Accepts integers from `1` to `9`.
    """

    background: str
    """Specifies the background color of the solid color overlay.

    Accepts an RGB hex code (e.g., `FF0000`), an RGBA code (e.g., `FFAABB50`), or a
    color name.
    """

    gradient: Union[Literal[True], str]
    """Creates a linear gradient with two colors.

    Pass `true` for a default gradient, or provide a string for a custom gradient.
    Only works if the base asset is an image. See
    [gradient](https://imagekit.io/docs/effects-and-enhancements#gradient---e-gradient).
    """

    height: Union[float, str]
    """Controls the height of the solid color overlay.

    Accepts a numeric value or an arithmetic expression. Learn about
    [arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """

    radius: Union[float, Literal["max"]]
    """Specifies the corner radius of the solid color overlay.

    Set to `max` for circular or oval shape. See
    [radius](https://imagekit.io/docs/effects-and-enhancements#radius---r).
    """

    width: Union[float, str]
    """Controls the width of the solid color overlay.

    Accepts a numeric value or an arithmetic expression (e.g., `bw_mul_0.2` or
    `bh_div_2`). Learn about
    [arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
