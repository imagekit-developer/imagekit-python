from typing import List
from imagekitio.models.results.FileResult import FileResult
from imagekitio.models.results.ResponseMetadata import ResponseMetadata


class ListFileResult:

    def __init__(self, list: List[FileResult]):
        self.list = list
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
