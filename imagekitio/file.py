import json
from json import dumps
from typing import Any, Dict

from requests_toolbelt import MultipartEncoder

from .constants.errors import ERRORS
from .constants.files import VALID_FILE_OPTIONS, VALID_UPLOAD_OPTIONS
from .constants.url import URL
from .exceptions.BadRequestException import BadRequestException
from .exceptions.ConflictException import ConflictException
from .exceptions.NotFoundException import NotFoundException
from .results.bulk_delete_file_result import BulkDeleteFileResult
from .results.copy_folder_result import CopyFolderResult
from .results.custom_metadata_fields_result import CustomMetadataFieldsResult
from .results.file_result import FileResult
from .results.get_bulk_job_status_result import GetBulkJobStatusResult
from .results.get_metadata_result import GetMetadataResult
from .results.list_custom_metadata_fields_result import ListCustomMetadataFieldsResult
from .results.list_file_result import ListFileResult
from .results.purge_cache_result import PurgeCacheResult
from .results.purge_cache_status_result import PurgeCacheStatusResult
from .results.rename_file_result import RenameFileResult
from .results.tags_result import TagsResult
from .results.upload_file_result import UploadFileResult
from .utils.formatter import (
    request_formatter,
    snake_to_lower_camel,
)
from .utils.utils import (
    general_api_throw_exception, get_response_json, populate_response_metadata, convert_to_response_object,
    convert_to_list_response_object, throw_other_exception
)


