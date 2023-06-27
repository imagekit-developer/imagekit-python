from .CustomMetadataFieldsResult import CustomMetadataFieldsResult
from .CustomMetadataSchema import CustomMetadataSchema
from .ResponseMetadata import ResponseMetadata


class CustomMetadataFieldsResultWithResponseMetadata(CustomMetadataFieldsResult):
    def __init__(
        self,
        id=None,
        name=None,
        label=None,
        schema:dict = {},
        **kwargs
    ):
        super(CustomMetadataFieldsResultWithResponseMetadata, self).__init__(
            id, name, label, schema,**kwargs
        )
        self.response_metadata: ResponseMetadata = ResponseMetadata("", "", "")
