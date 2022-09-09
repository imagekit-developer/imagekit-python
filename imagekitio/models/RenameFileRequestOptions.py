class RenameFileRequestOptions:
    def __init__(
        self, file_path: str = None, new_file_name: str = None, purge_cache: bool = None
    ):
        if file_path is not None:
            self.file_path = file_path
        if new_file_name is not None:
            self.new_file_name = new_file_name
        if purge_cache is not None:
            self.purge_cache = purge_cache
