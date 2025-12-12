# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import (
    custom_metadata_field_list_params,
    custom_metadata_field_create_params,
    custom_metadata_field_update_params,
)
from .._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.custom_metadata_field import CustomMetadataField
from ..types.custom_metadata_field_list_response import CustomMetadataFieldListResponse
from ..types.custom_metadata_field_delete_response import CustomMetadataFieldDeleteResponse

__all__ = ["CustomMetadataFieldsResource", "AsyncCustomMetadataFieldsResource"]


class CustomMetadataFieldsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CustomMetadataFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return CustomMetadataFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CustomMetadataFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return CustomMetadataFieldsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        label: str,
        name: str,
        schema: custom_metadata_field_create_params.Schema,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomMetadataField:
        """This API creates a new custom metadata field.

        Once a custom metadata field is
        created either through this API or using the dashboard UI, its value can be set
        on the assets. The value of a field for an asset can be set using the media
        library UI or programmatically through upload or update assets API.

        Args:
          label: Human readable name of the custom metadata field. This should be unique across
              all non deleted custom metadata fields. This name is displayed as form field
              label to the users while setting field value on an asset in the media library
              UI.

          name: API name of the custom metadata field. This should be unique across all
              (including deleted) custom metadata fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/customMetadataFields",
            body=maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "schema": schema,
                },
                custom_metadata_field_create_params.CustomMetadataFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomMetadataField,
        )

    def update(
        self,
        id: str,
        *,
        label: str | Omit = omit,
        schema: custom_metadata_field_update_params.Schema | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomMetadataField:
        """
        This API updates the label or schema of an existing custom metadata field.

        Args:
          label: Human readable name of the custom metadata field. This should be unique across
              all non deleted custom metadata fields. This name is displayed as form field
              label to the users while setting field value on an asset in the media library
              UI. This parameter is required if `schema` is not provided.

          schema: An object that describes the rules for the custom metadata key. This parameter
              is required if `label` is not provided. Note: `type` cannot be updated and will
              be ignored if sent with the `schema`. The schema will be validated as per the
              existing `type`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._patch(
            f"/v1/customMetadataFields/{id}",
            body=maybe_transform(
                {
                    "label": label,
                    "schema": schema,
                },
                custom_metadata_field_update_params.CustomMetadataFieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomMetadataField,
        )

    def list(
        self,
        *,
        folder_path: str | Omit = omit,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomMetadataFieldListResponse:
        """This API returns the array of created custom metadata field objects.

        By default
        the API returns only non deleted field objects, but you can include deleted
        fields in the API response.

        You can also filter results by a specific folder path to retrieve custom
        metadata fields applicable at that location. This path-specific filtering is
        useful when using the **Path policy** feature to determine which custom metadata
        fields are selected for a given path.

        Args:
          folder_path: The folder path (e.g., `/path/to/folder`) for which to retrieve applicable
              custom metadata fields. Useful for determining path-specific field selections
              when the [Path policy](https://imagekit.io/docs/dam/path-policy) feature is in
              use.

          include_deleted: Set it to `true` to include deleted field objects in the API response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/customMetadataFields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "folder_path": folder_path,
                        "include_deleted": include_deleted,
                    },
                    custom_metadata_field_list_params.CustomMetadataFieldListParams,
                ),
            ),
            cast_to=CustomMetadataFieldListResponse,
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
    ) -> CustomMetadataFieldDeleteResponse:
        """This API deletes a custom metadata field.

        Even after deleting a custom metadata
        field, you cannot create any new custom metadata field with the same name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return self._delete(
            f"/v1/customMetadataFields/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomMetadataFieldDeleteResponse,
        )


class AsyncCustomMetadataFieldsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCustomMetadataFieldsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCustomMetadataFieldsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCustomMetadataFieldsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncCustomMetadataFieldsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        label: str,
        name: str,
        schema: custom_metadata_field_create_params.Schema,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomMetadataField:
        """This API creates a new custom metadata field.

        Once a custom metadata field is
        created either through this API or using the dashboard UI, its value can be set
        on the assets. The value of a field for an asset can be set using the media
        library UI or programmatically through upload or update assets API.

        Args:
          label: Human readable name of the custom metadata field. This should be unique across
              all non deleted custom metadata fields. This name is displayed as form field
              label to the users while setting field value on an asset in the media library
              UI.

          name: API name of the custom metadata field. This should be unique across all
              (including deleted) custom metadata fields.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/customMetadataFields",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "name": name,
                    "schema": schema,
                },
                custom_metadata_field_create_params.CustomMetadataFieldCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomMetadataField,
        )

    async def update(
        self,
        id: str,
        *,
        label: str | Omit = omit,
        schema: custom_metadata_field_update_params.Schema | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomMetadataField:
        """
        This API updates the label or schema of an existing custom metadata field.

        Args:
          label: Human readable name of the custom metadata field. This should be unique across
              all non deleted custom metadata fields. This name is displayed as form field
              label to the users while setting field value on an asset in the media library
              UI. This parameter is required if `schema` is not provided.

          schema: An object that describes the rules for the custom metadata key. This parameter
              is required if `label` is not provided. Note: `type` cannot be updated and will
              be ignored if sent with the `schema`. The schema will be validated as per the
              existing `type`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._patch(
            f"/v1/customMetadataFields/{id}",
            body=await async_maybe_transform(
                {
                    "label": label,
                    "schema": schema,
                },
                custom_metadata_field_update_params.CustomMetadataFieldUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomMetadataField,
        )

    async def list(
        self,
        *,
        folder_path: str | Omit = omit,
        include_deleted: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CustomMetadataFieldListResponse:
        """This API returns the array of created custom metadata field objects.

        By default
        the API returns only non deleted field objects, but you can include deleted
        fields in the API response.

        You can also filter results by a specific folder path to retrieve custom
        metadata fields applicable at that location. This path-specific filtering is
        useful when using the **Path policy** feature to determine which custom metadata
        fields are selected for a given path.

        Args:
          folder_path: The folder path (e.g., `/path/to/folder`) for which to retrieve applicable
              custom metadata fields. Useful for determining path-specific field selections
              when the [Path policy](https://imagekit.io/docs/dam/path-policy) feature is in
              use.

          include_deleted: Set it to `true` to include deleted field objects in the API response.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/customMetadataFields",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "folder_path": folder_path,
                        "include_deleted": include_deleted,
                    },
                    custom_metadata_field_list_params.CustomMetadataFieldListParams,
                ),
            ),
            cast_to=CustomMetadataFieldListResponse,
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
    ) -> CustomMetadataFieldDeleteResponse:
        """This API deletes a custom metadata field.

        Even after deleting a custom metadata
        field, you cannot create any new custom metadata field with the same name.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not id:
            raise ValueError(f"Expected a non-empty value for `id` but received {id!r}")
        return await self._delete(
            f"/v1/customMetadataFields/{id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CustomMetadataFieldDeleteResponse,
        )


class CustomMetadataFieldsResourceWithRawResponse:
    def __init__(self, custom_metadata_fields: CustomMetadataFieldsResource) -> None:
        self._custom_metadata_fields = custom_metadata_fields

        self.create = to_raw_response_wrapper(
            custom_metadata_fields.create,
        )
        self.update = to_raw_response_wrapper(
            custom_metadata_fields.update,
        )
        self.list = to_raw_response_wrapper(
            custom_metadata_fields.list,
        )
        self.delete = to_raw_response_wrapper(
            custom_metadata_fields.delete,
        )


class AsyncCustomMetadataFieldsResourceWithRawResponse:
    def __init__(self, custom_metadata_fields: AsyncCustomMetadataFieldsResource) -> None:
        self._custom_metadata_fields = custom_metadata_fields

        self.create = async_to_raw_response_wrapper(
            custom_metadata_fields.create,
        )
        self.update = async_to_raw_response_wrapper(
            custom_metadata_fields.update,
        )
        self.list = async_to_raw_response_wrapper(
            custom_metadata_fields.list,
        )
        self.delete = async_to_raw_response_wrapper(
            custom_metadata_fields.delete,
        )


class CustomMetadataFieldsResourceWithStreamingResponse:
    def __init__(self, custom_metadata_fields: CustomMetadataFieldsResource) -> None:
        self._custom_metadata_fields = custom_metadata_fields

        self.create = to_streamed_response_wrapper(
            custom_metadata_fields.create,
        )
        self.update = to_streamed_response_wrapper(
            custom_metadata_fields.update,
        )
        self.list = to_streamed_response_wrapper(
            custom_metadata_fields.list,
        )
        self.delete = to_streamed_response_wrapper(
            custom_metadata_fields.delete,
        )


class AsyncCustomMetadataFieldsResourceWithStreamingResponse:
    def __init__(self, custom_metadata_fields: AsyncCustomMetadataFieldsResource) -> None:
        self._custom_metadata_fields = custom_metadata_fields

        self.create = async_to_streamed_response_wrapper(
            custom_metadata_fields.create,
        )
        self.update = async_to_streamed_response_wrapper(
            custom_metadata_fields.update,
        )
        self.list = async_to_streamed_response_wrapper(
            custom_metadata_fields.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            custom_metadata_fields.delete,
        )
