# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo
from .shared_params.extensions import Extensions
from .shared_params.base_overlay import BaseOverlay
from .shared_params.text_overlay import TextOverlay
from .shared.streaming_resolution import StreamingResolution
from .shared_params.overlay_timing import OverlayTiming
from .shared.transformation_position import TransformationPosition
from .shared_params.overlay_position import OverlayPosition
from .shared_params.subtitle_overlay import SubtitleOverlay
from .shared_params.solid_color_overlay import SolidColorOverlay
from .shared_params.responsive_image_attributes import ResponsiveImageAttributes
from .shared_params.text_overlay_transformation import TextOverlayTransformation
from .shared_params.subtitle_overlay_transformation import SubtitleOverlayTransformation
from .shared_params.solid_color_overlay_transformation import SolidColorOverlayTransformation

__all__ = ["DummyCreateParams"]


class DummyCreateParams(TypedDict, total=False):
    base_overlay: Annotated[BaseOverlay, PropertyInfo(alias="baseOverlay")]

    extensions: Extensions
    """Array of extensions to be applied to the asset.

    Each extension can be configured with specific parameters based on the extension
    type.
    """

    get_image_attributes_options: Annotated[
        "GetImageAttributesOptions", PropertyInfo(alias="getImageAttributesOptions")
    ]
    """
    Options for generating responsive image attributes including `src`, `srcSet`,
    and `sizes` for HTML `<img>` elements. This schema extends `SrcOptions` to add
    support for responsive image generation with breakpoints.
    """

    image_overlay: Annotated["ImageOverlay", PropertyInfo(alias="imageOverlay")]

    overlay: "Overlay"
    """Specifies an overlay to be applied on the parent image or video.

    ImageKit supports overlays including images, text, videos, subtitles, and solid
    colors. See
    [Overlay using layers](https://imagekit.io/docs/transformations#overlay-using-layers).
    """

    overlay_position: Annotated[OverlayPosition, PropertyInfo(alias="overlayPosition")]

    overlay_timing: Annotated[OverlayTiming, PropertyInfo(alias="overlayTiming")]

    responsive_image_attributes: Annotated[ResponsiveImageAttributes, PropertyInfo(alias="responsiveImageAttributes")]
    """
    Resulting set of attributes suitable for an HTML `<img>` element. Useful for
    enabling responsive image loading with `srcSet` and `sizes`.
    """

    solid_color_overlay: Annotated[SolidColorOverlay, PropertyInfo(alias="solidColorOverlay")]

    solid_color_overlay_transformation: Annotated[
        SolidColorOverlayTransformation, PropertyInfo(alias="solidColorOverlayTransformation")
    ]

    src_options: Annotated["SrcOptions", PropertyInfo(alias="srcOptions")]
    """Options for generating ImageKit URLs with transformations.

    See the [Transformations guide](https://imagekit.io/docs/transformations).
    """

    streaming_resolution: Annotated[StreamingResolution, PropertyInfo(alias="streamingResolution")]
    """
    Available streaming resolutions for
    [adaptive bitrate streaming](https://imagekit.io/docs/adaptive-bitrate-streaming)
    """

    subtitle_overlay: Annotated[SubtitleOverlay, PropertyInfo(alias="subtitleOverlay")]

    subtitle_overlay_transformation: Annotated[
        SubtitleOverlayTransformation, PropertyInfo(alias="subtitleOverlayTransformation")
    ]
    """Subtitle styling options.

    [Learn more](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
    from the docs.
    """

    text_overlay: Annotated[TextOverlay, PropertyInfo(alias="textOverlay")]

    text_overlay_transformation: Annotated[TextOverlayTransformation, PropertyInfo(alias="textOverlayTransformation")]

    transformation: "Transformation"
    """The SDK provides easy-to-use names for transformations.

    These names are converted to the corresponding transformation string before
    being added to the URL. SDKs are updated regularly to support new
    transformations. If you want to use a transformation that is not supported by
    the SDK, You can use the `raw` parameter to pass the transformation string
    directly. See the
    [Transformations documentation](https://imagekit.io/docs/transformations).
    """

    transformation_position: Annotated[TransformationPosition, PropertyInfo(alias="transformationPosition")]
    """
    By default, the transformation string is added as a query parameter in the URL,
    e.g., `?tr=w-100,h-100`. If you want to add the transformation string in the
    path of the URL, set this to `path`. Learn more in the
    [Transformations guide](https://imagekit.io/docs/transformations).
    """

    video_overlay: Annotated["VideoOverlay", PropertyInfo(alias="videoOverlay")]


from .shared_params.overlay import Overlay
from .shared_params.src_options import SrcOptions
from .shared_params.image_overlay import ImageOverlay
from .shared_params.video_overlay import VideoOverlay
from .shared_params.transformation import Transformation
from .shared_params.get_image_attributes_options import GetImageAttributesOptions
