from .ResponseMetadata import ResponseMetadata


class PurgeCacheResult:
    def __init__(self, request_id=None):
        self.request_id = request_id
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
