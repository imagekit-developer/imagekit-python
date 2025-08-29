# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Dict, List, Optional
from typing_extensions import Literal, override

from pydantic import Field as FieldInfo

from .base_overlay import BaseOverlay

__all__ = ["VideoOverlay"]


class VideoOverlay(BaseOverlay):
    input: str
    """Specifies the relative path to the video used as an overlay."""

    type: Literal["video"]

    encoding: Optional[Literal["auto", "plain", "base64"]] = None
    """
    The input path can be included in the layer as either `i-{input}` or
    `ie-{base64_encoded_input}`. By default, the SDK determines the appropriate
    format automatically. To always use base64 encoding (`ie-{base64}`), set this
    parameter to `base64`. To always use plain text (`i-{input}`), set it to
    `plain`.
    """

    transformation: Optional[List["Transformation"]] = None
    """Array of transformation to be applied to the overlay video.

    Except `streamingResolutions`, all other video transformations are supported.
    """

    __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        @override
        def __getattr__(self, attr: str) -> str: ...


from .transformation import Transformation
