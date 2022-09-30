from typing import List

from .CustomMetadataFieldsResult import CustomMetadataFieldsResult
from .ResponseMetadata import ResponseMetadata


class ListCustomMetadataFieldsResult:
    def __init__(self, list: List[CustomMetadataFieldsResult]):
        self.list = list
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
