class ResponseMetadata:
    def __init__(self, raw=None, http_status_code=None, headers=None):
        self.raw = raw
        self.http_status_code = http_status_code
        self.headers = headers
