# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import named_transformation_create_params, named_transformation_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from .._utils import path_template, maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.shared.named_transformation import NamedTransformation
from ..types.named_transformation_list_response import NamedTransformationListResponse

__all__ = ["NamedTransformationsResource", "AsyncNamedTransformationsResource"]


class NamedTransformationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NamedTransformationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return NamedTransformationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NamedTransformationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return NamedTransformationsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        transformation: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedTransformation:
        """
        Creates a new named transformation and returns the created object.

        A named transformation is a short, reusable name for a transformation string.
        Use it in image and video URLs as `tr:n-<name>`, and update the underlying
        transformation later without changing existing URLs. Learn more about
        [named transformations](https://imagekit.io/docs/transformations#named-transformations).

        You can create up to 250 named transformations per account.

        Args:
          name: Alias for the transformation string, used in URLs as `tr:n-<name>`. This is
              case-sensitive, contains only alphanumeric characters or `_` (underscore), and
              is unique across all named transformations for your account.

          transformation: The transformation string this named transformation refers to. Learn more about
              the [transformation string syntax](https://imagekit.io/docs/transformations).

          enabled: Whether the named transformation is currently enabled. When set to `false`,
              requests using this named transformation fail at delivery time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/named-transformations",
            body=maybe_transform(
                {
                    "name": name,
                    "transformation": transformation,
                    "enabled": enabled,
                },
                named_transformation_create_params.NamedTransformationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
        )

    def update(
        self,
        id: str,
        *,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        transformation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedTransformation:
        """
        Updates the named transformation identified by `id` and returns the updated
        object. Only the fields present in the request body are updated; other fields
        stay unchanged.

        Renaming or disabling a named transformation fails with a `409` error if it is
        still referenced (via the `n-<name>` token) by an upload pre-transformation or
        post-transformation setting. This check is best-effort and can't detect
        references in your own application code or in previously generated URLs.

        Args:
          id: Unique identifier for a named transformation.

          enabled: Whether the named transformation is enabled. Omit to leave the current value
              unchanged.

          name: Alias for the transformation string, used in URLs as `tr:n-<name>`. This is
              case-sensitive, contains only alphanumeric characters or `_` (underscore), and
              is unique across all named transformations for your account.

          transformation: The transformation string this named transformation refers to. Learn more about
              the [transformation string syntax](https://imagekit.io/docs/transformations).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            path_template("/v1/named-transformations/{id}", id=id),
            body=maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "transformation": transformation,
                },
                named_transformation_update_params.NamedTransformationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
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
    ) -> NamedTransformationListResponse:
        """Returns an array of all named transformations configured for your account."""
        return self._get(
            "/v1/named-transformations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformationListResponse,
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
        """
        Permanently deletes the named transformation identified by `id`.

        Deletion fails with a `409` error if the named transformation is still
        referenced (via the `n-<name>` token) by an upload pre-transformation or
        post-transformation setting. This check is best-effort and can't detect
        references in your own application code or in previously generated URLs.

        Args:
          id: Unique identifier for a named transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            path_template("/v1/named-transformations/{id}", id=id),
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
    ) -> NamedTransformation:
        """
        Retrieves the named transformation identified by `id`.

        Args:
          id: Unique identifier for a named transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._get(
            path_template("/v1/named-transformations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
        )


class AsyncNamedTransformationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNamedTransformationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNamedTransformationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNamedTransformationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncNamedTransformationsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        transformation: str,
        enabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedTransformation:
        """
        Creates a new named transformation and returns the created object.

        A named transformation is a short, reusable name for a transformation string.
        Use it in image and video URLs as `tr:n-<name>`, and update the underlying
        transformation later without changing existing URLs. Learn more about
        [named transformations](https://imagekit.io/docs/transformations#named-transformations).

        You can create up to 250 named transformations per account.

        Args:
          name: Alias for the transformation string, used in URLs as `tr:n-<name>`. This is
              case-sensitive, contains only alphanumeric characters or `_` (underscore), and
              is unique across all named transformations for your account.

          transformation: The transformation string this named transformation refers to. Learn more about
              the [transformation string syntax](https://imagekit.io/docs/transformations).

          enabled: Whether the named transformation is currently enabled. When set to `false`,
              requests using this named transformation fail at delivery time.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/named-transformations",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "transformation": transformation,
                    "enabled": enabled,
                },
                named_transformation_create_params.NamedTransformationCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
        )

    async def update(
        self,
        id: str,
        *,
        enabled: bool | Omit = omit,
        name: str | Omit = omit,
        transformation: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedTransformation:
        """
        Updates the named transformation identified by `id` and returns the updated
        object. Only the fields present in the request body are updated; other fields
        stay unchanged.

        Renaming or disabling a named transformation fails with a `409` error if it is
        still referenced (via the `n-<name>` token) by an upload pre-transformation or
        post-transformation setting. This check is best-effort and can't detect
        references in your own application code or in previously generated URLs.

        Args:
          id: Unique identifier for a named transformation.

          enabled: Whether the named transformation is enabled. Omit to leave the current value
              unchanged.

          name: Alias for the transformation string, used in URLs as `tr:n-<name>`. This is
              case-sensitive, contains only alphanumeric characters or `_` (underscore), and
              is unique across all named transformations for your account.

          transformation: The transformation string this named transformation refers to. Learn more about
              the [transformation string syntax](https://imagekit.io/docs/transformations).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            path_template("/v1/named-transformations/{id}", id=id),
            body=await async_maybe_transform(
                {
                    "enabled": enabled,
                    "name": name,
                    "transformation": transformation,
                },
                named_transformation_update_params.NamedTransformationUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
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
    ) -> NamedTransformationListResponse:
        """Returns an array of all named transformations configured for your account."""
        return await self._get(
            "/v1/named-transformations",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformationListResponse,
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
        """
        Permanently deletes the named transformation identified by `id`.

        Deletion fails with a `409` error if the named transformation is still
        referenced (via the `n-<name>` token) by an upload pre-transformation or
        post-transformation setting. This check is best-effort and can't detect
        references in your own application code or in previously generated URLs.

        Args:
          id: Unique identifier for a named transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            path_template("/v1/named-transformations/{id}", id=id),
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
    ) -> NamedTransformation:
        """
        Retrieves the named transformation identified by `id`.

        Args:
          id: Unique identifier for a named transformation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._get(
            path_template("/v1/named-transformations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
        )


class NamedTransformationsResourceWithRawResponse:
    def __init__(self, named_transformations: NamedTransformationsResource) -> None:
        self._named_transformations = named_transformations

        self.create = to_raw_response_wrapper(
            named_transformations.create,
        )
        self.update = to_raw_response_wrapper(
            named_transformations.update,
        )
        self.list = to_raw_response_wrapper(
            named_transformations.list,
        )
        self.delete = to_raw_response_wrapper(
            named_transformations.delete,
        )
        self.get = to_raw_response_wrapper(
            named_transformations.get,
        )


class AsyncNamedTransformationsResourceWithRawResponse:
    def __init__(self, named_transformations: AsyncNamedTransformationsResource) -> None:
        self._named_transformations = named_transformations

        self.create = async_to_raw_response_wrapper(
            named_transformations.create,
        )
        self.update = async_to_raw_response_wrapper(
            named_transformations.update,
        )
        self.list = async_to_raw_response_wrapper(
            named_transformations.list,
        )
        self.delete = async_to_raw_response_wrapper(
            named_transformations.delete,
        )
        self.get = async_to_raw_response_wrapper(
            named_transformations.get,
        )


class NamedTransformationsResourceWithStreamingResponse:
    def __init__(self, named_transformations: NamedTransformationsResource) -> None:
        self._named_transformations = named_transformations

        self.create = to_streamed_response_wrapper(
            named_transformations.create,
        )
        self.update = to_streamed_response_wrapper(
            named_transformations.update,
        )
        self.list = to_streamed_response_wrapper(
            named_transformations.list,
        )
        self.delete = to_streamed_response_wrapper(
            named_transformations.delete,
        )
        self.get = to_streamed_response_wrapper(
            named_transformations.get,
        )


class AsyncNamedTransformationsResourceWithStreamingResponse:
    def __init__(self, named_transformations: AsyncNamedTransformationsResource) -> None:
        self._named_transformations = named_transformations

        self.create = async_to_streamed_response_wrapper(
            named_transformations.create,
        )
        self.update = async_to_streamed_response_wrapper(
            named_transformations.update,
        )
        self.list = async_to_streamed_response_wrapper(
            named_transformations.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            named_transformations.delete,
        )
        self.get = async_to_streamed_response_wrapper(
            named_transformations.get,
        )
