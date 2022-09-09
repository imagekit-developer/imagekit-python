from .CustomMetadataFieldsResult import CustomMetadataFieldsResult
from .CustomMetadataSchema import CustomMetadataSchema
from .ResponseMetadata import ResponseMetadata


class CustomMetadataFieldsResultWithResponseMetadata(CustomMetadataFieldsResult):
    def __init__(
        self,
        id,
        name,
        label,
        schema: CustomMetadataSchema = CustomMetadataSchema(
            None, None, None, None, None, None, None, None
        ),
    ):
        super(CustomMetadataFieldsResultWithResponseMetadata, self).__init__(
            id, name, label, schema
        )
        self.response_metadata: ResponseMetadata = ResponseMetadata("", "", "")
