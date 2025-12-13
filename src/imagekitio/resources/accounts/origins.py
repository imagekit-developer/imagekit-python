# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Any, cast
from typing_extensions import Literal, overload

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ..._utils import required_args, maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.accounts import origin_create_params, origin_update_params
from ...types.accounts.origin_response import OriginResponse
from ...types.accounts.origin_list_response import OriginListResponse

__all__ = ["OriginsResource", "AsyncOriginsResource"]


class OriginsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OriginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return OriginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OriginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return OriginsResourceWithStreamingResponse(self)

    @overload
    def create(
        self,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["S3"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        access_key: str,
        bucket: str,
        endpoint: str,
        name: str,
        secret_key: str,
        type: Literal["S3_COMPATIBLE"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          endpoint: Custom S3-compatible endpoint.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          s3_force_path_style: Use path-style S3 URLs?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["CLOUDINARY_BACKUP"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        base_url: str,
        name: str,
        type: Literal["WEB_FOLDER"],
        base_url_for_canonical_header: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          base_url: Root URL for the web folder origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          forward_host_header_to_origin: Forward the Host header to origin?

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        name: str,
        type: Literal["WEB_PROXY"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        bucket: str,
        client_email: str,
        name: str,
        private_key: str,
        type: Literal["GCS"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        account_name: str,
        container: str,
        name: str,
        sas_token: str,
        type: Literal["AZURE_BLOB"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def create(
        self,
        *,
        base_url: str,
        client_id: str,
        client_secret: str,
        name: str,
        password: str,
        type: Literal["AKENEO_PIM"],
        username: str,
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          base_url: Akeneo instance base URL.

          client_id: Akeneo API client ID.

          client_secret: Akeneo API client secret.

          name: Display name of the origin.

          password: Akeneo API password.

          username: Akeneo API username.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["access_key", "bucket", "name", "secret_key", "type"],
        ["access_key", "bucket", "endpoint", "name", "secret_key", "type"],
        ["base_url", "name", "type"],
        ["name", "type"],
        ["bucket", "client_email", "name", "private_key", "type"],
        ["account_name", "container", "name", "sas_token", "type"],
        ["base_url", "client_id", "client_secret", "name", "password", "type", "username"],
    )
    def create(
        self,
        *,
        access_key: str | Omit = omit,
        bucket: str | Omit = omit,
        name: str,
        secret_key: str | Omit = omit,
        type: Literal["S3"]
        | Literal["S3_COMPATIBLE"]
        | Literal["CLOUDINARY_BACKUP"]
        | Literal["WEB_FOLDER"]
        | Literal["WEB_PROXY"]
        | Literal["GCS"]
        | Literal["AZURE_BLOB"]
        | Literal["AKENEO_PIM"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        endpoint: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        base_url: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        client_email: str | Omit = omit,
        private_key: str | Omit = omit,
        account_name: str | Omit = omit,
        container: str | Omit = omit,
        sas_token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        password: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        return cast(
            OriginResponse,
            self._post(
                "/v1/accounts/origins",
                body=maybe_transform(
                    {
                        "access_key": access_key,
                        "bucket": bucket,
                        "name": name,
                        "secret_key": secret_key,
                        "type": type,
                        "base_url_for_canonical_header": base_url_for_canonical_header,
                        "include_canonical_header": include_canonical_header,
                        "prefix": prefix,
                        "endpoint": endpoint,
                        "s3_force_path_style": s3_force_path_style,
                        "base_url": base_url,
                        "forward_host_header_to_origin": forward_host_header_to_origin,
                        "client_email": client_email,
                        "private_key": private_key,
                        "account_name": account_name,
                        "container": container,
                        "sas_token": sas_token,
                        "client_id": client_id,
                        "client_secret": client_secret,
                        "password": password,
                        "username": username,
                    },
                    origin_create_params.OriginCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    def update(
        self,
        id: str,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["S3"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        access_key: str,
        bucket: str,
        endpoint: str,
        name: str,
        secret_key: str,
        type: Literal["S3_COMPATIBLE"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          endpoint: Custom S3-compatible endpoint.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          s3_force_path_style: Use path-style S3 URLs?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["CLOUDINARY_BACKUP"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        base_url: str,
        name: str,
        type: Literal["WEB_FOLDER"],
        base_url_for_canonical_header: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          base_url: Root URL for the web folder origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          forward_host_header_to_origin: Forward the Host header to origin?

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        name: str,
        type: Literal["WEB_PROXY"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        bucket: str,
        client_email: str,
        name: str,
        private_key: str,
        type: Literal["GCS"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        account_name: str,
        container: str,
        name: str,
        sas_token: str,
        type: Literal["AZURE_BLOB"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        id: str,
        *,
        base_url: str,
        client_id: str,
        client_secret: str,
        name: str,
        password: str,
        type: Literal["AKENEO_PIM"],
        username: str,
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          base_url: Akeneo instance base URL.

          client_id: Akeneo API client ID.

          client_secret: Akeneo API client secret.

          name: Display name of the origin.

          password: Akeneo API password.

          username: Akeneo API username.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["access_key", "bucket", "name", "secret_key", "type"],
        ["access_key", "bucket", "endpoint", "name", "secret_key", "type"],
        ["base_url", "name", "type"],
        ["name", "type"],
        ["bucket", "client_email", "name", "private_key", "type"],
        ["account_name", "container", "name", "sas_token", "type"],
        ["base_url", "client_id", "client_secret", "name", "password", "type", "username"],
    )
    def update(
        self,
        id: str,
        *,
        access_key: str | Omit = omit,
        bucket: str | Omit = omit,
        name: str,
        secret_key: str | Omit = omit,
        type: Literal["S3"]
        | Literal["S3_COMPATIBLE"]
        | Literal["CLOUDINARY_BACKUP"]
        | Literal["WEB_FOLDER"]
        | Literal["WEB_PROXY"]
        | Literal["GCS"]
        | Literal["AZURE_BLOB"]
        | Literal["AKENEO_PIM"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        endpoint: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        base_url: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        client_email: str | Omit = omit,
        private_key: str | Omit = omit,
        account_name: str | Omit = omit,
        container: str | Omit = omit,
        sas_token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        password: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            OriginResponse,
            self._put(
                f"/v1/accounts/origins/{id}",
                body=maybe_transform(
                    {
                        "access_key": access_key,
                        "bucket": bucket,
                        "name": name,
                        "secret_key": secret_key,
                        "type": type,
                        "base_url_for_canonical_header": base_url_for_canonical_header,
                        "include_canonical_header": include_canonical_header,
                        "prefix": prefix,
                        "endpoint": endpoint,
                        "s3_force_path_style": s3_force_path_style,
                        "base_url": base_url,
                        "forward_host_header_to_origin": forward_host_header_to_origin,
                        "client_email": client_email,
                        "private_key": private_key,
                        "account_name": account_name,
                        "container": container,
                        "sas_token": sas_token,
                        "client_id": client_id,
                        "client_secret": client_secret,
                        "password": password,
                        "username": username,
                    },
                    origin_update_params.OriginUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginListResponse:
        """**Note:** This API is currently in beta.


        Returns an array of all configured origins for the current account.
        """
        return self._get(
            "/v1/accounts/origins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OriginListResponse,
        )

    def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Note:** This API is currently in beta.


        Permanently removes the origin identified by `id`. If the origin is in use by
        any URL‑endpoints, the API will return an error.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/accounts/origins/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Retrieves the origin identified by `id`.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            OriginResponse,
            self._get(
                f"/v1/accounts/origins/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class AsyncOriginsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOriginsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOriginsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOriginsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncOriginsResourceWithStreamingResponse(self)

    @overload
    async def create(
        self,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["S3"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        access_key: str,
        bucket: str,
        endpoint: str,
        name: str,
        secret_key: str,
        type: Literal["S3_COMPATIBLE"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          endpoint: Custom S3-compatible endpoint.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          s3_force_path_style: Use path-style S3 URLs?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["CLOUDINARY_BACKUP"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        base_url: str,
        name: str,
        type: Literal["WEB_FOLDER"],
        base_url_for_canonical_header: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          base_url: Root URL for the web folder origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          forward_host_header_to_origin: Forward the Host header to origin?

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        name: str,
        type: Literal["WEB_PROXY"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        bucket: str,
        client_email: str,
        name: str,
        private_key: str,
        type: Literal["GCS"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        account_name: str,
        container: str,
        name: str,
        sas_token: str,
        type: Literal["AZURE_BLOB"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def create(
        self,
        *,
        base_url: str,
        client_id: str,
        client_secret: str,
        name: str,
        password: str,
        type: Literal["AKENEO_PIM"],
        username: str,
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Creates a new origin and returns the origin object.

        Args:
          base_url: Akeneo instance base URL.

          client_id: Akeneo API client ID.

          client_secret: Akeneo API client secret.

          name: Display name of the origin.

          password: Akeneo API password.

          username: Akeneo API username.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["access_key", "bucket", "name", "secret_key", "type"],
        ["access_key", "bucket", "endpoint", "name", "secret_key", "type"],
        ["base_url", "name", "type"],
        ["name", "type"],
        ["bucket", "client_email", "name", "private_key", "type"],
        ["account_name", "container", "name", "sas_token", "type"],
        ["base_url", "client_id", "client_secret", "name", "password", "type", "username"],
    )
    async def create(
        self,
        *,
        access_key: str | Omit = omit,
        bucket: str | Omit = omit,
        name: str,
        secret_key: str | Omit = omit,
        type: Literal["S3"]
        | Literal["S3_COMPATIBLE"]
        | Literal["CLOUDINARY_BACKUP"]
        | Literal["WEB_FOLDER"]
        | Literal["WEB_PROXY"]
        | Literal["GCS"]
        | Literal["AZURE_BLOB"]
        | Literal["AKENEO_PIM"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        endpoint: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        base_url: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        client_email: str | Omit = omit,
        private_key: str | Omit = omit,
        account_name: str | Omit = omit,
        container: str | Omit = omit,
        sas_token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        password: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        return cast(
            OriginResponse,
            await self._post(
                "/v1/accounts/origins",
                body=await async_maybe_transform(
                    {
                        "access_key": access_key,
                        "bucket": bucket,
                        "name": name,
                        "secret_key": secret_key,
                        "type": type,
                        "base_url_for_canonical_header": base_url_for_canonical_header,
                        "include_canonical_header": include_canonical_header,
                        "prefix": prefix,
                        "endpoint": endpoint,
                        "s3_force_path_style": s3_force_path_style,
                        "base_url": base_url,
                        "forward_host_header_to_origin": forward_host_header_to_origin,
                        "client_email": client_email,
                        "private_key": private_key,
                        "account_name": account_name,
                        "container": container,
                        "sas_token": sas_token,
                        "client_id": client_id,
                        "client_secret": client_secret,
                        "password": password,
                        "username": username,
                    },
                    origin_create_params.OriginCreateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    @overload
    async def update(
        self,
        id: str,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["S3"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        access_key: str,
        bucket: str,
        endpoint: str,
        name: str,
        secret_key: str,
        type: Literal["S3_COMPATIBLE"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          endpoint: Custom S3-compatible endpoint.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          s3_force_path_style: Use path-style S3 URLs?

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        access_key: str,
        bucket: str,
        name: str,
        secret_key: str,
        type: Literal["CLOUDINARY_BACKUP"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          access_key: Access key for the bucket.

          bucket: S3 bucket name.

          name: Display name of the origin.

          secret_key: Secret key for the bucket.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          prefix: Path prefix inside the bucket.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        base_url: str,
        name: str,
        type: Literal["WEB_FOLDER"],
        base_url_for_canonical_header: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          base_url: Root URL for the web folder origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          forward_host_header_to_origin: Forward the Host header to origin?

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        name: str,
        type: Literal["WEB_PROXY"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        bucket: str,
        client_email: str,
        name: str,
        private_key: str,
        type: Literal["GCS"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        account_name: str,
        container: str,
        name: str,
        sas_token: str,
        type: Literal["AZURE_BLOB"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          name: Display name of the origin.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        id: str,
        *,
        base_url: str,
        client_id: str,
        client_secret: str,
        name: str,
        password: str,
        type: Literal["AKENEO_PIM"],
        username: str,
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Updates the origin identified by `id` and returns the updated origin object.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          base_url: Akeneo instance base URL.

          client_id: Akeneo API client ID.

          client_secret: Akeneo API client secret.

          name: Display name of the origin.

          password: Akeneo API password.

          username: Akeneo API username.

          base_url_for_canonical_header: URL used in the Canonical header (if enabled).

          include_canonical_header: Whether to send a Canonical header.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @required_args(
        ["access_key", "bucket", "name", "secret_key", "type"],
        ["access_key", "bucket", "endpoint", "name", "secret_key", "type"],
        ["base_url", "name", "type"],
        ["name", "type"],
        ["bucket", "client_email", "name", "private_key", "type"],
        ["account_name", "container", "name", "sas_token", "type"],
        ["base_url", "client_id", "client_secret", "name", "password", "type", "username"],
    )
    async def update(
        self,
        id: str,
        *,
        access_key: str | Omit = omit,
        bucket: str | Omit = omit,
        name: str,
        secret_key: str | Omit = omit,
        type: Literal["S3"]
        | Literal["S3_COMPATIBLE"]
        | Literal["CLOUDINARY_BACKUP"]
        | Literal["WEB_FOLDER"]
        | Literal["WEB_PROXY"]
        | Literal["GCS"]
        | Literal["AZURE_BLOB"]
        | Literal["AKENEO_PIM"],
        base_url_for_canonical_header: str | Omit = omit,
        include_canonical_header: bool | Omit = omit,
        prefix: str | Omit = omit,
        endpoint: str | Omit = omit,
        s3_force_path_style: bool | Omit = omit,
        base_url: str | Omit = omit,
        forward_host_header_to_origin: bool | Omit = omit,
        client_email: str | Omit = omit,
        private_key: str | Omit = omit,
        account_name: str | Omit = omit,
        container: str | Omit = omit,
        sas_token: str | Omit = omit,
        client_id: str | Omit = omit,
        client_secret: str | Omit = omit,
        password: str | Omit = omit,
        username: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            OriginResponse,
            await self._put(
                f"/v1/accounts/origins/{id}",
                body=await async_maybe_transform(
                    {
                        "access_key": access_key,
                        "bucket": bucket,
                        "name": name,
                        "secret_key": secret_key,
                        "type": type,
                        "base_url_for_canonical_header": base_url_for_canonical_header,
                        "include_canonical_header": include_canonical_header,
                        "prefix": prefix,
                        "endpoint": endpoint,
                        "s3_force_path_style": s3_force_path_style,
                        "base_url": base_url,
                        "forward_host_header_to_origin": forward_host_header_to_origin,
                        "client_email": client_email,
                        "private_key": private_key,
                        "account_name": account_name,
                        "container": container,
                        "sas_token": sas_token,
                        "client_id": client_id,
                        "client_secret": client_secret,
                        "password": password,
                        "username": username,
                    },
                    origin_update_params.OriginUpdateParams,
                ),
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginListResponse:
        """**Note:** This API is currently in beta.


        Returns an array of all configured origins for the current account.
        """
        return await self._get(
            "/v1/accounts/origins",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=OriginListResponse,
        )

    async def delete(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """**Note:** This API is currently in beta.


        Permanently removes the origin identified by `id`. If the origin is in use by
        any URL‑endpoints, the API will return an error.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/accounts/origins/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def get(
        self,
        id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> OriginResponse:
        """**Note:** This API is currently in beta.


        Retrieves the origin identified by `id`.

        Args:
          id: Unique identifier for the origin. This is generated by ImageKit when you create
              a new origin.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return cast(
            OriginResponse,
            await self._get(
                f"/v1/accounts/origins/{id}",
                options=make_request_options(
                    extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
                ),
                cast_to=cast(Any, OriginResponse),  # Union types cannot be passed in as arguments in the type system
            ),
        )


class OriginsResourceWithRawResponse:
    def __init__(self, origins: OriginsResource) -> None:
        self._origins = origins

        self.create = to_raw_response_wrapper(
            origins.create,
        )
        self.update = to_raw_response_wrapper(
            origins.update,
        )
        self.list = to_raw_response_wrapper(
            origins.list,
        )
        self.delete = to_raw_response_wrapper(
            origins.delete,
        )
        self.get = to_raw_response_wrapper(
            origins.get,
        )


class AsyncOriginsResourceWithRawResponse:
    def __init__(self, origins: AsyncOriginsResource) -> None:
        self._origins = origins

        self.create = async_to_raw_response_wrapper(
            origins.create,
        )
        self.update = async_to_raw_response_wrapper(
            origins.update,
        )
        self.list = async_to_raw_response_wrapper(
            origins.list,
        )
        self.delete = async_to_raw_response_wrapper(
            origins.delete,
        )
        self.get = async_to_raw_response_wrapper(
            origins.get,
        )


class OriginsResourceWithStreamingResponse:
    def __init__(self, origins: OriginsResource) -> None:
        self._origins = origins

        self.create = to_streamed_response_wrapper(
            origins.create,
        )
        self.update = to_streamed_response_wrapper(
            origins.update,
        )
        self.list = to_streamed_response_wrapper(
            origins.list,
        )
        self.delete = to_streamed_response_wrapper(
            origins.delete,
        )
        self.get = to_streamed_response_wrapper(
            origins.get,
        )


class AsyncOriginsResourceWithStreamingResponse:
    def __init__(self, origins: AsyncOriginsResource) -> None:
        self._origins = origins

        self.create = async_to_streamed_response_wrapper(
            origins.create,
        )
        self.update = async_to_streamed_response_wrapper(
            origins.update,
        )
        self.list = async_to_streamed_response_wrapper(
            origins.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            origins.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            origins.get,
        )
