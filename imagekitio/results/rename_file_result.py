class RenameFileResult:

    def __init__(self, purge_request_id: str = ""):
        self.purge_request_id = purge_request_id
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
