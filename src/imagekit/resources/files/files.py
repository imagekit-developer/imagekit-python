# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List
from typing_extensions import Literal

import httpx

from .batch import (
    BatchResource,
    AsyncBatchResource,
    BatchResourceWithRawResponse,
    AsyncBatchResourceWithRawResponse,
    BatchResourceWithStreamingResponse,
    AsyncBatchResourceWithStreamingResponse,
)
from .purge import (
    PurgeResource,
    AsyncPurgeResource,
    PurgeResourceWithRawResponse,
    AsyncPurgeResourceWithRawResponse,
    PurgeResourceWithStreamingResponse,
    AsyncPurgeResourceWithStreamingResponse,
)
from ...types import (
    file_copy_params,
    file_list_params,
    file_move_params,
    file_rename_params,
    file_add_tags_params,
    file_upload_v1_params,
    file_upload_v2_params,
    file_remove_tags_params,
    file_remove_ai_tags_params,
)
from .details import (
    DetailsResource,
    AsyncDetailsResource,
    DetailsResourceWithRawResponse,
    AsyncDetailsResourceWithRawResponse,
    DetailsResourceWithStreamingResponse,
    AsyncDetailsResourceWithStreamingResponse,
)
from ..._types import NOT_GIVEN, Body, Query, Headers, NoneType, NotGiven
from ..._utils import maybe_transform, async_maybe_transform
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
from ..._base_client import make_request_options
from ...types.file_list_response import FileListResponse
from ...types.file_rename_response import FileRenameResponse
from ...types.file_add_tags_response import FileAddTagsResponse
from ...types.file_upload_v1_response import FileUploadV1Response
from ...types.file_upload_v2_response import FileUploadV2Response
from ...types.file_remove_tags_response import FileRemoveTagsResponse
from ...types.file_remove_ai_tags_response import FileRemoveAITagsResponse

__all__ = ["FilesResource", "AsyncFilesResource"]


