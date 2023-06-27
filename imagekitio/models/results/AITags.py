class AITags:
    def __init__(self, name=None, confidence=None, source=None,**kwargs):
        self.name = name
        self.confidence = confidence
        self.source = source
        for key in kwargs.keys():
                self.__setattr__(key,kwargs[key])
    def __getattr__(self,key):
        return None

