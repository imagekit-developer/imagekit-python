# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Interoperability"]


class Interoperability(BaseModel):
    interop_index: Optional[str] = FieldInfo(alias="InteropIndex", default=None)

    interop_version: Optional[str] = FieldInfo(alias="InteropVersion", default=None)
