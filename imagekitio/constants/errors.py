import enum


class ERRORS(enum.Enum):
    MANDATORY_INITIALIZATION_MISSING = {
        "message": "Missing public_key or private_key or url_endpoint during ImageKit initialization",
        help: "",
    }
    INVALID_TRANSFORMATION_POSITION = {
        "message": "Invalid transformationPosition parameter",
        help: "",
    }
    MANDATORY_SRC_OR_PATH = {
        "message": "Pass one of the mandatory parameter path or src"
    }
    INVALID_URL_GENERATION_PARAMETER = {"message": "Invalid url parameter", help: ""}
    INVALID_TRANSFORMATION_OPTIONS = {
        "message": "Invalid transformation parameter options",
        help: "",
    }
    CACHE_PURGE_URL_MISSING = {
        "message": "Missing URL parameter for this request",
        help: "",
    }
    CACHE_PURGE_STATUS_ID_MISSING = {
        "message": "Missing Request ID parameter for this request",
        help: "",
    }
    FILE_ID_MISSING = {
        "message": "Missing File ID parameter for this request",
        help: "",
    }
    UPDATE_DATA_MISSING = {
        "message": "Missing file update data for this request",
        help: "",
    }
    UPDATE_DATA_TAGS_INVALID = {
        "message": "Invalid tags parameter for this request",
        help: "tags should be passed as null or an array like ['tag1', 'tag2']",
    }
    UPDATE_DATA_COORDS_INVALID = (
        {
            "message": "Invalid custom_coordinates parameter for this request",
            help: "custom_coordinates should be passed as null or a string like 'x,y,width,height'",
        },
    )

    LIST_FILES_INPUT_MISSING = {
        "message": "Missing options for list files",
        help: "If you do not want to pass any parameter for listing, pass an empty object",
    }
    MISSING_FILE_URL = {"message": "Missing file_url for purge_cache", help: ""}
    MISSING_UPLOAD_DATA = {"message": "Missing data for upload", help: ""}
    MISSING_UPLOAD_FILE_PARAMETER = {
        "message": "Missing file parameter for upload",
        help: "",
    }
    MISSING_UPLOAD_FILENAME_PARAMETER = {
        "message": "Missing fileName parameter for upload",
        help: "",
    }

    INVALID_PHASH_VALUE = (
        {
            "message": "Invalid pHash value",
            help: "Both pHash strings must be valid hexadecimal numbers",
        },
    )
    MISSING_PHASH_VALUE = {
        "message": "Missing pHash value",
        help: "Please pass two pHash values",
    }
    UNEQUAL_STRING_LENGTH = {
        "message": "Unequal pHash string length",
        help: "For distance calculation, the two pHash strings must have equal length",
    }
