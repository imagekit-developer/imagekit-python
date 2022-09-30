class CreateFolderRequestOptions:
    def __init__(self, folder_name: str = None, parent_folder_path: str = None):
        if folder_name is not None:
            self.folder_name = folder_name
        if parent_folder_path is not None:
            self.parent_folder_path = parent_folder_path
