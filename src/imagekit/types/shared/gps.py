# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["Gps"]


class Gps(BaseModel):
    gps_version_id: Optional[List[int]] = FieldInfo(alias="GPSVersionID", default=None)
