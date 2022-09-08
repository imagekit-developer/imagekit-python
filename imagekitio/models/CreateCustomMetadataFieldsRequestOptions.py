from ..models.CustomMetadataFieldsSchema import CustomMetadataFieldsSchema


class CreateCustomMetadataFieldsRequestOptions:
    def __init__(
        self,
        name: str = None,
        label: str = None,
        schema: CustomMetadataFieldsSchema = None,
    ):
        self.name = name
        self.label = label
        if schema is None or schema == {}:
            CustomMetadataFieldsSchema(None, None, None, None, None, None, None, None)
        else:
            if type(schema) == CustomMetadataFieldsSchema:
                self.schema = schema
            else:
                self.schema = (
                    CustomMetadataFieldsSchema(
                        schema["type"] if "type" in schema else None,
                        schema["select_options"]
                        if "select_options" in schema
                        else None,
                        schema["default_value"] if "default_value" in schema else None,
                        schema["is_value_required"]
                        if "is_value_required" in schema
                        else None,
                        schema["min_value"] if "min_value" in schema else None,
                        schema["max_value"] if "max_value" in schema else None,
                        schema["min_length"] if "min_length" in schema else None,
                        schema["max_length"],
                    )
                    if "max_length" in schema
                    else None
                )
