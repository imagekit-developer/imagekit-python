from typing import List


class MetadataExifGPS:
    def __init__(self, gps_version_id=None):
        if gps_version_id is None:
            gps_version_id = []
        self.gps_version_id: List[int] = []
        for i in gps_version_id:
            self.gps_version_id.append(i)
