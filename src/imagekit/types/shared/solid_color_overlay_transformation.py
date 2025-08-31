# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from ..._models import BaseModel

__all__ = ["SolidColorOverlayTransformation"]


class SolidColorOverlayTransformation(BaseModel):
    alpha: Optional[float] = None
    """Specifies the transparency level of the solid color overlay.

    Accepts integers from `1` to `9`.
    """

    background: Optional[str] = None
    """Specifies the background color of the solid color overlay.

    Accepts an RGB hex code (e.g., `FF0000`), an RGBA code (e.g., `FFAABB50`), or a
    color name.
    """

    gradient: Union[Literal[True], str, None] = None
    """Creates a linear gradient with two colors.

    Pass `true` for a default gradient, or provide a string for a custom gradient.
    Only works if the base asset is an image. See
    [gradient](https://imagekit.io/docs/effects-and-enhancements#gradient---e-gradient).
    """

    height: Union[float, str, None] = None
    """Controls the height of the solid color overlay.

    Accepts a numeric value or an arithmetic expression. Learn about
    [arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """

    radius: Union[float, Literal["max"], None] = None
    """Specifies the corner radius of the solid color overlay.

    Set to `max` for circular or oval shape. See
    [radius](https://imagekit.io/docs/effects-and-enhancements#radius---r).
    """

    width: Union[float, str, None] = None
    """Controls the width of the solid color overlay.

    Accepts a numeric value or an arithmetic expression (e.g., `bw_mul_0.2` or
    `bh_div_2`). Learn about
    [arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
