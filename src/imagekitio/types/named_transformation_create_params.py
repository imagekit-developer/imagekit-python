# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["NamedTransformationCreateParams"]


class NamedTransformationCreateParams(TypedDict, total=False):
    name: Required[str]
    """Alias for the transformation string, used in URLs as `tr:n-<name>`.

    Must contain only alphanumeric characters or `_` (no hyphens), and be unique for
    your account. Name matching is case-sensitive.
    """

    transformation: Required[str]
    """
    The transformation string this name refers to, for example
    `w-150,h-150,fo-center,cm-resize`. The `tr:` prefix is optional; if present, it
    is validated. The string must be a valid ImageKit transformation and cannot
    itself reference another named transformation (no nesting). Learn more about the
    [transformation syntax](https://imagekit.io/docs/transformations).
    """

    enabled: bool
    """Whether the named transformation is currently enabled.

    When this is set to `false`, requests using such disabled named transformations
    fail at delivery time.
    """
