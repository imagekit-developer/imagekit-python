
class UploadResult:

    def __init__(self, type, name, created_at, updated_at, file_id, tags, ai_tags, version_info, embedded_metadata, custom_coordinates, custom_metadata, is_private_file, url, thumbnail, file_type, file_path, height, width, size, has_alpha, mime):
        self.type = type
        self.name = name
        self.created_at = created_at
        self.updated_at = updated_at
        self.file_id = file_id
        self.tags = tags
        self.ai_tags = ai_tags
        self.version_info = version_info
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

    def __str__(self):
        return str(self.__dict__)
