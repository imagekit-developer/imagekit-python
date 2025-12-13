# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from .base_overlay import BaseOverlay
from .text_overlay_transformation import TextOverlayTransformation

__all__ = ["TextOverlay"]


class TextOverlay(BaseOverlay):
    text: str
    """Specifies the text to be displayed in the overlay.

    The SDK automatically handles special characters and encoding.
    """

    type: Literal["text"]

    encoding: Optional[Literal["auto", "plain", "base64"]] = None
    """
    Text can be included in the layer as either `i-{input}` (plain text) or
    `ie-{base64_encoded_input}` (base64). By default, the SDK selects the
    appropriate format based on the input text. To always use base64
    (`ie-{base64}`), set this parameter to `base64`. To always use plain text
    (`i-{input}`), set it to `plain`.
    """

    transformation: Optional[List[TextOverlayTransformation]] = None
    """Control styling of the text overlay.

    See
    [Text overlays](https://imagekit.io/docs/add-overlays-on-images#text-overlay).
    """
