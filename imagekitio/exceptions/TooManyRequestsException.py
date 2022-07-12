class TooManyRequestsException(Exception):

    def __init__(self, message, response_help, response_metadata):
        self.message = message
        self.response_help = response_help
        self.response_metadata = response_metadata

    def __str__(self):
        return str(self.message)
