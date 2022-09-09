from ..models.CustomMetaDataTypeEnum import CustomMetaDataTypeEnum


class CustomMetadataFieldsSchema:
    def __init__(
        self,
        type: CustomMetaDataTypeEnum = None,
        select_options=None,
        default_value=None,
        is_value_required: bool = None,
        min_value=None,
        max_value=None,
        min_length: int = None,
        max_length: int = None,
    ):
        if type is not None:
            self.type = type.name
        if select_options is not None:
            self.select_options = select_options
        if default_value is not None:
            self.default_value = default_value
        if is_value_required is not None:
            self.is_value_required = is_value_required
        if min_value is not None:
            self.min_value = min_value
        if max_value is not None:
            self.max_value = max_value
        if min_length is not None:
            self.min_length = min_length
        if max_length is not None:
            self.max_length = max_length
