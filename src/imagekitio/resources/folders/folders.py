# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .job import (
    JobResource,
    AsyncJobResource,
    JobResourceWithRawResponse,
    AsyncJobResourceWithRawResponse,
    JobResourceWithStreamingResponse,
    AsyncJobResourceWithStreamingResponse,
)
from ...types import (
    folder_copy_params,
    folder_move_params,
    folder_create_params,
    folder_delete_params,
    folder_rename_params,
)
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.folder_copy_response import FolderCopyResponse
from ...types.folder_move_response import FolderMoveResponse
from ...types.folder_create_response import FolderCreateResponse
from ...types.folder_delete_response import FolderDeleteResponse
from ...types.folder_rename_response import FolderRenameResponse

__all__ = ["FoldersResource", "AsyncFoldersResource"]


class FoldersResource(SyncAPIResource):
    @cached_property
    def job(self) -> JobResource:
        return JobResource(self._client)

    @cached_property
    def with_raw_response(self) -> FoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return FoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return FoldersResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        folder_name: str,
        parent_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """This will create a new folder.

        You can specify the folder name and location of
        the parent folder where this new folder should be created.

        Args:
          folder_name: The folder will be created with this name.

              All characters except alphabets and numbers (inclusive of unicode letters,
              marks, and numerals in other languages) will be replaced by an underscore i.e.
              `_`.

          parent_folder_path: The folder where the new folder should be created, for root use `/` else the
              path e.g. `containing/folder/`.

              Note: If any folder(s) is not present in the parentFolderPath parameter, it will
              be automatically created. For example, if you pass `/product/images/summer`,
              then `product`, `images`, and `summer` folders will be created if they don't
              already exist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/folder",
            body=maybe_transform(
                {
                    "folder_name": folder_name,
                    "parent_folder_path": parent_folder_path,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    def delete(
        self,
        *,
        folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """This will delete a folder and all its contents permanently.

        The API returns an
        empty response.

        Args:
          folder_path: Full path to the folder you want to delete. For example `/folder/to/delete/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._delete(
            "/v1/folder",
            body=maybe_transform({"folder_path": folder_path}, folder_delete_params.FolderDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    def copy(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        include_versions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCopyResponse:
        """This will copy one folder into another.

        The selected folder, its nested folders,
        files, and their versions (in `includeVersions` is set to true) are copied in
        this operation. Note: If any file at the destination has the same name as the
        source file, then the source file and its versions will be appended to the
        destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to copy the source folder
              into.

          source_folder_path: The full path to the source folder you want to copy.

          include_versions: Option to copy all versions of files that are nested inside the selected folder.
              By default, only the current version of each file will be copied. When set to
              true, all versions of each file will be copied. Default value - `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/bulkJobs/copyFolder",
            body=maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                    "include_versions": include_versions,
                },
                folder_copy_params.FolderCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCopyResponse,
        )

    def move(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderMoveResponse:
        """This will move one folder into another.

        The selected folder, its nested folders,
        files, and their versions are moved in this operation. Note: If any file at the
        destination has the same name as the source file, then the source file and its
        versions will be appended to the destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to move the source folder
              into.

          source_folder_path: The full path to the source folder you want to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/bulkJobs/moveFolder",
            body=maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                },
                folder_move_params.FolderMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderMoveResponse,
        )

    def rename(
        self,
        *,
        folder_path: str,
        new_folder_name: str,
        purge_cache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderRenameResponse:
        """This API allows you to rename an existing folder.

        The folder and all its nested
        assets and sub-folders will remain unchanged, but their paths will be updated to
        reflect the new folder name.

        Args:
          folder_path: The full path to the folder you want to rename.

          new_folder_name: The new name for the folder.

              All characters except alphabets and numbers (inclusive of unicode letters,
              marks, and numerals in other languages) and `-` will be replaced by an
              underscore i.e. `_`.

          purge_cache: Option to purge cache for the old nested files and their versions' URLs.

              When set to true, it will internally issue a purge cache request on CDN to
              remove the cached content of the old nested files and their versions. There will
              only be one purge request for all the nested files, which will be counted
              against your monthly purge quota.

              Note: A purge cache request will be issued against
              `https://ik.imagekit.io/old/folder/path*` (with a wildcard at the end). This
              will remove all nested files, their versions' URLs, and any transformations made
              using query parameters on these files or their versions. However, the cache for
              file transformations made using path parameters will persist. You can purge them
              using the purge API. For more details, refer to the purge API documentation.

              Default value - `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/v1/bulkJobs/renameFolder",
            body=maybe_transform(
                {
                    "folder_path": folder_path,
                    "new_folder_name": new_folder_name,
                    "purge_cache": purge_cache,
                },
                folder_rename_params.FolderRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderRenameResponse,
        )


class AsyncFoldersResource(AsyncAPIResource):
    @cached_property
    def job(self) -> AsyncJobResource:
        return AsyncJobResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncFoldersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFoldersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFoldersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/imagekit-developer/imagekit-python#with_streaming_response
        """
        return AsyncFoldersResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        folder_name: str,
        parent_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCreateResponse:
        """This will create a new folder.

        You can specify the folder name and location of
        the parent folder where this new folder should be created.

        Args:
          folder_name: The folder will be created with this name.

              All characters except alphabets and numbers (inclusive of unicode letters,
              marks, and numerals in other languages) will be replaced by an underscore i.e.
              `_`.

          parent_folder_path: The folder where the new folder should be created, for root use `/` else the
              path e.g. `containing/folder/`.

              Note: If any folder(s) is not present in the parentFolderPath parameter, it will
              be automatically created. For example, if you pass `/product/images/summer`,
              then `product`, `images`, and `summer` folders will be created if they don't
              already exist.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/folder",
            body=await async_maybe_transform(
                {
                    "folder_name": folder_name,
                    "parent_folder_path": parent_folder_path,
                },
                folder_create_params.FolderCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCreateResponse,
        )

    async def delete(
        self,
        *,
        folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderDeleteResponse:
        """This will delete a folder and all its contents permanently.

        The API returns an
        empty response.

        Args:
          folder_path: Full path to the folder you want to delete. For example `/folder/to/delete/`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._delete(
            "/v1/folder",
            body=await async_maybe_transform({"folder_path": folder_path}, folder_delete_params.FolderDeleteParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderDeleteResponse,
        )

    async def copy(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        include_versions: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderCopyResponse:
        """This will copy one folder into another.

        The selected folder, its nested folders,
        files, and their versions (in `includeVersions` is set to true) are copied in
        this operation. Note: If any file at the destination has the same name as the
        source file, then the source file and its versions will be appended to the
        destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to copy the source folder
              into.

          source_folder_path: The full path to the source folder you want to copy.

          include_versions: Option to copy all versions of files that are nested inside the selected folder.
              By default, only the current version of each file will be copied. When set to
              true, all versions of each file will be copied. Default value - `false`.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/bulkJobs/copyFolder",
            body=await async_maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                    "include_versions": include_versions,
                },
                folder_copy_params.FolderCopyParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderCopyResponse,
        )

    async def move(
        self,
        *,
        destination_path: str,
        source_folder_path: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderMoveResponse:
        """This will move one folder into another.

        The selected folder, its nested folders,
        files, and their versions are moved in this operation. Note: If any file at the
        destination has the same name as the source file, then the source file and its
        versions will be appended to the destination file version history.

        Args:
          destination_path: Full path to the destination folder where you want to move the source folder
              into.

          source_folder_path: The full path to the source folder you want to move.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/bulkJobs/moveFolder",
            body=await async_maybe_transform(
                {
                    "destination_path": destination_path,
                    "source_folder_path": source_folder_path,
                },
                folder_move_params.FolderMoveParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderMoveResponse,
        )

    async def rename(
        self,
        *,
        folder_path: str,
        new_folder_name: str,
        purge_cache: bool | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FolderRenameResponse:
        """This API allows you to rename an existing folder.

        The folder and all its nested
        assets and sub-folders will remain unchanged, but their paths will be updated to
        reflect the new folder name.

        Args:
          folder_path: The full path to the folder you want to rename.

          new_folder_name: The new name for the folder.

              All characters except alphabets and numbers (inclusive of unicode letters,
              marks, and numerals in other languages) and `-` will be replaced by an
              underscore i.e. `_`.

          purge_cache: Option to purge cache for the old nested files and their versions' URLs.

              When set to true, it will internally issue a purge cache request on CDN to
              remove the cached content of the old nested files and their versions. There will
              only be one purge request for all the nested files, which will be counted
              against your monthly purge quota.

              Note: A purge cache request will be issued against
              `https://ik.imagekit.io/old/folder/path*` (with a wildcard at the end). This
              will remove all nested files, their versions' URLs, and any transformations made
              using query parameters on these files or their versions. However, the cache for
              file transformations made using path parameters will persist. You can purge them
              using the purge API. For more details, refer to the purge API documentation.

              Default value - `false`

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/v1/bulkJobs/renameFolder",
            body=await async_maybe_transform(
                {
                    "folder_path": folder_path,
                    "new_folder_name": new_folder_name,
                    "purge_cache": purge_cache,
                },
                folder_rename_params.FolderRenameParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FolderRenameResponse,
        )


class FoldersResourceWithRawResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_raw_response_wrapper(
            folders.create,
        )
        self.delete = to_raw_response_wrapper(
            folders.delete,
        )
        self.copy = to_raw_response_wrapper(
            folders.copy,
        )
        self.move = to_raw_response_wrapper(
            folders.move,
        )
        self.rename = to_raw_response_wrapper(
            folders.rename,
        )

    @cached_property
    def job(self) -> JobResourceWithRawResponse:
        return JobResourceWithRawResponse(self._folders.job)


class AsyncFoldersResourceWithRawResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_raw_response_wrapper(
            folders.create,
        )
        self.delete = async_to_raw_response_wrapper(
            folders.delete,
        )
        self.copy = async_to_raw_response_wrapper(
            folders.copy,
        )
        self.move = async_to_raw_response_wrapper(
            folders.move,
        )
        self.rename = async_to_raw_response_wrapper(
            folders.rename,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithRawResponse:
        return AsyncJobResourceWithRawResponse(self._folders.job)


class FoldersResourceWithStreamingResponse:
    def __init__(self, folders: FoldersResource) -> None:
        self._folders = folders

        self.create = to_streamed_response_wrapper(
            folders.create,
        )
        self.delete = to_streamed_response_wrapper(
            folders.delete,
        )
        self.copy = to_streamed_response_wrapper(
            folders.copy,
        )
        self.move = to_streamed_response_wrapper(
            folders.move,
        )
        self.rename = to_streamed_response_wrapper(
            folders.rename,
        )

    @cached_property
    def job(self) -> JobResourceWithStreamingResponse:
        return JobResourceWithStreamingResponse(self._folders.job)


class AsyncFoldersResourceWithStreamingResponse:
    def __init__(self, folders: AsyncFoldersResource) -> None:
        self._folders = folders

        self.create = async_to_streamed_response_wrapper(
            folders.create,
        )
        self.delete = async_to_streamed_response_wrapper(
            folders.delete,
        )
        self.copy = async_to_streamed_response_wrapper(
            folders.copy,
        )
        self.move = async_to_streamed_response_wrapper(
            folders.move,
        )
        self.rename = async_to_streamed_response_wrapper(
            folders.rename,
        )

    @cached_property
    def job(self) -> AsyncJobResourceWithStreamingResponse:
        return AsyncJobResourceWithStreamingResponse(self._folders.job)
