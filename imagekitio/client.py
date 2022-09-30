from typing import Any, Dict

from .constants.errors import ERRORS
from .file import File
from .models.CopyFileRequestOptions import CopyFileRequestOptions
from .models.CopyFolderRequestOptions import CopyFolderRequestOptions
from .models.CreateCustomMetadataFieldsRequestOptions import (
    CreateCustomMetadataFieldsRequestOptions,
)
from .models.CreateFolderRequestOptions import CreateFolderRequestOptions
from .models.DeleteFolderRequestOptions import DeleteFolderRequestOptions
from .models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions
from .models.MoveFileRequestOptions import MoveFileRequestOptions
from .models.MoveFolderRequestOptions import MoveFolderRequestOptions
from .models.RenameFileRequestOptions import RenameFileRequestOptions
from .models.UpdateCustomMetadataFieldsRequestOptions import (
    UpdateCustomMetadataFieldsRequestOptions,
)
from .models.UpdateFileRequestOptions import UpdateFileRequestOptions
from .models.UploadFileRequestOptions import UploadFileRequestOptions
from .models.results.BulkDeleteFileResult import BulkDeleteFileResult
from .models.results.CustomMetadataFieldsResultWithResponseMetadata import (
    CustomMetadataFieldsResultWithResponseMetadata,
)
from .models.results.FileResultWithResponseMetadata import (
    FileResultWithResponseMetadata,
)
from .models.results.FolderResult import FolderResult
from .models.results.GetBulkJobStatusResult import GetBulkJobStatusResult
from .models.results.GetMetadataResult import GetMetadataResult
from .models.results.ListCustomMetadataFieldsResult import (
    ListCustomMetadataFieldsResult,
)
from .models.results.ListFileResult import ListFileResult
from .models.results.PurgeCacheResult import PurgeCacheResult
from .models.results.PurgeCacheStatusResult import PurgeCacheStatusResult
from .models.results.RenameFileResult import RenameFileResult
from .models.results.ResponseMetadataResult import ResponseMetadataResult
from .models.results.TagsResult import TagsResult
from .models.results.UploadFileResult import UploadFileResult
from .resource import ImageKitRequest
from .url import Url
from .utils.calculation import get_authenticated_params, hamming_distance


