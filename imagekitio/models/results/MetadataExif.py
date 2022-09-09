from .MetadataExifExif import MetadataExifExif
from .MetadataExifGPS import MetadataExifGPS
from .MetadataExifInteroperability import MetadataExifInteroperability
from .MetadataExifThumbnail import MetadataExifThumbnail
from .MetadataExifImage import MetadataExifImage


class MetadataExif:
    def __init__(
        self,
        image: MetadataExifImage = None,
        thumbnail: MetadataExifThumbnail = None,
        exif: MetadataExifExif = None,
        gps: MetadataExifGPS = None,
        interoperability: MetadataExifInteroperability = None,
        makernote=None,
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
                    image["Make"] if "Make" in image else None,
                    image["Model"] if "Model" in image else None,
                    image["Orientation"] if "Orientation" in image else None,
                    image["XResolution"] if "XResolution" in image else None,
                    image["YResolution"] if "YResolution" in image else None,
                    image["ResolutionUnit"] if "ResolutionUnit" in image else None,
                    image["Software"] if "Software" in image else None,
                    image["ModifyDate"] if "ModifyDate" in image else None,
                    image["YCbCrPositioning"] if "YCbCrPositioning" in image else None,
                    image["ExifOffset"] if "ExifOffset" in image else None,
                    image["GPSInfo"] if "GPSInfo" in image else None,
                )

        if thumbnail is None or thumbnail == {}:
            self.thumbnail = MetadataExifThumbnail(None, None, None, None, None, None)
        else:
            if type(thumbnail) == MetadataExifThumbnail:
                self.thumbnail = thumbnail
            else:
                self.thumbnail = MetadataExifThumbnail(
                    thumbnail["Compression"] if "Compression" in thumbnail else None,
                    thumbnail["XResolution"] if "XResolution" in thumbnail else None,
                    thumbnail["YResolution"] if "YResolution" in thumbnail else None,
                    thumbnail["ResolutionUnit"]
                    if "ResolutionUnit" in thumbnail
                    else None,
                    thumbnail["ThumbnailOffset"]
                    if "ThumbnailOffset" in thumbnail
                    else None,
                    thumbnail["ThumbnailLength"]
                    if "ThumbnailLength" in thumbnail
                    else None,
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
                    exif["ExposureTime"] if "ExposureTime" in exif else None,
                    exif["FNumber"] if "FNumber" in exif else None,
                    exif["ExposureProgram"] if "ExposureProgram" in exif else None,
                    exif["ISO"] if "ISO" in exif else None,
                    exif["ExifVersion"] if "ExifVersion" in exif else None,
                    exif["DateTimeOriginal"] if "DateTimeOriginal" in exif else None,
                    exif["CreateDate"] if "CreateDate" in exif else None,
                    exif["ShutterSpeedValue"] if "ShutterSpeedValue" in exif else None,
                    exif["ApertureValue"] if "ApertureValue" in exif else None,
                    exif["ExposureCompensation"]
                    if "ExposureCompensation" in exif
                    else None,
                    exif["MeteringMode"] if "MeteringMode" in exif else None,
                    exif["Flash"] if "Flash" in exif else None,
                    exif["FocalLength"] if "FocalLength" in exif else None,
                    exif["SubSecTime"] if "SubSecTime" in exif else None,
                    exif["SubSecTimeOriginal"]
                    if "SubSecTimeOriginal" in exif
                    else None,
                    exif["SubSecTimeDigitized"]
                    if "SubSecTimeDigitized" in exif
                    else None,
                    exif["FlashpixVersion"] if "FlashpixVersion" in exif else None,
                    exif["ColorSpace"] if "ColorSpace" in exif else None,
                    exif["ExifImageWidth"] if "ExifImageWidth" in exif else None,
                    exif["ExifImageHeight"] if "ExifImageHeight" in exif else None,
                    exif["InteropOffset"] if "InteropOffset" in exif else None,
                    exif["FocalPlaneXResolution"]
                    if "FocalPlaneXResolution" in exif
                    else None,
                    exif["FocalPlaneYResolution"]
                    if "FocalPlaneYResolution" in exif
                    else None,
                    exif["FocalPlaneResolutionUnit"]
                    if "FocalPlaneResolutionUnit" in exif
                    else None,
                    exif["CustomRendered"] if "CustomRendered" in exif else None,
                    exif["ExposureMode"] if "ExposureMode" in exif else None,
                    exif["WhiteBalance"] if "WhiteBalance" in exif else None,
                    exif["SceneCaptureType"] if "SceneCaptureType" in exif else None,
                )

        if gps is None or gps == {}:
            self.gps = MetadataExifGPS(None)
        else:
            if type(gps) == MetadataExifGPS:
                self.gps = gps
            else:
                self.gps = MetadataExifGPS(
                    gps["GPSVersionID"] if "GPSVersionID" in gps else None
                )

        if interoperability is None or interoperability == {}:
            self.interoperability = MetadataExifInteroperability(None, None)
        else:
            if type(interoperability) == MetadataExifInteroperability:
                self.interoperability = interoperability
            else:
                self.interoperability = MetadataExifInteroperability(
                    interoperability["InteropIndex"]
                    if "InteropIndex" in interoperability
                    else None,
                    interoperability["InteropVersion"]
                    if "InteropVersion" in interoperability
                    else None,
                )

        self.makernote = makernote
