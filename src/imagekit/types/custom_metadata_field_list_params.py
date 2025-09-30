# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["CustomMetadataFieldListParams"]


class CustomMetadataFieldListParams(TypedDict, total=False):
    folder_path: Annotated[str, PropertyInfo(alias="folderPath")]
    """
    The folder path (e.g., `/path/to/folder`) for which to retrieve applicable
    custom metadata fields. Useful for determining path-specific field selections
    when the [Path policy](https://imagekit.io/docs/dam/path-policy) feature is in
    use.
    """

    include_deleted: Annotated[bool, PropertyInfo(alias="includeDeleted")]
    """Set it to `true` to include deleted field objects in the API response."""
