from .ResponseMetadata import ResponseMetadata


class TagsResult:
    def __init__(self, successfully_updated_file_ids=None,**kwargs):
        self.successfully_updated_file_ids = successfully_updated_file_ids
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
