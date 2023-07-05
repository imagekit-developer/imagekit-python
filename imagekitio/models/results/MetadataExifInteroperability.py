class MetadataExifInteroperability:
    def __init__(self, interop_index=None, interop_version=None,**kwargs):
        self.interop_index = interop_index
        self.interop_version = interop_version
        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None

