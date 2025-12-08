# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["UsageGetParams"]


class UsageGetParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """Specify a `endDate` in `YYYY-MM-DD` format.

    It should be after the `startDate`. The difference between `startDate` and
    `endDate` should be less than 90 days.
    """

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """Specify a `startDate` in `YYYY-MM-DD` format.

    It should be before the `endDate`. The difference between `startDate` and
    `endDate` should be less than 90 days.
    """
