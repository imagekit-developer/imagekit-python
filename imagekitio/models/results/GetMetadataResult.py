from .MetadataExifExif import MetadataExifExif
from .MetadataExifGPS import MetadataExifGPS
from .MetadataExifInteroperability import MetadataExifInteroperability
from .MetadataExifThumbnail import MetadataExifThumbnail
from .MetadataExif import MetadataExif
from .MetadataExifImage import MetadataExifImage
from .ResponseMetadata import ResponseMetadata


class GetMetadataResult:
    def __init__(
        self,
        height=None,
        width=None,
        size=None,
        format=None,
        has_color_profile=None,
        quality=None,
        density=None,
        has_transparency=None,
        p_hash=None,
        exif: dict = {},
    ):
        self.height = height
        self.width = width
        self.size = size
        self.format = format
        self.has_color_profile = has_color_profile
        self.quality = quality
        self.density = density
        self.has_transparency = has_transparency
        self.p_hash = p_hash
        self.exif: MetadataExif = MetadataExif(
            exif["image"] if "image" in exif else None,
            exif["thumbnail"] if "thumbnail" in exif else None,
            exif["exif"] if "exif" in exif else None,
            exif["gps"] if "gps" in exif else None,
            exif["interoperability"] if "interoperability" in exif else None,
            exif["makernote"] if "makernote" in exif else None,
        )
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
