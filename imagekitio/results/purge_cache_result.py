class PurgeCacheResult:

    def __init__(self, request_id):
        self.request_id = request_id
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
