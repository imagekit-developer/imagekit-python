import array


class ListAndSearchFileRequestOptions:
    def __init__(
        self,
        type: str = None,
        sort: str = None,
        path: str = None,
        search_query: str = None,
        file_type: str = None,
        limit: int = None,
        skip: int = None,
        tags=None,
    ):
        if type is not None:
            self.type = type
        if sort is not None:
            self.sort = sort
        if path is not None:
            self.path = path
        if search_query is not None:
            self.search_query = search_query
        if file_type is not None:
            self.file_type = file_type
        if limit is not None:
            self.limit = limit
        if skip is not None:
            self.skip = skip
        if tags is not None:
            self.tags = tags
