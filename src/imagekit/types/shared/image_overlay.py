# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Optional
from typing_extensions import Literal

from .base_overlay import BaseOverlay

__all__ = ["ImageOverlay"]


class ImageOverlay(BaseOverlay):
    input: str
    """Specifies the relative path to the image used as an overlay."""

    type: Literal["image"]

    encoding: Optional[Literal["auto", "plain", "base64"]] = None
    """
    The input path can be included in the layer as either `i-{input}` or
    `ie-{base64_encoded_input}`. By default, the SDK determines the appropriate
    format automatically. To always use base64 encoding (`ie-{base64}`), set this
    parameter to `base64`. To always use plain text (`i-{input}`), set it to
    `plain`.
    """

    transformation: Optional[List["Transformation"]] = None
    """Array of transformations to be applied to the overlay image.

    Supported transformations depends on the base/parent asset.
    """


from .transformation import Transformation
