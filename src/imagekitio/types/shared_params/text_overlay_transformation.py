# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["TextOverlayTransformation"]


class TextOverlayTransformation(TypedDict, total=False):
    alpha: float
    """Specifies the transparency level of the text overlay.

    Accepts integers from `1` to `9`.
    """

    background: str
    """
    Specifies the background color of the text overlay. Accepts an RGB hex code, an
    RGBA code, or a color name.
    """

    flip: Literal["h", "v", "h_v", "v_h"]
    """Flip the text overlay horizontally, vertically, or both."""

    font_color: Annotated[str, PropertyInfo(alias="fontColor")]
    """Specifies the font color of the overlaid text.

    Accepts an RGB hex code (e.g., `FF0000`), an RGBA code (e.g., `FFAABB50`), or a
    color name.
    """

    font_family: Annotated[str, PropertyInfo(alias="fontFamily")]
    """Specifies the font family of the overlaid text.

    Choose from the supported fonts list or use a custom font. See
    [Supported fonts](https://imagekit.io/docs/add-overlays-on-images#supported-text-font-list)
    and
    [Custom font](https://imagekit.io/docs/add-overlays-on-images#change-font-family-in-text-overlay).
    """

    font_size: Annotated[Union[float, str], PropertyInfo(alias="fontSize")]
    """Specifies the font size of the overlaid text.

    Accepts a numeric value or an arithmetic expression.
    """

    inner_alignment: Annotated[Literal["left", "right", "center"], PropertyInfo(alias="innerAlignment")]
    """
    Specifies the inner alignment of the text when width is more than the text
    length.
    """

    line_height: Annotated[Union[float, str], PropertyInfo(alias="lineHeight")]
    """Specifies the line height of the text overlay.

    Accepts integer values representing line height in points. It can also accept
    [arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations)
    such as `bw_mul_0.2`, or `bh_div_20`.
    """

    padding: Union[float, str]
    """
    Specifies the padding around the overlaid text. Can be provided as a single
    positive integer or multiple values separated by underscores (following CSS
    shorthand order). Arithmetic expressions are also accepted.
    """

    radius: Union[float, Literal["max"]]
    """
    Specifies the corner radius of the text overlay. Set to `max` to achieve a
    circular or oval shape.
    """

    rotation: Union[float, str]
    """
    Specifies the rotation angle of the text overlay. Accepts a numeric value for
    clockwise rotation or a string prefixed with "N" for counter-clockwise rotation.
    """

    typography: str
    """Specifies the typography style of the text. Supported values:

    - Single styles: `b` (bold), `i` (italic), `strikethrough`.
    - Combinations: Any combination separated by underscores, e.g., `b_i`,
      `b_i_strikethrough`.
    """

    width: Union[float, str]
    """Specifies the maximum width (in pixels) of the overlaid text.

    The text wraps automatically, and arithmetic expressions (e.g., `bw_mul_0.2` or
    `bh_div_2`) are supported. Useful when used in conjunction with the
    `background`. Learn about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
