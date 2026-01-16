# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
import base64
from typing import TYPE_CHECKING, Any, Mapping
from typing_extensions import Self, override

import httpx

from . import _exceptions
from ._qs import Querystring
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
from ._compat import cached_property
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import ImageKitError, APIStatusError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

if TYPE_CHECKING:
    from .resources import (
        beta,
        cache,
        dummy,
        files,
        assets,
        folders,
        accounts,
        saved_extensions,
        custom_metadata_fields,
    )
    from .resources.dummy import DummyResource, AsyncDummyResource
    from .resources.assets import AssetsResource, AsyncAssetsResource
    from .resources.webhooks import WebhooksResource, AsyncWebhooksResource
    from .resources.beta.beta import BetaResource, AsyncBetaResource
    from .resources.cache.cache import CacheResource, AsyncCacheResource
    from .resources.files.files import FilesResource, AsyncFilesResource
    from .resources.folders.folders import FoldersResource, AsyncFoldersResource
    from .resources.saved_extensions import SavedExtensionsResource, AsyncSavedExtensionsResource
    from .resources.accounts.accounts import AccountsResource, AsyncAccountsResource
    from .resources.custom_metadata_fields import CustomMetadataFieldsResource, AsyncCustomMetadataFieldsResource
    from .lib.helper import HelperResource, AsyncHelperResource

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

    @cached_property
    def dummy(self) -> DummyResource:
        from .resources.dummy import DummyResource

        return DummyResource(self)

    @cached_property
    def custom_metadata_fields(self) -> CustomMetadataFieldsResource:
        from .resources.custom_metadata_fields import CustomMetadataFieldsResource

        return CustomMetadataFieldsResource(self)

    @cached_property
    def files(self) -> FilesResource:
        from .resources.files import FilesResource

        return FilesResource(self)

    @cached_property
    def saved_extensions(self) -> SavedExtensionsResource:
        from .resources.saved_extensions import SavedExtensionsResource

        return SavedExtensionsResource(self)

    @cached_property
    def assets(self) -> AssetsResource:
        from .resources.assets import AssetsResource

        return AssetsResource(self)

    @cached_property
    def cache(self) -> CacheResource:
        from .resources.cache import CacheResource

        return CacheResource(self)

    @cached_property
    def folders(self) -> FoldersResource:
        from .resources.folders import FoldersResource

        return FoldersResource(self)

    @cached_property
    def accounts(self) -> AccountsResource:
        from .resources.accounts import AccountsResource

        return AccountsResource(self)

    @cached_property
    def beta(self) -> BetaResource:
        from .resources.beta import BetaResource

        return BetaResource(self)

    @cached_property
    def webhooks(self) -> WebhooksResource:
        from .resources.webhooks import WebhooksResource

        return WebhooksResource(self)

    @cached_property
    def helper(self) -> HelperResource:
        from .lib.helper import HelperResource

        return HelperResource(self)

    @cached_property
    def with_raw_response(self) -> ImageKitWithRawResponse:
        return ImageKitWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ImageKitWithStreamedResponse:
        return ImageKitWithStreamedResponse(self)

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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
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

    @cached_property
    def dummy(self) -> AsyncDummyResource:
        from .resources.dummy import AsyncDummyResource

        return AsyncDummyResource(self)

    @cached_property
    def custom_metadata_fields(self) -> AsyncCustomMetadataFieldsResource:
        from .resources.custom_metadata_fields import AsyncCustomMetadataFieldsResource

        return AsyncCustomMetadataFieldsResource(self)

    @cached_property
    def files(self) -> AsyncFilesResource:
        from .resources.files import AsyncFilesResource

        return AsyncFilesResource(self)

    @cached_property
    def saved_extensions(self) -> AsyncSavedExtensionsResource:
        from .resources.saved_extensions import AsyncSavedExtensionsResource

        return AsyncSavedExtensionsResource(self)

    @cached_property
    def assets(self) -> AsyncAssetsResource:
        from .resources.assets import AsyncAssetsResource

        return AsyncAssetsResource(self)

    @cached_property
    def cache(self) -> AsyncCacheResource:
        from .resources.cache import AsyncCacheResource

        return AsyncCacheResource(self)

    @cached_property
    def folders(self) -> AsyncFoldersResource:
        from .resources.folders import AsyncFoldersResource

        return AsyncFoldersResource(self)

    @cached_property
    def accounts(self) -> AsyncAccountsResource:
        from .resources.accounts import AsyncAccountsResource

        return AsyncAccountsResource(self)

    @cached_property
    def beta(self) -> AsyncBetaResource:
        from .resources.beta import AsyncBetaResource

        return AsyncBetaResource(self)

    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        from .resources.webhooks import AsyncWebhooksResource

        return AsyncWebhooksResource(self)

    @cached_property
    def helper(self) -> AsyncHelperResource:
        from .lib.helper import AsyncHelperResource

        return AsyncHelperResource(self)

    @cached_property
    def with_raw_response(self) -> AsyncImageKitWithRawResponse:
        return AsyncImageKitWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncImageKitWithStreamedResponse:
        return AsyncImageKitWithStreamedResponse(self)

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
        if headers.get("Authorization") or isinstance(custom_headers.get("Authorization"), Omit):
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
    _client: ImageKit

    def __init__(self, client: ImageKit) -> None:
        self._client = client

    @cached_property
    def dummy(self) -> dummy.DummyResourceWithRawResponse:
        from .resources.dummy import DummyResourceWithRawResponse

        return DummyResourceWithRawResponse(self._client.dummy)

    @cached_property
    def custom_metadata_fields(self) -> custom_metadata_fields.CustomMetadataFieldsResourceWithRawResponse:
        from .resources.custom_metadata_fields import CustomMetadataFieldsResourceWithRawResponse

        return CustomMetadataFieldsResourceWithRawResponse(self._client.custom_metadata_fields)

    @cached_property
    def files(self) -> files.FilesResourceWithRawResponse:
        from .resources.files import FilesResourceWithRawResponse

        return FilesResourceWithRawResponse(self._client.files)

    @cached_property
    def saved_extensions(self) -> saved_extensions.SavedExtensionsResourceWithRawResponse:
        from .resources.saved_extensions import SavedExtensionsResourceWithRawResponse

        return SavedExtensionsResourceWithRawResponse(self._client.saved_extensions)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithRawResponse:
        from .resources.assets import AssetsResourceWithRawResponse

        return AssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def cache(self) -> cache.CacheResourceWithRawResponse:
        from .resources.cache import CacheResourceWithRawResponse

        return CacheResourceWithRawResponse(self._client.cache)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithRawResponse:
        from .resources.folders import FoldersResourceWithRawResponse

        return FoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithRawResponse:
        from .resources.accounts import AccountsResourceWithRawResponse

        return AccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def beta(self) -> beta.BetaResourceWithRawResponse:
        from .resources.beta import BetaResourceWithRawResponse

        return BetaResourceWithRawResponse(self._client.beta)


