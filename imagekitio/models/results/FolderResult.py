from .ResponseMetadata import ResponseMetadata


class FolderResult:
    def __init__(self, job_id=None,**kwargs):
        self.job_id = job_id
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
