from .CustomMetadataSchema import CustomMetadataSchema


class CustomMetadataFieldsResult:
    def __init__(
        self,
        id,
        name,
        label,
        schema: CustomMetadataSchema = CustomMetadataSchema(
            None, None, None, None, None, None, None, None
        ),
    ):
        self.id = id
        self.name = name
        self.label = label
        self.schema = schema
