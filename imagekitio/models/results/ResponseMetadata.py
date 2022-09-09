class ResponseMetadata:
    def __init__(self, raw, http_status_code, headers):
        self.raw = raw
        self.http_status_code = http_status_code
        self.headers = headers
