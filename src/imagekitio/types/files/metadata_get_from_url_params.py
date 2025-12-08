# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, TypedDict

__all__ = ["MetadataGetFromURLParams"]


class MetadataGetFromURLParams(TypedDict, total=False):
    url: Required[str]
    """Should be a valid file URL.

    It should be accessible using your ImageKit.io account.
    """
