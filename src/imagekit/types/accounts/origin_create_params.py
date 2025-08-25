# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

from .origin_request_param import OriginRequestParam

__all__ = ["OriginCreateParams"]


class OriginCreateParams(TypedDict, total=False):
    origin: Required[OriginRequestParam]
    """Schema for origin request resources."""
