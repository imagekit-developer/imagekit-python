from .MetadataExifExif import MetadataExifExif
from .MetadataExifGPS import MetadataExifGPS
from .MetadataExifInteroperability import MetadataExifInteroperability
from .MetadataExifThumbnail import MetadataExifThumbnail
from .MetadataExif import MetadataExif
from .MetadataExifImage import MetadataExifImage
from .ResponseMetadata import ResponseMetadata
from ...utils.utils import camel_dict_to_snake_dict


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
        **kwargs
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
            ** camel_dict_to_snake_dict(exif)
        )
        self.__response_metadata: ResponseMetadata = ResponseMetadata("", "", "")

        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None

    @property
    def response_metadata(self):
        return self.__response_metadata

    @response_metadata.setter
    def response_metadata(self, value):
        self.__response_metadata = value
