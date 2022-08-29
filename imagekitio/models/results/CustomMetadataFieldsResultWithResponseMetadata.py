from imagekitio.models.results.CustomMetadataFieldsResult import CustomMetadataFieldsResult
from imagekitio.models.results.CustomMetadataSchema import CustomMetadataSchema
from imagekitio.models.results.ResponseMetadata import ResponseMetadata


class CustomMetadataFieldsResultWithResponseMetadata(CustomMetadataFieldsResult):

    def __init__(self, id, name, label,
                 schema: CustomMetadataSchema = CustomMetadataSchema(None, None, None, None, None, None, None, None)):
        super(CustomMetadataFieldsResultWithResponseMetadata, self).__init__(id, name, label, schema)
        self.response_metadata: ResponseMetadata = ResponseMetadata("", "", "")
