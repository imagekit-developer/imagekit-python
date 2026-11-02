# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Generic, TypeVar, Optional
from typing_extensions import override

from pydantic import Field as FieldInfo

from ._base_client import BasePage, PageInfo, BaseSyncPage, BaseAsyncPage

__all__ = ["SyncTagCursor", "AsyncTagCursor"]

_T = TypeVar("_T")


class SyncTagCursor(BaseSyncPage[_T], BasePage[_T], Generic[_T]):
    tags: List[_T]
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        tags = self.tags
        if not tags:
            return []
        return tags

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})


class AsyncTagCursor(BaseAsyncPage[_T], BasePage[_T], Generic[_T]):
    tags: List[_T]
    next_cursor: Optional[str] = FieldInfo(alias="nextCursor", default=None)

    @override
    def _get_page_items(self) -> List[_T]:
        tags = self.tags
        if not tags:
            return []
        return tags

    @override
    def next_page_info(self) -> Optional[PageInfo]:
        next_cursor = self.next_cursor
        if not next_cursor:
            return None

        return PageInfo(params={"cursor": next_cursor})
