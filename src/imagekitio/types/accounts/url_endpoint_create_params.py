# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._types import SequenceNotStr
from ..._utils import PropertyInfo

__all__ = ["URLEndpointCreateParams", "URLRewriter", "URLRewriterCloudinary", "URLRewriterImgix", "URLRewriterAkamai"]


class URLEndpointCreateParams(TypedDict, total=False):
    description: Required[str]
    """Description of the URL endpoint."""

    origins: SequenceNotStr[str]
    """
    Ordered list of origin IDs to try when the file isn’t in the Media Library;
    ImageKit checks them in the sequence provided. Origin must be created before it
    can be used in a URL endpoint.
    """

    url_prefix: Annotated[str, PropertyInfo(alias="urlPrefix")]
    """
    Path segment appended to your base URL to form the endpoint (letters, digits,
    and hyphens only — or empty for the default endpoint).
    """

    url_rewriter: Annotated[URLRewriter, PropertyInfo(alias="urlRewriter")]
    """Configuration for third-party URL rewriting."""


class URLRewriterCloudinary(TypedDict, total=False):
    type: Required[Literal["CLOUDINARY"]]

    preserve_asset_delivery_types: Annotated[bool, PropertyInfo(alias="preserveAssetDeliveryTypes")]
    """Whether to preserve `<asset_type>/<delivery_type>` in the rewritten URL."""


class URLRewriterImgix(TypedDict, total=False):
    type: Required[Literal["IMGIX"]]


class URLRewriterAkamai(TypedDict, total=False):
    type: Required[Literal["AKAMAI"]]


URLRewriter: TypeAlias = Union[URLRewriterCloudinary, URLRewriterImgix, URLRewriterAkamai]
