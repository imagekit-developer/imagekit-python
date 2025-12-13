# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Mapping, Optional, cast
from typing_extensions import Literal, overload

import httpx

from .bulk import (
    BulkResource,
    AsyncBulkResource,
    BulkResourceWithRawResponse,
    AsyncBulkResourceWithRawResponse,
    BulkResourceWithStreamingResponse,
    AsyncBulkResourceWithStreamingResponse,
)
from ...types import (
    file_copy_params,
    file_move_params,
    file_rename_params,
    file_update_params,
    file_upload_params,
)
from ..._types import (
    Body,
    Omit,
    Query,
    Headers,
    NoneType,
    NotGiven,
    FileTypes,
    SequenceNotStr,
    omit,
    not_given,
)
from ..._utils import extract_files, maybe_transform, deepcopy_minimal, async_maybe_transform
from .metadata import (
    MetadataResource,
    AsyncMetadataResource,
    MetadataResourceWithRawResponse,
    AsyncMetadataResourceWithRawResponse,
    MetadataResourceWithStreamingResponse,
    AsyncMetadataResourceWithStreamingResponse,
)
from .versions import (
    VersionsResource,
    AsyncVersionsResource,
    VersionsResourceWithRawResponse,
    AsyncVersionsResourceWithRawResponse,
    VersionsResourceWithStreamingResponse,
    AsyncVersionsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...types.file import File
from ..._base_client import make_request_options
from ...lib.serialization_utils import serialize_upload_options
from ...types.file_copy_response import FileCopyResponse
from ...types.file_move_response import FileMoveResponse
from ...types.file_rename_response import FileRenameResponse
from ...types.file_update_response import FileUpdateResponse
from ...types.file_upload_response import FileUploadResponse
from ...types.shared_params.extensions import Extensions

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def bulk(self) -> BulkResource:
        return BulkResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

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

    @overload
    def update(
        self,
        file_id: str,
        *,
        custom_coordinates: Optional[str] | Omit = omit,
        custom_metadata: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        extensions: Extensions | Omit = omit,
        remove_ai_tags: Union[SequenceNotStr[str], Literal["all"]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
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

          description: Optional text to describe the contents of the file.

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
        publish: file_update_params.ChangePublicationStatusPublish | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
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
        custom_coordinates: Optional[str] | Omit = omit,
        custom_metadata: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        extensions: Extensions | Omit = omit,
        remove_ai_tags: Union[SequenceNotStr[str], Literal["all"]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_url: str | Omit = omit,
        publish: file_update_params.ChangePublicationStatusPublish | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return self._patch(
            f"/v1/files/{file_id}/details",
            body=maybe_transform(
                {
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
                    "description": description,
                    "extensions": extensions,
                    "remove_ai_tags": remove_ai_tags,
                    "tags": tags,
                    "webhook_url": webhook_url,
                    "publish": publish,
                },
                file_update_params.FileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUpdateResponse,
        )

    def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        This API deletes the file and all its file versions permanently.

        Note: If a file or specific transformation has been requested in the past, then
        the response is cached. Deleting a file does not purge the cache. You can purge
        the cache using purge cache API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/v1/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def copy(
        self,
        *,
        destination_path: str,
        source_file_path: str,
        include_file_versions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCopyResponse:
        """
        This will copy a file from one folder to another.

        Note: If any file at the destination has the same name as the source file, then
        the source file and its versions (if `includeFileVersions` is set to true) will
        be appended to the destination file version history.

        Args:
          destination_path: Full path to the folder you want to copy the above file into.

          source_file_path: The full path of the file you want to copy.

          include_file_versions: Option to copy all versions of a file. By default, only the current version of
              the file is copied. When set to true, all versions of the file will be copied.
              Default value - `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/copy",
            body=maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_file_path": source_file_path,
                    "include_file_versions": include_file_versions,
                },
                file_copy_params.FileCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCopyResponse,
        )

    def get(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
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
            cast_to=File,
        )

    def move(
        self,
        *,
        destination_path: str,
        source_file_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMoveResponse:
        """
        This will move a file and all its versions from one folder to another.

        Note: If any file at the destination has the same name as the source file, then
        the source file and its versions will be appended to the destination file.

        Args:
          destination_path: Full path to the folder you want to move the above file into.

          source_file_path: The full path of the file you want to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/move",
            body=maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_file_path": source_file_path,
                },
                file_move_params.FileMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileMoveResponse,
        )

    def rename(
        self,
        *,
        file_path: str,
        new_file_name: str,
        purge_cache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRenameResponse:
        """
        You can rename an already existing file in the media library using rename file
        API. This operation would rename all file versions of the file.

        Note: The old URLs will stop working. The file/file version URLs cached on CDN
        will continue to work unless a purge is requested.

        Args:
          file_path: The full path of the file you want to rename.

          new_file_name:
              The new name of the file. A filename can contain:

              Alphanumeric Characters: `a-z`, `A-Z`, `0-9` (including Unicode letters, marks,
              and numerals in other languages). Special Characters: `.`, `_`, and `-`.

              Any other character, including space, will be replaced by `_`.

          purge_cache: Option to purge cache for the old file and its versions' URLs.

              When set to true, it will internally issue a purge cache request on CDN to
              remove cached content of old file and its versions. This purge request is
              counted against your monthly purge quota.

              Note: If the old file were accessible at
              `https://ik.imagekit.io/demo/old-filename.jpg`, a purge cache request would be
              issued against `https://ik.imagekit.io/demo/old-filename.jpg*` (with a wildcard
              at the end). It will remove the file and its versions' URLs and any
              transformations made using query parameters on this file or its versions.
              However, the cache for file transformations made using path parameters will
              persist. You can purge them using the purge API. For more details, refer to the
              purge API documentation.

              Default value - `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/v1/files/rename",
            body=maybe_transform(
                {
                    "file_path": file_path,
                    "new_file_name": new_file_name,
                    "purge_cache": purge_cache,
                },
                file_rename_params.FileRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRenameResponse,
        )

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
        expire: int | Omit = omit,
        extensions: Extensions | Omit = omit,
        folder: str | Omit = omit,
        is_private_file: bool | Omit = omit,
        is_published: bool | Omit = omit,
        overwrite_ai_tags: bool | Omit = omit,
        overwrite_custom_metadata: bool | Omit = omit,
        overwrite_file: bool | Omit = omit,
        overwrite_tags: bool | Omit = omit,
        public_key: str | Omit = omit,
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
        signature: str | Omit = omit,
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
        """
        ImageKit.io allows you to upload files directly from both the server and client
        sides. For server-side uploads, private API key authentication is used. For
        client-side uploads, generate a one-time `token`, `signature`, and `expire` from
        your secure backend using private API.
        [Learn more](/docs/api-reference/upload-file/upload-file#how-to-implement-client-side-file-upload)
        about how to implement client-side file upload.

        The [V2 API](/docs/api-reference/upload-file/upload-file-v2) enhances security
        by verifying the entire payload using JWT.

        **File size limit** \\
        On the free plan, the maximum upload file sizes are 20MB for images, audio, and raw
        files and 100MB for videos. On the paid plan, these limits increase to 40MB for images,
        audio, and raw files and 2GB for videos. These limits can be further increased with
        higher-tier plans.

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

          file_name:
              The name with which the file has to be uploaded. The file name can contain:

              - Alphanumeric Characters: `a-z`, `A-Z`, `0-9`.
              - Special Characters: `.`, `-`

              Any other character including space will be replaced by `_`

          token: A unique value that the ImageKit.io server will use to recognize and prevent
              subsequent retries for the same request. We suggest using V4 UUIDs, or another
              random string with enough entropy to avoid collisions. This field is only
              required for authentication when uploading a file from the client side.

              **Note**: Sending a value that has been used in the past will result in a
              validation error. Even if your previous request resulted in an error, you should
              always send a new value for this field.

          checks: Server-side checks to run on the asset. Read more about
              [Upload API checks](/docs/api-reference/upload-file/upload-file#upload-api-checks).

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

          expire: The time until your signature is valid. It must be a
              [Unix time](https://en.wikipedia.org/wiki/Unix_time) in less than 1 hour into
              the future. It should be in seconds. This field is only required for
              authentication when uploading a file from the client side.

          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          folder: The folder path in which the image has to be uploaded. If the folder(s) didn't
              exist before, a new folder(s) is created.

              The folder name can contain:

              - Alphanumeric Characters: `a-z` , `A-Z` , `0-9`
              - Special Characters: `/` , `_` , `-`

              Using multiple `/` creates a nested folder.

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

          public_key: Your ImageKit.io public key. This field is only required for authentication when
              uploading a file from the client side.

          response_fields: Array of response field keys to include in the API response body.

          signature: HMAC-SHA1 digest of the token+expire using your ImageKit.io private API key as a
              key. Learn how to create a signature on the page below. This should be in
              lowercase.

              Signature must be calculated on the server-side. This field is only required for
              authentication when uploading a file from the client side.

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
                "expire": expire,
                "extensions": extensions,
                "folder": folder,
                "is_private_file": is_private_file,
                "is_published": is_published,
                "overwrite_ai_tags": overwrite_ai_tags,
                "overwrite_custom_metadata": overwrite_custom_metadata,
                "overwrite_file": overwrite_file,
                "overwrite_tags": overwrite_tags,
                "public_key": public_key,
                "response_fields": response_fields,
                "signature": signature,
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
            "/api/v1/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v1/files/upload",
            body=maybe_transform(body, file_upload_params.FileUploadParams),
            files=files,
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadResponse,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def bulk(self) -> AsyncBulkResource:
        return AsyncBulkResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

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

    @overload
    async def update(
        self,
        file_id: str,
        *,
        custom_coordinates: Optional[str] | Omit = omit,
        custom_metadata: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        extensions: Extensions | Omit = omit,
        remove_ai_tags: Union[SequenceNotStr[str], Literal["all"]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_url: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
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

          description: Optional text to describe the contents of the file.

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
        publish: file_update_params.ChangePublicationStatusPublish | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
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
        custom_coordinates: Optional[str] | Omit = omit,
        custom_metadata: Dict[str, object] | Omit = omit,
        description: str | Omit = omit,
        extensions: Extensions | Omit = omit,
        remove_ai_tags: Union[SequenceNotStr[str], Literal["all"]] | Omit = omit,
        tags: Optional[SequenceNotStr[str]] | Omit = omit,
        webhook_url: str | Omit = omit,
        publish: file_update_params.ChangePublicationStatusPublish | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileUpdateResponse:
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        return await self._patch(
            f"/v1/files/{file_id}/details",
            body=await async_maybe_transform(
                {
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
                    "description": description,
                    "extensions": extensions,
                    "remove_ai_tags": remove_ai_tags,
                    "tags": tags,
                    "webhook_url": webhook_url,
                    "publish": publish,
                },
                file_update_params.FileUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUpdateResponse,
        )

    async def delete(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        This API deletes the file and all its file versions permanently.

        Note: If a file or specific transformation has been requested in the past, then
        the response is cached. Deleting a file does not purge the cache. You can purge
        the cache using purge cache API.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not file_id:
            raise ValueError(f"Expected a non-empty value for `file_id` but received {file_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/v1/files/{file_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def copy(
        self,
        *,
        destination_path: str,
        source_file_path: str,
        include_file_versions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileCopyResponse:
        """
        This will copy a file from one folder to another.

        Note: If any file at the destination has the same name as the source file, then
        the source file and its versions (if `includeFileVersions` is set to true) will
        be appended to the destination file version history.

        Args:
          destination_path: Full path to the folder you want to copy the above file into.

          source_file_path: The full path of the file you want to copy.

          include_file_versions: Option to copy all versions of a file. By default, only the current version of
              the file is copied. When set to true, all versions of the file will be copied.
              Default value - `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/copy",
            body=await async_maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_file_path": source_file_path,
                    "include_file_versions": include_file_versions,
                },
                file_copy_params.FileCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileCopyResponse,
        )

    async def get(
        self,
        file_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> File:
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
            cast_to=File,
        )

    async def move(
        self,
        *,
        destination_path: str,
        source_file_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileMoveResponse:
        """
        This will move a file and all its versions from one folder to another.

        Note: If any file at the destination has the same name as the source file, then
        the source file and its versions will be appended to the destination file.

        Args:
          destination_path: Full path to the folder you want to move the above file into.

          source_file_path: The full path of the file you want to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/move",
            body=await async_maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_file_path": source_file_path,
                },
                file_move_params.FileMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileMoveResponse,
        )

    async def rename(
        self,
        *,
        file_path: str,
        new_file_name: str,
        purge_cache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FileRenameResponse:
        """
        You can rename an already existing file in the media library using rename file
        API. This operation would rename all file versions of the file.

        Note: The old URLs will stop working. The file/file version URLs cached on CDN
        will continue to work unless a purge is requested.

        Args:
          file_path: The full path of the file you want to rename.

          new_file_name:
              The new name of the file. A filename can contain:

              Alphanumeric Characters: `a-z`, `A-Z`, `0-9` (including Unicode letters, marks,
              and numerals in other languages). Special Characters: `.`, `_`, and `-`.

              Any other character, including space, will be replaced by `_`.

          purge_cache: Option to purge cache for the old file and its versions' URLs.

              When set to true, it will internally issue a purge cache request on CDN to
              remove cached content of old file and its versions. This purge request is
              counted against your monthly purge quota.

              Note: If the old file were accessible at
              `https://ik.imagekit.io/demo/old-filename.jpg`, a purge cache request would be
              issued against `https://ik.imagekit.io/demo/old-filename.jpg*` (with a wildcard
              at the end). It will remove the file and its versions' URLs and any
              transformations made using query parameters on this file or its versions.
              However, the cache for file transformations made using path parameters will
              persist. You can purge them using the purge API. For more details, refer to the
              purge API documentation.

              Default value - `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/v1/files/rename",
            body=await async_maybe_transform(
                {
                    "file_path": file_path,
                    "new_file_name": new_file_name,
                    "purge_cache": purge_cache,
                },
                file_rename_params.FileRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRenameResponse,
        )

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
        expire: int | Omit = omit,
        extensions: Extensions | Omit = omit,
        folder: str | Omit = omit,
        is_private_file: bool | Omit = omit,
        is_published: bool | Omit = omit,
        overwrite_ai_tags: bool | Omit = omit,
        overwrite_custom_metadata: bool | Omit = omit,
        overwrite_file: bool | Omit = omit,
        overwrite_tags: bool | Omit = omit,
        public_key: str | Omit = omit,
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
        signature: str | Omit = omit,
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
        """
        ImageKit.io allows you to upload files directly from both the server and client
        sides. For server-side uploads, private API key authentication is used. For
        client-side uploads, generate a one-time `token`, `signature`, and `expire` from
        your secure backend using private API.
        [Learn more](/docs/api-reference/upload-file/upload-file#how-to-implement-client-side-file-upload)
        about how to implement client-side file upload.

        The [V2 API](/docs/api-reference/upload-file/upload-file-v2) enhances security
        by verifying the entire payload using JWT.

        **File size limit** \\
        On the free plan, the maximum upload file sizes are 20MB for images, audio, and raw
        files and 100MB for videos. On the paid plan, these limits increase to 40MB for images,
        audio, and raw files and 2GB for videos. These limits can be further increased with
        higher-tier plans.

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

          file_name:
              The name with which the file has to be uploaded. The file name can contain:

              - Alphanumeric Characters: `a-z`, `A-Z`, `0-9`.
              - Special Characters: `.`, `-`

              Any other character including space will be replaced by `_`

          token: A unique value that the ImageKit.io server will use to recognize and prevent
              subsequent retries for the same request. We suggest using V4 UUIDs, or another
              random string with enough entropy to avoid collisions. This field is only
              required for authentication when uploading a file from the client side.

              **Note**: Sending a value that has been used in the past will result in a
              validation error. Even if your previous request resulted in an error, you should
              always send a new value for this field.

          checks: Server-side checks to run on the asset. Read more about
              [Upload API checks](/docs/api-reference/upload-file/upload-file#upload-api-checks).

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

          expire: The time until your signature is valid. It must be a
              [Unix time](https://en.wikipedia.org/wiki/Unix_time) in less than 1 hour into
              the future. It should be in seconds. This field is only required for
              authentication when uploading a file from the client side.

          extensions: Array of extensions to be applied to the asset. Each extension can be configured
              with specific parameters based on the extension type.

          folder: The folder path in which the image has to be uploaded. If the folder(s) didn't
              exist before, a new folder(s) is created.

              The folder name can contain:

              - Alphanumeric Characters: `a-z` , `A-Z` , `0-9`
              - Special Characters: `/` , `_` , `-`

              Using multiple `/` creates a nested folder.

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

          public_key: Your ImageKit.io public key. This field is only required for authentication when
              uploading a file from the client side.

          response_fields: Array of response field keys to include in the API response body.

          signature: HMAC-SHA1 digest of the token+expire using your ImageKit.io private API key as a
              key. Learn how to create a signature on the page below. This should be in
              lowercase.

              Signature must be calculated on the server-side. This field is only required for
              authentication when uploading a file from the client side.

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
                "expire": expire,
                "extensions": extensions,
                "folder": folder,
                "is_private_file": is_private_file,
                "is_published": is_published,
                "overwrite_ai_tags": overwrite_ai_tags,
                "overwrite_custom_metadata": overwrite_custom_metadata,
                "overwrite_file": overwrite_file,
                "overwrite_tags": overwrite_tags,
                "public_key": public_key,
                "response_fields": response_fields,
                "signature": signature,
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
            "/api/v1/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v1/files/upload",
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

        self.update = to_raw_response_wrapper(
            files.update,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.copy = to_raw_response_wrapper(
            files.copy,
        )
        self.get = to_raw_response_wrapper(
            files.get,
        )
        self.move = to_raw_response_wrapper(
            files.move,
        )
        self.rename = to_raw_response_wrapper(
            files.rename,
        )
        self.upload = to_raw_response_wrapper(
            files.upload,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithRawResponse:
        return BulkResourceWithRawResponse(self._files.bulk)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._files.versions)

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._files.metadata)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.update = async_to_raw_response_wrapper(
            files.update,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.copy = async_to_raw_response_wrapper(
            files.copy,
        )
        self.get = async_to_raw_response_wrapper(
            files.get,
        )
        self.move = async_to_raw_response_wrapper(
            files.move,
        )
        self.rename = async_to_raw_response_wrapper(
            files.rename,
        )
        self.upload = async_to_raw_response_wrapper(
            files.upload,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithRawResponse:
        return AsyncBulkResourceWithRawResponse(self._files.bulk)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._files.versions)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._files.metadata)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.update = to_streamed_response_wrapper(
            files.update,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.copy = to_streamed_response_wrapper(
            files.copy,
        )
        self.get = to_streamed_response_wrapper(
            files.get,
        )
        self.move = to_streamed_response_wrapper(
            files.move,
        )
        self.rename = to_streamed_response_wrapper(
            files.rename,
        )
        self.upload = to_streamed_response_wrapper(
            files.upload,
        )

    @cached_property
    def bulk(self) -> BulkResourceWithStreamingResponse:
        return BulkResourceWithStreamingResponse(self._files.bulk)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._files.versions)

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._files.metadata)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.update = async_to_streamed_response_wrapper(
            files.update,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.copy = async_to_streamed_response_wrapper(
            files.copy,
        )
        self.get = async_to_streamed_response_wrapper(
            files.get,
        )
        self.move = async_to_streamed_response_wrapper(
            files.move,
        )
        self.rename = async_to_streamed_response_wrapper(
            files.rename,
        )
        self.upload = async_to_streamed_response_wrapper(
            files.upload,
        )

    @cached_property
    def bulk(self) -> AsyncBulkResourceWithStreamingResponse:
        return AsyncBulkResourceWithStreamingResponse(self._files.bulk)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._files.versions)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._files.metadata)
