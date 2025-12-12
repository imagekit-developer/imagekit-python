# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from typing_extensions import Annotated, TypedDict

from .._types import SequenceNotStr
from .._utils import PropertyInfo

__all__ = ["CustomMetadataFieldUpdateParams", "Schema"]


class CustomMetadataFieldUpdateParams(TypedDict, total=False):
    label: str
    """Human readable name of the custom metadata field.

    This should be unique across all non deleted custom metadata fields. This name
    is displayed as form field label to the users while setting field value on an
    asset in the media library UI. This parameter is required if `schema` is not
    provided.
    """

    schema: Schema
    """An object that describes the rules for the custom metadata key.

    This parameter is required if `label` is not provided. Note: `type` cannot be
    updated and will be ignored if sent with the `schema`. The schema will be
    validated as per the existing `type`.
    """


class Schema(TypedDict, total=False):
    """An object that describes the rules for the custom metadata key.

    This parameter is required if `label` is not provided. Note: `type` cannot be updated and will be ignored if sent with the `schema`. The schema will be validated as per the existing `type`.
    """

    default_value: Annotated[
        Union[str, float, bool, SequenceNotStr[Union[str, float, bool]]], PropertyInfo(alias="defaultValue")
    ]
    """The default value for this custom metadata field.

    This property is only required if `isValueRequired` property is set to `true`.
    The value should match the `type` of custom metadata field.
    """

    is_value_required: Annotated[bool, PropertyInfo(alias="isValueRequired")]
    """Sets this custom metadata field as required.

    Setting custom metadata fields on an asset will throw error if the value for all
    required fields are not present in upload or update asset API request body.
    """

    max_length: Annotated[float, PropertyInfo(alias="maxLength")]
    """Maximum length of string.

    Only set this property if `type` is set to `Text` or `Textarea`.
    """

    max_value: Annotated[Union[str, float], PropertyInfo(alias="maxValue")]
    """Maximum value of the field.

    Only set this property if field type is `Date` or `Number`. For `Date` type
    field, set the minimum date in ISO8601 string format. For `Number` type field,
    set the minimum numeric value.
    """

    min_length: Annotated[float, PropertyInfo(alias="minLength")]
    """Minimum length of string.

    Only set this property if `type` is set to `Text` or `Textarea`.
    """

    min_value: Annotated[Union[str, float], PropertyInfo(alias="minValue")]
    """Minimum value of the field.

    Only set this property if field type is `Date` or `Number`. For `Date` type
    field, set the minimum date in ISO8601 string format. For `Number` type field,
    set the minimum numeric value.
    """

    select_options: Annotated[SequenceNotStr[Union[str, float, bool]], PropertyInfo(alias="selectOptions")]
    """An array of allowed values.

    This property is only required if `type` property is set to `SingleSelect` or
    `MultiSelect`.
    """
