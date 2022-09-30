class MoveFileRequestOptions:
    def __init__(self, source_file_path: str = None, destination_path: str = None):
        if source_file_path is not None:
            self.source_file_path = source_file_path
        if destination_path is not None:
            self.destination_path = destination_path
