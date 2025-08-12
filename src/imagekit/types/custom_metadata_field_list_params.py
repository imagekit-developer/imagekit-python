# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomMetadataFieldListParams"]


class CustomMetadataFieldListParams(TypedDict, total=False):
    include_deleted: Annotated[bool, PropertyInfo(alias="includeDeleted")]
    """Set it to `true` to include deleted field objects in the API response.

    Default value is `false`.
    """
