# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union
from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.streaming_resolution import StreamingResolution

__all__ = ["Transformation"]


class Transformation(TypedDict, total=False):
    """The SDK provides easy-to-use names for transformations.

    These names are converted to the corresponding transformation string before being added to the URL.
    SDKs are updated regularly to support new transformations. If you want to use a transformation that is not supported by the SDK,
    You can use the `raw` parameter to pass the transformation string directly.
    See the [Transformations documentation](https://imagekit.io/docs/transformations).
    """

    ai_change_background: Annotated[str, PropertyInfo(alias="aiChangeBackground")]
    """Uses AI to change the background.

    Provide a text prompt or a base64-encoded prompt, e.g., `prompt-snow road` or
    `prompte-[urlencoded_base64_encoded_text]`. Not supported inside overlay. See
    [AI Change Background](https://imagekit.io/docs/ai-transformations#change-background-e-changebg).
    """

    ai_drop_shadow: Annotated[Union[Literal[True], str], PropertyInfo(alias="aiDropShadow")]
    """
    Adds an AI-based drop shadow around a foreground object on a transparent or
    removed background. Optionally, control the direction, elevation, and saturation
    of the light source (e.g., `az-45` to change light direction). Pass `true` for
    the default drop shadow, or provide a string for a custom drop shadow. Supported
    inside overlay. See
    [AI Drop Shadow](https://imagekit.io/docs/ai-transformations#ai-drop-shadow-e-dropshadow).
    """

    ai_edit: Annotated[str, PropertyInfo(alias="aiEdit")]
    """Uses AI to edit images based on a text prompt.

    Provide a text prompt or a base64-encoded prompt, e.g., `prompt-snow road` or
    `prompte-[urlencoded_base64_encoded_text]`. Not supported inside overlay.
    See [AI Edit](https://imagekit.io/docs/ai-transformations#edit-image-e-edit).
    """

    ai_remove_background: Annotated[Literal[True], PropertyInfo(alias="aiRemoveBackground")]
    """Applies ImageKit's in-house background removal.

    Supported inside overlay. See
    [AI Background Removal](https://imagekit.io/docs/ai-transformations#imagekit-background-removal-e-bgremove).
    """

    ai_remove_background_external: Annotated[Literal[True], PropertyInfo(alias="aiRemoveBackgroundExternal")]
    """Uses third-party background removal.

    Note: It is recommended to use aiRemoveBackground, ImageKit's in-house solution,
    which is more cost-effective. Supported inside overlay. See
    [External Background Removal](https://imagekit.io/docs/ai-transformations#background-removal-e-removedotbg).
    """

    ai_retouch: Annotated[Literal[True], PropertyInfo(alias="aiRetouch")]
    """Performs AI-based retouching to improve faces or product shots.

    Not supported inside overlay. See
    [AI Retouch](https://imagekit.io/docs/ai-transformations#retouch-e-retouch).
    """

    ai_upscale: Annotated[Literal[True], PropertyInfo(alias="aiUpscale")]
    """Upscales images beyond their original dimensions using AI.

    Not supported inside overlay. See
    [AI Upscale](https://imagekit.io/docs/ai-transformations#upscale-e-upscale).
    """

    ai_variation: Annotated[Literal[True], PropertyInfo(alias="aiVariation")]
    """Generates a variation of an image using AI.

    This produces a new image with slight variations from the original, such as
    changes in color, texture, and other visual elements, while preserving the
    structure and essence of the original image. Not supported inside overlay. See
    [AI Generate Variations](https://imagekit.io/docs/ai-transformations#generate-variations-of-an-image-e-genvar).
    """

    aspect_ratio: Annotated[Union[float, str], PropertyInfo(alias="aspectRatio")]
    """Specifies the aspect ratio for the output, e.g., "ar-4-3".

    Typically used with either width or height (but not both). For example:
    aspectRatio = `4:3`, `4_3`, or an expression like `iar_div_2`. See
    [Image resize and crop – Aspect ratio](https://imagekit.io/docs/image-resize-and-crop#aspect-ratio---ar).
    """

    audio_codec: Annotated[Literal["aac", "opus", "none"], PropertyInfo(alias="audioCodec")]
    """Specifies the audio codec, e.g., `aac`, `opus`, or `none`.

    See [Audio codec](https://imagekit.io/docs/video-optimization#audio-codec---ac).
    """

    background: str
    """
    Specifies the background to be used in conjunction with certain cropping
    strategies when resizing an image.

    - A solid color: e.g., `red`, `F3F3F3`, `AAFF0010`. See
      [Solid color background](https://imagekit.io/docs/effects-and-enhancements#solid-color-background).
    - A blurred background: e.g., `blurred`, `blurred_25_N15`, etc. See
      [Blurred background](https://imagekit.io/docs/effects-and-enhancements#blurred-background).
    - Expand the image boundaries using generative fill: `genfill`. Not supported
      inside overlay. Optionally, control the background scene by passing a text
      prompt: `genfill[:-prompt-${text}]` or
      `genfill[:-prompte-${urlencoded_base64_encoded_text}]`. See
      [Generative fill background](https://imagekit.io/docs/ai-transformations#generative-fill-bg-genfill).
    """

    blur: float
    """Specifies the Gaussian blur level.

    Accepts an integer value between 1 and 100, or an expression like `bl-10`. See
    [Blur](https://imagekit.io/docs/effects-and-enhancements#blur---bl).
    """

    border: str
    """Adds a border to the output media.

    Accepts a string in the format `<border-width>_<hex-code>` (e.g., `5_FFF000` for
    a 5px yellow border), or an expression like `ih_div_20_FF00FF`. See
    [Border](https://imagekit.io/docs/effects-and-enhancements#border---b).
    """

    color_profile: Annotated[bool, PropertyInfo(alias="colorProfile")]
    """
    Indicates whether the output image should retain the original color profile. See
    [Color profile](https://imagekit.io/docs/image-optimization#color-profile---cp).
    """

    contrast_stretch: Annotated[Literal[True], PropertyInfo(alias="contrastStretch")]
    """
    Automatically enhances the contrast of an image (contrast stretch). See
    [Contrast Stretch](https://imagekit.io/docs/effects-and-enhancements#contrast-stretch---e-contrast).
    """

    crop: Literal["force", "at_max", "at_max_enlarge", "at_least", "maintain_ratio"]
    """Crop modes for image resizing.

    See
    [Crop modes & focus](https://imagekit.io/docs/image-resize-and-crop#crop-crop-modes--focus).
    """

    crop_mode: Annotated[Literal["pad_resize", "extract", "pad_extract"], PropertyInfo(alias="cropMode")]
    """Additional crop modes for image resizing.

    See
    [Crop modes & focus](https://imagekit.io/docs/image-resize-and-crop#crop-crop-modes--focus).
    """

    default_image: Annotated[str, PropertyInfo(alias="defaultImage")]
    """
    Specifies a fallback image if the resource is not found, e.g., a URL or file
    path. See
    [Default image](https://imagekit.io/docs/image-transformation#default-image---di).
    """

    dpr: float
    """
    Accepts values between 0.1 and 5, or `auto` for automatic device pixel ratio
    (DPR) calculation. See
    [DPR](https://imagekit.io/docs/image-resize-and-crop#dpr---dpr).
    """

    duration: Union[float, str]
    """Specifies the duration (in seconds) for trimming videos, e.g., `5` or `10.5`.

    Typically used with startOffset to indicate the length from the start offset.
    Arithmetic expressions are supported. See
    [Trim videos – Duration](https://imagekit.io/docs/trim-videos#duration---du).
    """

    end_offset: Annotated[Union[float, str], PropertyInfo(alias="endOffset")]
    """Specifies the end offset (in seconds) for trimming videos, e.g., `5` or `10.5`.

    Typically used with startOffset to define a time window. Arithmetic expressions
    are supported. See
    [Trim videos – End offset](https://imagekit.io/docs/trim-videos#end-offset---eo).
    """

    flip: Literal["h", "v", "h_v", "v_h"]
    """Flips or mirrors an image either horizontally, vertically, or both.

    Acceptable values: `h` (horizontal), `v` (vertical), `h_v` (horizontal and
    vertical), or `v_h`. See
    [Flip](https://imagekit.io/docs/effects-and-enhancements#flip---fl).
    """

    focus: str
    """
    Refines padding and cropping behavior for pad resize, maintain ratio, and
    extract crop modes. Supports manual positions and coordinate-based focus. With
    AI-based cropping, you can automatically keep key subjects in frame—such as
    faces or detected objects (e.g., `fo-face`, `fo-person`, `fo-car`)— while
    resizing.

    - See [Focus](https://imagekit.io/docs/image-resize-and-crop#focus---fo).
    - [Object aware cropping](https://imagekit.io/docs/image-resize-and-crop#object-aware-cropping---fo-object-name)
    """

    format: Literal["auto", "webp", "jpg", "jpeg", "png", "gif", "svg", "mp4", "webm", "avif", "orig"]
    """
    Specifies the output format for images or videos, e.g., `jpg`, `png`, `webp`,
    `mp4`, or `auto`. You can also pass `orig` for images to return the original
    format. ImageKit automatically delivers images and videos in the optimal format
    based on device support unless overridden by the dashboard settings or the
    format parameter. See
    [Image format](https://imagekit.io/docs/image-optimization#format---f) and
    [Video format](https://imagekit.io/docs/video-optimization#format---f).
    """

    gradient: Union[Literal[True], str]
    """Creates a linear gradient with two colors.

    Pass `true` for a default gradient, or provide a string for a custom gradient.
    See
    [Gradient](https://imagekit.io/docs/effects-and-enhancements#gradient---e-gradient).
    """

    grayscale: Literal[True]
    """Enables a grayscale effect for images.

    See
    [Grayscale](https://imagekit.io/docs/effects-and-enhancements#grayscale---e-grayscale).
    """

    height: Union[float, str]
    """Specifies the height of the output.

    If a value between 0 and 1 is provided, it is treated as a percentage (e.g.,
    `0.5` represents 50% of the original height). You can also supply arithmetic
    expressions (e.g., `ih_mul_0.5`). Height transformation –
    [Images](https://imagekit.io/docs/image-resize-and-crop#height---h) ·
    [Videos](https://imagekit.io/docs/video-resize-and-crop#height---h)
    """

    lossless: bool
    """
    Specifies whether the output image (in JPEG or PNG) should be compressed
    losslessly. See
    [Lossless compression](https://imagekit.io/docs/image-optimization#lossless-webp-and-png---lo).
    """

    metadata: bool
    """By default, ImageKit removes all metadata during automatic image compression.

    Set this to true to preserve metadata. See
    [Image metadata](https://imagekit.io/docs/image-optimization#image-metadata---md).
    """

    named: str
    """Named transformation reference.

    See
    [Named transformations](https://imagekit.io/docs/transformations#named-transformations).
    """

    opacity: float
    """Specifies the opacity level of the output image.

    See [Opacity](https://imagekit.io/docs/effects-and-enhancements#opacity---o).
    """

    original: bool
    """
    If set to true, serves the original file without applying any transformations.
    See
    [Deliver original file as-is](https://imagekit.io/docs/core-delivery-features#deliver-original-file-as-is---orig-true).
    """

    overlay: "Overlay"
    """Specifies an overlay to be applied on the parent image or video.

    ImageKit supports overlays including images, text, videos, subtitles, and solid
    colors. See
    [Overlay using layers](https://imagekit.io/docs/transformations#overlay-using-layers).
    """

    page: Union[float, str]
    """
    Extracts a specific page or frame from multi-page or layered files (PDF, PSD,
    AI). For example, specify by number (e.g., `2`), a range (e.g., `3-4` for the
    2nd and 3rd layers), or by name (e.g., `name-layer-4` for a PSD layer). See
    [Thumbnail extraction](https://imagekit.io/docs/vector-and-animated-images#get-thumbnail-from-psd-pdf-ai-eps-and-animated-files).
    """

    progressive: bool
    """Specifies whether the output JPEG image should be rendered progressively.

    Progressive loading begins with a low-quality, pixelated version of the full
    image, which gradually improves to provide a faster perceived load time. See
    [Progressive images](https://imagekit.io/docs/image-optimization#progressive-image---pr).
    """

    quality: float
    """
    Specifies the quality of the output image for lossy formats such as JPEG, WebP,
    and AVIF. A higher quality value results in a larger file size with better
    quality, while a lower value produces a smaller file size with reduced quality.
    See [Quality](https://imagekit.io/docs/image-optimization#quality---q).
    """

    radius: Union[float, Literal["max"]]
    """
    Specifies the corner radius for rounded corners (e.g., 20) or `max` for circular
    or oval shape. See
    [Radius](https://imagekit.io/docs/effects-and-enhancements#radius---r).
    """

    raw: str
    """Pass any transformation not directly supported by the SDK.

    This transformation string is appended to the URL as provided.
    """

    rotation: Union[float, str]
    """Specifies the rotation angle in degrees.

    Positive values rotate the image clockwise; you can also use, for example, `N40`
    for counterclockwise rotation or `auto` to use the orientation specified in the
    image's EXIF data. For videos, only the following values are supported: 0, 90,
    180, 270, or 360. See
    [Rotate](https://imagekit.io/docs/effects-and-enhancements#rotate---rt).
    """

    shadow: Union[Literal[True], str]
    """Adds a shadow beneath solid objects in an image with a transparent background.

    For AI-based drop shadows, refer to aiDropShadow. Pass `true` for a default
    shadow, or provide a string for a custom shadow. See
    [Shadow](https://imagekit.io/docs/effects-and-enhancements#shadow---e-shadow).
    """

    sharpen: Union[Literal[True], float]
    """Sharpens the input image, highlighting edges and finer details.

    Pass `true` for default sharpening, or provide a numeric value for custom
    sharpening. See
    [Sharpen](https://imagekit.io/docs/effects-and-enhancements#sharpen---e-sharpen).
    """

    start_offset: Annotated[Union[float, str], PropertyInfo(alias="startOffset")]
    """Specifies the start offset (in seconds) for trimming videos, e.g., `5` or
    `10.5`.

    Arithmetic expressions are also supported. See
    [Trim videos – Start offset](https://imagekit.io/docs/trim-videos#start-offset---so).
    """

    streaming_resolutions: Annotated[List[StreamingResolution], PropertyInfo(alias="streamingResolutions")]
    """
    An array of resolutions for adaptive bitrate streaming, e.g., [`240`, `360`,
    `480`, `720`, `1080`]. See
    [Adaptive Bitrate Streaming](https://imagekit.io/docs/adaptive-bitrate-streaming).
    """

    trim: Union[Literal[True], float]
    """Useful for images with a solid or nearly solid background and a central object.

    This parameter trims the background, leaving only the central object in the
    output image. See
    [Trim edges](https://imagekit.io/docs/effects-and-enhancements#trim-edges---t).
    """

    unsharp_mask: Annotated[Union[Literal[True], str], PropertyInfo(alias="unsharpMask")]
    """Applies Unsharp Masking (USM), an image sharpening technique.

    Pass `true` for a default unsharp mask, or provide a string for a custom unsharp
    mask. See
    [Unsharp Mask](https://imagekit.io/docs/effects-and-enhancements#unsharp-mask---e-usm).
    """

    video_codec: Annotated[Literal["h264", "vp9", "av1", "none"], PropertyInfo(alias="videoCodec")]
    """Specifies the video codec, e.g., `h264`, `vp9`, `av1`, or `none`.

    See [Video codec](https://imagekit.io/docs/video-optimization#video-codec---vc).
    """

    width: Union[float, str]
    """Specifies the width of the output.

    If a value between 0 and 1 is provided, it is treated as a percentage (e.g.,
    `0.4` represents 40% of the original width). You can also supply arithmetic
    expressions (e.g., `iw_div_2`). Width transformation –
    [Images](https://imagekit.io/docs/image-resize-and-crop#width---w) ·
    [Videos](https://imagekit.io/docs/video-resize-and-crop#width---w)
    """

    x: Union[float, str]
    """Focus using cropped image coordinates - X coordinate.

    See
    [Focus using cropped coordinates](https://imagekit.io/docs/image-resize-and-crop#example---focus-using-cropped-image-coordinates).
    """

    x_center: Annotated[Union[float, str], PropertyInfo(alias="xCenter")]
    """Focus using cropped image coordinates - X center coordinate.

    See
    [Focus using cropped coordinates](https://imagekit.io/docs/image-resize-and-crop#example---focus-using-cropped-image-coordinates).
    """

    y: Union[float, str]
    """Focus using cropped image coordinates - Y coordinate.

    See
    [Focus using cropped coordinates](https://imagekit.io/docs/image-resize-and-crop#example---focus-using-cropped-image-coordinates).
    """

    y_center: Annotated[Union[float, str], PropertyInfo(alias="yCenter")]
    """Focus using cropped image coordinates - Y center coordinate.

    See
    [Focus using cropped coordinates](https://imagekit.io/docs/image-resize-and-crop#example---focus-using-cropped-image-coordinates).
    """

    zoom: float
    """
    Accepts a numeric value that determines how much to zoom in or out of the
    cropped area. It should be used in conjunction with fo-face or fo-<object_name>.
    See [Zoom](https://imagekit.io/docs/image-resize-and-crop#zoom---z).
    """


from .overlay import Overlay
