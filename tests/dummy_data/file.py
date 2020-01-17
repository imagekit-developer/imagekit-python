FAILED_GENERIC_RESP = {"message": "Hi There is an error"}
SUCCESS_GENERIC_RESP = {"response": "Success"}
AUTHENTICATION_ERR_MSG = {
    "message": "Your account cannot be authenticated.",
    "help": "For support kindly contact us at support@imagekit.io .",
}
FAILED_DELETE_RESP = {"message": "Item Not Found"}

SUCCESS_PURGE_CACHE_MSG = {"request_id": "fake_abc_xyz"}

SUCCESS_PURGE_CACHE_STATUS_MSG = {"status": "pending"}

SERVER_ERR_MSG = {
    "message": "We have experienced an internal error while processing your request.",
    "help": "For support kindly contact us at support@imagekit.io .",
}

SUCCESS_LIST_RESP_MESSAGE = {
    "response": [
        {
            "type": "file",
            "name": "default-image.jpg",
            "fileId": "53dgd6023f28ft7fse488992c",
            "tags": None,
            "customCoordinates": None,
            "isPrivateFile": None,
            "url": "https://ik.imagekit.io/fakeid/default-image.jpg",
            "thumbnail": "https://ik.imagekit.io/fakeid/tr:n-media_library_thumbnail/default-image.jpg",
            "fileType": "image",
            "filePath": "/default-image.jpg",
        },
        {
            "type": "file",
            "name": "default-image.jpg",
            "fileId": "53dgd6023f28ft7fse488992c",
            "tags": None,
            "customCoordinates": None,
            "isPrivateFile": None,
            "url": "https://ik.imagekit.io/fakeid/default-image.jpg",
            "thumbnail": "https://ik.imagekit.io/fakeid/tr:n-media_library_thumbnail/default-image.jpg",
            "fileType": "image",
            "filePath": "/default-image.jpg",
        },
    ],
}

SUCCESS_DETAIL_MSG = {
    "response": {
        "type": "file",
        "name": "default-image.jpg",
        "fileId": "53dgd6023f28ft7fse488992c",
        "tags": None,
        "customCoordinates": None,
        "isPrivateFile": None,
        "url": "https://ik.imagekit.io/fakeid/default-image.jpg",
        "thumbnail": "https://ik.imagekit.io/fakeid/tr:n-media_library_thumbnail/default-image.jpg",
        "fileType": "image",
        "filePath": "/default-image.jpg",
    }
}
