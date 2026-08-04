# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamedTransformationCreateParams"]


class NamedTransformationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the named transformation.

    This is the alias used to refer to the transformation string in image and video
    URLs, for example `tr:n-<name>`. Can only contain alphanumeric characters, `_`
    and `-`, and must be unique for your account (case-insensitive).
    """

    transformation: Required[str]
    """The transformation string this name refers to.

    It must start with `tr:` followed by one or more transformation parameters, for
    example `tr:w-150,h-150,fo-center,cm-resize`. Learn more about the
    [transformation syntax](https://imagekit.io/docs/transformations).
    """

    disabled: bool
    """Whether this named transformation is disabled.

    Set to `true` to temporarily disable it without deleting it — requests using a
    disabled named transformation fail at delivery time.
    """
