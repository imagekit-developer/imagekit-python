class UploadFileResult:

    def __init__(self, file_id, name, url, thumbnail_url: str = None, height: int = None, width: int = None, size: int = None, file_path: str = None, tags: {} = None,
                 ai_tags: {} = None, version_info: {} = None,
                 is_private_file=False, custom_coordinates: {} = None, custom_metadata: {} = None,
                 embedded_metadata: {} = None, extension_status: {} = None, file_type: str = None):
        self.file_id = file_id
        self.name = name
        self.url = url
        self.thumbnail_url = thumbnail_url
        self.height = height
        self.width = width
        self.size = size
        self.file_path = file_path
        self.tags = tags
        self.ai_tags = ai_tags
        self.version_info = version_info
        self.is_private_file = is_private_file
        self.custom_coordinates = custom_coordinates
        self.custom_metadata = custom_metadata
        self.embedded_metadata = embedded_metadata
        self.extension_status = extension_status
        self.file_type = file_type
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
