from .ResponseMetadata import ResponseMetadata


class GetBulkJobStatusResult:
    def __init__(self, job_id=None, type=None, status=None,**kwargs):
        self.job_id = job_id
        self.type = type
        self.status = status
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")
        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None


    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
