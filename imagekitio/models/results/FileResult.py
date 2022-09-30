from typing import List
from .AITags import AITags
from .VersionInfo import VersionInfo


class FileResult:
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
        embedded_metadata: dict = {},
        custom_coordinates: str = "",
        custom_metadata: dict = {},
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
        extension_status: dict = {},
    ):
        self.type = type
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.file_id = file_id
        self.tags = tags
        self.ai_tags: List[AITags] = []
        if ai_tags is not None:
            for i in ai_tags:
                self.ai_tags.append(
                    AITags(
                        i["name"] if "name" in i else None,
                        i["confidence"] if "confidence" in i else None,
                        i["source"] if "source" in i else None,
                    )
                )
        self.version_info = VersionInfo(version_info["id"], version_info["name"])
        self.embedded_metadata = embedded_metadata
        self.custom_coordinates = custom_coordinates
        self.custom_metadata = custom_metadata
        self.is_private_file = is_private_file
        self.url = url
        self.thumbnail = thumbnail
        self.file_type = file_type
        self.file_path = file_path
        self.height = height
        self.width = width
        self.size = size
        self.has_alpha = has_alpha
        self.mime = mime
        self.extension_status = extension_status
