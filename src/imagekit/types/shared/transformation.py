# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .streaming_resolution import StreamingResolution

__all__ = ["Transformation"]


class Transformation(BaseModel):
    ai_change_background: Optional[str] = FieldInfo(alias="aiChangeBackground", default=None)
    """Uses AI to change the background.

    Provide a text prompt or a base64-encoded prompt, e.g., `prompt-snow road` or
    `prompte-[urlencoded_base64_encoded_text]`. Not supported inside overlay.
    """

    ai_drop_shadow: Union[Literal[True], str, None] = FieldInfo(alias="aiDropShadow", default=None)
    """
    Adds an AI-based drop shadow around a foreground object on a transparent or
    removed background. Optionally, control the direction, elevation, and saturation
    of the light source (e.g., `az-45` to change light direction). Pass `true` for
    the default drop shadow, or provide a string for a custom drop shadow. Supported
    inside overlay.
    """

    ai_remove_background: Optional[Literal[True]] = FieldInfo(alias="aiRemoveBackground", default=None)
    """Applies ImageKit's in-house background removal. Supported inside overlay."""

    ai_remove_background_external: Optional[Literal[True]] = FieldInfo(alias="aiRemoveBackgroundExternal", default=None)
    """Uses third-party background removal.

    Note: It is recommended to use aiRemoveBackground, ImageKit's in-house solution,
    which is more cost-effective. Supported inside overlay.
    """

    ai_retouch: Optional[Literal[True]] = FieldInfo(alias="aiRetouch", default=None)
    """Performs AI-based retouching to improve faces or product shots.

    Not supported inside overlay.
    """

    ai_upscale: Optional[Literal[True]] = FieldInfo(alias="aiUpscale", default=None)
    """Upscales images beyond their original dimensions using AI.

    Not supported inside overlay.
    """

    ai_variation: Optional[Literal[True]] = FieldInfo(alias="aiVariation", default=None)
    """Generates a variation of an image using AI.

    This produces a new image with slight variations from the original, such as
    changes in color, texture, and other visual elements, while preserving the
    structure and essence of the original image. Not supported inside overlay.
    """

    aspect_ratio: Union[float, str, None] = FieldInfo(alias="aspectRatio", default=None)
    """Specifies the aspect ratio for the output, e.g., "ar-4-3".

    Typically used with either width or height (but not both). For example:
    aspectRatio = `4:3`, `4_3`, or an expression like `iar_div_2`.
    """

    audio_codec: Optional[Literal["aac", "opus", "none"]] = FieldInfo(alias="audioCodec", default=None)
    """Specifies the audio codec, e.g., `aac`, `opus`, or `none`."""

    background: Optional[str] = None
    """
    Specifies the background to be used in conjunction with certain cropping
    strategies when resizing an image.

    - A solid color: e.g., `red`, `F3F3F3`, `AAFF0010`.
    - A blurred background: e.g., `blurred`, `blurred_25_N15`, etc.
    - Expand the image boundaries using generative fill: `genfill`. Not supported
      inside overlay. Optionally, control the background scene by passing a text
      prompt: `genfill[:-prompt-${text}]` or
      `genfill[:-prompte-${urlencoded_base64_encoded_text}]`.
    """

    blur: Optional[float] = None
    """Specifies the Gaussian blur level.

    Accepts an integer value between 1 and 100, or an expression like `bl-10`.
    """

    border: Optional[str] = None
    """Adds a border to the output media.

    Accepts a string in the format `<border-width>_<hex-code>` (e.g., `5_FFF000` for
    a 5px yellow border), or an expression like `ih_div_20_FF00FF`.
    """

    color_profile: Optional[bool] = FieldInfo(alias="colorProfile", default=None)
    """Indicates whether the output image should retain the original color profile."""

    contrast_stretch: Optional[Literal[True]] = FieldInfo(alias="contrastStretch", default=None)
    """Automatically enhances the contrast of an image (contrast stretch)."""

    crop: Optional[Literal["force", "at_max", "at_max_enlarge", "at_least", "maintain_ratio"]] = None
    """Crop modes for image resizing"""

    crop_mode: Optional[Literal["pad_resize", "extract", "pad_extract"]] = FieldInfo(alias="cropMode", default=None)
    """Additional crop modes for image resizing"""

    default_image: Optional[str] = FieldInfo(alias="defaultImage", default=None)
    """
    Specifies a fallback image if the resource is not found, e.g., a URL or file
    path.
    """

    dpr: Optional[float] = None
    """
    Accepts values between 0.1 and 5, or `auto` for automatic device pixel ratio
    (DPR) calculation.
    """

    duration: Union[float, str, None] = None
    """Specifies the duration (in seconds) for trimming videos, e.g., `5` or `10.5`.

    Typically used with startOffset to indicate the length from the start offset.
    Arithmetic expressions are supported.
    """

    end_offset: Union[float, str, None] = FieldInfo(alias="endOffset", default=None)
    """Specifies the end offset (in seconds) for trimming videos, e.g., `5` or `10.5`.

    Typically used with startOffset to define a time window. Arithmetic expressions
    are supported.
    """

    flip: Optional[Literal["h", "v", "h_v", "v_h"]] = None
    """Flips or mirrors an image either horizontally, vertically, or both.

    Acceptable values: `h` (horizontal), `v` (vertical), `h_v` (horizontal and
    vertical), or `v_h`.
    """

    focus: Optional[str] = None
    """
    This parameter can be used with pad resize, maintain ratio, or extract crop to
    modify the padding or cropping behavior.
    """

    format: Optional[Literal["auto", "webp", "jpg", "jpeg", "png", "gif", "svg", "mp4", "webm", "avif", "orig"]] = None
    """
    Specifies the output format for images or videos, e.g., `jpg`, `png`, `webp`,
    `mp4`, or `auto`. You can also pass `orig` for images to return the original
    format. ImageKit automatically delivers images and videos in the optimal format
    based on device support unless overridden by the dashboard settings or the
    format parameter.
    """

    gradient: Union[Literal[True], str, None] = None
    """Creates a linear gradient with two colors.

    Pass `true` for a default gradient, or provide a string for a custom gradient.
    """

    grayscale: Optional[Literal[True]] = None
    """Enables a grayscale effect for images."""

    height: Union[float, str, None] = None
    """Specifies the height of the output.

    If a value between 0 and 1 is provided, it is treated as a percentage (e.g.,
    `0.5` represents 50% of the original height). You can also supply arithmetic
    expressions (e.g., `ih_mul_0.5`).
    """

    lossless: Optional[bool] = None
    """
    Specifies whether the output image (in JPEG or PNG) should be compressed
    losslessly.
    """

    metadata: Optional[bool] = None
    """By default, ImageKit removes all metadata during automatic image compression.

    Set this to true to preserve metadata.
    """

    named: Optional[str] = None
    """Named transformation reference"""

    opacity: Optional[float] = None
    """Specifies the opacity level of the output image."""

    original: Optional[bool] = None
    """If set to true, serves the original file without applying any transformations."""

    overlay: Optional["Overlay"] = None
    """Specifies an overlay to be applied on the parent image or video.

    ImageKit supports overlays including images, text, videos, subtitles, and solid
    colors.
    """

    page: Union[float, str, None] = None
    """
    Extracts a specific page or frame from multi-page or layered files (PDF, PSD,
    AI). For example, specify by number (e.g., `2`), a range (e.g., `3-4` for the
    2nd and 3rd layers), or by name (e.g., `name-layer-4` for a PSD layer).
    """

    progressive: Optional[bool] = None
    """Specifies whether the output JPEG image should be rendered progressively.

    Progressive loading begins with a low-quality, pixelated version of the full
    image, which gradually improves to provide a faster perceived load time.
    """

    quality: Optional[float] = None
    """
    Specifies the quality of the output image for lossy formats such as JPEG, WebP,
    and AVIF. A higher quality value results in a larger file size with better
    quality, while a lower value produces a smaller file size with reduced quality.
    """

    radius: Union[float, Literal["max"], None] = None
    """
    Specifies the corner radius for rounded corners (e.g., 20) or `max` for
    circular/oval shapes.
    """

    raw: Optional[str] = None
    """Pass any transformation not directly supported by the SDK.

    This transformation string is appended to the URL as provided.
    """

    rotation: Union[float, str, None] = None
    """Specifies the rotation angle in degrees.

    Positive values rotate the image clockwise; you can also use, for example, `N40`
    for counterclockwise rotation or `auto` to use the orientation specified in the
    image's EXIF data. For videos, only the following values are supported: 0, 90,
    180, 270, or 360.
    """

    shadow: Union[Literal[True], str, None] = None
    """Adds a shadow beneath solid objects in an image with a transparent background.

    For AI-based drop shadows, refer to aiDropShadow. Pass `true` for a default
    shadow, or provide a string for a custom shadow.
    """

    sharpen: Union[Literal[True], float, None] = None
    """Sharpens the input image, highlighting edges and finer details.

    Pass `true` for default sharpening, or provide a numeric value for custom
    sharpening.
    """

    start_offset: Union[float, str, None] = FieldInfo(alias="startOffset", default=None)
    """Specifies the start offset (in seconds) for trimming videos, e.g., `5` or
    `10.5`.

    Arithmetic expressions are also supported.
    """

    streaming_resolutions: Optional[List[StreamingResolution]] = FieldInfo(alias="streamingResolutions", default=None)
    """
    An array of resolutions for adaptive bitrate streaming, e.g., [`240`, `360`,
    `480`, `720`, `1080`].
    """

    trim: Union[Literal[True], float, None] = None
    """Useful for images with a solid or nearly solid background and a central object.

    This parameter trims the background, leaving only the central object in the
    output image.
    """

    unsharp_mask: Union[Literal[True], str, None] = FieldInfo(alias="unsharpMask", default=None)
    """Applies Unsharp Masking (USM), an image sharpening technique.

    Pass `true` for a default unsharp mask, or provide a string for a custom unsharp
    mask.
    """

    video_codec: Optional[Literal["h264", "vp9", "av1", "none"]] = FieldInfo(alias="videoCodec", default=None)
    """Specifies the video codec, e.g., `h264`, `vp9`, `av1`, or `none`."""

    width: Union[float, str, None] = None
    """Specifies the width of the output.

    If a value between 0 and 1 is provided, it is treated as a percentage (e.g.,
    `0.4` represents 40% of the original width). You can also supply arithmetic
    expressions (e.g., `iw_div_2`).
    """

    x: Union[float, str, None] = None
    """Focus using cropped image coordinates - X coordinate"""

    x_center: Union[float, str, None] = FieldInfo(alias="xCenter", default=None)
    """Focus using cropped image coordinates - X center coordinate"""

    y: Union[float, str, None] = None
    """Focus using cropped image coordinates - Y coordinate"""

    y_center: Union[float, str, None] = FieldInfo(alias="yCenter", default=None)
    """Focus using cropped image coordinates - Y center coordinate"""

    zoom: Optional[float] = None
    """
    Accepts a numeric value that determines how much to zoom in or out of the
    cropped area. It should be used in conjunction with fo-face or fo-<object_name>.
    """

    __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...


from .overlay import Overlay
