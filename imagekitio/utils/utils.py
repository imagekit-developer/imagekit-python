from json import loads, dumps
from requests.models import Response

from imagekitio.exceptions.BadRequestException import BadRequestException
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.InternalServerException import InternalServerException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.exceptions.PartialSuccessException import PartialSuccessException
from imagekitio.exceptions.TooManyRequestsException import TooManyRequestsException
from imagekitio.exceptions.UnauthorizedException import UnauthorizedException
from imagekitio.exceptions.UnknownException import UnknownException
from imagekitio.utils.formatter import camel_dict_to_snake_dict

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
    response_metadata = {"raw": resp, "httpStatusCode": response.status_code, "headers": response.headers}
    return response_metadata


def general_api_throw_exception(response: Response):
    resp = get_response_json(response)
    response_meta_data = populate_response_metadata(response)
    error_message = resp['message'] if type(resp) == dict else ""
    response_help = resp['help'] if type(resp) == dict and 'help' in resp else ""
    if response.status_code == 400:
        raise BadRequestException(error_message, response_help, response_meta_data)
    elif response.status_code == 401:
        raise UnauthorizedException(error_message, response_help, response_meta_data)
    elif response.status_code == 403:
        raise ForbiddenException(error_message, response_help, response_meta_data)
    elif response.status_code == 429:
        raise TooManyRequestsException(error_message, response_help, response_meta_data)
    elif response.status_code == 500 or response.status_code == 502 or response.status_code == 503 or response.status_code == 504:
        raise InternalServerException(error_message, response_help, response_meta_data)
    else:
        raise UnknownException(error_message, response_help, response_meta_data)


def throw_other_exception(response: Response):
    resp = get_response_json(response)
    response_meta_data = populate_response_metadata(response)
    error_message = resp['message'] if type(resp) == dict else ""
    response_help = resp['help'] if type(resp) == dict else ""
    if response.status_code == 207:
        raise PartialSuccessException(error_message, response_help, response_meta_data)
    elif response.status_code == 404:
        raise NotFoundException(error_message, response_help, response_meta_data)
    else:
        raise UnknownException(error_message, response_help, response_meta_data)


def convert_to_response_object(resp: Response, response_object):
    error = None
    res_new = loads(dumps(camel_dict_to_snake_dict(resp.json())))
    u = response_object(**res_new)
    response = {"error": error, "response": u.__str__()}
    u.response_metadata['raw'] = resp.json()
    u.response_metadata['httpStatusCode'] = resp.status_code
    u.response_metadata['headers'] = resp.headers
    return response


def convert_to_list_response_object(resp: Response, response_object, list_response_object):
    error = None
    response_list = []
    for item in resp.json():
        res_new = loads(dumps(camel_dict_to_snake_dict(item)))
        u = response_object(**res_new)
        response_list.append(u.__str__())

    u = list_response_object({'list': response_list})
    response = {"error": error, "response": u.__str__()}
    u.response_metadata['raw'] = resp.json()
    u.response_metadata['httpStatusCode'] = resp.status_code
    u.response_metadata['headers'] = resp.headers
    return response
