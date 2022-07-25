class GetBulkJobStatusResult:

    def __init__(self, job_id, type, status):
        self.job_id = job_id
        self.type = type
        self.status = status
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
