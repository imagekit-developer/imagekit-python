# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SolidColorOverlayTransformation"]


class SolidColorOverlayTransformation(BaseModel):
    alpha: Optional[float] = None
    """Alpha transparency level"""

    background: Optional[str] = None
    """Background color"""

    gradient: Union[Literal[True], str, None] = None
    """Gradient effect for the overlay"""

    height: Union[float, str, None] = None
    """Height of the solid color overlay"""

    radius: Union[float, Literal["max"], None] = None
    """Corner radius of the solid color overlay"""

    width: Union[float, str, None] = None
    """Width of the solid color overlay"""

    __pydantic_extra__: Dict[str, str] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]
    if TYPE_CHECKING:
        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> str: ...
