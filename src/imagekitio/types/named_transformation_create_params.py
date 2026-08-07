# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamedTransformationCreateParams"]


class NamedTransformationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Name of the named transformation.

    This is the alias used to refer to the transformation string in image and video
    URLs, for example `tr:n-<name>`. Can only contain alphanumeric characters or `_`
    (hyphens are not allowed), and must be unique for your account. Name matching is
    case-sensitive, so `Small_Thumbnail` and `small_thumbnail` are treated as
    different names.
    """

    transformation: Required[str]
    """
    The transformation this name refers to, expressed as one or more comma-separated
    transformation parameters, for example `w-150,h-150,fo-center,cm-resize`. You do
    not need to prefix this with `tr:` — it is added automatically. If you do
    include it, it must appear in lowercase at the start of the string, or the
    request is rejected. Learn more about the
    [transformation syntax](https://imagekit.io/docs/transformations).
    """

    enabled: bool
    """Whether this named transformation is enabled.

    Set to `false` to temporarily disable it without deleting it — requests using a
    disabled named transformation fail at delivery time.
    """
