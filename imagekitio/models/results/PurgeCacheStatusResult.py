from .ResponseMetadata import ResponseMetadata


class PurgeCacheStatusResult:
    def __init__(self, status=None):
        self.status = status
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
