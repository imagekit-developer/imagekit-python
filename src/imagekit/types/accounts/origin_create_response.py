# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "OriginCreateResponse",
    "S3",
    "S3Compatible",
    "CloudinaryBackup",
    "WebFolder",
    "WebProxy",
    "GoogleCloudStorageGcs",
    "AzureBlobStorage",
    "AkeneoPim",
]


class S3(BaseModel):
    access_key: str = FieldInfo(alias="accessKey")
    """Access key for the bucket."""

    bucket: str
    """S3 bucket name."""

    name: str
    """Display name of the origin."""

    secret_key: str = FieldInfo(alias="secretKey")
    """Secret key for the bucket."""

    type: Literal["S3"]

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""

    prefix: Optional[str] = None
    """Path prefix inside the bucket."""


class S3Compatible(BaseModel):
    access_key: str = FieldInfo(alias="accessKey")
    """Access key for the bucket."""

    bucket: str
    """S3 bucket name."""

    endpoint: str
    """Custom S3-compatible endpoint."""

    name: str
    """Display name of the origin."""

    secret_key: str = FieldInfo(alias="secretKey")
    """Secret key for the bucket."""

    type: Literal["S3_COMPATIBLE"]

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""

    prefix: Optional[str] = None
    """Path prefix inside the bucket."""

    s3_force_path_style: Optional[bool] = FieldInfo(alias="s3ForcePathStyle", default=None)
    """Use path-style S3 URLs?"""


class CloudinaryBackup(BaseModel):
    access_key: str = FieldInfo(alias="accessKey")
    """Access key for the bucket."""

    bucket: str
    """S3 bucket name."""

    name: str
    """Display name of the origin."""

    secret_key: str = FieldInfo(alias="secretKey")
    """Secret key for the bucket."""

    type: Literal["CLOUDINARY_BACKUP"]

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""

    prefix: Optional[str] = None
    """Path prefix inside the bucket."""


class WebFolder(BaseModel):
    base_url: str = FieldInfo(alias="baseUrl")
    """Root URL for the web folder origin."""

    name: str
    """Display name of the origin."""

    type: Literal["WEB_FOLDER"]

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    forward_host_header_to_origin: Optional[bool] = FieldInfo(alias="forwardHostHeaderToOrigin", default=None)
    """Forward the Host header to origin?"""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""


class WebProxy(BaseModel):
    name: str
    """Display name of the origin."""

    type: Literal["WEB_PROXY"]

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""


class GoogleCloudStorageGcs(BaseModel):
    bucket: str

    client_email: str = FieldInfo(alias="clientEmail")

    name: str
    """Display name of the origin."""

    private_key: str = FieldInfo(alias="privateKey")

    type: Literal["GCS"]

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""

    prefix: Optional[str] = None


class AzureBlobStorage(BaseModel):
    account_name: str = FieldInfo(alias="accountName")

    container: str

    name: str
    """Display name of the origin."""

    sas_token: str = FieldInfo(alias="sasToken")

    type: Literal["AZURE_BLOB"]

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""

    prefix: Optional[str] = None


class AkeneoPim(BaseModel):
    base_url: str = FieldInfo(alias="baseUrl")
    """Akeneo instance base URL."""

    client_id: str = FieldInfo(alias="clientId")
    """Akeneo API client ID."""

    client_secret: str = FieldInfo(alias="clientSecret")
    """Akeneo API client secret."""

    name: str
    """Display name of the origin."""

    password: str
    """Akeneo API password."""

    type: Literal["AKENEO_PIM"]

    username: str
    """Akeneo API username."""

    id: Optional[str] = None

    base_url_for_canonical_header: Optional[str] = FieldInfo(alias="baseUrlForCanonicalHeader", default=None)
    """URL used in the Canonical header (if enabled)."""

    include_canonical_header: Optional[bool] = FieldInfo(alias="includeCanonicalHeader", default=None)
    """Whether to send a Canonical header."""


OriginCreateResponse: TypeAlias = Union[
    S3, S3Compatible, CloudinaryBackup, WebFolder, WebProxy, GoogleCloudStorageGcs, AzureBlobStorage, AkeneoPim
]
