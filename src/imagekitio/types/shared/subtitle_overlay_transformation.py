# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SubtitleOverlayTransformation"]


class SubtitleOverlayTransformation(BaseModel):
    """Subtitle styling options.

    [Learn more](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer) from the docs.
    """

    background: Optional[str] = None
    """
    Specifies the subtitle background color using a standard color name, an RGB
    color code (e.g., FF0000), or an RGBA color code (e.g., FFAABB50).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    color: Optional[str] = None
    """
    Sets the font color of the subtitle text using a standard color name, an RGB
    color code (e.g., FF0000), or an RGBA color code (e.g., FFAABB50).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    font_family: Optional[str] = FieldInfo(alias="fontFamily", default=None)
    """Font family for subtitles.

    Refer to the
    [supported fonts](https://imagekit.io/docs/add-overlays-on-images#supported-text-font-list).
    """

    font_outline: Optional[str] = FieldInfo(alias="fontOutline", default=None)
    """Sets the font outline of the subtitle text.

    Requires the outline width (an integer) and the outline color (as an RGB color
    code, RGBA color code, or standard web color name) separated by an underscore.
    Example: `fol-2_blue` (outline width of 2px and outline color blue),
    `fol-2_A1CCDD` (outline width of 2px and outline color `#A1CCDD`) and
    `fol-2_A1CCDD50` (outline width of 2px and outline color `#A1CCDD` at 50%
    opacity).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    font_shadow: Optional[str] = FieldInfo(alias="fontShadow", default=None)
    """Sets the font shadow for the subtitle text.

    Requires the shadow color (as an RGB color code, RGBA color code, or standard
    web color name) and shadow indent (an integer) separated by an underscore.
    Example: `fsh-blue_2` (shadow color blue, indent of 2px), `fsh-A1CCDD_3` (shadow
    color `#A1CCDD`, indent of 3px), `fsh-A1CCDD50_3` (shadow color `#A1CCDD` at 50%
    opacity, indent of 3px).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    font_size: Optional[float] = FieldInfo(alias="fontSize", default=None)
    """Sets the font size of subtitle text.

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    typography: Optional[Literal["b", "i", "b_i"]] = None
    """Sets the typography style of the subtitle text.

    Supports values are `b` for bold, `i` for italics, and `b_i` for bold with
    italics.

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """
