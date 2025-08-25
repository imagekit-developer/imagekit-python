# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union
from typing_extensions import TypeAlias

from .file import File
from .folder import Folder

__all__ = ["AssetListResponse", "AssetListResponseItem"]

AssetListResponseItem: TypeAlias = Union[File, Folder]

AssetListResponse: TypeAlias = List[AssetListResponseItem]
