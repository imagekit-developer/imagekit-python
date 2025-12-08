# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ResponsiveImageAttributes"]


class ResponsiveImageAttributes(TypedDict, total=False):
    """
    Resulting set of attributes suitable for an HTML `<img>` element.
    Useful for enabling responsive image loading with `srcSet` and `sizes`.
    """

    src: Required[str]
    """URL for the _largest_ candidate (assigned to plain `src`)."""

    sizes: str
    """`sizes` returned (or synthesised as `100vw`).

    The value for the HTML `sizes` attribute.
    """

    src_set: Annotated[str, PropertyInfo(alias="srcSet")]
    """Candidate set with `w` or `x` descriptors.

    Multiple image URLs separated by commas, each with a descriptor.
    """

    width: float
    """Width as a number (if `width` was provided in the input options)."""
