class CopyFolderRequestOptions:
    def __init__(
        self,
        source_folder_path: str = None,
        destination_path: str = None,
        include_file_versions: bool = None,
    ):
        if source_folder_path is not None:
            self.source_folder_path = source_folder_path
        if destination_path is not None:
            self.destination_path = destination_path
        if include_file_versions is not None:
            self.include_file_versions = include_file_versions
