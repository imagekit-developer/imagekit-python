# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Iterable, Optional
from typing_extensions import Literal, overload

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.files import detail_update_params
from ..._base_client import make_request_options
from ...types.files.detail_update_response import DetailUpdateResponse
from ...types.files.detail_retrieve_response import DetailRetrieveResponse

__all__ = ["DetailsResource", "AsyncDetailsResource"]


class DetailsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return DetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return DetailsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveResponse:
        """
        This API returns an object with details or attributes about the current version
        of the file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._get(
            f"/v1/files/{file_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveResponse,
        )

    @overload
    def update(
        self,
        file_id: str,
        *,
        custom_coordinates: Optional[str] | NotGiven = NOT_GIVEN,
        custom_metadata: object | NotGiven = NOT_GIVEN,
        extensions: Iterable[detail_update_params.UpdateFileDetailsExtension] | NotGiven = NOT_GIVEN,
        remove_ai_tags: Union[List[str], Literal["all"]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailUpdateResponse:
        """
        This API updates the details or attributes of the current version of the file.
        You can update `tags`, `customCoordinates`, `customMetadata`, publication
        status, remove existing `AITags` and apply extensions using this API.

        Args:
          custom_coordinates: Define an important area in the image in the format `x,y,width,height` e.g.
              `10,10,100,100`. Send `null` to unset this value.

          custom_metadata: A key-value data to be associated with the asset. To unset a key, send `null`
              value for that key. Before setting any custom metadata on an asset you have to
              create the field using custom metadata fields API.

          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          remove_ai_tags: An array of AITags associated with the file that you want to remove, e.g.
              `["car", "vehicle", "motorsports"]`.

              If you want to remove all AITags associated with the file, send a string -
              "all".

              Note: The remove operation for `AITags` executes before any of the `extensions`
              are processed.

          tags: An array of tags associated with the file, such as `["tag1", "tag2"]`. Send
              `null` to unset all tags associated with the file.

          webhook_url: The final status of extensions after they have completed execution will be
              delivered to this endpoint as a POST request.
              [Learn more](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#webhook-payload-structure)
              about the webhook payload structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    def update(
        self,
        file_id: str,
        *,
        publish: detail_update_params.ChangePublicationStatusPublish | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailUpdateResponse:
        """
        This API updates the details or attributes of the current version of the file.
        You can update `tags`, `customCoordinates`, `customMetadata`, publication
        status, remove existing `AITags` and apply extensions using this API.

        Args:
          publish: Configure the publication status of a file and its versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    def update(
        self,
        file_id: str,
        *,
        custom_coordinates: Optional[str] | NotGiven = NOT_GIVEN,
        custom_metadata: object | NotGiven = NOT_GIVEN,
        extensions: Iterable[detail_update_params.UpdateFileDetailsExtension] | NotGiven = NOT_GIVEN,
        remove_ai_tags: Union[List[str], Literal["all"]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        publish: detail_update_params.ChangePublicationStatusPublish | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailUpdateResponse:
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/v1/files/{file_id}/details",
            body=maybe_transform(
                {
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
                    "extensions": extensions,
                    "remove_ai_tags": remove_ai_tags,
                    "tags": tags,
                    "webhook_url": webhook_url,
                    "publish": publish,
                },
                detail_update_params.DetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailUpdateResponse,
        )


class AsyncDetailsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetailsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetailsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetailsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return AsyncDetailsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailRetrieveResponse:
        """
        This API returns an object with details or attributes about the current version
        of the file.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._get(
            f"/v1/files/{file_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailRetrieveResponse,
        )

    @overload
    async def update(
        self,
        file_id: str,
        *,
        custom_coordinates: Optional[str] | NotGiven = NOT_GIVEN,
        custom_metadata: object | NotGiven = NOT_GIVEN,
        extensions: Iterable[detail_update_params.UpdateFileDetailsExtension] | NotGiven = NOT_GIVEN,
        remove_ai_tags: Union[List[str], Literal["all"]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailUpdateResponse:
        """
        This API updates the details or attributes of the current version of the file.
        You can update `tags`, `customCoordinates`, `customMetadata`, publication
        status, remove existing `AITags` and apply extensions using this API.

        Args:
          custom_coordinates: Define an important area in the image in the format `x,y,width,height` e.g.
              `10,10,100,100`. Send `null` to unset this value.

          custom_metadata: A key-value data to be associated with the asset. To unset a key, send `null`
              value for that key. Before setting any custom metadata on an asset you have to
              create the field using custom metadata fields API.

          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          remove_ai_tags: An array of AITags associated with the file that you want to remove, e.g.
              `["car", "vehicle", "motorsports"]`.

              If you want to remove all AITags associated with the file, send a string -
              "all".

              Note: The remove operation for `AITags` executes before any of the `extensions`
              are processed.

          tags: An array of tags associated with the file, such as `["tag1", "tag2"]`. Send
              `null` to unset all tags associated with the file.

          webhook_url: The final status of extensions after they have completed execution will be
              delivered to this endpoint as a POST request.
              [Learn more](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#webhook-payload-structure)
              about the webhook payload structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    @overload
    async def update(
        self,
        file_id: str,
        *,
        publish: detail_update_params.ChangePublicationStatusPublish | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailUpdateResponse:
        """
        This API updates the details or attributes of the current version of the file.
        You can update `tags`, `customCoordinates`, `customMetadata`, publication
        status, remove existing `AITags` and apply extensions using this API.

        Args:
          publish: Configure the publication status of a file and its versions.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        ...

    async def update(
        self,
        file_id: str,
        *,
        custom_coordinates: Optional[str] | NotGiven = NOT_GIVEN,
        custom_metadata: object | NotGiven = NOT_GIVEN,
        extensions: Iterable[detail_update_params.UpdateFileDetailsExtension] | NotGiven = NOT_GIVEN,
        remove_ai_tags: Union[List[str], Literal["all"]] | NotGiven = NOT_GIVEN,
        tags: Optional[List[str]] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        publish: detail_update_params.ChangePublicationStatusPublish | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetailUpdateResponse:
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/v1/files/{file_id}/details",
            body=await async_maybe_transform(
                {
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
                    "extensions": extensions,
                    "remove_ai_tags": remove_ai_tags,
                    "tags": tags,
                    "webhook_url": webhook_url,
                    "publish": publish,
                },
                detail_update_params.DetailUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DetailUpdateResponse,
        )


class DetailsResourceWithRawResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.retrieve = to_raw_response_wrapper(
            details.retrieve,
        )
        self.update = to_raw_response_wrapper(
            details.update,
        )


class AsyncDetailsResourceWithRawResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.retrieve = async_to_raw_response_wrapper(
            details.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            details.update,
        )


class DetailsResourceWithStreamingResponse:
    def __init__(self, details: DetailsResource) -> None:
        self._details = details

        self.retrieve = to_streamed_response_wrapper(
            details.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            details.update,
        )


class AsyncDetailsResourceWithStreamingResponse:
    def __init__(self, details: AsyncDetailsResource) -> None:
        self._details = details

        self.retrieve = async_to_streamed_response_wrapper(
            details.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            details.update,
        )
