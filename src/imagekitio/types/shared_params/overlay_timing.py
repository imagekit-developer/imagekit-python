# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import TypedDict

__all__ = ["OverlayTiming"]


class OverlayTiming(TypedDict, total=False):
    duration: Union[float, str]
    """
    Specifies the duration (in seconds) during which the overlay should appear on
    the base video. Accepts a positive number up to two decimal places (e.g., `20`
    or `20.50`) and arithmetic expressions such as `bdu_mul_0.4` or `bdu_sub_idu`.
    Applies only if the base asset is a video. Maps to `ldu` in the URL.
    """

    end: Union[float, str]
    """
    Specifies the end time (in seconds) for when the overlay should disappear from
    the base video. If both end and duration are provided, duration is ignored.
    Accepts a positive number up to two decimal places (e.g., `20` or `20.50`) and
    arithmetic expressions such as `bdu_mul_0.4` or `bdu_sub_idu`. Applies only if
    the base asset is a video. Maps to `leo` in the URL.
    """

    start: Union[float, str]
    """
    Specifies the start time (in seconds) for when the overlay should appear on the
    base video. Accepts a positive number up to two decimal places (e.g., `20` or
    `20.50`) and arithmetic expressions such as `bdu_mul_0.4` or `bdu_sub_idu`.
    Applies only if the base asset is a video. Maps to `lso` in the URL.
    """
