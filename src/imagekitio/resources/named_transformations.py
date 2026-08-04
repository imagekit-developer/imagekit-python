# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import named_transformation_create_params, named_transformation_update_params
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
        disabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedTransformation:
        """
        Creates a new named transformation and returns the created object.

        Named transformations let you assign a short, reusable name to a complex
        transformation string, so it can be applied in image and video URLs as
        `tr:n-<name>` and later updated without changing any existing URLs.

        Learn more about
        [named transformations](https://imagekit.io/docs/transformations#named-transformations).

        Args:
          name: Name of the named transformation. This is the alias used to refer to the
              transformation string in image and video URLs, for example `tr:n-<name>`. Can
              only contain alphanumeric characters, `_` and `-`, and must be unique for your
              account (case-insensitive).

          transformation: The transformation string this name refers to. It must start with `tr:` followed
              by one or more transformation parameters, for example
              `tr:w-150,h-150,fo-center,cm-resize`. Learn more about the
              [transformation syntax](https://imagekit.io/docs/transformations).

          disabled: Whether this named transformation is disabled. Set to `true` to temporarily
              disable it without deleting it — requests using a disabled named transformation
              fail at delivery time.

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
                    "disabled": disabled,
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
        disabled: bool | Omit = omit,
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
        object. Only the fields present in the request body are updated; omitted fields
        are left unchanged.

        Args:
          disabled: Whether this named transformation is disabled.

          name: Updated name of the named transformation. Can only contain alphanumeric
              characters, `_` and `-`, and must be unique for your account (case-insensitive).

          transformation: Updated transformation string. It must start with `tr:` followed by one or more
              transformation parameters.

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
                    "disabled": disabled,
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
    ) -> NamedTransformation:
        """
        Permanently deletes the named transformation identified by `id` and returns the
        deleted object.

        **Note:**

        - If another named transformation, or your account's upload
          pre-transformation/post-transformation settings, reference this named
          transformation (via the `n-<name>` token), the request fails with a `409`
          error whose `message` describes what it is referenced by. Remove those
          references first, then retry the deletion. This is a best-effort check and
          cannot detect references baked into your own application code or previously
          generated URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            path_template("/v1/named-transformations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
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
        disabled: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> NamedTransformation:
        """
        Creates a new named transformation and returns the created object.

        Named transformations let you assign a short, reusable name to a complex
        transformation string, so it can be applied in image and video URLs as
        `tr:n-<name>` and later updated without changing any existing URLs.

        Learn more about
        [named transformations](https://imagekit.io/docs/transformations#named-transformations).

        Args:
          name: Name of the named transformation. This is the alias used to refer to the
              transformation string in image and video URLs, for example `tr:n-<name>`. Can
              only contain alphanumeric characters, `_` and `-`, and must be unique for your
              account (case-insensitive).

          transformation: The transformation string this name refers to. It must start with `tr:` followed
              by one or more transformation parameters, for example
              `tr:w-150,h-150,fo-center,cm-resize`. Learn more about the
              [transformation syntax](https://imagekit.io/docs/transformations).

          disabled: Whether this named transformation is disabled. Set to `true` to temporarily
              disable it without deleting it — requests using a disabled named transformation
              fail at delivery time.

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
                    "disabled": disabled,
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
        disabled: bool | Omit = omit,
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
        object. Only the fields present in the request body are updated; omitted fields
        are left unchanged.

        Args:
          disabled: Whether this named transformation is disabled.

          name: Updated name of the named transformation. Can only contain alphanumeric
              characters, `_` and `-`, and must be unique for your account (case-insensitive).

          transformation: Updated transformation string. It must start with `tr:` followed by one or more
              transformation parameters.

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
                    "disabled": disabled,
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
    ) -> NamedTransformation:
        """
        Permanently deletes the named transformation identified by `id` and returns the
        deleted object.

        **Note:**

        - If another named transformation, or your account's upload
          pre-transformation/post-transformation settings, reference this named
          transformation (via the `n-<name>` token), the request fails with a `409`
          error whose `message` describes what it is referenced by. Remove those
          references first, then retry the deletion. This is a best-effort check and
          cannot detect references baked into your own application code or previously
          generated URLs.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            path_template("/v1/named-transformations/{id}", id=id),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NamedTransformation,
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
