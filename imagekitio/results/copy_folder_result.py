class CopyFolderResult:

    def __init__(self, job_id):
        self.job_id = job_id
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
