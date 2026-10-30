# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date, datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .contract_units import ContractUnits

__all__ = ["ContractGetResponse"]


class ContractGetResponse(BaseModel):
    has_contract: bool = FieldInfo(alias="hasContract")
    """Whether the account has an active contract.

    The other fields are present only when it does.
    """

    as_of: Optional[datetime] = FieldInfo(alias="asOf", default=None)
    """When `consumed` was last computed.

    `null` if it has not been computed for the contract yet; `consumed` is then all
    zeros.
    """

    consumed: Optional[ContractUnits] = None
    """Usage consumed in the current contract term.

    For an agency account, this includes the child accounts billed to it.
    """

    contract_months: Optional[int] = FieldInfo(alias="contractMonths", default=None)
    """Length of each contract term in months."""

    effective_contract_end_date: Optional[date] = FieldInfo(alias="effectiveContractEndDate", default=None)
    """End date of the current contract term."""

    effective_contract_start_date: Optional[date] = FieldInfo(alias="effectiveContractStartDate", default=None)
    """Start date of the current contract term.

    It moves forward when the contract renews.
    """

    original_contract_start_date: Optional[date] = FieldInfo(alias="originalContractStartDate", default=None)
    """Start date of the first contract term."""

    quota: Optional[ContractUnits] = None
    """Usage included in the current contract term."""
