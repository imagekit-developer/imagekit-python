# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
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
    """Flip the text overlay horizontally, vertically, or both."""

    font_color: Optional[str] = FieldInfo(alias="fontColor", default=None)
    """Specifies the font color of the overlaid text.

    Accepts an RGB hex code (e.g., `FF0000`), an RGBA code (e.g., `FFAABB50`), or a
    color name.
    """

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Specifies the font family of the overlaid text.

    Choose from the supported fonts list or use a custom font.
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
    """Specifies the line height of the text overlay."""

    padding: Union[float, str, None] = None
    """
    Specifies the padding around the overlaid text. Can be provided as a single
    positive integer or multiple values separated by underscores (following CSS
    shorthand order). Arithmetic expressions are also accepted.
    """

    radius: Union[float, Literal["max"], None] = None
    """
    Specifies the corner radius of the text overlay. Set to `max` to achieve a
    circular or oval shape.
    """

    rotation: Union[float, str, None] = None
    """
    Specifies the rotation angle of the text overlay. Accepts a numeric value for
    clockwise rotation or a string prefixed with "N" for counter-clockwise rotation.
    """

    typography: Optional[Literal["b", "i", "b_i"]] = None
    """
    Specifies the typography style of the text. Supported values: `b` for bold, `i`
    for italics, and `b_i` for bold with italics.
    """

    width: Union[float, str, None] = None
    """Specifies the maximum width (in pixels) of the overlaid text.

    The text wraps automatically, and arithmetic expressions (e.g., `bw_mul_0.2` or
    `bh_div_2`) are supported. Useful when used in conjunction with the
    `background`.
    """

    __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
