# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamedTransformationCreateParams"]


class NamedTransformationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Alias for the transformation string, used in URLs as `tr:n-<name>`.

    This is case-sensitive, contains only alphanumeric characters or `_`
    (underscore), and is unique across all named transformations for your account.
    """

    transformation: Required[str]
    """The transformation string this named transformation refers to.

    Learn more about the
    [transformation string syntax](https://imagekit.io/docs/transformations).
    """

    enabled: bool
    """Whether the named transformation is currently enabled.

    When set to `false`, requests using this named transformation fail at delivery
    time.
    """
