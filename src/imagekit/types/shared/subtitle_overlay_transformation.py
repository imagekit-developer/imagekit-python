# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubtitleOverlayTransformation"]


class SubtitleOverlayTransformation(BaseModel):
    background: Optional[str] = None
    """Background color for subtitles"""

    color: Optional[str] = None
    """Text color for subtitles"""

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Font family for subtitles"""

    font_outline: Optional[str] = FieldInfo(alias="fontOutline", default=None)
    """Font outline for subtitles"""

    font_shadow: Optional[str] = FieldInfo(alias="fontShadow", default=None)
    """Font shadow for subtitles"""

    font_size: Union[float, str, None] = FieldInfo(alias="fontSize", default=None)
    """Font size for subtitles"""

    typography: Optional[Literal["b", "i", "b_i"]] = None
    """Typography style for subtitles"""
