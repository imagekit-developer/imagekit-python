class CustomMetadataSchema:
    def __init__(
        self,
        type=None,
        select_options=None,
        default_value=None,
        is_value_required=None,
        min_value=None,
        max_value=None,
        min_length=None,
        max_length=None,
    ):
        self.type = type
        self.select_options = select_options
        self.default_value = default_value
        self.is_value_required = is_value_required
        self.min_value = min_value
        self.max_value = max_value
        self.min_length = min_length
        self.max_length = max_length
