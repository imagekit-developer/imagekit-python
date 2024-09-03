import json
from typing import List


class UploadFileRequestOptions:
    def __init__(
        self,
        use_unique_file_name: bool = None,
        tags: List[str] = None,
        folder: str = None,
        is_private_file: bool = None,
        custom_coordinates: str = None,
        response_fields: List[str] = None,
        extensions: json = None,
        webhook_url: str = None,
        overwrite_file: bool = None,
        overwrite_ai_tags: bool = None,
        overwrite_tags: bool = None,
        overwrite_custom_metadata: bool = None,
        custom_metadata: json = None,
        transformation: json = None,
        checks: str = None,
        is_published: bool = None,
    ):
        if use_unique_file_name is not None:
            self.use_unique_file_name = use_unique_file_name
        if tags is not None:
            self.tags = tags
        if folder is not None:
            self.folder = folder
        if is_private_file is not None:
            self.is_private_file = is_private_file
        if custom_coordinates is not None:
            self.custom_coordinates = custom_coordinates
        if response_fields is not None:
            self.response_fields = response_fields
        if extensions is not None:
            self.extensions = extensions
        if webhook_url is not None:
            self.webhook_url = webhook_url
        if overwrite_file is not None:
            self.overwrite_file = overwrite_file
        if overwrite_ai_tags is not None:
            self.overwrite_ai_tags = overwrite_ai_tags
        if overwrite_tags is not None:
            self.overwrite_tags = overwrite_tags
        if overwrite_custom_metadata is not None:
            self.overwrite_custom_metadata = overwrite_custom_metadata
        if custom_metadata is not None:
            self.custom_metadata = custom_metadata
        if transformation is not None:
            self.transformation = transformation
        if checks is not None:
            self.checks = checks
        if is_published is not None:
            self.is_published = is_published
