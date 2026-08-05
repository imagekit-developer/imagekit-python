# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NamedTransformationUpdateParams"]


class NamedTransformationUpdateParams(TypedDict, total=False):
    disabled: bool
    """Whether this named transformation is disabled."""

    name: str
    """Updated name of the named transformation.

    Can only contain alphanumeric characters, `_` and `-`, and must be unique for
    your account (case-insensitive).
    """

    transformation: str
    """Updated transformation string.

    It must start with `tr:` followed by one or more transformation parameters.
    """
