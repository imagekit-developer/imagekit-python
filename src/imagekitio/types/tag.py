# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from datetime import datetime

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Tag"]


class Tag(BaseModel):
    """
    A tag in use in your media library, aggregated case-insensitively across the assets that carry it.
    """

    asset_count: int = FieldInfo(alias="assetCount")
    """
    The number of assets carrying the tag, counted across both tag sources
    (user-generated tags and AI-generated tags) and all file types regardless of the
    request's filters.
    """

    label: str
    """The tag as it was spelled when it was last applied to any asset.

    Use it for display.
    """

    last_used_at: datetime = FieldInfo(alias="lastUsedAt")
    """
    When the tag was last applied to an asset matching the `tagSource` and
    `fileType` filters of the request, in ISO 8601 format.
    """

    name: str
    """The tag in lowercase.

    Tags are case-insensitive, so this is the unique key of the tag within your
    account.
    """
