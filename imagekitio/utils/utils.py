import ast
from json import loads, dumps
from requests.models import Response

from ..exceptions.BadRequestException import BadRequestException
from ..exceptions.ForbiddenException import ForbiddenException
from ..exceptions.InternalServerException import InternalServerException
from ..exceptions.NotFoundException import NotFoundException
from ..exceptions.PartialSuccessException import PartialSuccessException
from ..exceptions.TooManyRequestsException import TooManyRequestsException
from ..exceptions.UnauthorizedException import UnauthorizedException
from ..exceptions.UnknownException import UnknownException
from ..models.results.ResponseMetadata import ResponseMetadata
from ..models.results.ResponseMetadataResult import ResponseMetadataResult
from ..utils.formatter import camel_dict_to_snake_dict

try:
    from simplejson.errors import JSONDecodeError
except ImportError:
    from json import JSONDecodeError


def get_response_json(response: Response):
    try:
        resp = response.json()
    except JSONDecodeError:
        resp = response.text
    return resp


def populate_response_metadata(response: Response):
    resp = get_response_json(response)
    response_metadata = ResponseMetadata(resp, response.status_code, response.headers)
    return response_metadata


def general_api_throw_exception(response: Response):
    resp = get_response_json(response)
    response_meta_data = populate_response_metadata(response)
    if type(resp) == str:
        resp = ast.literal_eval(resp)
    error_message = resp["message"] if type(resp) == dict else ""
    response_help = resp["help"] if type(resp) == dict and "help" in resp else ""
    if response.status_code == 400:
        raise BadRequestException(error_message, response_help, response_meta_data)
    elif response.status_code == 401:
        raise UnauthorizedException(error_message, response_help, response_meta_data)
    elif response.status_code == 403:
        raise ForbiddenException(error_message, response_help, response_meta_data)
    elif response.status_code == 429:
        raise TooManyRequestsException(error_message, response_help, response_meta_data)
    elif (
        response.status_code == 500
        or response.status_code == 502
        or response.status_code == 503
        or response.status_code == 504
    ):
        raise InternalServerException(error_message, response_help, response_meta_data)
    else:
        raise UnknownException(error_message, response_help, response_meta_data)


def throw_other_exception(response: Response):
    resp = get_response_json(response)
    response_meta_data = populate_response_metadata(response)
    if type(resp) == str:
        resp = ast.literal_eval(resp)
    error_message = resp["message"] if type(resp) == dict else ""
    response_help = resp["help"] if type(resp) == dict else ""
    if response.status_code == 207:
        raise PartialSuccessException(error_message, response_help, response_meta_data)
    elif response.status_code == 404:
        raise NotFoundException(error_message, response_help, response_meta_data)
    else:
        raise UnknownException(error_message, response_help, response_meta_data)


def convert_to_response_object(resp: Response, response_object):
    res_new = loads(dumps(camel_dict_to_snake_dict(resp.json())))
    u = response_object(**res_new)
    u.response_metadata = ResponseMetadata(resp.json(), resp.status_code, resp.headers)
    return u


def convert_to_response_metadata_result_object(resp: Response = None):
    u = ResponseMetadataResult()
    u.response_metadata = ResponseMetadata(
        resp.json() if resp.status_code != 204 else None, resp.status_code, resp.headers
    )
    return u


def convert_to_list_response_object(
    resp: Response, response_object, list_response_object
):
    response_list = []
    for item in resp.json():
        res_new = loads(dumps(camel_dict_to_snake_dict(item)))
        u = response_object(**res_new)
        response_list.append(u)

    u = list_response_object(response_list)
    u.response_metadata = ResponseMetadata(resp.json(), resp.status_code, resp.headers)
    return u
