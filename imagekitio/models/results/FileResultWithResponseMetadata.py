from typing import List

from imagekitio.models.results.AITags import AITags
from imagekitio.models.results.FileResult import FileResult
from imagekitio.models.results.ResponseMetadata import ResponseMetadata
from imagekitio.models.results.VersionInfo import VersionInfo


class FileResultWithResponseMetadata(FileResult):

    def __init__(self, type, name, created_at, updated_at, file_id, tags,
                 ai_tags: List[AITags] = AITags(None, None, None), version_info: VersionInfo = VersionInfo(None, None),
                 embedded_metadata=None,
                 custom_coordinates: str = '', custom_metadata=None, is_private_file=False, url: str = '',
                 thumbnail: str = '', file_type: str = '', file_path: str = '',
                 height: int = None, width: int = None, size: int = None, has_alpha=False, mime: str = None,
                 extension_status=None):
        super(FileResultWithResponseMetadata, self).__init__(type, name, created_at, updated_at, file_id, tags, ai_tags, version_info,
                            embedded_metadata,
                            custom_coordinates, custom_metadata, is_private_file, url, thumbnail, file_type, file_path,
                            height, width, size, has_alpha, mime, extension_status)
        self.response_metadata: ResponseMetadata = ResponseMetadata("", "", "")
