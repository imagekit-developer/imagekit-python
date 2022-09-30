class MoveFolderRequestOptions:
    def __init__(self, source_folder_path: str = None, destination_path: str = None):
        if source_folder_path is not None:
            self.source_folder_path = source_folder_path
        if destination_path is not None:
            self.destination_path = destination_path
