class MetadataExifImage:

    def __init__(self, make, model, orientation, x_resolution, y_resolution, resolution_unit, software, modify_date,
                 y_cb_cr_positioning, exif_offset, gps_info):
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
