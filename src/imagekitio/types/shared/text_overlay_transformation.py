# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TextOverlayTransformation"]


class TextOverlayTransformation(BaseModel):
    alpha: Optional[float] = None
    """Specifies the transparency level of the text overlay.

    Accepts integers from `1` to `9`.
    """

    background: Optional[str] = None
    """
    Specifies the background color of the text overlay. Accepts an RGB hex code, an
    RGBA code, or a color name.
    """

    flip: Optional[Literal["h", "v", "h_v", "v_h"]] = None
    """
    Flip/mirror the text horizontally, vertically, or in both directions. Acceptable
    values: `h` (horizontal), `v` (vertical), `h_v` (horizontal and vertical), or
    `v_h`.
    """

    font_color: Optional[str] = FieldInfo(alias="fontColor", default=None)
    """Specifies the font color of the overlaid text.

    Accepts an RGB hex code (e.g., `FF0000`), an RGBA code (e.g., `FFAABB50`), or a
    color name.
    """

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Specifies the font family of the overlaid text.

    Choose from the supported fonts list or use a custom font. See
    [Supported fonts](https://imagekit.io/docs/add-overlays-on-images#supported-text-font-list)
    and
    [Custom font](https://imagekit.io/docs/add-overlays-on-images#change-font-family-in-text-overlay).
    """

    font_size: Union[float, str, None] = FieldInfo(alias="fontSize", default=None)
    """Specifies the font size of the overlaid text.

    Accepts a numeric value or an arithmetic expression.
    """

    inner_alignment: Optional[Literal["left", "right", "center"]] = FieldInfo(alias="innerAlignment", default=None)
    """
    Specifies the inner alignment of the text when width is more than the text
    length.
    """

    line_height: Union[float, str, None] = FieldInfo(alias="lineHeight", default=None)
    """Specifies the line height for multi-line text overlays.

    It will come into effect only if the text wraps over multiple lines. Accepts
    either an integer value or an arithmetic expression.
    """

    padding: Union[float, str, None] = None
    """
    Specifies the padding around the overlaid text. Can be provided as a single
    positive integer or multiple values separated by underscores (following CSS
    shorthand order). Arithmetic expressions are also accepted.
    """

    radius: Union[float, Literal["max"], str, None] = None
    """Specifies the corner radius:

    - Single value (positive integer): Applied to all corners (e.g., `20`).
    - `max`: Creates a circular or oval shape.
    - Per-corner array: Provide four underscore-separated values representing
      top-left, top-right, bottom-right, and bottom-left corners respectively (e.g.,
      `10_20_30_40`). See
      [Radius](https://imagekit.io/docs/effects-and-enhancements#radius---r).
    """

    rotation: Union[float, str, None] = None
    """
    Specifies the rotation angle of the text overlay. Accepts a numeric value for
    clockwise rotation or a string prefixed with "N" for counter-clockwise rotation.
    """

    typography: Optional[str] = None
    """Specifies the typography style of the text. Supported values:

    - Single styles: `b` (bold), `i` (italic), `strikethrough`.
    - Combinations: Any combination separated by underscores, e.g., `b_i`,
      `b_i_strikethrough`.
    """

    width: Union[float, str, None] = None
    """Specifies the maximum width (in pixels) of the overlaid text.

    The text wraps automatically, and arithmetic expressions (e.g., `bw_mul_0.2` or
    `bh_div_2`) are supported. Useful when used in conjunction with the
    `background`. Learn about
    [Arithmetic expressions](https://imagekit.io/docs/arithmetic-expressions-in-transformations).
    """
