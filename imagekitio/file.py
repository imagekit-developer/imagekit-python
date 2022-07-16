import base64
import functools
import io
import json
from ast import literal_eval
from .results.upload_result import UploadResult
from json import dumps
from typing import Any, Dict

from .constants.errors import ERRORS
from .constants.files import VALID_FILE_OPTIONS, VALID_UPLOAD_OPTIONS
from .constants.url import URL
from .exceptions.NotFoundException import NotFoundException
from .utils.formatter import (
    camel_dict_to_snake_dict,
    request_formatter,
    snake_to_lower_camel,
)
from .utils.utils import (
    general_api_throw_exception, get_response_json, populate_response_metadata
)

try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json import JSONDecodeError

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

        url = URL.UPLOAD_URL.value
        headers = self.request.create_headers()

        files = {
            "file": file,
            "fileName": (None, file_name),
        }

        if not options:
            options = dict()
        else:
            options = self.validate_upload(options)
        if options is False:
            raise ValueError("Invalid upload options")
        if isinstance(file, str) or isinstance(file, bytes):
            files.update({"file": (None, file)})
        resp = self.request.request(
            "Post", url=url, files=files, data=options, headers=headers
        )
        he = resp.request.body
        str_he = he.decode('UTF-8', "ignore")
        print("he:===>", str_he)
        if resp.status_code == 200:
            error = None
            response = resp.json()
        else:
            general_api_throw_exception(resp)
        response_metadata = {"httpStatusCode": resp.status_code, "headers": resp.headers}
        response = {"error": error, "response": response, "responseMetaData": response_metadata}
        return response

    def list(self, options: dict) -> Dict:
        """Returns list files on ImageKit Server
        :param: options dictionary of options
        :return: list of the response
        """

        formatted_options = request_formatter(options)
        if not self.is_valid_list_options(formatted_options):
            raise ValueError("Invalid option for list_files")
        url = URL.BASE_URL.value
        headers = self.request.create_headers()

        resp = self.request.request(
            method="GET", url=url, headers=headers, params=options
        )
        if resp.status_code == 200:
            error = None
            response = resp.json()
        else:
            general_api_throw_exception(resp)
        response_metadata = {"httpStatusCode": resp.status_code, "headers": resp.headers}
        response = {"error": error, "response": response, "responseMetaData": response_metadata}
        return response

    def details(self, file_identifier: str = None) -> Dict:
        """returns file detail
        """
        if not file_identifier:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/{}/details".format(URL.BASE_URL.value, file_identifier)
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            error = None
            res_new = json.loads(json.dumps(camel_dict_to_snake_dict(resp.json())))
            u = UploadResult(**res_new)
            response = {"error": error, "response": u.__str__()}
            return response
        else:
            general_api_throw_exception(resp)

    def get_file_versions(self, file_identifier: str = None) -> Dict:
        """returns file detail
        """
        if not file_identifier:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/{}/versions".format(URL.BASE_URL.value, file_identifier)
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            error = None
            response = resp.json()
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response_json['message'] if type(response_json) == dict else ""
            response_help = response_json['help'] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)
        response_metadata = {"httpStatusCode": resp.status_code, "headers": resp.headers}
        response = {"error": error, "response": response, "responseMetaData": response_metadata}
        return response

    def get_file_version_details(self, file_identifier: str = None, version_identifier: str = None) -> Dict:
        """returns file detail
        """
        if not file_identifier:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        if not version_identifier:
            raise TypeError(ERRORS.VERSION_ID_MISSING.value)
        url = "{}/{}/versions/{}".format(URL.BASE_URL.value, file_identifier, version_identifier)
        resp = self.request.request(
            method="GET", url=url, headers=self.request.create_headers(),
        )
        if resp.status_code == 200:
            error = None
            response = resp.json()
        elif resp.status_code == 404:
            response_json = get_response_json(resp)
            response_meta_data = populate_response_metadata(resp)
            error_message = response_json['message'] if type(response_json) == dict else ""
            response_help = response_json['help'] if type(response_json) == dict else ""
            raise NotFoundException(error_message, response_help, response_meta_data)
        else:
            general_api_throw_exception(resp)
        response_metadata = {"httpStatusCode": resp.status_code, "headers": resp.headers}
        response = {"error": error, "response": response, "responseMetaData": response_metadata}
        return response

    def update_file_details(self, file_id: str, options: dict):
        """Update detail of a file(like tags, coordinates)
        update details identified by file_id and options,
        which is already uploaded
        """
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/{}/details/".format(URL.BASE_URL.value, file_id)
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        data = dumps(request_formatter(options))
        resp = self.request.request(method="Patch", url=url, headers=headers, data=data)
        if resp.status_code == 200:
            error = None
            response = resp.json()
        else:
            general_api_throw_exception(resp)
        response_metadata = {"httpStatusCode": resp.status_code, "headers": resp.headers}
        response = {"error": error, "response": response, "responseMetaData": response_metadata}
        return response

    def delete(self, file_id: str = None) -> Dict:
        """Delete file by file_id
        deletes file from imagekit server
        """
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)
        url = "{}/{}".format(URL.BASE_URL.value, file_id)
        resp = self.request.request(
            method="Delete", url=url, headers=self.request.create_headers()
        )
        if resp.status_code > 204:
            error = resp.text
            response = None
        else:
            error = None
            response = None
        response = {"error": error, "response": response}
        return response

    def batch_delete(self, file_ids: list = None):
        """Delete bulk files
        Delete files by batch ids
        """
        if not file_ids:
            raise ValueError("Need to pass ids in list")
        url = URL.BASE_URL.value + URL.BULK_FILE_DELETE.value
        resp = self.request.request(
            method="POST",
            url=url,
            headers=self.request.create_headers(),
            data={"fileIds": file_ids},
        )

        if resp.status_code > 204:
            error = resp.text
            response = None
        else:
            error = None
            response = resp.json()

        response = {"error": error, "response": response}
        return response

    def purge_cache(self, file_url: str = None) -> Dict[str, Any]:
        """Use from child class to purge cache
        """
        if not file_url:
            raise TypeError(ERRORS.MISSING_FILE_URL.value)
        url = URL.BASE_URL.value + URL.PURGE_CACHE.value
        headers = {"Content-Type": "application/json"}
        headers.update(self.request.get_auth_headers())
        body = {"url": file_url}
        resp = self.request.request(
            "Post", headers=headers, url=url, data=dumps(body)
        )
        formatted_resp = camel_dict_to_snake_dict(resp.json())
        if resp.status_code > 204:
            error = formatted_resp
            response = None
        else:
            error = None
            response = formatted_resp
        response = {"error": error, "response": response}
        return response

    def get_purge_cache_status(self, cache_request_id: str = None) -> Dict[str, Any]:
        """Get purge cache status by cache_request_id
        :return: cache_request_id
        """
        if not cache_request_id:
            raise TypeError(ERRORS.CACHE_PURGE_STATUS_ID_MISSING.value)

        url = "{}/purge/{}".format(URL.BASE_URL.value, cache_request_id)
        headers = self.request.create_headers()
        resp = self.request.request("GET", url, headers=headers)
        formatted_resp = camel_dict_to_snake_dict(resp.json())

        if resp.status_code > 200:
            error = formatted_resp
            response = None
        else:
            error = None
            response = formatted_resp
        response = {"error": error, "response": response}
        return response

    def get_metadata(self, file_id: str = None):
        """Get metadata by file_id
        """
        if not file_id:
            raise TypeError(ERRORS.FILE_ID_MISSING.value)

        url = "{}/{}/metadata".format(URL.BASE_URL.value, file_id)
        resp = self.request.request("GET", url, headers=self.request.create_headers())
        formatted_resp = camel_dict_to_snake_dict(resp.json())
        if resp.status_code > 200:
            error = resp.json()
            response = None
        else:
            error = None
            response = resp.json()
        response = {"error": error, "response": response}
        return response

    def get_metadata_from_remote_url(self, remote_file_url: str):
        if not remote_file_url:
            raise ValueError("You must provide remote url")
        url = URL.REMOTE_METADATA_FULL_URL.value
        param = {"url": remote_file_url}
        resp = self.request.request(
            "GET", url, headers=self.request.create_headers(), params=param
        )

        if resp.status_code > 204:
            error = resp.json()
            response = None
        else:
            error = None
            response = resp.json()
        response = {"error": error, "response": response}
        return response

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
