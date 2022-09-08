from typing import List
from .AITags import AITags
from .VersionInfo import VersionInfo


class FileResult:
    def __init__(
        self,
        type,
        name,
        created_at,
        updated_at,
        file_id,
        tags,
        ai_tags: List[AITags] = AITags(None, None, None),
        version_info: VersionInfo = VersionInfo(None, None),
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
    ):
        if extension_status is None:
            extension_status = {}
        if embedded_metadata is None:
            embedded_metadata = {}
        if custom_metadata is None:
            custom_metadata = {}
        self.type = type
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.file_id = file_id
        self.tags = tags
        self.ai_tags: List[AITags] = []
        if ai_tags is not None:
            for i in ai_tags:
                self.ai_tags.append(AITags(i["name"], i["confidence"], i["source"]))
        else:
            self.ai_tags.append(AITags(None, None, None))
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
