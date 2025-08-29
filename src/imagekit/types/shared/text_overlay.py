# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal, override

from pydantic import Field as FieldInfo

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
    """Control styling of the text overlay."""

    __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        @override
        def __getattr__(self, attr: str) -> str: ...
