from enum import Enum


class URL:
    BASE_URL = "https://api.imagekit.io/v1/files"
    PURGE_CACHE = "/purge"
    UPLOAD_URL = "https://upload.imagekit.io/api/v1/files/upload"
    BULK_FILE_DELETE = "/batch/deleteByFileIds"
    REMOTE_METADATA_FULL_URL = "https://api.imagekit.io/v1/metadata"
    API_BASE_URL = "https://api.imagekit.io/"
    UPLOAD_BASE_URL = "https://upload.imagekit.io/"
