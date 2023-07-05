class EmbeddedMetadata:
    
    def __init__(self, x_resolution=None, y_resolution=None, date_created=None, date_time_created=None,**kwargs):
        self.x_resolution = x_resolution
        self.y_resolution = y_resolution
        self.date_created = date_created
        self.date_time_created = date_time_created
        for key in kwargs.keys():
            self.__setattr__(key,kwargs[key])

    def __getattr__(self,attr):
        return None
        


