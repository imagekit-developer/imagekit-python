# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NamedTransformation"]


class NamedTransformation(BaseModel):
    """
    A named transformation is an alias for a transformation string, letting you apply and later update complex transformations without changing your image or video URLs. Learn more about [named transformations](https://imagekit.io/docs/transformations#named-transformations).
    """

    id: Optional[str] = None
    """Unique identifier for a named transformation."""

    created_at: Optional[datetime] = FieldInfo(alias="createdAt", default=None)
    """ISO 8601 timestamp of when the named transformation was created."""

    enabled: Optional[bool] = None
    """Whether the named transformation is currently enabled.

    When set to `false`, requests using this named transformation fail at delivery
    time.
    """

    name: Optional[str] = None
    """Alias for the transformation string, used in URLs as `tr:n-<name>`.

    This is case-sensitive, contains only alphanumeric characters or `_`
    (underscore), and is unique across all named transformations for your account.
    """

    transformation: Optional[str] = None
    """The transformation string this named transformation refers to.

    Learn more about the
    [transformation string syntax](https://imagekit.io/docs/transformations).
    """
