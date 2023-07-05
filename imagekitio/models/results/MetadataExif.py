from .MetadataExifExif import MetadataExifExif
from .MetadataExifGPS import MetadataExifGPS
from .MetadataExifInteroperability import MetadataExifInteroperability
from .MetadataExifThumbnail import MetadataExifThumbnail
from .MetadataExifImage import MetadataExifImage
from ...utils.utils import camel_dict_to_snake_dict


class MetadataExif:
    def __init__(
        self,
        image: MetadataExifImage = None,
        thumbnail: MetadataExifThumbnail = None,
        exif: MetadataExifExif = None,
        gps: MetadataExifGPS = None,
        interoperability: MetadataExifInteroperability = None,
        makernote=None,
        ** kwargs
    ):  
        if makernote is None:
            makernote = {}
        if image is None or image == {}:
            self.image = MetadataExifImage(
                None, None, None, None, None, None, None, None, None, None, None
            )
        else:
            if type(image) == MetadataExifImage:
                self.image = image
            else:
                self.image = MetadataExifImage(
                    **camel_dict_to_snake_dict(image)
                )

        if thumbnail is None or thumbnail == {}:
            self.thumbnail = MetadataExifThumbnail(None, None, None, None, None, None)
        else:
            if type(thumbnail) == MetadataExifThumbnail:
                self.thumbnail = thumbnail
            else:
                self.thumbnail = MetadataExifThumbnail(
                    **camel_dict_to_snake_dict(thumbnail)
                )
        if exif is None or exif == {}:
            self.exif = MetadataExifExif(
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
            )
        else:
            if type(exif) == MetadataExifExif:
                self.exif = exif
            else:
                self.exif = MetadataExifExif(
                    **camel_dict_to_snake_dict(exif)
                )
        if gps is None or gps == {}:
            self.gps = MetadataExifGPS(None)
        else:
            if type(gps) == MetadataExifGPS:
                self.gps = gps
            else:
                self.gps = MetadataExifGPS(   
                    **camel_dict_to_snake_dict(gps)
                )

        if interoperability is None or interoperability == {}:
            self.interoperability = MetadataExifInteroperability(None, None)
        else:
            if type(interoperability) == MetadataExifInteroperability:
                self.interoperability = interoperability
            else:
                self.interoperability = MetadataExifInteroperability(
                    **camel_dict_to_snake_dict(interoperability)
                )

        self.makernote = makernote
        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None
