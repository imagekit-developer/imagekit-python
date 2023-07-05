class ResponseMetadata:
    def __init__(self, raw=None, http_status_code=None, headers=None,**kwargs):
        self.raw = raw
        self.http_status_code = http_status_code
        self.headers = headers
        for key in kwargs.keys():
            self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None
