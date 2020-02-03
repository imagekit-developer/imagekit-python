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

    def upload(self, file=None, file_name=None, options=None) -> Dict[str, Any]:
        """Provides upload functionality
        """
        return self.file.upload(file, file_name, options)

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

    def update_file_details(self, file_id: str, options: dict = None) -> Dict:
        """Update file detail by file id and options
        """
        return self.file.update_file_details(file_id, options)

    def delete_file(self, file_id: str = None) -> Dict[str, Any]:
        """Delete file by file_id
        """
        return self.file.delete(file_id)

    def bulk_delete(self, file_ids: list = None):
        """Delete files in bulk by provided list of ids
        """
        return self.file.batch_delete(file_ids)

    def bulk_file_delete(self, file_ids: list = None):
        """Delete files in bulk by provided list of ids
        """
        return self.file.batch_delete(file_ids)

    def purge_cache(self, file_url: str = None) -> Dict[str, Any]:
        """Purge Cache from server by file url
        """
        return self.file.purge_cache(file_url)

    def purge_file_cache(self, file_url: str = None) -> Dict[str, Any]:
        """Purge Cache from server by file url
        """
        return self.file.purge_cache(file_url)

    def get_purge_cache_status(self, purge_cache_id: str = "") -> Dict[str, Any]:
        """Get Purge Cache status by purge cache request_id
        """
        return self.file.get_purge_cache_status(str(purge_cache_id))

    def get_purge_file_cache_status(self, purge_cache_id: str = "") -> Dict[str, Any]:
        """Get Purge Cache status by purge cache request_id
        """
        return self.file.get_purge_cache_status(str(purge_cache_id))

    def get_metadata(self, file_id: str = None) -> Dict[str, Any]:
        """Get Meta Data of a file by file id
        """
        return self.file.get_metadata(str(file_id))

    def get_file_metadata(self, file_id: str = None) -> Dict[str, Any]:
        """Get Meta Data of a file by file id
        """
        return self.file.get_metadata(str(file_id))

    def get_remote_url_metadata(self, remote_file_url: str = ""):
        return self.file.get_metadata_from_remote_url(remote_file_url)

    def get_remote_file_url_metadata(self, remote_file_url: str = ""):
        return self.file.get_metadata_from_remote_url(remote_file_url)

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
