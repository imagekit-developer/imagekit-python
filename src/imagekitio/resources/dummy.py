# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..types import dummy_create_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.shared_params.overlay import Overlay
from ..types.shared_params.extensions import Extensions
from ..types.shared_params.src_options import SrcOptions
from ..types.shared_params.base_overlay import BaseOverlay
from ..types.shared_params.text_overlay import TextOverlay
from ..types.shared.streaming_resolution import StreamingResolution
from ..types.shared_params.image_overlay import ImageOverlay
from ..types.shared_params.video_overlay import VideoOverlay
from ..types.shared_params.overlay_timing import OverlayTiming
from ..types.shared_params.transformation import Transformation
from ..types.shared.transformation_position import TransformationPosition
from ..types.shared_params.overlay_position import OverlayPosition
from ..types.shared_params.subtitle_overlay import SubtitleOverlay
from ..types.shared_params.solid_color_overlay import SolidColorOverlay
from ..types.shared_params.responsive_image_attributes import ResponsiveImageAttributes
from ..types.shared_params.text_overlay_transformation import TextOverlayTransformation
from ..types.shared_params.get_image_attributes_options import GetImageAttributesOptions
from ..types.shared_params.subtitle_overlay_transformation import SubtitleOverlayTransformation
from ..types.shared_params.solid_color_overlay_transformation import SolidColorOverlayTransformation

__all__ = ["DummyResource", "AsyncDummyResource"]


class DummyResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DummyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return DummyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DummyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return DummyResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        base_overlay: BaseOverlay | Omit = omit,
        extensions: Extensions | Omit = omit,
        get_image_attributes_options: GetImageAttributesOptions | Omit = omit,
        image_overlay: ImageOverlay | Omit = omit,
        overlay: Overlay | Omit = omit,
        overlay_position: OverlayPosition | Omit = omit,
        overlay_timing: OverlayTiming | Omit = omit,
        responsive_image_attributes: ResponsiveImageAttributes | Omit = omit,
        solid_color_overlay: SolidColorOverlay | Omit = omit,
        solid_color_overlay_transformation: SolidColorOverlayTransformation | Omit = omit,
        src_options: SrcOptions | Omit = omit,
        streaming_resolution: StreamingResolution | Omit = omit,
        subtitle_overlay: SubtitleOverlay | Omit = omit,
        subtitle_overlay_transformation: SubtitleOverlayTransformation | Omit = omit,
        text_overlay: TextOverlay | Omit = omit,
        text_overlay_transformation: TextOverlayTransformation | Omit = omit,
        transformation: Transformation | Omit = omit,
        transformation_position: TransformationPosition | Omit = omit,
        video_overlay: VideoOverlay | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Internal test endpoint for SDK generation purposes only.

        This endpoint
        demonstrates usage of all shared models defined in the Stainless configuration
        and is not intended for public consumption.

        Args:
          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          get_image_attributes_options: Options for generating responsive image attributes including `src`, `srcSet`,
              and `sizes` for HTML `<img>` elements. This schema extends `SrcOptions` to add
              support for responsive image generation with breakpoints.

          overlay: Specifies an overlay to be applied on the parent image or video. ImageKit
              supports overlays including images, text, videos, subtitles, and solid colors.
              See
              [Overlay using layers](https://imagekit.io/docs/transformations#overlay-using-layers).

          responsive_image_attributes: Resulting set of attributes suitable for an HTML `<img>` element. Useful for
              enabling responsive image loading with `srcSet` and `sizes`.

          src_options: Options for generating ImageKit URLs with transformations. See the
              [Transformations guide](https://imagekit.io/docs/transformations).

          streaming_resolution: Available streaming resolutions for
              [adaptive bitrate streaming](https://imagekit.io/docs/adaptive-bitrate-streaming)

          subtitle_overlay_transformation: Subtitle styling options.
              [Learn more](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
              from the docs.

          transformation: The SDK provides easy-to-use names for transformations. These names are
              converted to the corresponding transformation string before being added to the
              URL. SDKs are updated regularly to support new transformations. If you want to
              use a transformation that is not supported by the SDK, You can use the `raw`
              parameter to pass the transformation string directly. See the
              [Transformations documentation](https://imagekit.io/docs/transformations).

          transformation_position: By default, the transformation string is added as a query parameter in the URL,
              e.g., `?tr=w-100,h-100`. If you want to add the transformation string in the
              path of the URL, set this to `path`. Learn more in the
              [Transformations guide](https://imagekit.io/docs/transformations).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._post(
            "/v1/dummy/test",
            body=maybe_transform(
                {
                    "base_overlay": base_overlay,
                    "extensions": extensions,
                    "get_image_attributes_options": get_image_attributes_options,
                    "image_overlay": image_overlay,
                    "overlay": overlay,
                    "overlay_position": overlay_position,
                    "overlay_timing": overlay_timing,
                    "responsive_image_attributes": responsive_image_attributes,
                    "solid_color_overlay": solid_color_overlay,
                    "solid_color_overlay_transformation": solid_color_overlay_transformation,
                    "src_options": src_options,
                    "streaming_resolution": streaming_resolution,
                    "subtitle_overlay": subtitle_overlay,
                    "subtitle_overlay_transformation": subtitle_overlay_transformation,
                    "text_overlay": text_overlay,
                    "text_overlay_transformation": text_overlay_transformation,
                    "transformation": transformation,
                    "transformation_position": transformation_position,
                    "video_overlay": video_overlay,
                },
                dummy_create_params.DummyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncDummyResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDummyResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDummyResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDummyResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncDummyResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        base_overlay: BaseOverlay | Omit = omit,
        extensions: Extensions | Omit = omit,
        get_image_attributes_options: GetImageAttributesOptions | Omit = omit,
        image_overlay: ImageOverlay | Omit = omit,
        overlay: Overlay | Omit = omit,
        overlay_position: OverlayPosition | Omit = omit,
        overlay_timing: OverlayTiming | Omit = omit,
        responsive_image_attributes: ResponsiveImageAttributes | Omit = omit,
        solid_color_overlay: SolidColorOverlay | Omit = omit,
        solid_color_overlay_transformation: SolidColorOverlayTransformation | Omit = omit,
        src_options: SrcOptions | Omit = omit,
        streaming_resolution: StreamingResolution | Omit = omit,
        subtitle_overlay: SubtitleOverlay | Omit = omit,
        subtitle_overlay_transformation: SubtitleOverlayTransformation | Omit = omit,
        text_overlay: TextOverlay | Omit = omit,
        text_overlay_transformation: TextOverlayTransformation | Omit = omit,
        transformation: Transformation | Omit = omit,
        transformation_position: TransformationPosition | Omit = omit,
        video_overlay: VideoOverlay | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """Internal test endpoint for SDK generation purposes only.

        This endpoint
        demonstrates usage of all shared models defined in the Stainless configuration
        and is not intended for public consumption.

        Args:
          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          get_image_attributes_options: Options for generating responsive image attributes including `src`, `srcSet`,
              and `sizes` for HTML `<img>` elements. This schema extends `SrcOptions` to add
              support for responsive image generation with breakpoints.

          overlay: Specifies an overlay to be applied on the parent image or video. ImageKit
              supports overlays including images, text, videos, subtitles, and solid colors.
              See
              [Overlay using layers](https://imagekit.io/docs/transformations#overlay-using-layers).

          responsive_image_attributes: Resulting set of attributes suitable for an HTML `<img>` element. Useful for
              enabling responsive image loading with `srcSet` and `sizes`.

          src_options: Options for generating ImageKit URLs with transformations. See the
              [Transformations guide](https://imagekit.io/docs/transformations).

          streaming_resolution: Available streaming resolutions for
              [adaptive bitrate streaming](https://imagekit.io/docs/adaptive-bitrate-streaming)

          subtitle_overlay_transformation: Subtitle styling options.
              [Learn more](https://imagekit.io/docs/add-overlays-on-videos#styling-controls-for-subtitles-layer)
              from the docs.

          transformation: The SDK provides easy-to-use names for transformations. These names are
              converted to the corresponding transformation string before being added to the
              URL. SDKs are updated regularly to support new transformations. If you want to
              use a transformation that is not supported by the SDK, You can use the `raw`
              parameter to pass the transformation string directly. See the
              [Transformations documentation](https://imagekit.io/docs/transformations).

          transformation_position: By default, the transformation string is added as a query parameter in the URL,
              e.g., `?tr=w-100,h-100`. If you want to add the transformation string in the
              path of the URL, set this to `path`. Learn more in the
              [Transformations guide](https://imagekit.io/docs/transformations).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._post(
            "/v1/dummy/test",
            body=await async_maybe_transform(
                {
                    "base_overlay": base_overlay,
                    "extensions": extensions,
                    "get_image_attributes_options": get_image_attributes_options,
                    "image_overlay": image_overlay,
                    "overlay": overlay,
                    "overlay_position": overlay_position,
                    "overlay_timing": overlay_timing,
                    "responsive_image_attributes": responsive_image_attributes,
                    "solid_color_overlay": solid_color_overlay,
                    "solid_color_overlay_transformation": solid_color_overlay_transformation,
                    "src_options": src_options,
                    "streaming_resolution": streaming_resolution,
                    "subtitle_overlay": subtitle_overlay,
                    "subtitle_overlay_transformation": subtitle_overlay_transformation,
                    "text_overlay": text_overlay,
                    "text_overlay_transformation": text_overlay_transformation,
                    "transformation": transformation,
                    "transformation_position": transformation_position,
                    "video_overlay": video_overlay,
                },
                dummy_create_params.DummyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class DummyResourceWithRawResponse:
    def __init__(self, dummy: DummyResource) -> None:
        self._dummy = dummy

        self.create = to_raw_response_wrapper(
            dummy.create,
        )


class AsyncDummyResourceWithRawResponse:
    def __init__(self, dummy: AsyncDummyResource) -> None:
        self._dummy = dummy

        self.create = async_to_raw_response_wrapper(
            dummy.create,
        )


class DummyResourceWithStreamingResponse:
    def __init__(self, dummy: DummyResource) -> None:
        self._dummy = dummy

        self.create = to_streamed_response_wrapper(
            dummy.create,
        )


class AsyncDummyResourceWithStreamingResponse:
    def __init__(self, dummy: AsyncDummyResource) -> None:
        self._dummy = dummy

        self.create = async_to_streamed_response_wrapper(
            dummy.create,
        )
