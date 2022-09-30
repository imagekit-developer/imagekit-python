from .CustomMetadataSchema import CustomMetadataSchema


class CustomMetadataFieldsResult:
    def __init__(
        self,
        id=None,
        name=None,
        label=None,
        schema: dict = {},
    ):
        self.id = id
        self.name = name
        self.label = label
        self.schema = CustomMetadataSchema(
            schema["type"],
            schema["selectOptions"] if "selectOptions" in schema else None,
            schema["defaultValue"] if "defaultValue" in schema else None,
            schema["isValueRequired"] if "isValueRequired" in schema else None,
            schema["minValue"] if "minValue" in schema else None,
            schema["maxValue"] if "maxValue" in schema else None,
            schema["minLength"] if "minLength" in schema else None,
            schema["maxValue"] if "maxValue" in schema else None,
        )