class FilesResource(SyncAPIResource):
    @cached_property
    def details(self) -> DetailsResource:
        return DetailsResource(self._client)

    @cached_property
    def batch(self) -> BatchResource:
        return BatchResource(self._client)

    @cached_property
    def versions(self) -> VersionsResource:
        return VersionsResource(self._client)

    @cached_property
    def purge(self) -> PurgeResource:
        return PurgeResource(self._client)

    @cached_property
    def metadata(self) -> MetadataResource:
        return MetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> FilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return FilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return FilesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        file_type: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        search_query: str | NotGiven = NOT_GIVEN,
        skip: str | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        type: Literal["file", "file-version", "folder", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        This API can list all the uploaded files and folders in your ImageKit.io media
        library. In addition, you can fine-tune your query by specifying various filters
        by generating a query string in a Lucene-like syntax and provide this generated
        string as the value of the `searchQuery`.

        Args:
          file_type:
              Type of files to include in the result set. Accepts three values:

              `all` - include all types of files in the result set. `image` - only search in
              image type files. `non-image` - only search in files that are not images, e.g.,
              JS or CSS or video files.

              Default value - `all`

          limit:
              The maximum number of results to return in response:

              Minimum value - 1

              Maximum value - 1000

              Default value - 1000

          path: Folder path if you want to limit the search within a specific folder. For
              example, `/sales-banner/` will only search in folder sales-banner.

          search_query: Query string in a Lucene-like query language e.g. `createdAt > "7d"`.

              Note : When the searchQuery parameter is present, the following query parameters
              will have no effect on the result:

              1. `tags`
              2. `type`
              3. `name`

              [Learn more](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#advanced-search-queries)
              from examples.

          skip:
              The number of results to skip before returning results:

              Minimum value - 0

              Default value - 0

          sort:
              You can sort based on the following fields:

              1. name - `ASC_NAME` or `DESC_NAME`
              2. createdAt - `ASC_CREATED` or `DESC_CREATED`
              3. updatedAt - `ASC_UPDATED` or `DESC_UPDATED`
              4. height - `ASC_HEIGHT` or `DESC_HEIGHT`
              5. width - `ASC_WIDTH` or `DESC_WIDTH`
              6. size - `ASC_SIZE` or `DESC_SIZE`

              Default value - `ASC_CREATED`

          type: Limit search to one of `file`, `file-version`, or `folder`. Pass `all` to
              include `files` and `folders` in search results (`file-version` will not be
              included in this case).

              Default value - `file`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "file_type": file_type,
                        "limit": limit,
                        "path": path,
                        "search_query": search_query,
                        "skip": skip,
                        "sort": sort,
                        "type": type,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def add_tags(
        self,
        *,
        file_ids: List[str],
        tags: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileAddTagsResponse:
        """This API adds tags to multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds to which you want to add tags.

          tags: An array of tags that you want to add to the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/addTags",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                file_add_tags_params.FileAddTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileAddTagsResponse,
        )

    def copy(
        self,
        *,
        destination_path: str,
        source_file_path: str,
        include_file_versions: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            cast_to=object,
        )

    def remove_ai_tags(
        self,
        *,
        ai_tags: List[str],
        file_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileRemoveAITagsResponse:
        """This API removes AITags from multiple files in bulk.

        A maximum of 50 files can
        be specified at a time.

        Args:
          ai_tags: An array of AITags that you want to remove from the files.

          file_ids: An array of fileIds from which you want to remove AITags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/removeAITags",
            body=maybe_transform(
                {
                    "ai_tags": ai_tags,
                    "file_ids": file_ids,
                },
                file_remove_ai_tags_params.FileRemoveAITagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRemoveAITagsResponse,
        )

    def remove_tags(
        self,
        *,
        file_ids: List[str],
        tags: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileRemoveTagsResponse:
        """This API removes tags from multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds from which you want to remove tags.

          tags: An array of tags that you want to remove from the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/files/removeTags",
            body=maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                file_remove_tags_params.FileRemoveTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRemoveTagsResponse,
        )

    def rename(
        self,
        *,
        file_path: str,
        new_file_name: str,
        purge_cache: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    def upload_v1(
        self,
        *,
        file: str,
        file_name: str,
        token: str | NotGiven = NOT_GIVEN,
        checks: str | NotGiven = NOT_GIVEN,
        custom_coordinates: str | NotGiven = NOT_GIVEN,
        custom_metadata: str | NotGiven = NOT_GIVEN,
        expire: str | NotGiven = NOT_GIVEN,
        extensions: str | NotGiven = NOT_GIVEN,
        folder: str | NotGiven = NOT_GIVEN,
        is_private_file: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        is_published: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_ai_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_custom_metadata: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_file: str | NotGiven = NOT_GIVEN,
        overwrite_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        public_key: str | NotGiven = NOT_GIVEN,
        response_fields: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        transformation: str | NotGiven = NOT_GIVEN,
        use_unique_file_name: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileUploadV1Response:
        """
        ImageKit.io allows you to upload files directly from both the server and client
        sides. For server-side uploads, private API key authentication is used. For
        client-side uploads, generate a one-time `token`, `signature`, and `expiration`
        from your secure backend using private API.
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
          file: Pass the HTTP URL or base64 string. When passing a URL in the file parameter,
              please ensure that our servers can access the URL. In case ImageKit is unable to
              download the file from the specified URL, a `400` error response is returned.
              This will also result in a `400` error if the file download request is aborted
              if response headers are not received in 8 seconds.

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

          custom_metadata: Stringified JSON key-value data to be associated with the asset.

          expire: The time until your signature is valid. It must be a
              [Unix time](https://en.wikipedia.org/wiki/Unix_time) in less than 1 hour into
              the future. It should be in seconds. This field is only required for
              authentication when uploading a file from the client side.

          extensions: Stringified JSON object with an array of extensions to be applied to the image.
              Refer to extensions schema in
              [update file API request body](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#request-body).

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

          response_fields: Comma-separated values of the fields that you want the API to return in the
              response.

              For example, set the value of this field to
              `tags,customCoordinates,isPrivateFile` to get the value of `tags`,
              `customCoordinates`, and `isPrivateFile` in the response.

              Accepts combination of `tags`, `customCoordinates`, `isPrivateFile`,
              `embeddedMetadata`, `isPublished`, `customMetadata`, and `metadata`.

          signature: HMAC-SHA1 digest of the token+expire using your ImageKit.io private API key as a
              key. Learn how to create a signature on the page below. This should be in
              lowercase.

              Signature must be calculated on the server-side. This field is only required for
              authentication when uploading a file from the client side.

          tags: Set the tags while uploading the file.

              Comma-separated value of tags in the format `tag1,tag2,tag3`. The maximum length
              of all characters should not exceed 500. `%` is not allowed.

              If this field is not specified and the file is overwritten then the tags will be
              removed.

          transformation:
              Stringified JSON object with properties for pre and post transformations:

              `pre` - Accepts a "string" containing a valid transformation used for requesting
              a pre-transformation for an image or a video file.

              `post` - Accepts an array of objects with properties:

              - `type`: One of `transformation`, `gif-to-video`, `thumbnail`, or `abs`
                (Adaptive bitrate streaming).
              - `value`: A "string" corresponding to the required transformation. Required if
                `type` is `transformation` or `abs`. Optional if `type` is `gif-to-video` or
                `thumbnail`.
              - `protocol`: Either `hls` or `dash`, applicable only if `type` is `abs`.

              Read more about
              [Adaptive bitrate streaming (ABS)](/docs/adaptive-bitrate-streaming).

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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v1/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v1/files/upload",
            body=maybe_transform(
                {
                    "file": file,
                    "file_name": file_name,
                    "token": token,
                    "checks": checks,
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
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
                },
                file_upload_v1_params.FileUploadV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadV1Response,
        )

    def upload_v2(
        self,
        *,
        file: str,
        file_name: str,
        token: str | NotGiven = NOT_GIVEN,
        checks: str | NotGiven = NOT_GIVEN,
        custom_coordinates: str | NotGiven = NOT_GIVEN,
        custom_metadata: str | NotGiven = NOT_GIVEN,
        extensions: str | NotGiven = NOT_GIVEN,
        folder: str | NotGiven = NOT_GIVEN,
        is_private_file: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        is_published: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_ai_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_custom_metadata: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_file: str | NotGiven = NOT_GIVEN,
        overwrite_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        response_fields: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        transformation: str | NotGiven = NOT_GIVEN,
        use_unique_file_name: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileUploadV2Response:
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
          file: Pass the HTTP URL or base64 string. When passing a URL in the file parameter,
              please ensure that our servers can access the URL. In case ImageKit is unable to
              download the file from the specified URL, a `400` error response is returned.
              This will also result in a `400` error if the file download request is aborted
              if response headers are not received in 8 seconds.

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

          custom_metadata: Stringified JSON key-value data to be associated with the asset.

          extensions: Stringified JSON object with an array of extensions to be applied to the image.
              Refer to extensions schema in
              [update file API request body](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#request-body).

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

          response_fields: Comma-separated values of the fields that you want the API to return in the
              response.

              For example, set the value of this field to
              `tags,customCoordinates,isPrivateFile` to get the value of `tags`,
              `customCoordinates`, and `isPrivateFile` in the response.

              Accepts combination of `tags`, `customCoordinates`, `isPrivateFile`,
              `embeddedMetadata`, `isPublished`, `customMetadata`, and `metadata`.

          tags: Set the tags while uploading the file.

              Comma-separated value of tags in the format `tag1,tag2,tag3`. The maximum length
              of all characters should not exceed 500. `%` is not allowed.

              If this field is not specified and the file is overwritten then the tags will be
              removed.

          transformation:
              Stringified JSON object with properties for pre and post transformations:

              `pre` - Accepts a "string" containing a valid transformation used for requesting
              a pre-transformation for an image or a video file.

              `post` - Accepts an array of objects with properties:

              - `type`: One of `transformation`, `gif-to-video`, `thumbnail`, or `abs`
                (Adaptive bitrate streaming).
              - `value`: A "string" corresponding to the required transformation. Required if
                `type` is `transformation` or `abs`. Optional if `type` is `gif-to-video` or
                `thumbnail`.
              - `protocol`: Either `hls` or `dash`, applicable only if `type` is `abs`.

              Read more about
              [Adaptive bitrate streaming (ABS)](/docs/adaptive-bitrate-streaming).

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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return self._post(
            "/api/v2/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v2/files/upload",
            body=maybe_transform(
                {
                    "file": file,
                    "file_name": file_name,
                    "token": token,
                    "checks": checks,
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
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
                },
                file_upload_v2_params.FileUploadV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadV2Response,
        )


class AsyncFilesResource(AsyncAPIResource):
    @cached_property
    def details(self) -> AsyncDetailsResource:
        return AsyncDetailsResource(self._client)

    @cached_property
    def batch(self) -> AsyncBatchResource:
        return AsyncBatchResource(self._client)

    @cached_property
    def versions(self) -> AsyncVersionsResource:
        return AsyncVersionsResource(self._client)

    @cached_property
    def purge(self) -> AsyncPurgeResource:
        return AsyncPurgeResource(self._client)

    @cached_property
    def metadata(self) -> AsyncMetadataResource:
        return AsyncMetadataResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFilesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFilesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFilesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/imagekit-python#with_streaming_response
        """
        return AsyncFilesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        file_type: str | NotGiven = NOT_GIVEN,
        limit: str | NotGiven = NOT_GIVEN,
        path: str | NotGiven = NOT_GIVEN,
        search_query: str | NotGiven = NOT_GIVEN,
        skip: str | NotGiven = NOT_GIVEN,
        sort: str | NotGiven = NOT_GIVEN,
        type: Literal["file", "file-version", "folder", "all"] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileListResponse:
        """
        This API can list all the uploaded files and folders in your ImageKit.io media
        library. In addition, you can fine-tune your query by specifying various filters
        by generating a query string in a Lucene-like syntax and provide this generated
        string as the value of the `searchQuery`.

        Args:
          file_type:
              Type of files to include in the result set. Accepts three values:

              `all` - include all types of files in the result set. `image` - only search in
              image type files. `non-image` - only search in files that are not images, e.g.,
              JS or CSS or video files.

              Default value - `all`

          limit:
              The maximum number of results to return in response:

              Minimum value - 1

              Maximum value - 1000

              Default value - 1000

          path: Folder path if you want to limit the search within a specific folder. For
              example, `/sales-banner/` will only search in folder sales-banner.

          search_query: Query string in a Lucene-like query language e.g. `createdAt > "7d"`.

              Note : When the searchQuery parameter is present, the following query parameters
              will have no effect on the result:

              1. `tags`
              2. `type`
              3. `name`

              [Learn more](/docs/api-reference/digital-asset-management-dam/list-and-search-assets#advanced-search-queries)
              from examples.

          skip:
              The number of results to skip before returning results:

              Minimum value - 0

              Default value - 0

          sort:
              You can sort based on the following fields:

              1. name - `ASC_NAME` or `DESC_NAME`
              2. createdAt - `ASC_CREATED` or `DESC_CREATED`
              3. updatedAt - `ASC_UPDATED` or `DESC_UPDATED`
              4. height - `ASC_HEIGHT` or `DESC_HEIGHT`
              5. width - `ASC_WIDTH` or `DESC_WIDTH`
              6. size - `ASC_SIZE` or `DESC_SIZE`

              Default value - `ASC_CREATED`

          type: Limit search to one of `file`, `file-version`, or `folder`. Pass `all` to
              include `files` and `folders` in search results (`file-version` will not be
              included in this case).

              Default value - `file`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/v1/files",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "file_type": file_type,
                        "limit": limit,
                        "path": path,
                        "search_query": search_query,
                        "skip": skip,
                        "sort": sort,
                        "type": type,
                    },
                    file_list_params.FileListParams,
                ),
            ),
            cast_to=FileListResponse,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def add_tags(
        self,
        *,
        file_ids: List[str],
        tags: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileAddTagsResponse:
        """This API adds tags to multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds to which you want to add tags.

          tags: An array of tags that you want to add to the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/addTags",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                file_add_tags_params.FileAddTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileAddTagsResponse,
        )

    async def copy(
        self,
        *,
        destination_path: str,
        source_file_path: str,
        include_file_versions: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            cast_to=object,
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
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> object:
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
            cast_to=object,
        )

    async def remove_ai_tags(
        self,
        *,
        ai_tags: List[str],
        file_ids: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileRemoveAITagsResponse:
        """This API removes AITags from multiple files in bulk.

        A maximum of 50 files can
        be specified at a time.

        Args:
          ai_tags: An array of AITags that you want to remove from the files.

          file_ids: An array of fileIds from which you want to remove AITags.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/removeAITags",
            body=await async_maybe_transform(
                {
                    "ai_tags": ai_tags,
                    "file_ids": file_ids,
                },
                file_remove_ai_tags_params.FileRemoveAITagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRemoveAITagsResponse,
        )

    async def remove_tags(
        self,
        *,
        file_ids: List[str],
        tags: List[str],
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileRemoveTagsResponse:
        """This API removes tags from multiple files in bulk.

        A maximum of 50 files can be
        specified at a time.

        Args:
          file_ids: An array of fileIds from which you want to remove tags.

          tags: An array of tags that you want to remove from the files.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/files/removeTags",
            body=await async_maybe_transform(
                {
                    "file_ids": file_ids,
                    "tags": tags,
                },
                file_remove_tags_params.FileRemoveTagsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileRemoveTagsResponse,
        )

    async def rename(
        self,
        *,
        file_path: str,
        new_file_name: str,
        purge_cache: bool | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
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

    async def upload_v1(
        self,
        *,
        file: str,
        file_name: str,
        token: str | NotGiven = NOT_GIVEN,
        checks: str | NotGiven = NOT_GIVEN,
        custom_coordinates: str | NotGiven = NOT_GIVEN,
        custom_metadata: str | NotGiven = NOT_GIVEN,
        expire: str | NotGiven = NOT_GIVEN,
        extensions: str | NotGiven = NOT_GIVEN,
        folder: str | NotGiven = NOT_GIVEN,
        is_private_file: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        is_published: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_ai_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_custom_metadata: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_file: str | NotGiven = NOT_GIVEN,
        overwrite_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        public_key: str | NotGiven = NOT_GIVEN,
        response_fields: str | NotGiven = NOT_GIVEN,
        signature: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        transformation: str | NotGiven = NOT_GIVEN,
        use_unique_file_name: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileUploadV1Response:
        """
        ImageKit.io allows you to upload files directly from both the server and client
        sides. For server-side uploads, private API key authentication is used. For
        client-side uploads, generate a one-time `token`, `signature`, and `expiration`
        from your secure backend using private API.
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
          file: Pass the HTTP URL or base64 string. When passing a URL in the file parameter,
              please ensure that our servers can access the URL. In case ImageKit is unable to
              download the file from the specified URL, a `400` error response is returned.
              This will also result in a `400` error if the file download request is aborted
              if response headers are not received in 8 seconds.

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

          custom_metadata: Stringified JSON key-value data to be associated with the asset.

          expire: The time until your signature is valid. It must be a
              [Unix time](https://en.wikipedia.org/wiki/Unix_time) in less than 1 hour into
              the future. It should be in seconds. This field is only required for
              authentication when uploading a file from the client side.

          extensions: Stringified JSON object with an array of extensions to be applied to the image.
              Refer to extensions schema in
              [update file API request body](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#request-body).

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

          response_fields: Comma-separated values of the fields that you want the API to return in the
              response.

              For example, set the value of this field to
              `tags,customCoordinates,isPrivateFile` to get the value of `tags`,
              `customCoordinates`, and `isPrivateFile` in the response.

              Accepts combination of `tags`, `customCoordinates`, `isPrivateFile`,
              `embeddedMetadata`, `isPublished`, `customMetadata`, and `metadata`.

          signature: HMAC-SHA1 digest of the token+expire using your ImageKit.io private API key as a
              key. Learn how to create a signature on the page below. This should be in
              lowercase.

              Signature must be calculated on the server-side. This field is only required for
              authentication when uploading a file from the client side.

          tags: Set the tags while uploading the file.

              Comma-separated value of tags in the format `tag1,tag2,tag3`. The maximum length
              of all characters should not exceed 500. `%` is not allowed.

              If this field is not specified and the file is overwritten then the tags will be
              removed.

          transformation:
              Stringified JSON object with properties for pre and post transformations:

              `pre` - Accepts a "string" containing a valid transformation used for requesting
              a pre-transformation for an image or a video file.

              `post` - Accepts an array of objects with properties:

              - `type`: One of `transformation`, `gif-to-video`, `thumbnail`, or `abs`
                (Adaptive bitrate streaming).
              - `value`: A "string" corresponding to the required transformation. Required if
                `type` is `transformation` or `abs`. Optional if `type` is `gif-to-video` or
                `thumbnail`.
              - `protocol`: Either `hls` or `dash`, applicable only if `type` is `abs`.

              Read more about
              [Adaptive bitrate streaming (ABS)](/docs/adaptive-bitrate-streaming).

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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v1/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v1/files/upload",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "file_name": file_name,
                    "token": token,
                    "checks": checks,
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
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
                },
                file_upload_v1_params.FileUploadV1Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadV1Response,
        )

    async def upload_v2(
        self,
        *,
        file: str,
        file_name: str,
        token: str | NotGiven = NOT_GIVEN,
        checks: str | NotGiven = NOT_GIVEN,
        custom_coordinates: str | NotGiven = NOT_GIVEN,
        custom_metadata: str | NotGiven = NOT_GIVEN,
        extensions: str | NotGiven = NOT_GIVEN,
        folder: str | NotGiven = NOT_GIVEN,
        is_private_file: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        is_published: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_ai_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_custom_metadata: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        overwrite_file: str | NotGiven = NOT_GIVEN,
        overwrite_tags: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        response_fields: str | NotGiven = NOT_GIVEN,
        tags: str | NotGiven = NOT_GIVEN,
        transformation: str | NotGiven = NOT_GIVEN,
        use_unique_file_name: Literal["true", "false"] | NotGiven = NOT_GIVEN,
        webhook_url: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FileUploadV2Response:
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
          file: Pass the HTTP URL or base64 string. When passing a URL in the file parameter,
              please ensure that our servers can access the URL. In case ImageKit is unable to
              download the file from the specified URL, a `400` error response is returned.
              This will also result in a `400` error if the file download request is aborted
              if response headers are not received in 8 seconds.

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

          custom_metadata: Stringified JSON key-value data to be associated with the asset.

          extensions: Stringified JSON object with an array of extensions to be applied to the image.
              Refer to extensions schema in
              [update file API request body](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#request-body).

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

          response_fields: Comma-separated values of the fields that you want the API to return in the
              response.

              For example, set the value of this field to
              `tags,customCoordinates,isPrivateFile` to get the value of `tags`,
              `customCoordinates`, and `isPrivateFile` in the response.

              Accepts combination of `tags`, `customCoordinates`, `isPrivateFile`,
              `embeddedMetadata`, `isPublished`, `customMetadata`, and `metadata`.

          tags: Set the tags while uploading the file.

              Comma-separated value of tags in the format `tag1,tag2,tag3`. The maximum length
              of all characters should not exceed 500. `%` is not allowed.

              If this field is not specified and the file is overwritten then the tags will be
              removed.

          transformation:
              Stringified JSON object with properties for pre and post transformations:

              `pre` - Accepts a "string" containing a valid transformation used for requesting
              a pre-transformation for an image or a video file.

              `post` - Accepts an array of objects with properties:

              - `type`: One of `transformation`, `gif-to-video`, `thumbnail`, or `abs`
                (Adaptive bitrate streaming).
              - `value`: A "string" corresponding to the required transformation. Required if
                `type` is `transformation` or `abs`. Optional if `type` is `gif-to-video` or
                `thumbnail`.
              - `protocol`: Either `hls` or `dash`, applicable only if `type` is `abs`.

              Read more about
              [Adaptive bitrate streaming (ABS)](/docs/adaptive-bitrate-streaming).

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
        # It should be noted that the actual Content-Type header that will be
        # sent to the server will contain a `boundary` parameter, e.g.
        # multipart/form-data; boundary=---abc--
        extra_headers = {"Content-Type": "multipart/form-data", **(extra_headers or {})}
        return await self._post(
            "/api/v2/files/upload"
            if self._client._base_url_overridden
            else "https://upload.imagekit.io/api/v2/files/upload",
            body=await async_maybe_transform(
                {
                    "file": file,
                    "file_name": file_name,
                    "token": token,
                    "checks": checks,
                    "custom_coordinates": custom_coordinates,
                    "custom_metadata": custom_metadata,
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
                },
                file_upload_v2_params.FileUploadV2Params,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FileUploadV2Response,
        )


class FilesResourceWithRawResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_raw_response_wrapper(
            files.list,
        )
        self.delete = to_raw_response_wrapper(
            files.delete,
        )
        self.add_tags = to_raw_response_wrapper(
            files.add_tags,
        )
        self.copy = to_raw_response_wrapper(
            files.copy,
        )
        self.move = to_raw_response_wrapper(
            files.move,
        )
        self.remove_ai_tags = to_raw_response_wrapper(
            files.remove_ai_tags,
        )
        self.remove_tags = to_raw_response_wrapper(
            files.remove_tags,
        )
        self.rename = to_raw_response_wrapper(
            files.rename,
        )
        self.upload_v1 = to_raw_response_wrapper(
            files.upload_v1,
        )
        self.upload_v2 = to_raw_response_wrapper(
            files.upload_v2,
        )

    @cached_property
    def details(self) -> DetailsResourceWithRawResponse:
        return DetailsResourceWithRawResponse(self._files.details)

    @cached_property
    def batch(self) -> BatchResourceWithRawResponse:
        return BatchResourceWithRawResponse(self._files.batch)

    @cached_property
    def versions(self) -> VersionsResourceWithRawResponse:
        return VersionsResourceWithRawResponse(self._files.versions)

    @cached_property
    def purge(self) -> PurgeResourceWithRawResponse:
        return PurgeResourceWithRawResponse(self._files.purge)

    @cached_property
    def metadata(self) -> MetadataResourceWithRawResponse:
        return MetadataResourceWithRawResponse(self._files.metadata)


class AsyncFilesResourceWithRawResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_raw_response_wrapper(
            files.list,
        )
        self.delete = async_to_raw_response_wrapper(
            files.delete,
        )
        self.add_tags = async_to_raw_response_wrapper(
            files.add_tags,
        )
        self.copy = async_to_raw_response_wrapper(
            files.copy,
        )
        self.move = async_to_raw_response_wrapper(
            files.move,
        )
        self.remove_ai_tags = async_to_raw_response_wrapper(
            files.remove_ai_tags,
        )
        self.remove_tags = async_to_raw_response_wrapper(
            files.remove_tags,
        )
        self.rename = async_to_raw_response_wrapper(
            files.rename,
        )
        self.upload_v1 = async_to_raw_response_wrapper(
            files.upload_v1,
        )
        self.upload_v2 = async_to_raw_response_wrapper(
            files.upload_v2,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithRawResponse:
        return AsyncDetailsResourceWithRawResponse(self._files.details)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithRawResponse:
        return AsyncBatchResourceWithRawResponse(self._files.batch)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithRawResponse:
        return AsyncVersionsResourceWithRawResponse(self._files.versions)

    @cached_property
    def purge(self) -> AsyncPurgeResourceWithRawResponse:
        return AsyncPurgeResourceWithRawResponse(self._files.purge)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithRawResponse:
        return AsyncMetadataResourceWithRawResponse(self._files.metadata)


class FilesResourceWithStreamingResponse:
    def __init__(self, files: FilesResource) -> None:
        self._files = files

        self.list = to_streamed_response_wrapper(
            files.list,
        )
        self.delete = to_streamed_response_wrapper(
            files.delete,
        )
        self.add_tags = to_streamed_response_wrapper(
            files.add_tags,
        )
        self.copy = to_streamed_response_wrapper(
            files.copy,
        )
        self.move = to_streamed_response_wrapper(
            files.move,
        )
        self.remove_ai_tags = to_streamed_response_wrapper(
            files.remove_ai_tags,
        )
        self.remove_tags = to_streamed_response_wrapper(
            files.remove_tags,
        )
        self.rename = to_streamed_response_wrapper(
            files.rename,
        )
        self.upload_v1 = to_streamed_response_wrapper(
            files.upload_v1,
        )
        self.upload_v2 = to_streamed_response_wrapper(
            files.upload_v2,
        )

    @cached_property
    def details(self) -> DetailsResourceWithStreamingResponse:
        return DetailsResourceWithStreamingResponse(self._files.details)

    @cached_property
    def batch(self) -> BatchResourceWithStreamingResponse:
        return BatchResourceWithStreamingResponse(self._files.batch)

    @cached_property
    def versions(self) -> VersionsResourceWithStreamingResponse:
        return VersionsResourceWithStreamingResponse(self._files.versions)

    @cached_property
    def purge(self) -> PurgeResourceWithStreamingResponse:
        return PurgeResourceWithStreamingResponse(self._files.purge)

    @cached_property
    def metadata(self) -> MetadataResourceWithStreamingResponse:
        return MetadataResourceWithStreamingResponse(self._files.metadata)


class AsyncFilesResourceWithStreamingResponse:
    def __init__(self, files: AsyncFilesResource) -> None:
        self._files = files

        self.list = async_to_streamed_response_wrapper(
            files.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            files.delete,
        )
        self.add_tags = async_to_streamed_response_wrapper(
            files.add_tags,
        )
        self.copy = async_to_streamed_response_wrapper(
            files.copy,
        )
        self.move = async_to_streamed_response_wrapper(
            files.move,
        )
        self.remove_ai_tags = async_to_streamed_response_wrapper(
            files.remove_ai_tags,
        )
        self.remove_tags = async_to_streamed_response_wrapper(
            files.remove_tags,
        )
        self.rename = async_to_streamed_response_wrapper(
            files.rename,
        )
        self.upload_v1 = async_to_streamed_response_wrapper(
            files.upload_v1,
        )
        self.upload_v2 = async_to_streamed_response_wrapper(
            files.upload_v2,
        )

    @cached_property
    def details(self) -> AsyncDetailsResourceWithStreamingResponse:
        return AsyncDetailsResourceWithStreamingResponse(self._files.details)

    @cached_property
    def batch(self) -> AsyncBatchResourceWithStreamingResponse:
        return AsyncBatchResourceWithStreamingResponse(self._files.batch)

    @cached_property
    def versions(self) -> AsyncVersionsResourceWithStreamingResponse:
        return AsyncVersionsResourceWithStreamingResponse(self._files.versions)

    @cached_property
    def purge(self) -> AsyncPurgeResourceWithStreamingResponse:
        return AsyncPurgeResourceWithStreamingResponse(self._files.purge)

    @cached_property
    def metadata(self) -> AsyncMetadataResourceWithStreamingResponse:
        return AsyncMetadataResourceWithStreamingResponse(self._files.metadata)
