# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NamedTransformationUpdateParams"]


class NamedTransformationUpdateParams(TypedDict, total=False):
    enabled: bool
    """Whether this named transformation is enabled.

    If omitted, the existing value is left unchanged.
    """

    name: str
    """Updated name of the named transformation.

    Can only contain alphanumeric characters and `_`, and must be unique for your
    account. Name matching is case-sensitive, so `Small_Thumbnail` and
    `small_thumbnail` are treated as different names.
    """

    transformation: str
    """
    Updated transformation, expressed as one or more comma-separated transformation
    parameters. You do not need to prefix this with `tr:` — it is added
    automatically. If you do include it, it must appear in lowercase at the start of
    the string, or the request is rejected.
    """
