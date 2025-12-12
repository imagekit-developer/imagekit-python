# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ResponsiveImageAttributes"]


class ResponsiveImageAttributes(BaseModel):
    """
    Resulting set of attributes suitable for an HTML `<img>` element.
    Useful for enabling responsive image loading with `srcSet` and `sizes`.
    """

    src: str
    """URL for the _largest_ candidate (assigned to plain `src`)."""

    sizes: Optional[str] = None
    """`sizes` returned (or synthesised as `100vw`).

    The value for the HTML `sizes` attribute.
    """

    src_set: Optional[str] = FieldInfo(alias="srcSet", default=None)
    """Candidate set with `w` or `x` descriptors.

    Multiple image URLs separated by commas, each with a descriptor.
    """

    width: Optional[float] = None
    """Width as a number (if `width` was provided in the input options)."""