class File(object):
    def __init__(self, request_obj):
        self.request = request_obj

    def upload(self, file, file_name, options) -> Dict:
        """Upload file to server using local image or url
        :param file: either local file path or network file path
        :param file_name: intended file name
        :param options: intended options
        :return: json response from server
        """
        if not file:
            raise TypeError(ERRORS.MISSING_UPLOAD_FILE_PARAMETER.value)
        if not file_name:
            raise TypeError(ERRORS.MISSING_UPLOAD_FILENAME_PARAMETER.value)
        url = "%s%s" % (URL.UPLOAD_BASE_URL, "/api/v1/files/upload")
        headers = self.request.create_headers()
        files = {
            "file": file,
            "fileName": file_name,
        }
        if not options:
            options = dict()
        else:
            options = self.validate_upload(options)
        if options is False:
            raise ValueError("Invalid upload options")
        if isinstance(file, str) or isinstance(file, bytes):
            files.update({"file": (None, file)})
        all_fields = {**files, **options}
        multipart_data = MultipartEncoder(fields=all_fields, boundary='--randomBoundary---------------------')
        headers.update({'Content-Type': multipart_data.content_type})
        resp = self.request.request(
            "Post", url=url, data=multipart_data, headers=headers
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, UploadFileResult)
            return response
        else:
            general_api_throw_exception(resp)

    def list(self, options: dict) -> Dict:
        """Returns list files on ImageKit Server
        :param: options dictionary of options
        :return: list of the response
        """

        formatted_options = request_formatter(options)
        if not self.is_valid_list_options(formatted_options):
            raise ValueError("Invalid option for list_files")
        url = "{}/v1/files".format(URL.API_BASE_URL)
        headers = self.request.create_headers()

        resp = self.request.request(
            method="GET", url=url, headers=headers, params=options
        )
        if resp.status_code == 200:
            response = convert_to_list_response_object(resp, FileResult, ListFileResult)
            return response
        else:
            general_api_throw_exception(resp)

    def details(self, file_identifier: str = None) -> Dict:
        """returns file detail
        """
        if not file_identifier:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, file_identifier)
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResult)
            return response
        else:
            general_api_throw_exception(resp)

    def get_file_versions(self, file_identifier: str = None) -> Dict:
        """returns file versions
        """
        if not file_identifier:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, file_identifier)
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            response = convert_to_list_response_object(resp, FileResult, ListFileResult)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response_json['message'] if type(response_json) == dict else ""
            response_help = response_json['help'] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def get_file_version_details(self, file_identifier: str = None, version_identifier: str = None) -> Dict:
        """returns file version detail
        """
        if not file_identifier:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        if not version_identifier:
            raise TypeError(ERRORS.VERSION_ID_MISSING.value)
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, file_identifier, version_identifier)
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResult)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response_json['message'] if type(response_json) == dict else ""
            response_help = response_json['help'] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def update_file_details(self, file_id: str, options: dict):
        """Update detail of a file(like tags, coordinates)
        update details identified by file_id and options,
        which is already uploaded
        """
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        data = dumps(request_formatter(options))
        resp = self.request.request(method="Patch", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResult)
            return response
        else:
            general_api_throw_exception(resp)

    def manage_tags(self, file_ids, tags, action):
        """Add or Remove tags of files
        :param file_ids: array of file ids
        :param tags: array of tags
        :param action: to identify call either for removeTags or addTags
        """
        url = "{}/v1/files/removeTags".format(
            URL.API_BASE_URL) if action == "removeTags" else "{}/v1/files/addTags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        data = json.dumps({"fileIds": file_ids, "tags": tags})
        resp = self.request.request(method="Post", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, TagsResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        else:
            general_api_throw_exception(resp)

    def remove_ai_tags(self, file_ids, a_i_tags):
        """Remove AI tags of files
        :param file_ids: array of file ids
        :param a_i_tags: array of AI tags
        """
        url = "{}/v1/files/removeAITags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        data = json.dumps({"fileIds": file_ids, "AITags": a_i_tags})
        resp = self.request.request(method="Post", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, TagsResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        else:
            general_api_throw_exception(resp)

    def delete(self, file_id: str = None) -> Dict:
        """Delete file by file_id
        deletes file from imagekit server
        """
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/v1/files/{}".format(URL.API_BASE_URL, file_id)
        resp = self.request.request(
            method="Delete", url=url, headers=self.request.create_headers()
        )
        if resp.status_code == 204:
            response = {
                "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
            response = {"error": None, "response": response}
            return response
        else:
            general_api_throw_exception(resp)

    def delete_file_version(self, file_id, version_id):
        """Delete file version by file_id and version_id
        """
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, file_id, version_id)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        resp = self.request.request(
            method="Delete",
            url=url,
            headers=headers
        )
        if resp.status_code == 204:
            response = {
                "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
            response = {"error": None, "response": response}
            return response
        elif resp.status_code == 400 or resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response['message'] if type(response) == dict else ""
            response_help = response['help'] if type(response) == dict else ""
            if resp.status_code == 400:
                raise BadRequestException(error_message, response_help, response_meta_data)
            elif resp.status_code == 404:
                raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def batch_delete(self, file_ids: list = None):
        """Delete bulk files
        Delete files by batch ids
        """
        if not file_ids:
            raise ValueError("Need to pass ids in list")
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        data = json.dumps({"fileIds": file_ids})
        resp = self.request.request(
            method="POST",
            url=url,
            headers=headers,
            data=data
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, BulkDeleteFileResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        else:
            general_api_throw_exception(resp)

    def copy_file(self, options):
        """Copy file by provided sourceFilePath, destinationPath and includeFileVersions as an options
        """
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        formatted_options = json.dumps(request_formatter(options))
        resp = self.request.request(
            method="Post",
            url=url,
            headers=headers,
            data=formatted_options
        )
        if resp.status_code == 204:
            response = {
                "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
            response = {"error": None, "response": response}
            return response
        elif resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response['message'] if type(response) == dict else ""
            response_help = response['help'] if type(response) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def move_file(self, options):
        """Move file by provided sourceFilePath and destinationPath as an options
        """
        url = "{}/v1/files/move".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        formatted_options = json.dumps(request_formatter(options))
        resp = self.request.request(
            method="Post",
            url=url,
            headers=headers,
            data=formatted_options
        )
        if resp.status_code == 204:
            response = {
                "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
            response = {"error": None, "response": response}
            return response
        elif resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response['message'] if type(response) == dict else ""
            response_help = response['help'] if type(response) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def rename_file(self, options):
        """Rename file by provided filePath, newFileName and purgeCache as an options
        """
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        formatted_options = json.dumps(request_formatter(options))
        resp = self.request.request(
            method="Put",
            url=url,
            headers=headers,
            data=formatted_options
        )
        if resp.status_code == 200:
            if resp.text == "{}":
                response = {
                    "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
                response = {"error": None, "response": response}
            else:
                response = convert_to_response_object(resp, RenameFileResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        elif resp.status_code == 409:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response['message'] if type(response) == dict else ""
            response_help = response['help'] if type(response) == dict else ""
            raise ConflictException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def restore_file_version(self, file_id, version_id):
        """Restore file by provided fileId and versionId
        """
        url = "{}/v1/files/{}/versions/{}/restore".format(URL.API_BASE_URL, file_id, version_id)
        headers = self.request.create_headers()
        resp = self.request.request(
            method="Put",
            url=url,
            headers=headers,
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResult)
            return response
        elif resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response['message'] if type(response) == dict else ""
            response_help = response['help'] if type(response) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def create_folder(self, options):
        """Create folder by provided folderName and parentFolderPath
        """
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        formatted_data = request_formatter(options)
        resp = self.request.request(
            method="Post",
            url=url,
            headers=headers,
            data=formatted_data
        )
        if resp.status_code == 201:
            response = {
                "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
            response = {"error": None, "response": response}
            return response

    def delete_folder(self, options):
        """Delete folder by provided folderPath as an options
        """
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        formatted_data = request_formatter(options)
        resp = self.request.request(
            method="Delete",
            url=url,
            headers=headers,
            data=formatted_data
        )
        if resp.status_code == 204:
            response = {
                "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
            response = {"error": None, "response": response}
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response_json['message'] if type(response_json) == dict else ""
            response_help = response_json['help'] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def copy_folder(self, options):
        """Copy folder by provided sourceFolderPath, destinationPath and includeFileVersions as an options
        """
        url = "{}/v1/bulkJobs/copyFolder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        headers.update({"Content-Type": "application/json"})
        formatted_data = json.dumps(request_formatter(options))
        resp = self.request.request(
            method="Post",
            url=url,
            headers=headers,
            data=formatted_data
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, CopyFolderResult)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response_json['message'] if type(response_json) == dict else ""
            response_help = response_json['help'] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def move_folder(self, options):
        """Move folder by provided sourceFolderPath and destinationPath as an options
        """
        url = "{}/v1/bulkJobs/moveFolder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        headers.update({"Content-Type": "application/json"})
        formatted_data = json.dumps(request_formatter(options))
        resp = self.request.request(
            method="Post",
            url=url,
            headers=headers,
            data=formatted_data
        )

        if resp.status_code == 200:
            response = convert_to_response_object(resp, CopyFolderResult)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response_json['message'] if type(response_json) == dict else ""
            response_help = response_json['help'] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def get_bulk_job_status(self, job_id):
        """Get bulk job status by provided only jobId
        """
        url = "{}/v1/bulkJobs/{}".format(URL.API_BASE_URL, job_id)
        headers = self.request.create_headers()
        resp = self.request.request(
            method="Get",
            url=url,
            headers=headers,
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, GetBulkJobStatusResult)
            return response
        else:
            general_api_throw_exception(resp)

    def purge_cache(self, file_url: str = None) -> Dict[str, Any]:
        """Use from child class to purge cache
        """
        if not file_url:
            raise TypeError(ERRORS.MISSING_FILE_URL.value)
        url = URL.API_BASE_URL + "/v1/files/purge"
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        body = {"url": file_url}
        resp = self.request.request(
            "Post", headers=headers, url=url, data=dumps(body)
        )
        if resp.status_code == 201:
            response = convert_to_response_object(resp, PurgeCacheResult)
            return response
        else:
            general_api_throw_exception(resp)

    def get_purge_cache_status(self, cache_request_id: str = None) -> Dict[str, Any]:
        """Get purge cache status by cache_request_id
        :return: cache_request_id
        """
        if not cache_request_id:
            raise TypeError(ERRORS.CACHE_PURGE_STATUS_ID_MISSING.value)

        url = "{}/v1/files/purge/{}".format(URL.API_BASE_URL, cache_request_id)
        headers = self.request.create_headers()
        resp = self.request.request("GET", url, headers=headers)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, PurgeCacheStatusResult)
            return response
        else:
            general_api_throw_exception(resp)

    def get_metadata(self, file_id: str = None):
        """Get metadata by file_id
        """
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)

        url = "{}/v1/files/{}/metadata".format(URL.API_BASE_URL, file_id)
        resp = self.request.request("GET", url, headers=self.request.create_headers())
        if resp.status_code == 200:
            response = convert_to_response_object(resp, GetMetadataResult)
            return response
        else:
            general_api_throw_exception(resp)

    def get_metadata_from_remote_url(self, remote_file_url: str):
        """Get remote metadata by provided remote_file_url
        """
        if not remote_file_url:
            raise ValueError("You must provide remote url")
        url = "{}/v1/metadata".format(URL.API_BASE_URL)
        param = {"url": remote_file_url}
        resp = self.request.request(
            "GET", url, headers=self.request.create_headers(), params=param
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, GetMetadataResult)
            return response
        else:
            general_api_throw_exception(resp)

    def create_custom_metadata_fields(self, options):
        """creates custom metadata fields by passing name, label and schema as an options
        """
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        options['schema'] = request_formatter(options['schema'])
        formatted_options = json.dumps(request_formatter(options))
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        resp = self.request.request(
            method="Post", url=url, headers=headers, data=formatted_options
        )
        if resp.status_code == 201:
            response = convert_to_response_object(resp, CustomMetadataFieldsResult)
            return response
        else:
            if resp.status_code == 400:
                response_json = get_response_json(resp)
                response_meta_data = populate_response_metadata(resp)
                error_message = response_json['message'] if type(response_json) == dict else ""
                response_help = response_json['help'] if type(response_json) == dict else ""
                raise BadRequestException(error_message, response_help, response_meta_data)

    def get_custom_metadata_fields(self, include_deleted: bool = False):
        """get custom metadata fields
        """
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        param = {"includeDeleted": include_deleted}
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(), params=param
        )
        if resp.status_code == 200:
            response = convert_to_list_response_object(resp, CustomMetadataFieldsResult, ListCustomMetadataFieldsResult)
            return response

    def update_custom_metadata_fields(self, custom_metadata_field_identifier, options):
        """updates custom metadata fields by passing id of custom metadata field and params as an options
        """
        if not custom_metadata_field_identifier:
            raise ValueError(ERRORS.MISSING_CUSTOM_METADATA_FIELD_ID)
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, custom_metadata_field_identifier)
        if 'schema' in options:
            options['schema'] = request_formatter(options['schema'])
        formatted_options = json.dumps(request_formatter(options))
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        resp = self.request.request(
            method="Patch", url=url, headers=headers, data=formatted_options
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, CustomMetadataFieldsResult)
            return response
        else:
            if resp.status_code == 400 or resp.status_code == 404:
                response_json = get_response_json(resp)
                response_meta_data = populate_response_metadata(resp)
                error_message = response_json['message'] if type(response_json) == dict else ""
                response_help = response_json['help'] if type(response_json) == dict else ""
                if resp.status_code == 400:
                    raise BadRequestException(error_message, response_help, response_meta_data)
                else:
                    raise NotFoundException(error_message, response_help, response_meta_data)

    def delete_custom_metadata_field(self, custom_metadata_field_identifier: str):
        """Deletes custom metadata fields by passing custom_metadata_field_identifier
        """
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, custom_metadata_field_identifier)
        resp = self.request.request(
            "Delete", url, headers=self.request.create_headers()
        )
        if resp.status_code == 204:
            response = {
                "_response_metadata": {"raw": None, "httpStatusCode": resp.status_code, "headers": resp.headers}}
            response = {"error": None, "response": response}
            return response
        else:
            if resp.status_code == 404:
                response_json = get_response_json(resp)
                response_meta_data = populate_response_metadata(resp)
                error_message = response_json['message'] if type(response_json) == dict else ""
                response_help = response_json['help'] if type(response_json) == dict else ""
                raise NotFoundException(error_message, response_help, response_meta_data)

    def is_valid_list_options(self, options: Dict[str, Any]) -> bool:
        """Returns if options are valid
        """
        valid_values = self.get_valid_list_values()
        for key in options:
            if key not in valid_values:
                return False
        return True

    @staticmethod
    def get_valid_list_values():
        """Returns valid options for list files
        """
        return VALID_FILE_OPTIONS

    @staticmethod
    def validate_upload(options):
        """
        Validates upload value, checks if params are valid,
        changes snake to camel case
        """
        response_list = []
        for key, val in options.items():
            if key not in VALID_UPLOAD_OPTIONS:
                return False
            if key == "response_fields":
                for i, j in enumerate(options[key]):
                    if j not in VALID_UPLOAD_OPTIONS:
                        return False
                    response_list.append(snake_to_lower_camel(j))
                val = ",".join(response_list)
                if val:
                    options[key] = ",".join(response_list)
                continue
            if isinstance(val, list):
                val = ",".join([str(i) for i in val])
                if val:
                    options[key] = val
                continue
            # imagekit server accepts 'true/false'
            elif isinstance(val, bool):
                val = str(val).lower()
            if val:
                options[key] = val
        return request_formatter(options)
