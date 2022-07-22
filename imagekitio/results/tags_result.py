class TagsResult:

    def __init__(self, successfully_updated_file_ids):
        self.successfully_updated_file_ids = successfully_updated_file_ids
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
