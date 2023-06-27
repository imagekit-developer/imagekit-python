from typing import List

from .AITags import AITags
from .FileResult import FileResult
from .ResponseMetadata import ResponseMetadata
from .VersionInfo import VersionInfo


class FileResultWithResponseMetadata(FileResult):
    def __init__(
        self,
        type=None,
        name=None,
        created_at=None,
        updated_at=None,
        file_id=None,
        tags=None,
        ai_tags: List[AITags] = [],
        version_info: dict = {},
        embedded_metadata=None,
        custom_coordinates: str = "",
        custom_metadata=None,
        is_private_file=False,
        url: str = "",
        thumbnail: str = "",
        file_type: str = "",
        file_path: str = "",
        height: int = None,
        width: int = None,
        size: int = None,
        has_alpha=False,
        mime: str = None,
        extension_status=None,
        **kwargs
    ):
        super().__init__(
            type,
            name,
            created_at,
            updated_at,
            file_id,
            tags,
            ai_tags,
            version_info,
            embedded_metadata,
            custom_coordinates,
            custom_metadata,
            is_private_file,
            url,
            thumbnail,
            file_type,
            file_path,
            height,
            width,
            size,
            has_alpha,
            mime,
            extension_status,
            **kwargs
        )
        self.response_metadata: ResponseMetadata = ResponseMetadata("", "", "")
