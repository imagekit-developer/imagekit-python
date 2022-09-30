class MetadataExifThumbnail:
    def __init__(
        self,
        compression=None,
        x_resolution=None,
        y_resolution=None,
        resolution_unit=None,
        thumbnail_offset=None,
        thumbnail_length=None,
    ):
        self.compression = compression
        self.x_resolution = x_resolution
        self.y_resolution = y_resolution
        self.resolution_unit = resolution_unit
        self.thumbnail_offset = thumbnail_offset
        self.thumbnail_length = thumbnail_length
