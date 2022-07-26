class ListCustomMetadataFieldsResult:

    def __init__(self, list):
        self.list = list['list']
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
