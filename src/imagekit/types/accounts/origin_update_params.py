# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .origin_param import OriginParam

__all__ = ["OriginUpdateParams"]


class OriginUpdateParams(TypedDict, total=False):
    origin: Required[OriginParam]
    """Schema for origin resources."""
