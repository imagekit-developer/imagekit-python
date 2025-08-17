# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AutoTaggingExtension"]


class AutoTaggingExtension(TypedDict, total=False):
    max_tags: Required[Annotated[int, PropertyInfo(alias="maxTags")]]
    """Maximum number of tags to attach to the asset."""

    min_confidence: Required[Annotated[int, PropertyInfo(alias="minConfidence")]]
    """Minimum confidence level for tags to be considered valid."""

    name: Required[Literal["google-auto-tagging", "aws-auto-tagging"]]
    """Specifies the auto-tagging extension used."""
