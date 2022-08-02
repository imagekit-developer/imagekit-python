from typing import Any, Dict

from .constants.errors import ERRORS
from .file import File
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

    def upload_file(self, file=None, file_name=None, options=None) -> Dict[str, Any]:
        """Provides upload functionality
        """
        return self.file.upload(file, file_name, options)

    def list_files(self, options: Dict) -> Dict:
        """Get list(filtered if given param) of images of client
        """
        return self.file.list(options)

    def get_file_details(self, file_identifier: str = None) -> Dict:
        """Get file_detail by file_id or file_url
        """
        return self.file.details(file_identifier)

    def get_file_versions(self, file_identifier: str = None) -> Dict:
        """Get file_version by file_id or file_url
        """
        return self.file.get_file_versions(file_identifier)

    def get_file_version_details(self, file_identifier: str = None, version_identifier: str = None) -> Dict:
        """Get file_version by file_id or file_url
        """
        return self.file.get_file_version_details(file_identifier, version_identifier)

    def update_file_details(self, file_id: str, options: dict = None) -> Dict:
        """Update file detail by file id and options
        """
        return self.file.update_file_details(file_id, options)

    def add_tags(self, file_ids, tags) -> Dict:
        """Add tags by file ids and tags
        """
        return self.file.manage_tags(file_ids, tags, "addTags")

    def remove_tags(self, file_ids, tags) -> Dict:
        """Add tags by file ids and tags
        """
        return self.file.manage_tags(file_ids, tags, "removeTags")

    def remove_ai_tags(self, file_ids, a_i_tags) -> Dict:
        """Add tags by file ids and AI tags
        """
        return self.file.remove_ai_tags(file_ids, a_i_tags)

    def delete_file(self, file_id: str = None) -> Dict[str, Any]:
        """Delete file by file_id
        """
        return self.file.delete(file_id)

    def delete_file_version(self, file_id, version_id):
        """Delete file version by provided file and version id
        """
        return self.file.delete_file_version(file_id, version_id)

    def bulk_file_delete(self, file_ids):
        """Delete files in bulk by provided list of ids
        """
        return self.file.batch_delete(file_ids)

    def copy_file(self, options):
        """Copy file by provided sourceFilePath, destinationPath and includeFileVersions as an options
        """
        return self.file.copy_file(options)

    def move_file(self, options):
        """Move file by provided sourceFilePath and destinationPath as an options
        """
        return self.file.move_file(options)

    def rename_file(self, options):
        """Rename file by provided filePath, newFileName and purgeCache as an options
        """
        return self.file.rename_file(options)

    def restore_file_version(self, file_id, version_id):
        """Rename file by provided filePath, newFileName and purgeCache as an options
        """
        return self.file.restore_file_version(file_id, version_id)

    def create_folder(self, options):
        """Create folder by provided folderName and parentFolderPath
        """
        return self.file.create_folder(options)

    def delete_folder(self, options):
        """Delete folder by provided folderPath
        """
        return self.file.delete_folder(options)

    def copy_folder(self, options):
        """Copy folder by provided sourceFolderPath, destinationPath and includeFileVersions as an options
        """
        return self.file.copy_folder(options)

    def move_folder(self, options):
        """Move folder by provided sourceFolderPath and destinationPath as an options
        """
        return self.file.move_folder(options)

    def get_bulk_job_status(self, job_id):
        """Get bulk job status by provided jobId
        """
        return self.file.get_bulk_job_status(job_id)

    def purge_file_cache(self, file_url: str = None) -> Dict[str, Any]:
        """Purge Cache from server by file url
        """
        return self.file.purge_cache(file_url)

    def get_purge_file_cache_status(self, purge_cache_id: str = "") -> Dict[str, Any]:
        """Get Purge Cache status by purge cache request_id
        """
        return self.file.get_purge_cache_status(str(purge_cache_id))

    def get_file_metadata(self, file_id: str = None) -> Dict[str, Any]:
        """Get Meta Data of a file by file id
        """
        return self.file.get_metadata(str(file_id))

    def get_remote_file_url_metadata(self, remote_file_url: str = ""):
        """Get remote metadata by provided remote_file_url
        """
        return self.file.get_metadata_from_remote_url(remote_file_url)

    def create_custom_metadata_fields(self, options):
        """creates custom metadata fields by passing name, label and schema as an options
        """
        return self.file.create_custom_metadata_fields(options)

    def get_custom_metadata_fields(self, include_deleted: bool = False):
        """get custom metadata fields
        """
        return self.file.get_custom_metadata_fields(include_deleted)

    def update_custom_metadata_fields(self, custom_metadata_field_identifier, options):
        """updates custom metadata fields by passing params as an options
        """
        return self.file.update_custom_metadata_fields(custom_metadata_field_identifier, options)

    def delete_custom_metadata_field(self, custom_metadata_field_identifier: str = ""):
        """Deletes custom metadata fields by passing custom_metadata_field_identifier
        """
        return self.file.delete_custom_metadata_field(custom_metadata_field_identifier)

    def url(self, options: Dict[str, Any]) -> str:
        """Get generated Url from options parameter
        """
        return self.url_obj.generate_url(options)

    @staticmethod
    def phash_distance(first, second):
        """Get hamming distance between two phash(to check similarity)
        """
        if not (first and second):
            raise TypeError(ERRORS.MISSING_PHASH_VALUE.value)
        return hamming_distance(first, second)

    def get_authentication_parameters(self, token="", expire=0):
        """Get Authentication parameters
        """
        return get_authenticated_params(token, expire, self.ik_request.private_key)