class ImageKit(object):
    """
    Main Class What user will use by creating
    instance
    """

    def __init__(
        self,
        public_key=None,
        private_key=None,
        url_endpoint=None,
        transformation_position=None,
        options=None,
    ):
        self.ik_request = ImageKitRequest(
            private_key, public_key, url_endpoint, transformation_position, options
        )
        self.file = File(self.ik_request)
        self.url_obj = Url(self.ik_request)

    def upload(self, file=None, file_name=None, options=None) -> UploadFileResult:
        """Provides upload functionality"""
        return self.file.upload(file, file_name, options)

    def upload_file(
        self, file=None, file_name=None, options: UploadFileRequestOptions = None
    ) -> UploadFileResult:
        """Provides upload functionality"""
        return self.file.upload(
            file, file_name, options if options is not None else None
        )

    def list_files(
        self, options: ListAndSearchFileRequestOptions = None
    ) -> ListFileResult:
        """Get list(filtered if given param) of images of client"""
        return self.file.list(options)

    def get_file_details(self, file_id: str = None) -> FileResultWithResponseMetadata:
        """Get file_detail by file_id or file_url"""
        return self.file.details(file_id)

    def get_file_versions(self, file_id: str = None) -> ListFileResult:
        """Get file_version by file_id or file_url"""
        return self.file.get_file_versions(file_id)

    def get_file_version_details(
        self, file_id: str = None, version_id: str = None
    ) -> FileResultWithResponseMetadata:
        """Get file_version details by file_id and version_id"""
        return self.file.get_file_version_details(file_id, version_id)

    def update_file_details(
        self, file_id: str, options: UpdateFileRequestOptions = None
    ) -> FileResultWithResponseMetadata:
        """Update file details by file id and options"""
        return self.file.update_file_details(file_id, options)

    def add_tags(self, file_ids, tags) -> TagsResult:
        """Add tags by file ids and tags"""
        return self.file.manage_tags(file_ids, tags, "addTags")

    def remove_tags(self, file_ids, tags) -> TagsResult:
        """Remove tags by file ids and tags"""
        return self.file.manage_tags(file_ids, tags, "removeTags")

    def remove_ai_tags(self, file_ids, ai_tags) -> TagsResult:
        """Remove AI tags by file ids and AI tags"""
        return self.file.remove_ai_tags(file_ids, ai_tags)

    def delete_file(self, file_id: str = None) -> ResponseMetadataResult:
        """Delete file by file_id"""
        return self.file.delete(file_id)

    def delete_file_version(self, file_id, version_id) -> ResponseMetadataResult:
        """Delete file version by provided file id and version id"""
        return self.file.delete_file_version(file_id, version_id)

    def bulk_delete(self, file_ids: list = None) -> BulkDeleteFileResult:
        """Delete files in bulk by provided list of file ids"""
        return self.file.batch_delete(file_ids)

    def bulk_file_delete(self, file_ids: list = None) -> BulkDeleteFileResult:
        """Delete files in bulk by provided list of file ids"""
        return self.file.batch_delete(file_ids)

    def copy_file(
        self, options: CopyFileRequestOptions = None
    ) -> ResponseMetadataResult:
        """Copy file by provided sourceFilePath, destinationPath and includeFileVersions as an options"""
        return self.file.copy_file(options)

    def move_file(
        self, options: MoveFileRequestOptions = None
    ) -> ResponseMetadataResult:
        """Move file by provided sourceFilePath and destinationPath as an options"""
        return self.file.move_file(options)

    def rename_file(self, options: RenameFileRequestOptions = None) -> RenameFileResult:
        """Rename file by provided filePath, newFileName and purgeCache as an options"""
        return self.file.rename_file(options)

    def restore_file_version(
        self, file_id, version_id
    ) -> FileResultWithResponseMetadata:
        """Restore file version by provided file id and version id"""
        return self.file.restore_file_version(file_id, version_id)

    def create_folder(
        self, options: CreateFolderRequestOptions = None
    ) -> ResponseMetadataResult:
        """Create folder by provided folderName and parentFolderPath as an options"""
        return self.file.create_folder(options)

    def delete_folder(
        self, options: DeleteFolderRequestOptions = None
    ) -> ResponseMetadataResult:
        """Delete folder by provided folderPath as an options"""
        return self.file.delete_folder(options)

    def copy_folder(self, options: CopyFolderRequestOptions = None) -> FolderResult:
        """Copy folder by provided sourceFolderPath, destinationPath and includeFileVersions as an options"""
        return self.file.copy_folder(options)

    def move_folder(self, options: MoveFolderRequestOptions = None) -> FolderResult:
        """Move folder by provided sourceFolderPath and destinationPath as an options"""
        return self.file.move_folder(options)

    def get_bulk_job_status(self, job_id) -> GetBulkJobStatusResult:
        """Get bulk job status by provided only jobId"""
        return self.file.get_bulk_job_status(job_id)

    def purge_cache(self, file_url: str = None) -> PurgeCacheResult:
        """Purge Cache from server by file url"""
        return self.file.purge_cache(file_url)

    def purge_file_cache(self, file_url: str = None) -> PurgeCacheResult:
        """Purge Cache from server by file url"""
        return self.file.purge_cache(file_url)

    def get_purge_cache_status(
        self, purge_cache_id: str = ""
    ) -> PurgeCacheStatusResult:
        """Get Purge Cache status by purge cache request_id"""
        return self.file.get_purge_cache_status(str(purge_cache_id))

    def get_purge_file_cache_status(
        self, purge_cache_id: str = ""
    ) -> PurgeCacheStatusResult:
        """Get Purge Cache status by purge cache request_id"""
        return self.file.get_purge_cache_status(str(purge_cache_id))

    def get_metadata(self, file_id: str = None) -> GetMetadataResult:
        """Get Meta Data of a file by file id"""
        return self.file.get_metadata(str(file_id))

    def get_file_metadata(self, file_id: str = None) -> GetMetadataResult:
        """Get Meta Data of a file by file id"""
        return self.file.get_metadata(str(file_id))

    def get_remote_url_metadata(self, remote_file_url: str = "") -> GetMetadataResult:
        return self.file.get_metadata_from_remote_url(remote_file_url)

    def get_remote_file_url_metadata(
        self, remote_file_url: str = ""
    ) -> GetMetadataResult:
        """Get remote metadata by provided remote_file_url"""
        return self.file.get_metadata_from_remote_url(remote_file_url)

    def create_custom_metadata_fields(
        self, options: CreateCustomMetadataFieldsRequestOptions = None
    ) -> CustomMetadataFieldsResultWithResponseMetadata:
        """creates custom metadata fields by passing name, label and schema as an options"""
        return self.file.create_custom_metadata_fields(options)

    def get_custom_metadata_fields(
        self, include_deleted: bool = False
    ) -> ListCustomMetadataFieldsResult:
        """get custom metadata fields"""
        return self.file.get_custom_metadata_fields(include_deleted)

    def update_custom_metadata_fields(
        self, field_id, options: UpdateCustomMetadataFieldsRequestOptions = None
    ) -> CustomMetadataFieldsResultWithResponseMetadata:
        """updates custom metadata fields by passing id of custom metadata field and params as an options"""
        return self.file.update_custom_metadata_fields(field_id, options)

    def delete_custom_metadata_field(
        self, field_id: str = ""
    ) -> ResponseMetadataResult:
        """Deletes custom metadata fields by passing field_id"""
        return self.file.delete_custom_metadata_field(field_id)

    def url(self, options: Dict[str, Any]) -> str:
        """Get generated Url from options parameter"""
        return self.url_obj.generate_url(options)

    @staticmethod
    def phash_distance(first, second):
        """Get hamming distance between two phash(to check similarity)"""
        if not (first and second):
            raise TypeError(ERRORS.MISSING_PHASH_VALUE.value)
        return hamming_distance(first, second)

    def get_authentication_parameters(self, token="", expire=0):
        """Get Authentication parameters"""
        return get_authenticated_params(token, expire, self.ik_request.private_key)
