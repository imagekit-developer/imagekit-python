# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NamedTransformationUpdateParams"]


class NamedTransformationUpdateParams(TypedDict, total=False):
    enabled: bool
    """Whether the named transformation is enabled.

    Omit to leave the current value unchanged.
    """

    name: str
    """Alias for the transformation string, used in URLs as `tr:n-<name>`.

    This is case-sensitive, contains only alphanumeric characters or `_`
    (underscore), and is unique across all named transformations for your account.
    """

    transformation: str
    """The transformation string this named transformation refers to.

    Learn more about the
    [transformation string syntax](https://imagekit.io/docs/transformations).
    """
