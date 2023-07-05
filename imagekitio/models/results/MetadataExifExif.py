class MetadataExifExif:
    def __init__(
        self,
        exposure_time=None,
        f_number=None,
        exposure_program=None,
        iso=None,
        exif_version=None,
        date_time_original=None,
        create_date=None,
        shutter_speed_value=None,
        aperture_value=None,
        exposure_compensation=None,
        metering_mode=None,
        flash=None,
        focal_length=None,
        sub_sec_time=None,
        sub_sec_time_original=None,
        sub_sec_time_digitized=None,
        flashpix_version=None,
        color_space=None,
        exif_image_width=None,
        exif_image_height=None,
        interop_offset=None,
        focal_plane_x_resolution=None,
        focal_plane_y_resolution=None,
        focal_plane_resolution_unit=None,
        custom_rendered=None,
        exposure_mode=None,
        white_balance=None,
        scene_capture_type=None,
        **kwargs
    ):
        self.exposure_time = exposure_time
        self.f_number = f_number
        self.exposure_program = exposure_program
        self.iso = iso
        self.exif_version = exif_version
        self.date_time_original = date_time_original
        self.create_date = create_date
        self.shutter_speed_value = shutter_speed_value
        self.aperture_value = aperture_value
        self.exposure_compensation = exposure_compensation
        self.metering_mode = metering_mode
        self.flash = flash
        self.focal_length = focal_length
        self.sub_sec_time = sub_sec_time
        self.sub_sec_time_original = sub_sec_time_original
        self.sub_sec_time_digitized = sub_sec_time_digitized
        self.flashpix_version = flashpix_version
        self.color_space = color_space
        self.exif_image_width = exif_image_width
        self.exif_image_height = exif_image_height
        self.interop_offset = interop_offset
        self.focal_plane_x_resolution = focal_plane_x_resolution
        self.focal_plane_y_resolution = focal_plane_y_resolution
        self.focal_plane_resolution_unit = focal_plane_resolution_unit
        self.custom_rendered = custom_rendered
        self.exposure_mode = exposure_mode
        self.white_balance = white_balance
        self.scene_capture_type = scene_capture_type
        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None
