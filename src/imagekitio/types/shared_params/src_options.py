# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable
from typing_extensions import Required, Annotated, TypedDict

from ..._utils import PropertyInfo
from ..shared.transformation_position import TransformationPosition

__all__ = ["SrcOptions"]


class SrcOptions(TypedDict, total=False):
    """Options for generating ImageKit URLs with transformations.

    See the [Transformations guide](https://imagekit.io/docs/transformations).
    """

    src: Required[str]
    """Accepts a relative or absolute path of the resource.

    If a relative path is provided, it is appended to the `urlEndpoint`. If an
    absolute path is provided, `urlEndpoint` is ignored.
    """

    url_endpoint: Required[Annotated[str, PropertyInfo(alias="urlEndpoint")]]
    """
    Get your urlEndpoint from the
    [ImageKit dashboard](https://imagekit.io/dashboard/url-endpoints).
    """

    expires_in: Annotated[float, PropertyInfo(alias="expiresIn")]
    """When you want the signed URL to expire, specified in seconds.

    If `expiresIn` is anything above 0, the URL will always be signed even if
    `signed` is set to false. If not specified and `signed` is `true`, the signed
    URL will not expire (valid indefinitely).

    Example: Setting `expiresIn: 3600` will make the URL expire 1 hour from
    generation time. After the expiry time, the signed URL will no longer be valid
    and ImageKit will return a 401 Unauthorized status code.

    [Learn more](https://imagekit.io/docs/media-delivery-basic-security#how-to-generate-signed-urls).
    """

    query_parameters: Annotated[Dict[str, str], PropertyInfo(alias="queryParameters")]
    """
    These are additional query parameters that you want to add to the final URL.
    They can be any query parameters and not necessarily related to ImageKit. This
    is especially useful if you want to add a versioning parameter to your URLs.
    """

    signed: bool
    """Whether to sign the URL or not.

    Set this to `true` if you want to generate a signed URL. If `signed` is `true`
    and `expiresIn` is not specified, the signed URL will not expire (valid
    indefinitely). Note: If `expiresIn` is set to any value above 0, the URL will
    always be signed regardless of this setting.
    [Learn more](https://imagekit.io/docs/media-delivery-basic-security#how-to-generate-signed-urls).
    """

    transformation: Iterable["Transformation"]
    """An array of objects specifying the transformations to be applied in the URL.

    If more than one transformation is specified, they are applied in the order they
    are specified as chained transformations. See
    [Chained transformations](https://imagekit.io/docs/transformations#chained-transformations).
    """

    transformation_position: Annotated[TransformationPosition, PropertyInfo(alias="transformationPosition")]
    """
    By default, the transformation string is added as a query parameter in the URL,
    e.g., `?tr=w-100,h-100`. If you want to add the transformation string in the
    path of the URL, set this to `path`. Learn more in the
    [Transformations guide](https://imagekit.io/docs/transformations).
    """


from .transformation import Transformation
