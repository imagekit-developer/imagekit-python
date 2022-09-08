class DeleteFolderRequestOptions:
    def __init__(self, folder_path: str = None):
        if folder_path is not None:
            self.folder_path = folder_path
