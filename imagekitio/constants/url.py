from enum import Enum


class URL(Enum):
    BASE_URL = "https://api.imagekit.io/v1/files"
    PURGE_CACHE = "/purge"
    UPLOAD = "/upload"
