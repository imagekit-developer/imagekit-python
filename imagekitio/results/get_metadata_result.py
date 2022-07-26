class GetMetadataResult:

    def __init__(self, height, width, size, format, has_color_profile, quality, density, has_transparency, p_hash, exif):
        self.height = height
        self.width = width
        self.size = size
        self.format = format
        self.has_color_profile = has_color_profile
        self.quality = quality
        self.density = density
        self.has_transparency = has_transparency
        self.p_hash = p_hash
        self.exif = exif
        self._response_metadata = {}

    def __str__(self):
        return self.__dict__

    @property
    def response_metadata(self):
        return self._response_metadata
