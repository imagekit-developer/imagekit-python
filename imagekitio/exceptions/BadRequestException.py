from ..models.results.ResponseMetadata import ResponseMetadata


class BadRequestException(Exception):
    def __init__(
        self,
        message,
        response_help,
        response_metadata: ResponseMetadata = ResponseMetadata(None, None, None),
    ):
        self.message = message
        self.response_help = response_help
        self.response_metadata = response_metadata

    def __str__(self):
        return str(self.message)
