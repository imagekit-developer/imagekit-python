# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .transformation_position import TransformationPosition

__all__ = ["SrcOptions"]


class SrcOptions(BaseModel):
    src: str
    """Accepts a relative or absolute path of the resource.

    If a relative path is provided, it is appended to the `urlEndpoint`. If an
    absolute path is provided, `urlEndpoint` is ignored.
    """

    url_endpoint: str = FieldInfo(alias="urlEndpoint")
    """
    Get your urlEndpoint from the
    [ImageKit dashboard](https://imagekit.io/dashboard/url-endpoints).
    """

    query_parameters: Optional[Dict[str, str]] = FieldInfo(alias="queryParameters", default=None)
    """
    These are additional query parameters that you want to add to the final URL.
    They can be any query parameters and not necessarily related to ImageKit. This
    is especially useful if you want to add a versioning parameter to your URLs.
    """

    transformation: Optional[List["Transformation"]] = None
    """An array of objects specifying the transformations to be applied in the URL.

    If more than one transformation is specified, they are applied in the order they
    are specified as chained transformations.
    """

    transformation_position: Optional[TransformationPosition] = FieldInfo(alias="transformationPosition", default=None)
    """
    By default, the transformation string is added as a query parameter in the URL,
    e.g., `?tr=w-100,h-100`. If you want to add the transformation string in the
    path of the URL, set this to `path`.
    """


from .transformation import Transformation
