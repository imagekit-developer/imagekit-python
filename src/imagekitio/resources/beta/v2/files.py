# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Mapping, cast
from typing_extensions import Literal

import httpx

from ...._types import (
    Body,
    Omit,
    Query,
    Headers,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ...._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.beta.v2 import file_upload_params
from ....lib.serialization_utils import serialize_upload_options
from ....types.shared_params.extensions import Extensions
from ....types.beta.v2.file_upload_response import FileUploadResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def upload(
        self,
        *,
        file: FileTypes,
        file_name: str,
        token: str | Omit = omit,
        checks: str | Omit = omit,
        custom_coordinates: str | Omit = omit,
        custom_metadata: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        extensions: Extensions | Omit = omit,
        folder: str | Omit = omit,
        is_private_file: bool | Omit = omit,
        is_published: bool | Omit = omit,
        overwrite_ai_tags: bool | Omit = omit,
        overwrite_custom_metadata: bool | Omit = omit,
        overwrite_file: bool | Omit = omit,
        overwrite_tags: bool | Omit = omit,
        response_fields: List[
            Literal[
                "tags",
                "customCoordinates",
                "isPrivateFile",
                "embeddedMetadata",
                "isPublished",
                "customMetadata",
                "metadata",
                "selectedFieldsSchema",
            ]
        ]
        | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transformation: file_upload_params.Transformation | Omit = omit,
        use_unique_file_name: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUploadResponse:
        """The V2 API enhances security by verifying the entire payload using JWT.

        This API
        is in beta.

        ImageKit.io allows you to upload files directly from both the server and client
        sides. For server-side uploads, private API key authentication is used. For
        client-side uploads, generate a one-time `token` from your secure backend using
        private API.
        [Learn more](/docs/api-reference/upload-file/upload-file-v2#how-to-implement-secure-client-side-file-upload)
        about how to implement secure client-side file upload.

        **File size limit** \\
        On the free plan, the maximum upload file sizes are 20MB for images, audio, and raw
        files, and 100MB for videos. On the paid plan, these limits increase to 40MB for
        images, audio, and raw files, and 2GB for videos. These limits can be further increased
        with higher-tier plans.

        **Version limit** \\
        A file can have a maximum of 100 versions.

        **Demo applications**

        - A full-fledged
          [upload widget using Uppy](https://github.com/imagekit-samples/uppy-uploader),
          supporting file selections from local storage, URL, Dropbox, Google Drive,
          Instagram, and more.
        - [Quick start guides](/docs/quick-start-guides) for various frameworks and
          technologies.

        Args:
          file:
              The API accepts any of the following:

              - **Binary data** – send the raw bytes as `multipart/form-data`.
              - **HTTP / HTTPS URL** – a publicly reachable URL that ImageKit’s servers can
                fetch.
              - **Base64 string** – the file encoded as a Base64 data URI or plain Base64.

              When supplying a URL, the server must receive the response headers within 8
              seconds; otherwise the request fails with 400 Bad Request.

          file_name: The name with which the file has to be uploaded.

          token: This is the client-generated JSON Web Token (JWT). The ImageKit.io server uses
              it to authenticate and check that the upload request parameters have not been
              tampered with after the token has been generated. Learn how to create the token
              on the page below. This field is only required for authentication when uploading
              a file from the client side.

              **Note**: Sending a JWT that has been used in the past will result in a
              validation error. Even if your previous request resulted in an error, you should
              always send a new token.

              **⚠️Warning**: JWT must be generated on the server-side because it is generated
              using your account's private API key. This field is required for authentication
              when uploading a file from the client-side.

          checks: Server-side checks to run on the asset. Read more about
              [Upload API checks](/docs/api-reference/upload-file/upload-file-v2#upload-api-checks).

          custom_coordinates: Define an important area in the image. This is only relevant for image type
              files.

              - To be passed as a string with the x and y coordinates of the top-left corner,
                and width and height of the area of interest in the format `x,y,width,height`.
                For example - `10,10,100,100`
              - Can be used with fo-customtransformation.
              - If this field is not specified and the file is overwritten, then
                customCoordinates will be removed.

          custom_metadata: JSON key-value pairs to associate with the asset. Create the custom metadata
              fields before setting these values.

          description: Optional text to describe the contents of the file.

          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          folder: The folder path in which the image has to be uploaded. If the folder(s) didn't
              exist before, a new folder(s) is created. Using multiple `/` creates a nested
              folder.

          is_private_file: Whether to mark the file as private or not.

              If `true`, the file is marked as private and is accessible only using named
              transformation or signed URL.

          is_published: Whether to upload file as published or not.

              If `false`, the file is marked as unpublished, which restricts access to the
              file only via the media library. Files in draft or unpublished state can only be
              publicly accessed after being published.

              The option to upload in draft state is only available in custom enterprise
              pricing plans.

          overwrite_ai_tags: If set to `true` and a file already exists at the exact location, its AITags
              will be removed. Set `overwriteAITags` to `false` to preserve AITags.

          overwrite_custom_metadata: If the request does not have `customMetadata`, and a file already exists at the
              exact location, existing customMetadata will be removed.

          overwrite_file: If `false` and `useUniqueFileName` is also `false`, and a file already exists at
              the exact location, upload API will return an error immediately.

          overwrite_tags: If the request does not have `tags`, and a file already exists at the exact
              location, existing tags will be removed.

          response_fields: Array of response field keys to include in the API response body.

          tags: Set the tags while uploading the file. Provide an array of tag strings (e.g.
              `["tag1", "tag2", "tag3"]`). The combined length of all tag characters must not
              exceed 500, and the `%` character is not allowed. If this field is not specified
              and the file is overwritten, the existing tags will be removed.

          transformation: Configure pre-processing (`pre`) and post-processing (`post`) transformations.

              - `pre` — applied before the file is uploaded to the Media Library.
                Useful for reducing file size or applying basic optimizations upfront (e.g.,
                resize, compress).

              - `post` — applied immediately after upload.
                Ideal for generating transformed versions (like video encodes or thumbnails)
                in advance, so they're ready for delivery without delay.

              You can mix and match any combination of post-processing types.

          use_unique_file_name: Whether to use a unique filename for this file or not.

              If `true`, ImageKit.io will add a unique suffix to the filename parameter to get
              a unique filename.

              If `false`, then the image is uploaded with the provided filename parameter, and
              any existing file with the same name is replaced.

          webhook_url: The final status of extensions after they have completed execution will be
              delivered to this endpoint as a POST request.
              [Learn more](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#webhook-payload-structure)
              about the webhook payload structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "file_name": file_name,
                "token": token,
                "checks": checks,
                "custom_coordinates": custom_coordinates,
                "custom_metadata": custom_metadata,
                "description": description,
                "extensions": extensions,
                "folder": folder,
                "is_private_file": is_private_file,
                "is_published": is_published,
                "overwrite_ai_tags": overwrite_ai_tags,
                "overwrite_custom_metadata": overwrite_custom_metadata,
                "overwrite_file": overwrite_file,
                "overwrite_tags": overwrite_tags,
                "response_fields": response_fields,
                "tags": tags,
                "transformation": transformation,
                "use_unique_file_name": use_unique_file_name,
                "webhook_url": webhook_url,
            }
        )
        body = serialize_upload_options(body)
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v2/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v2/files/upload",
            body=maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def upload(
        self,
        *,
        file: FileTypes,
        file_name: str,
        token: str | Omit = omit,
        checks: str | Omit = omit,
        custom_coordinates: str | Omit = omit,
        custom_metadata: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        extensions: Extensions | Omit = omit,
        folder: str | Omit = omit,
        is_private_file: bool | Omit = omit,
        is_published: bool | Omit = omit,
        overwrite_ai_tags: bool | Omit = omit,
        overwrite_custom_metadata: bool | Omit = omit,
        overwrite_file: bool | Omit = omit,
        overwrite_tags: bool | Omit = omit,
        response_fields: List[
            Literal[
                "tags",
                "customCoordinates",
                "isPrivateFile",
                "embeddedMetadata",
                "isPublished",
                "customMetadata",
                "metadata",
                "selectedFieldsSchema",
            ]
        ]
        | Omit = omit,
        tags: SequenceNotStr[str] | Omit = omit,
        transformation: file_upload_params.Transformation | Omit = omit,
        use_unique_file_name: bool | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUploadResponse:
        """The V2 API enhances security by verifying the entire payload using JWT.

        This API
        is in beta.

        ImageKit.io allows you to upload files directly from both the server and client
        sides. For server-side uploads, private API key authentication is used. For
        client-side uploads, generate a one-time `token` from your secure backend using
        private API.
        [Learn more](/docs/api-reference/upload-file/upload-file-v2#how-to-implement-secure-client-side-file-upload)
        about how to implement secure client-side file upload.

        **File size limit** \\
        On the free plan, the maximum upload file sizes are 20MB for images, audio, and raw
        files, and 100MB for videos. On the paid plan, these limits increase to 40MB for
        images, audio, and raw files, and 2GB for videos. These limits can be further increased
        with higher-tier plans.

        **Version limit** \\
        A file can have a maximum of 100 versions.

        **Demo applications**

        - A full-fledged
          [upload widget using Uppy](https://github.com/imagekit-samples/uppy-uploader),
          supporting file selections from local storage, URL, Dropbox, Google Drive,
          Instagram, and more.
        - [Quick start guides](/docs/quick-start-guides) for various frameworks and
          technologies.

        Args:
          file:
              The API accepts any of the following:

              - **Binary data** – send the raw bytes as `multipart/form-data`.
              - **HTTP / HTTPS URL** – a publicly reachable URL that ImageKit’s servers can
                fetch.
              - **Base64 string** – the file encoded as a Base64 data URI or plain Base64.

              When supplying a URL, the server must receive the response headers within 8
              seconds; otherwise the request fails with 400 Bad Request.

          file_name: The name with which the file has to be uploaded.

          token: This is the client-generated JSON Web Token (JWT). The ImageKit.io server uses
              it to authenticate and check that the upload request parameters have not been
              tampered with after the token has been generated. Learn how to create the token
              on the page below. This field is only required for authentication when uploading
              a file from the client side.

              **Note**: Sending a JWT that has been used in the past will result in a
              validation error. Even if your previous request resulted in an error, you should
              always send a new token.

              **⚠️Warning**: JWT must be generated on the server-side because it is generated
              using your account's private API key. This field is required for authentication
              when uploading a file from the client-side.

          checks: Server-side checks to run on the asset. Read more about
              [Upload API checks](/docs/api-reference/upload-file/upload-file-v2#upload-api-checks).

          custom_coordinates: Define an important area in the image. This is only relevant for image type
              files.

              - To be passed as a string with the x and y coordinates of the top-left corner,
                and width and height of the area of interest in the format `x,y,width,height`.
                For example - `10,10,100,100`
              - Can be used with fo-customtransformation.
              - If this field is not specified and the file is overwritten, then
                customCoordinates will be removed.

          custom_metadata: JSON key-value pairs to associate with the asset. Create the custom metadata
              fields before setting these values.

          description: Optional text to describe the contents of the file.

          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          folder: The folder path in which the image has to be uploaded. If the folder(s) didn't
              exist before, a new folder(s) is created. Using multiple `/` creates a nested
              folder.

          is_private_file: Whether to mark the file as private or not.

              If `true`, the file is marked as private and is accessible only using named
              transformation or signed URL.

          is_published: Whether to upload file as published or not.

              If `false`, the file is marked as unpublished, which restricts access to the
              file only via the media library. Files in draft or unpublished state can only be
              publicly accessed after being published.

              The option to upload in draft state is only available in custom enterprise
              pricing plans.

          overwrite_ai_tags: If set to `true` and a file already exists at the exact location, its AITags
              will be removed. Set `overwriteAITags` to `false` to preserve AITags.

          overwrite_custom_metadata: If the request does not have `customMetadata`, and a file already exists at the
              exact location, existing customMetadata will be removed.

          overwrite_file: If `false` and `useUniqueFileName` is also `false`, and a file already exists at
              the exact location, upload API will return an error immediately.

          overwrite_tags: If the request does not have `tags`, and a file already exists at the exact
              location, existing tags will be removed.

          response_fields: Array of response field keys to include in the API response body.

          tags: Set the tags while uploading the file. Provide an array of tag strings (e.g.
              `["tag1", "tag2", "tag3"]`). The combined length of all tag characters must not
              exceed 500, and the `%` character is not allowed. If this field is not specified
              and the file is overwritten, the existing tags will be removed.

          transformation: Configure pre-processing (`pre`) and post-processing (`post`) transformations.

              - `pre` — applied before the file is uploaded to the Media Library.
                Useful for reducing file size or applying basic optimizations upfront (e.g.,
                resize, compress).

              - `post` — applied immediately after upload.
                Ideal for generating transformed versions (like video encodes or thumbnails)
                in advance, so they're ready for delivery without delay.

              You can mix and match any combination of post-processing types.

          use_unique_file_name: Whether to use a unique filename for this file or not.

              If `true`, ImageKit.io will add a unique suffix to the filename parameter to get
              a unique filename.

              If `false`, then the image is uploaded with the provided filename parameter, and
              any existing file with the same name is replaced.

          webhook_url: The final status of extensions after they have completed execution will be
              delivered to this endpoint as a POST request.
              [Learn more](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#webhook-payload-structure)
              about the webhook payload structure.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        body = deepcopy_minimal(
            {
                "file": file,
                "file_name": file_name,
                "token": token,
                "checks": checks,
                "custom_coordinates": custom_coordinates,
                "custom_metadata": custom_metadata,
                "description": description,
                "extensions": extensions,
                "folder": folder,
                "is_private_file": is_private_file,
                "is_published": is_published,
                "overwrite_ai_tags": overwrite_ai_tags,
                "overwrite_custom_metadata": overwrite_custom_metadata,
                "overwrite_file": overwrite_file,
                "overwrite_tags": overwrite_tags,
                "response_fields": response_fields,
                "tags": tags,
                "transformation": transformation,
                "use_unique_file_name": use_unique_file_name,
                "webhook_url": webhook_url,
            }
        )
        body = serialize_upload_options(body)
        files = extract_files(cast(Mapping[str, object], body), paths=[["file"]])
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v2/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v2/files/upload",
            body=await async_maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadResponse,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.upload = to_raw_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.upload = async_to_raw_response_wrapper(
            files.upload,
        )


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.upload = to_streamed_response_wrapper(
            files.upload,
        )


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.upload = async_to_streamed_response_wrapper(
            files.upload,
        )
