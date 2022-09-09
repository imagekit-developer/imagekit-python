import json
from typing import List


class UpdateFileRequestOptions:
    def __init__(
        self,
        remove_a_i_tags: List[str] = None,
        webhook_url: str = None,
        extensions: json = None,
        tags: List[str] = None,
        custom_coordinates: str = None,
        custom_metadata: json = None,
    ):
        if remove_a_i_tags is not None:
            self.remove_a_i_tags = remove_a_i_tags
        if webhook_url is not None:
            self.webhook_url = webhook_url
        if extensions is not None:
            self.extensions = extensions
        if tags is not None:
            self.tags = tags
        if custom_coordinates is not None:
            self.custom_coordinates = custom_coordinates
        if custom_metadata is not None:
            self.custom_metadata = custom_metadata
