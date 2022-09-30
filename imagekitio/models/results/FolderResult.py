from .ResponseMetadata import ResponseMetadata


class FolderResult:
    def __init__(self, job_id=None):
        self.job_id = job_id
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
