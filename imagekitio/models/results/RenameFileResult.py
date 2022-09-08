from .ResponseMetadata import ResponseMetadata


class RenameFileResult:
    def __init__(self, purge_request_id: str = None):
        self.purge_request_id = purge_request_id
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