class AsyncImageKitWithRawResponse:
    _client: AsyncImageKit

    def __init__(self, client: AsyncImageKit) -> None:
        self._client = client

    @cached_property
    def dummy(self) -> dummy.AsyncDummyResourceWithRawResponse:
        from .resources.dummy import AsyncDummyResourceWithRawResponse

        return AsyncDummyResourceWithRawResponse(self._client.dummy)

    @cached_property
    def custom_metadata_fields(self) -> custom_metadata_fields.AsyncCustomMetadataFieldsResourceWithRawResponse:
        from .resources.custom_metadata_fields import AsyncCustomMetadataFieldsResourceWithRawResponse

        return AsyncCustomMetadataFieldsResourceWithRawResponse(self._client.custom_metadata_fields)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithRawResponse:
        from .resources.files import AsyncFilesResourceWithRawResponse

        return AsyncFilesResourceWithRawResponse(self._client.files)

    @cached_property
    def saved_extensions(self) -> saved_extensions.AsyncSavedExtensionsResourceWithRawResponse:
        from .resources.saved_extensions import AsyncSavedExtensionsResourceWithRawResponse

        return AsyncSavedExtensionsResourceWithRawResponse(self._client.saved_extensions)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithRawResponse:
        from .resources.assets import AsyncAssetsResourceWithRawResponse

        return AsyncAssetsResourceWithRawResponse(self._client.assets)

    @cached_property
    def cache(self) -> cache.AsyncCacheResourceWithRawResponse:
        from .resources.cache import AsyncCacheResourceWithRawResponse

        return AsyncCacheResourceWithRawResponse(self._client.cache)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithRawResponse:
        from .resources.folders import AsyncFoldersResourceWithRawResponse

        return AsyncFoldersResourceWithRawResponse(self._client.folders)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithRawResponse:
        from .resources.accounts import AsyncAccountsResourceWithRawResponse

        return AsyncAccountsResourceWithRawResponse(self._client.accounts)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithRawResponse:
        from .resources.beta import AsyncBetaResourceWithRawResponse

        return AsyncBetaResourceWithRawResponse(self._client.beta)


