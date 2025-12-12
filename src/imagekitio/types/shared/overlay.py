# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import TYPE_CHECKING, Union
from typing_extensions import Annotated, TypeAlias, TypeAliasType

from ..._utils import PropertyInfo
from ..._compat import PYDANTIC_V1
from .text_overlay import TextOverlay
from .subtitle_overlay import SubtitleOverlay
from .solid_color_overlay import SolidColorOverlay

__all__ = ["Overlay"]

if TYPE_CHECKING or not PYDANTIC_V1:
    Overlay = TypeAliasType(
        "Overlay",
        Annotated[
            Union[TextOverlay, "ImageOverlay", "VideoOverlay", SubtitleOverlay, SolidColorOverlay],
            PropertyInfo(discriminator="type"),
        ],
    )
else:
    Overlay: TypeAlias = Annotated[
        Union[TextOverlay, "ImageOverlay", "VideoOverlay", SubtitleOverlay, SolidColorOverlay],
        PropertyInfo(discriminator="type"),
    ]

from .image_overlay import ImageOverlay
from .video_overlay import VideoOverlay
