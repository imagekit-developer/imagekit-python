from imagekitio.models.results.MetadataExifExif import MetadataExifExif
from imagekitio.models.results.MetadataExifGPS import MetadataExifGPS
from imagekitio.models.results.MetadataExifInteroperability import MetadataExifInteroperability
from imagekitio.models.results.MetadataExifThumbnail import MetadataExifThumbnail
from imagekitio.models.results.MetadataExif import MetadataExif
from imagekitio.models.results.MetadataExifImage import MetadataExifImage
from imagekitio.models.results.ResponseMetadata import ResponseMetadata


class GetMetadataResult:

    def __init__(self, height, width, size, format, has_color_profile, quality, density, has_transparency, p_hash,
                 exif: MetadataExif = MetadataExif(
                     MetadataExifImage(None, None, None, None, None, None, None, None, None, None, None),
                     MetadataExifThumbnail(None, None, None, None, None, None),
                     MetadataExifExif(None, None, None, None, None, None, None, None, None, None, None, None, None,
                                      None, None, None, None, None, None, None, None, None, None, None, None, None,
                                      None, None), MetadataExifGPS(None), MetadataExifInteroperability(None, None),
                     {})):
        self.height = height
        self.width = width
        self.size = size
        self.format = format
        self.has_color_profile = has_color_profile
        self.quality = quality
        self.density = density
        self.has_transparency = has_transparency
        self.p_hash = p_hash
        self.exif: MetadataExif = MetadataExif(exif['image'] if 'image' in exif else None,
                                               exif['thumbnail'] if 'thumbnail' in exif else None,
                                               exif['exif'] if 'exif' in exif else None,
                                               exif['gps'] if 'gps' in exif else None,
                                               exif['interoperability'] if 'interoperability' in exif else None,
                                               exif['makernote'] if 'makernote' in exif else None)
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
