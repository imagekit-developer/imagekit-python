import re
from collections import ChainMap, OrderedDict
from typing import Dict, List


def camel_to_snake(name):
    """
    converts camelCase to snake_case for python
    """
    s1 = re.sub("(.)([A-Z][a-z]+)", r"\1_\2", name)
    return re.sub("([a-z0-9])([A-Z])", r"\1_\2", s1).lower()


def snake_to_lower_camel(word):
    """
    changes word snake to  lower camelCase example: my_plan -> MyPlan
    :return camelCaseWord
    """
    word_list = word.split("_")
    if word_list:
        return word_list[0] + "".join(x.title() for x in word_list[1:])
    return word


def request_formatter(data: dict) -> dict:
    """Converts all keys to camelCase format required for ImageKit server
    :param data: dict()
    :return: converted_dict -> dict()
    """
    return {snake_to_lower_camel(key): val for key, val in data.items()}


def camel_dict_to_snake_dict(data: dict) -> dict:
    """Convert the keys of dictionary from camel case to snake case
    """
    return {camel_to_snake(key): val for key, val in data.items()}


def flatten_dict(dict_list: List[Dict]) -> OrderedDict:
    """Convert list of dictionary to flatten dict
    :param dict_list: list of dictionary
    :return: flatten_dict
    """
    flat_dict = OrderedDict()
    for dict_var in dict_list:
        flat_dict.update(dict_var)
    return flat_dict
