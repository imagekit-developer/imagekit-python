from .CustomMetadataSchema import CustomMetadataSchema
from ...utils.utils import camel_dict_to_snake_dict

class CustomMetadataFieldsResult:
    def __init__(
        self,
        id=None,
        name=None,
        label=None,
        schema: dict = {},
        **kwargs
    ):
        self.id = id
        self.name = name
        self.label = label
        self.schema = CustomMetadataSchema(
            **camel_dict_to_snake_dict(schema)
        )
        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None

