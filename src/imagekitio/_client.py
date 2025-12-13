# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
from .lib import helper
from ._types import (
    Omit,
    Headers,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
    not_given,
)
from ._utils import is_given, get_async_library
from ._version import __version__
from .resources import dummy, assets, webhooks, custom_metadata_fields
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import ImageKitError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)
from .resources.beta import beta
from .resources.cache import cache
from .resources.files import files
from .resources.folders import folders
from .resources.accounts import accounts

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "ImageKit",
    "AsyncImageKit",
    "Client",
    "AsyncClient",
]


class ImageKit(SyncAPIClient):
    dummy: dummy.DummyResource
    custom_metadata_fields: custom_metadata_fields.CustomMetadataFieldsResource
    files: files.FilesResource
    assets: assets.AssetsResource
    cache: cache.CacheResource
    folders: folders.FoldersResource
    accounts: accounts.AccountsResource
    beta: beta.BetaResource
    webhooks: webhooks.WebhooksResource
    helper: helper.HelperResource
    with_raw_response: ImageKitWithRawResponse
    with_streaming_response: ImageKitWithStreamedResponse

    # client options
    private_key: str
    password: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        private_key: str | None = None,
        password: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous ImageKit client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `private_key` from `IMAGEKIT_PRIVATE_KEY`
        - `password` from `OPTIONAL_IMAGEKIT_IGNORES_THIS`
        - `webhook_secret` from `IMAGEKIT_WEBHOOK_SECRET`
        """
        if private_key is None:
            private_key = os.environ.get("IMAGEKIT_PRIVATE_KEY")
        if private_key is None:
            raise ImageKitError(
                "The private_key client option must be set either by passing private_key to the client or by setting the IMAGEKIT_PRIVATE_KEY environment variable"
            )
        self.private_key = private_key

        if password is None:
            password = os.environ.get("OPTIONAL_IMAGEKIT_IGNORES_THIS") or "do_not_set"
        self.password = password

        if webhook_secret is None:
            webhook_secret = os.environ.get("IMAGEKIT_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("IMAGE_KIT_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.imagekit.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.dummy = dummy.DummyResource(self)
        self.custom_metadata_fields = custom_metadata_fields.CustomMetadataFieldsResource(self)
        self.files = files.FilesResource(self)
        self.assets = assets.AssetsResource(self)
        self.cache = cache.CacheResource(self)
        self.folders = folders.FoldersResource(self)
        self.accounts = accounts.AccountsResource(self)
        self.beta = beta.BetaResource(self)
        self.webhooks = webhooks.WebhooksResource(self)
        self.helper = helper.HelperResource(self)
        self.with_raw_response = ImageKitWithRawResponse(self)
        self.with_streaming_response = ImageKitWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self.password is None:
            return {}
        credentials = f"{self.private_key}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.private_key and self.password and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the private_key or password to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        private_key: str | None = None,
        password: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            private_key=private_key or self.private_key,
            password=password or self.password,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncImageKit(AsyncAPIClient):
    dummy: dummy.AsyncDummyResource
    custom_metadata_fields: custom_metadata_fields.AsyncCustomMetadataFieldsResource
    files: files.AsyncFilesResource
    assets: assets.AsyncAssetsResource
    cache: cache.AsyncCacheResource
    folders: folders.AsyncFoldersResource
    accounts: accounts.AsyncAccountsResource
    beta: beta.AsyncBetaResource
    webhooks: webhooks.AsyncWebhooksResource
    helper: helper.AsyncHelperResource
    with_raw_response: AsyncImageKitWithRawResponse
    with_streaming_response: AsyncImageKitWithStreamedResponse

    # client options
    private_key: str
    password: str | None
    webhook_secret: str | None

    def __init__(
        self,
        *,
        private_key: str | None = None,
        password: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async AsyncImageKit client instance.

        This automatically infers the following arguments from their corresponding environment variables if they are not provided:
        - `private_key` from `IMAGEKIT_PRIVATE_KEY`
        - `password` from `OPTIONAL_IMAGEKIT_IGNORES_THIS`
        - `webhook_secret` from `IMAGEKIT_WEBHOOK_SECRET`
        """
        if private_key is None:
            private_key = os.environ.get("IMAGEKIT_PRIVATE_KEY")
        if private_key is None:
            raise ImageKitError(
                "The private_key client option must be set either by passing private_key to the client or by setting the IMAGEKIT_PRIVATE_KEY environment variable"
            )
        self.private_key = private_key

        if password is None:
            password = os.environ.get("OPTIONAL_IMAGEKIT_IGNORES_THIS") or "do_not_set"
        self.password = password

        if webhook_secret is None:
            webhook_secret = os.environ.get("IMAGEKIT_WEBHOOK_SECRET")
        self.webhook_secret = webhook_secret

        if base_url is None:
            base_url = os.environ.get("IMAGE_KIT_BASE_URL")
        self._base_url_overridden = base_url is not None
        if base_url is None:
            base_url = f"https://api.imagekit.io"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.dummy = dummy.AsyncDummyResource(self)
        self.custom_metadata_fields = custom_metadata_fields.AsyncCustomMetadataFieldsResource(self)
        self.files = files.AsyncFilesResource(self)
        self.assets = assets.AsyncAssetsResource(self)
        self.cache = cache.AsyncCacheResource(self)
        self.folders = folders.AsyncFoldersResource(self)
        self.accounts = accounts.AsyncAccountsResource(self)
        self.beta = beta.AsyncBetaResource(self)
        self.webhooks = webhooks.AsyncWebhooksResource(self)
        self.helper = helper.AsyncHelperResource(self)
        self.with_raw_response = AsyncImageKitWithRawResponse(self)
        self.with_streaming_response = AsyncImageKitWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        if self.password is None:
            return {}
        credentials = f"{self.private_key}:{self.password}".encode("ascii")
        header = f"Basic {base64.b64encode(credentials).decode('ascii')}"
        return {"Authorization": header}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    @override
    def _validate_headers(self, headers: Headers, custom_headers: Headers) -> None:
        if self.private_key and self.password and headers.get("Authorization"):
            return
        if isinstance(custom_headers.get("Authorization"), Omit):
            return

        raise TypeError(
            '"Could not resolve authentication method. Expected the private_key or password to be set. Or for the `Authorization` headers to be explicitly omitted"'
        )

    def copy(
        self,
        *,
        private_key: str | None = None,
        password: str | None = None,
        webhook_secret: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = not_given,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = not_given,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        client = self.__class__(
            private_key=private_key or self.private_key,
            password=password or self.password,
            webhook_secret=webhook_secret or self.webhook_secret,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )
        client._base_url_overridden = self._base_url_overridden or base_url is not None
        return client

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class ImageKitWithRawResponse:
    def __init__(self, client: ImageKit) -> None:
        self.dummy = dummy.DummyResourceWithRawResponse(client.dummy)
        self.custom_metadata_fields = custom_metadata_fields.CustomMetadataFieldsResourceWithRawResponse(
            client.custom_metadata_fields
        )
        self.files = files.FilesResourceWithRawResponse(client.files)
        self.assets = assets.AssetsResourceWithRawResponse(client.assets)
        self.cache = cache.CacheResourceWithRawResponse(client.cache)
        self.folders = folders.FoldersResourceWithRawResponse(client.folders)
        self.accounts = accounts.AccountsResourceWithRawResponse(client.accounts)
        self.beta = beta.BetaResourceWithRawResponse(client.beta)


class AsyncImageKitWithRawResponse:
    def __init__(self, client: AsyncImageKit) -> None:
        self.dummy = dummy.AsyncDummyResourceWithRawResponse(client.dummy)
        self.custom_metadata_fields = custom_metadata_fields.AsyncCustomMetadataFieldsResourceWithRawResponse(
            client.custom_metadata_fields
        )
        self.files = files.AsyncFilesResourceWithRawResponse(client.files)
        self.assets = assets.AsyncAssetsResourceWithRawResponse(client.assets)
        self.cache = cache.AsyncCacheResourceWithRawResponse(client.cache)
        self.folders = folders.AsyncFoldersResourceWithRawResponse(client.folders)
        self.accounts = accounts.AsyncAccountsResourceWithRawResponse(client.accounts)
        self.beta = beta.AsyncBetaResourceWithRawResponse(client.beta)


class ImageKitWithStreamedResponse:
    def __init__(self, client: ImageKit) -> None:
        self.dummy = dummy.DummyResourceWithStreamingResponse(client.dummy)
        self.custom_metadata_fields = custom_metadata_fields.CustomMetadataFieldsResourceWithStreamingResponse(
            client.custom_metadata_fields
        )
        self.files = files.FilesResourceWithStreamingResponse(client.files)
        self.assets = assets.AssetsResourceWithStreamingResponse(client.assets)
        self.cache = cache.CacheResourceWithStreamingResponse(client.cache)
        self.folders = folders.FoldersResourceWithStreamingResponse(client.folders)
        self.accounts = accounts.AccountsResourceWithStreamingResponse(client.accounts)
        self.beta = beta.BetaResourceWithStreamingResponse(client.beta)


class AsyncImageKitWithStreamedResponse:
    def __init__(self, client: AsyncImageKit) -> None:
        self.dummy = dummy.AsyncDummyResourceWithStreamingResponse(client.dummy)
        self.custom_metadata_fields = custom_metadata_fields.AsyncCustomMetadataFieldsResourceWithStreamingResponse(
            client.custom_metadata_fields
        )
        self.files = files.AsyncFilesResourceWithStreamingResponse(client.files)
        self.assets = assets.AsyncAssetsResourceWithStreamingResponse(client.assets)
        self.cache = cache.AsyncCacheResourceWithStreamingResponse(client.cache)
        self.folders = folders.AsyncFoldersResourceWithStreamingResponse(client.folders)
        self.accounts = accounts.AsyncAccountsResourceWithStreamingResponse(client.accounts)
        self.beta = beta.AsyncBetaResourceWithStreamingResponse(client.beta)


Client = ImageKit

AsyncClient = AsyncImageKit
