from .ResponseMetadata import ResponseMetadata


class TagsResult:
    def __init__(self, successfully_updated_file_ids=None):
        self.successfully_updated_file_ids = successfully_updated_file_ids
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
