# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .overlay_timing import OverlayTiming
from .overlay_position import OverlayPosition

__all__ = ["BaseOverlay"]


class BaseOverlay(BaseModel):
    layer_mode: Optional[Literal["multiply", "cutter", "cutout", "displace"]] = FieldInfo(
        alias="layerMode", default=None
    )
    """Controls how the layer blends with the base image or underlying content.

    Maps to `lm` in the URL. By default, layers completely cover the base image
    beneath them. Layer modes change this behavior:

    - `multiply`: Multiplies the pixel values of the layer with the base image. The
      result is always darker than the original images. This is ideal for applying
      shadows or color tints.
    - `displace`: Uses the layer as a displacement map to distort pixels in the base
      image. The red channel controls horizontal displacement, and the green channel
      controls vertical displacement. Requires `x` or `y` parameter to control
      displacement magnitude.
    - `cutout`: Acts as an inverse mask where opaque areas of the layer turn the
      base image transparent, while transparent areas leave the base image
      unchanged. This mode functions like a hole-punch, effectively cutting the
      shape of the layer out of the underlying image.
    - `cutter`: Acts as a shape mask where only the parts of the base image that
      fall inside the opaque area of the layer are preserved. This mode functions
      like a cookie-cutter, trimming the base image to match the specific dimensions
      and shape of the layer. See
      [Layer modes](https://imagekit.io/docs/add-overlays-on-images#layer-modes).
    """

    position: Optional[OverlayPosition] = None
    """
    Specifies the overlay's position relative to the parent asset. See
    [Position of Layer](https://imagekit.io/docs/transformations#position-of-layer).
    """

    timing: Optional[OverlayTiming] = None
    """
    Specifies timing information for the overlay (only applicable if the base asset
    is a video). See
    [Position of Layer](https://imagekit.io/docs/transformations#position-of-layer).
    """
