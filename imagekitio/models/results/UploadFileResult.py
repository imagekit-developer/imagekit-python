from typing import List

from .AITags import AITags
from .EmbeddedMetadata import EmbeddedMetadata
from .ResponseMetadata import ResponseMetadata
from .VersionInfo import VersionInfo


class UploadFileResult:
    def __init__(
        self,
        file_id=None,
        name=None,
        url=None,
        thumbnail_url: str = None,
        height: int = None,
        width: int = None,
        size: int = None,
        file_path: str = None,
        tags: dict = None,
        ai_tags: List[AITags] = AITags(None, None, None),
        version_info: VersionInfo = VersionInfo(None, None),
        is_private_file=False,
        custom_coordinates: dict = None,
        custom_metadata: dict = None,
        embedded_metadata: EmbeddedMetadata = EmbeddedMetadata(None, None, None, None),
        extension_status: dict = None,
        file_type: str = None,
        orientation: int = None
    ):
        self.file_id = file_id
        self.name = name
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.height = height
        self.width = width
        self.size = size
        self.file_path = file_path
        self.tags = tags
        self.ai_tags: List[AITags] = []
        if ai_tags is not None:
            for i in ai_tags:
                self.ai_tags.append(AITags(i["name"], i["confidence"], i["source"]))
        else:
            self.ai_tags.append(AITags(None, None, None))
        self.version_info = VersionInfo(version_info["id"], version_info["name"])
        self.is_private_file = is_private_file
        self.custom_coordinates = custom_coordinates
        self.custom_metadata = custom_metadata
        if embedded_metadata is None or embedded_metadata == {}:
            self.embedded_metadata = EmbeddedMetadata(None, None, None, None)
        else:
            if type(embedded_metadata) == EmbeddedMetadata:
                self.embedded_metadata = embedded_metadata
            else:
                self.embedded_metadata: EmbeddedMetadata = EmbeddedMetadata(
                    embedded_metadata["x_resolution"],
                    embedded_metadata["y_resolution"],
                    embedded_metadata["date_created"],
                    embedded_metadata["date_timecreated"],
                )
        self.extension_status = extension_status
        self.file_type = file_type
        self.orientation = orientation
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
