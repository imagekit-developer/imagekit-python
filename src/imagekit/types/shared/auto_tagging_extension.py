# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AutoTaggingExtension"]


class AutoTaggingExtension(BaseModel):
    max_tags: int = FieldInfo(alias="maxTags")
    """Maximum number of tags to attach to the asset."""

    min_confidence: int = FieldInfo(alias="minConfidence")
    """Minimum confidence level for tags to be considered valid."""

    name: Literal["google-auto-tagging", "aws-auto-tagging"]
    """Specifies the auto-tagging extension used."""
