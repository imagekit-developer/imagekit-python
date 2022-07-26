class CustomMetadataFieldsResult:

    def __init__(self, id, name, label, schema):
        self.id = id
        self.name = name
        self.label = label
        self.schema = schema
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
