# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ..._utils import PropertyInfo

__all__ = [
    "OriginRequestParam",
    "S3",
    "S3Compatible",
    "CloudinaryBackup",
    "WebFolder",
    "WebProxy",
    "Gcs",
    "AzureBlob",
    "AkeneoPim",
]


class S3(TypedDict, total=False):
    access_key: Required[Annotated[str, PropertyInfo(alias="accessKey")]]
    """Access key for the bucket."""

    bucket: Required[str]
    """S3 bucket name."""

    name: Required[str]
    """Display name of the origin."""

    secret_key: Required[Annotated[str, PropertyInfo(alias="secretKey")]]
    """Secret key for the bucket."""

    type: Required[Literal["S3"]]

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""

    prefix: str
    """Path prefix inside the bucket."""


class S3Compatible(TypedDict, total=False):
    access_key: Required[Annotated[str, PropertyInfo(alias="accessKey")]]
    """Access key for the bucket."""

    bucket: Required[str]
    """S3 bucket name."""

    endpoint: Required[str]
    """Custom S3-compatible endpoint."""

    name: Required[str]
    """Display name of the origin."""

    secret_key: Required[Annotated[str, PropertyInfo(alias="secretKey")]]
    """Secret key for the bucket."""

    type: Required[Literal["S3_COMPATIBLE"]]

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""

    prefix: str
    """Path prefix inside the bucket."""

    s3_force_path_style: Annotated[bool, PropertyInfo(alias="s3ForcePathStyle")]
    """Use path-style S3 URLs?"""


class CloudinaryBackup(TypedDict, total=False):
    access_key: Required[Annotated[str, PropertyInfo(alias="accessKey")]]
    """Access key for the bucket."""

    bucket: Required[str]
    """S3 bucket name."""

    name: Required[str]
    """Display name of the origin."""

    secret_key: Required[Annotated[str, PropertyInfo(alias="secretKey")]]
    """Secret key for the bucket."""

    type: Required[Literal["CLOUDINARY_BACKUP"]]

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""

    prefix: str
    """Path prefix inside the bucket."""


class WebFolder(TypedDict, total=False):
    base_url: Required[Annotated[str, PropertyInfo(alias="baseUrl")]]
    """Root URL for the web folder origin."""

    name: Required[str]
    """Display name of the origin."""

    type: Required[Literal["WEB_FOLDER"]]

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    forward_host_header_to_origin: Annotated[bool, PropertyInfo(alias="forwardHostHeaderToOrigin")]
    """Forward the Host header to origin?"""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""


class WebProxy(TypedDict, total=False):
    name: Required[str]
    """Display name of the origin."""

    type: Required[Literal["WEB_PROXY"]]

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""


class Gcs(TypedDict, total=False):
    bucket: Required[str]

    client_email: Required[Annotated[str, PropertyInfo(alias="clientEmail")]]

    name: Required[str]
    """Display name of the origin."""

    private_key: Required[Annotated[str, PropertyInfo(alias="privateKey")]]

    type: Required[Literal["GCS"]]

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""

    prefix: str


class AzureBlob(TypedDict, total=False):
    account_name: Required[Annotated[str, PropertyInfo(alias="accountName")]]

    container: Required[str]

    name: Required[str]
    """Display name of the origin."""

    sas_token: Required[Annotated[str, PropertyInfo(alias="sasToken")]]

    type: Required[Literal["AZURE_BLOB"]]

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""

    prefix: str


class AkeneoPim(TypedDict, total=False):
    base_url: Required[Annotated[str, PropertyInfo(alias="baseUrl")]]
    """Akeneo instance base URL."""

    client_id: Required[Annotated[str, PropertyInfo(alias="clientId")]]
    """Akeneo API client ID."""

    client_secret: Required[Annotated[str, PropertyInfo(alias="clientSecret")]]
    """Akeneo API client secret."""

    name: Required[str]
    """Display name of the origin."""

    password: Required[str]
    """Akeneo API password."""

    type: Required[Literal["AKENEO_PIM"]]

    username: Required[str]
    """Akeneo API username."""

    base_url_for_canonical_header: Annotated[str, PropertyInfo(alias="baseUrlForCanonicalHeader")]
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Annotated[bool, PropertyInfo(alias="includeCanonicalHeader")]
    """Whether to send a Canonical header."""


OriginRequestParam: TypeAlias = Union[
    S3, S3Compatible, CloudinaryBackup, WebFolder, WebProxy, Gcs, AzureBlob, AkeneoPim
]
