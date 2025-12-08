# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["SubtitleOverlayTransformation"]


class SubtitleOverlayTransformation(TypedDict, total=False):
    """Subtitle styling options.

    [Learn more](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer) from the docs.
    """

    background: str
    """
    Specifies the subtitle background color using a standard color name, an RGB
    color code (e.g., FF0000), or an RGBA color code (e.g., FFAABB50).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    color: str
    """
    Sets the font color of the subtitle text using a standard color name, an RGB
    color code (e.g., FF0000), or an RGBA color code (e.g., FFAABB50).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    font_family: Annotated[str, PropertyInfo(alias="fontFamily")]
    """Font family for subtitles.

    Refer to the
    [supported fonts](https://imagekit.io/docs/add-overlays-on-images#supported-text-font-list).
    """

    font_outline: Annotated[str, PropertyInfo(alias="fontOutline")]
    """Sets the font outline of the subtitle text.

    Requires the outline width (an integer) and the outline color (as an RGB color
    code, RGBA color code, or standard web color name) separated by an underscore.
    Example: `fol-2_blue` (outline width of 2px and outline color blue),
    `fol-2_A1CCDD` (outline width of 2px and outline color `#A1CCDD`) and
    `fol-2_A1CCDD50` (outline width of 2px and outline color `#A1CCDD` at 50%
    opacity).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    font_shadow: Annotated[str, PropertyInfo(alias="fontShadow")]
    """Sets the font shadow for the subtitle text.

    Requires the shadow color (as an RGB color code, RGBA color code, or standard
    web color name) and shadow indent (an integer) separated by an underscore.
    Example: `fsh-blue_2` (shadow color blue, indent of 2px), `fsh-A1CCDD_3` (shadow
    color `#A1CCDD`, indent of 3px), `fsh-A1CCDD50_3` (shadow color `#A1CCDD` at 50%
    opacity, indent of 3px).

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    font_size: Annotated[float, PropertyInfo(alias="fontSize")]
    """Sets the font size of subtitle text.

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """

    typography: Literal["b", "i", "b_i"]
    """Sets the typography style of the subtitle text.

    Supports values are `b` for bold, `i` for italics, and `b_i` for bold with
    italics.

    [Subtitle styling options](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    """