class ImageKitWithStreamedResponse:
    _client: ImageKit

    def __init__(self, client: ImageKit) -> None:
        self._client = client

    @cached_property
    def dummy(self) -> dummy.DummyResourceWithStreamingResponse:
        from .resources.dummy import DummyResourceWithStreamingResponse

        return DummyResourceWithStreamingResponse(self._client.dummy)

    @cached_property
    def custom_metadata_fields(self) -> custom_metadata_fields.CustomMetadataFieldsResourceWithStreamingResponse:
        from .resources.custom_metadata_fields import CustomMetadataFieldsResourceWithStreamingResponse

        return CustomMetadataFieldsResourceWithStreamingResponse(self._client.custom_metadata_fields)

    @cached_property
    def files(self) -> files.FilesResourceWithStreamingResponse:
        from .resources.files import FilesResourceWithStreamingResponse

        return FilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def saved_extensions(self) -> saved_extensions.SavedExtensionsResourceWithStreamingResponse:
        from .resources.saved_extensions import SavedExtensionsResourceWithStreamingResponse

        return SavedExtensionsResourceWithStreamingResponse(self._client.saved_extensions)

    @cached_property
    def assets(self) -> assets.AssetsResourceWithStreamingResponse:
        from .resources.assets import AssetsResourceWithStreamingResponse

        return AssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def cache(self) -> cache.CacheResourceWithStreamingResponse:
        from .resources.cache import CacheResourceWithStreamingResponse

        return CacheResourceWithStreamingResponse(self._client.cache)

    @cached_property
    def folders(self) -> folders.FoldersResourceWithStreamingResponse:
        from .resources.folders import FoldersResourceWithStreamingResponse

        return FoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def accounts(self) -> accounts.AccountsResourceWithStreamingResponse:
        from .resources.accounts import AccountsResourceWithStreamingResponse

        return AccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def beta(self) -> beta.BetaResourceWithStreamingResponse:
        from .resources.beta import BetaResourceWithStreamingResponse

        return BetaResourceWithStreamingResponse(self._client.beta)


class AsyncImageKitWithStreamedResponse:
    _client: AsyncImageKit

    def __init__(self, client: AsyncImageKit) -> None:
        self._client = client

    @cached_property
    def dummy(self) -> dummy.AsyncDummyResourceWithStreamingResponse:
        from .resources.dummy import AsyncDummyResourceWithStreamingResponse

        return AsyncDummyResourceWithStreamingResponse(self._client.dummy)

    @cached_property
    def custom_metadata_fields(self) -> custom_metadata_fields.AsyncCustomMetadataFieldsResourceWithStreamingResponse:
        from .resources.custom_metadata_fields import AsyncCustomMetadataFieldsResourceWithStreamingResponse

        return AsyncCustomMetadataFieldsResourceWithStreamingResponse(self._client.custom_metadata_fields)

    @cached_property
    def files(self) -> files.AsyncFilesResourceWithStreamingResponse:
        from .resources.files import AsyncFilesResourceWithStreamingResponse

        return AsyncFilesResourceWithStreamingResponse(self._client.files)

    @cached_property
    def saved_extensions(self) -> saved_extensions.AsyncSavedExtensionsResourceWithStreamingResponse:
        from .resources.saved_extensions import AsyncSavedExtensionsResourceWithStreamingResponse

        return AsyncSavedExtensionsResourceWithStreamingResponse(self._client.saved_extensions)

    @cached_property
    def assets(self) -> assets.AsyncAssetsResourceWithStreamingResponse:
        from .resources.assets import AsyncAssetsResourceWithStreamingResponse

        return AsyncAssetsResourceWithStreamingResponse(self._client.assets)

    @cached_property
    def cache(self) -> cache.AsyncCacheResourceWithStreamingResponse:
        from .resources.cache import AsyncCacheResourceWithStreamingResponse

        return AsyncCacheResourceWithStreamingResponse(self._client.cache)

    @cached_property
    def folders(self) -> folders.AsyncFoldersResourceWithStreamingResponse:
        from .resources.folders import AsyncFoldersResourceWithStreamingResponse

        return AsyncFoldersResourceWithStreamingResponse(self._client.folders)

    @cached_property
    def accounts(self) -> accounts.AsyncAccountsResourceWithStreamingResponse:
        from .resources.accounts import AsyncAccountsResourceWithStreamingResponse

        return AsyncAccountsResourceWithStreamingResponse(self._client.accounts)

    @cached_property
    def beta(self) -> beta.AsyncBetaResourceWithStreamingResponse:
        from .resources.beta import AsyncBetaResourceWithStreamingResponse

        return AsyncBetaResourceWithStreamingResponse(self._client.beta)


Client = ImageKit

AsyncClient = AsyncImageKit
