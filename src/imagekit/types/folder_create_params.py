# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FolderCreateParams"]


class FolderCreateParams(TypedDict, total=False):
    folder_name: Required[Annotated[str, PropertyInfo(alias="folderName")]]
    """The folder will be created with this name.

    All characters except alphabets and numbers (inclusive of unicode letters,
    marks, and numerals in other languages) will be replaced by an underscore i.e.
    `_`.
    """

    parent_folder_path: Required[Annotated[str, PropertyInfo(alias="parentFolderPath")]]
    """
    The folder where the new folder should be created, for root use `/` else the
    path e.g. `containing/folder/`.

    Note: If any folder(s) is not present in the parentFolderPath parameter, it will
    be automatically created. For example, if you pass `/product/images/summer`,
    then `product`, `images`, and `summer` folders will be created if they don't
    already exist.
    """
