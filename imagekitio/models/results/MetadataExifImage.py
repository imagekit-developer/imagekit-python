class MetadataExifImage:
    def __init__(
        self,
        make=None,
        model=None,
        orientation=None,
        x_resolution=None,
        y_resolution=None,
        resolution_unit=None,
        software=None,
        modify_date=None,
        y_cb_cr_positioning=None,
        exif_offset=None,
        gps_info=None,
        **kwargs
    ):
        self.make = make
        self.model = model
        self.orientation = orientation
        self.x_resolution = x_resolution
        self.y_resolution = y_resolution
        self.resolution_unit = resolution_unit
        self.software = software
        self.modify_date = modify_date
        self.y_cb_cr_positioning = y_cb_cr_positioning
        self.exif_offset = exif_offset
        self.gps_info = gps_info
        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None
