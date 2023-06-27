class VersionInfo:
    def __init__(self, id=None, name=None,**kwargs):
        self.id = id
        self.name = name
        for key in kwargs.keys():
            self.__setattr__(key,kwargs[key])

    def __getattr__(self,attr):
        return None
    

    

