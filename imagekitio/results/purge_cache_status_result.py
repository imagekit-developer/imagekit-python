class PurgeCacheStatusResult:

    def __init__(self, status):
        self.status = status
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
