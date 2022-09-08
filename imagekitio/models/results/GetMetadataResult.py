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
        height,
        width,
        size,
        format,
        has_color_profile,
        quality,
        density,
        has_transparency,
        p_hash,
        exif: MetadataExif = MetadataExif(
            MetadataExifImage(
                None, None, None, None, None, None, None, None, None, None, None
            ),
            MetadataExifThumbnail(None, None, None, None, None, None),
            MetadataExifExif(
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
                None,
            ),
            MetadataExifGPS(None),
            MetadataExifInteroperability(None, None),
            {},
        ),
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
        self.exif = exif
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
