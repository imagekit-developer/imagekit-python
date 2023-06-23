import ast
from json import dumps
from typing import Any, Dict

from requests_toolbelt import MultipartEncoder

from .constants.errors import ERRORS
from .constants.files import VALID_FILE_OPTIONS, VALID_UPLOAD_OPTIONS
from .constants.url import URL
from .exceptions.BadRequestException import BadRequestException
from .exceptions.ConflictException import ConflictException
from .exceptions.NotFoundException import NotFoundException
from .exceptions.UnknownException import UnknownException
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
from .models.results.CustomMetadataFieldsResult import CustomMetadataFieldsResult
from .models.results.CustomMetadataFieldsResultWithResponseMetadata import (
    CustomMetadataFieldsResultWithResponseMetadata,
)
from .models.results.FileResult import FileResult
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
from .utils.formatter import (
    request_formatter,
    snake_to_lower_camel,
)
from .utils.utils import (
    general_api_throw_exception,
    get_response_json,
    populate_response_metadata,
    convert_to_response_object,
    convert_to_list_response_object,
    throw_other_exception,
    convert_to_response_metadata_result_object,
)

from io import BufferedReader

class File(object):
    def __init__(self, request_obj):
        self.request = request_obj

    def upload(
        self, file, file_name, options: UploadFileRequestOptions = None
    ) -> UploadFileResult:
        """Upload file to server using local image or url
        :param file: either local file path or network file path
        :param file_name: intended file name
        :param options: intended options
        :return: UploadFileResult
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
            options = self.validate_upload(options.__dict__)
        if options is False:
            raise ValueError("Invalid upload options")
        if isinstance(file,BufferedReader):
            files.update({"file": (file_name,file,None)})
        elif isinstance(file, str) or isinstance(file, bytes):
            files.update({"file": (None, file)})
        if "overwriteAiTags" in options:
            options["overwriteAITags"] = options["overwriteAiTags"]
            del options["overwriteAiTags"]
        all_fields = {**files, **options}
        multipart_data = MultipartEncoder(
            fields=all_fields, boundary="--randomBoundary---------------------"
        )
        headers.update({"Content-Type": multipart_data.content_type})
        resp = self.request.request(
            "Post", url=url, data=multipart_data.read(), headers=headers
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, UploadFileResult)
            return response
        else:
            general_api_throw_exception(resp)

    def list(self, options: ListAndSearchFileRequestOptions = None) -> ListFileResult:
        """Returns list files on ImageKit Server
        :param: options dictionary of options
        :return: ListFileResult
        """
        if options is not None:
            if "tags" in options.__dict__ and isinstance(options.tags, list):
                val = ", ".join(options.tags)
                if val:
                    options.tags = val
            formatted_options = request_formatter(options.__dict__)
            if not self.is_valid_list_options(formatted_options):
                raise ValueError("Invalid option for list_files")
        else:
            formatted_options = dict()
        url = "{}/v1/files".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        resp = self.request.request(
            method="GET", url=url, headers=headers, params=formatted_options
        )
        if resp.status_code == 200:
            response = convert_to_list_response_object(resp, FileResult, ListFileResult)
            return response
        else:
            general_api_throw_exception(resp)

    def details(self, file_id: str = None) -> FileResultWithResponseMetadata:
        """returns file detail"""
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/v1/files/{}/details".format(URL.API_BASE_URL, file_id)
        resp = self.request.request(
            method="GET",
            url=url,
            headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResultWithResponseMetadata)
            return response
        else:
            general_api_throw_exception(resp)

    def get_file_versions(self, file_id: str = None) -> ListFileResult:
        """returns file versions"""
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/v1/files/{}/versions".format(URL.API_BASE_URL, file_id)
        resp = self.request.request(
            method="GET",
            url=url,
            headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            response = convert_to_list_response_object(resp, FileResult, ListFileResult)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def get_file_version_details(
        self, file_id: str = None, version_id: str = None
    ) -> FileResultWithResponseMetadata:
        """returns file version detail"""
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        if not version_id:
            raise TypeError(ERRORS.VERSION_ID_MISSING.value)
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, file_id, version_id)
        resp = self.request.request(
            method="GET",
            url=url,
            headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResultWithResponseMetadata)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def update_file_details(
        self, file_id: str, options: UpdateFileRequestOptions = None
    ) -> FileResultWithResponseMetadata:
        """Update detail of a file(like tags, coordinates)
        update details identified by file_id and options,
        which is already uploaded
        """
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/v1/files/{}/details/".format(URL.API_BASE_URL, file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        formatted_options = request_formatter(options.__dict__)
        if "removeAiTags" in formatted_options:
            remove_ai_tags_dict = {"removeAITags": formatted_options["removeAiTags"]}
            del formatted_options["removeAiTags"]
            request_data = {**remove_ai_tags_dict, **formatted_options}
        else:
            request_data = formatted_options
        data = dumps(request_data) if options is not None else dict()
        resp = self.request.request(method="Patch", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResultWithResponseMetadata)
            return response
        else:
            general_api_throw_exception(resp)

    def manage_tags(self, file_ids, tags, action) -> TagsResult:
        """Add or Remove tags of files
        :param file_ids: array of file ids
        :param tags: array of tags
        :param action: to identify call either for removeTags or addTags
        """
        url = (
            "{}/v1/files/removeTags".format(URL.API_BASE_URL)
            if action == "removeTags"
            else "{}/v1/files/addTags".format(URL.API_BASE_URL)
        )
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        data = dumps({"fileIds": file_ids, "tags": tags})
        resp = self.request.request(method="Post", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, TagsResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        else:
            general_api_throw_exception(resp)

    def remove_ai_tags(self, file_ids, ai_tags) -> TagsResult:
        """Remove AI tags of files
        :param file_ids: array of file ids
        :param ai_tags: array of AI tags
        """
        url = "{}/v1/files/removeAITags".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        data = dumps({"fileIds": file_ids, "AITags": ai_tags})
        resp = self.request.request(method="Post", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, TagsResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        else:
            general_api_throw_exception(resp)

    def delete(self, file_id: str = None) -> ResponseMetadataResult:
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
            response = convert_to_response_metadata_result_object(resp)
            return response
        else:
            general_api_throw_exception(resp)

    def delete_file_version(self, file_id, version_id) -> ResponseMetadataResult:
        """Delete file version by file_id and version_id"""
        url = "{}/v1/files/{}/versions/{}".format(URL.API_BASE_URL, file_id, version_id)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        resp = self.request.request(method="Delete", url=url, headers=headers)
        if resp.status_code == 204:
            response = convert_to_response_metadata_result_object(resp)
            return response
        elif resp.status_code == 400 or resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response) == str:
                response = ast.literal_eval(response)
            error_message = response["message"] if type(response) == dict else ""
            response_help = response["help"] if type(response) == dict else ""
            if resp.status_code == 400:
                raise BadRequestException(
                    error_message, response_help, response_meta_data
                )
            elif resp.status_code == 404:
                raise NotFoundException(
                    error_message, response_help, response_meta_data
                )
        else:
            general_api_throw_exception(resp)

    def batch_delete(self, file_ids: list = None) -> BulkDeleteFileResult:
        """Delete bulk files
        Delete files by batch ids
        """
        if not file_ids:
            raise ValueError("Need to pass ids in list")
        url = URL.API_BASE_URL + "/v1/files" + URL.BULK_FILE_DELETE
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        data = dumps({"fileIds": file_ids})
        resp = self.request.request(method="POST", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            response = convert_to_response_object(resp, BulkDeleteFileResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        else:
            general_api_throw_exception(resp)

    def copy_file(
        self, options: CopyFileRequestOptions = None
    ) -> ResponseMetadataResult:
        """Copy file by provided sourceFilePath, destinationPath and includeFileVersions as an options"""
        url = "{}/v1/files/copy".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        formatted_options = (
            dumps(request_formatter(options.__dict__))
            if options is not None
            else dict()
        )
        resp = self.request.request(
            method="Post", url=url, headers=headers, data=formatted_options
        )
        if resp.status_code == 204:
            response = convert_to_response_metadata_result_object(resp)
            return response
        elif resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response) == str:
                response = ast.literal_eval(response)
            error_message = response["message"] if type(response) == dict else ""
            response_help = response["help"] if type(response) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def move_file(
        self, options: MoveFileRequestOptions = None
    ) -> ResponseMetadataResult:
        """Move file by provided sourceFilePath and destinationPath as an options"""
        url = "{}/v1/files/move".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        formatted_options = (
            dumps(request_formatter(options.__dict__))
            if options is not None
            else dict()
        )
        resp = self.request.request(
            method="Post", url=url, headers=headers, data=formatted_options
        )
        if resp.status_code == 204:
            response = convert_to_response_metadata_result_object(resp)
            return response
        elif resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response) == str:
                response = ast.literal_eval(response)
            error_message = response["message"] if type(response) == dict else ""
            response_help = response["help"] if type(response) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def rename_file(self, options: RenameFileRequestOptions = None) -> RenameFileResult:
        """Rename file by provided filePath, newFileName and purgeCache as an options"""
        url = "{}/v1/files/rename".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        formatted_options = (
            dumps(request_formatter(options.__dict__))
            if options is not None
            else dict()
        )
        resp = self.request.request(
            method="Put", url=url, headers=headers, data=formatted_options
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, RenameFileResult)
            return response
        elif resp.status_code == 207 or resp.status_code == 404:
            throw_other_exception(resp)
        elif resp.status_code == 409:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response) == str:
                response = ast.literal_eval(response)
            error_message = response["message"] if type(response) == dict else ""
            response_help = response["help"] if type(response) == dict else ""
            raise ConflictException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def restore_file_version(
        self, file_id, version_id
    ) -> FileResultWithResponseMetadata:
        """Restore file by provided fileId and versionId"""
        url = "{}/v1/files/{}/versions/{}/restore".format(
            URL.API_BASE_URL, file_id, version_id
        )
        headers = self.request.create_headers()
        resp = self.request.request(
            method="Put",
            url=url,
            headers=headers,
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FileResultWithResponseMetadata)
            return response
        elif resp.status_code == 404:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response) == str:
                response = ast.literal_eval(response)
            error_message = response["message"] if type(response) == dict else ""
            response_help = response["help"] if type(response) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def create_folder(
        self, options: CreateFolderRequestOptions = None
    ) -> ResponseMetadataResult:
        """Create folder by provided folderName and parentFolderPath as an options"""
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        headers.update({"Content-Type": "application/json"})
        formatted_data = (
            dumps(request_formatter(options.__dict__)) if options is not None else dict()
        )
        resp = self.request.request(
            method="Post", url=url, headers=headers, data=formatted_data
        )
        if resp.status_code == 201:
            response = convert_to_response_metadata_result_object(resp)
            return response
        else:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response) == str:
                response = ast.literal_eval(response)
            error_message = response["message"] if type(response) == dict else ""
            response_help = response["help"] if type(response) == dict else ""
            raise UnknownException(error_message, response_help, response_meta_data)

    def delete_folder(
        self, options: DeleteFolderRequestOptions = None
    ) -> ResponseMetadataResult:
        """Delete folder by provided folderPath as an options"""
        url = "{}/v1/folder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        headers.update({"Content-Type": "application/json"})
        formatted_data = (
            dumps(request_formatter(options.__dict__)) if options is not None else dict()
        )
        resp = self.request.request(
            method="Delete", url=url, headers=headers, data=formatted_data
        )
        if resp.status_code == 204:
            response = convert_to_response_metadata_result_object(resp)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def copy_folder(self, options: CopyFolderRequestOptions = None) -> FolderResult:
        """Copy folder by provided sourceFolderPath, destinationPath and includeFileVersions as an options"""
        url = "{}/v1/bulkJobs/copyFolder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        headers.update({"Content-Type": "application/json"})
        formatted_data = (
            dumps(request_formatter(options.__dict__))
            if options is not None
            else dict()
        )
        resp = self.request.request(
            method="Post", url=url, headers=headers, data=formatted_data
        )
        if resp.status_code == 200:
            response = convert_to_response_object(resp, FolderResult)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def move_folder(self, options: MoveFolderRequestOptions = None) -> FolderResult:
        """Move folder by provided sourceFolderPath and destinationPath as an options"""
        url = "{}/v1/bulkJobs/moveFolder".format(URL.API_BASE_URL)
        headers = self.request.create_headers()
        headers.update({"Content-Type": "application/json"})
        formatted_data = (
            dumps(request_formatter(options.__dict__))
            if options is not None
            else dict()
        )
        resp = self.request.request(
            method="Post", url=url, headers=headers, data=formatted_data
        )

        if resp.status_code == 200:
            response = convert_to_response_object(resp, FolderResult)
            return response
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)

    def get_bulk_job_status(self, job_id) -> GetBulkJobStatusResult:
        """Get bulk job status by provided only jobId"""
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

    def purge_cache(self, file_url: str = None) -> PurgeCacheResult:
        """Use from child class to purge cache"""
        if not file_url:
            raise TypeError(ERRORS.MISSING_FILE_URL.value)
        url = URL.API_BASE_URL + "/v1/files/purge"
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        body = {"url": file_url}
        resp = self.request.request("Post", headers=headers, url=url, data=dumps(body))
        if resp.status_code == 201:
            response = convert_to_response_object(resp, PurgeCacheResult)
            return response
        else:
            general_api_throw_exception(resp)

    def get_purge_cache_status(
        self, cache_request_id: str = None
    ) -> PurgeCacheStatusResult:
        """Get purge cache status by cache_request_id
        :return: PurgeCacheStatusResult
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

    def get_metadata(self, file_id: str = None) -> GetMetadataResult:
        """Get metadata by file_id"""
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)

        url = "{}/v1/files/{}/metadata".format(URL.API_BASE_URL, file_id)
        resp = self.request.request("GET", url, headers=self.request.create_headers())
        if resp.status_code == 200:
            response = convert_to_response_object(resp, GetMetadataResult)
            return response
        else:
            general_api_throw_exception(resp)

    def get_metadata_from_remote_url(self, remote_file_url: str) -> GetMetadataResult:
        """Get remote metadata by provided remote_file_url"""
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

    def create_custom_metadata_fields(
        self, options: CreateCustomMetadataFieldsRequestOptions = None
    ) -> CustomMetadataFieldsResultWithResponseMetadata:
        """creates custom metadata fields by passing name, label and schema as an options"""
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        if options is not None:
            if "schema" in options.__dict__:
                options.schema.__dict__ = request_formatter(options.schema.__dict__)
            options_dict = options.__dict__
            if "schema" in options_dict:
                options_dict["schema"] = options.schema.__dict__
            formatted_options = dumps(options_dict)
        else:
            formatted_options = dict()

        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        resp = self.request.request(
            method="Post", url=url, headers=headers, data=formatted_options
        )
        if resp.status_code == 201:
            response = convert_to_response_object(
                resp, CustomMetadataFieldsResultWithResponseMetadata
            )
            return response
        else:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            if resp.status_code == 400:
                raise BadRequestException(
                    error_message, response_help, response_meta_data
                )
            else:
                raise UnknownException(error_message, response_help, response_meta_data)

    def get_custom_metadata_fields(
        self, include_deleted: bool = False
    ) -> ListCustomMetadataFieldsResult:
        """get custom metadata fields"""
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        param = {"includeDeleted": str(include_deleted).lower()}
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(), params=param
        )
        if resp.status_code == 200:
            response = convert_to_list_response_object(
                resp, CustomMetadataFieldsResult, ListCustomMetadataFieldsResult
            )
            return response
        else:
            response = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response) == str:
                response = ast.literal_eval(response)
            error_message = response["message"] if type(response) == dict else ""
            response_help = response["help"] if type(response) == dict else ""
            raise UnknownException(error_message, response_help, response_meta_data)

    def update_custom_metadata_fields(
        self, field_id, options: UpdateCustomMetadataFieldsRequestOptions = None
    ) -> CustomMetadataFieldsResultWithResponseMetadata:
        """updates custom metadata fields by passing id of custom metadata field and params as an options"""
        if not field_id:
            raise ValueError(ERRORS.MISSING_CUSTOM_METADATA_FIELD_ID)
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, field_id)
        if "schema" in options.__dict__:
            options.schema.__dict__ = request_formatter(options.schema.__dict__)
        options_dict = options.__dict__
        if "schema" in options_dict:
            options_dict["schema"] = options.schema.__dict__
        formatted_options = dumps(request_formatter(options_dict))
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.create_headers())
        resp = self.request.request(
            method="Patch", url=url, headers=headers, data=formatted_options
        )
        if resp.status_code == 200:
            response = convert_to_response_object(
                resp, CustomMetadataFieldsResultWithResponseMetadata
            )
            return response
        else:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            if resp.status_code == 400:
                raise BadRequestException(
                    error_message, response_help, response_meta_data
                )
            elif resp.status_code == 404:
                raise NotFoundException(
                    error_message, response_help, response_meta_data
                )
            else:
                raise UnknownException(error_message, response_help, response_meta_data)

    def delete_custom_metadata_field(self, field_id: str) -> ResponseMetadataResult:
        """Deletes custom metadata fields by passing field_id"""
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, field_id)
        resp = self.request.request(
            "Delete", url, headers=self.request.create_headers()
        )
        if resp.status_code == 204:
            response = convert_to_response_metadata_result_object(resp)
            return response
        else:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            if type(response_json) == str:
                response_json = ast.literal_eval(response_json)
            error_message = (
                response_json["message"] if type(response_json) == dict else ""
            )
            response_help = response_json["help"] if type(response_json) == dict else ""
            if resp.status_code == 404:
                raise NotFoundException(
                    error_message, response_help, response_meta_data
                )
            else:
                raise UnknownException(error_message, response_help, response_meta_data)

    def is_valid_list_options(self, options: Dict[str, Any]) -> bool:
        """Returns if options are valid"""
        valid_values = self.get_valid_list_values()
        for key in options:
            if key not in valid_values:
                return False
        return True

    @staticmethod
    def get_valid_list_values():
        """Returns valid options for list files"""
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
            if type(val) == dict or type(val) == tuple:
                options[key] = dumps(val)
                continue
            if key == "extensions":
                options[key] = dumps(val)
                continue
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
