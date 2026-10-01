# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Union, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["CustomMetadataField", "Schema"]


class Schema(BaseModel):
    """An object that describes the rules for the custom metadata field value."""

    type: Literal["Text", "Textarea", "Number", "Date", "Boolean", "SingleSelect", "MultiSelect"]
    """Type of the custom metadata field."""

    default_value: Union[str, float, bool, List[Union[str, float, bool]], None] = FieldInfo(
        alias="defaultValue", default=None
    )
    """The default value for this custom metadata field.

    Data type of default value depends on the field type.
    """

    is_value_required: Optional[bool] = FieldInfo(alias="isValueRequired", default=None)
    """Specifies if the this custom metadata field is required or not."""

    max_length: Optional[float] = FieldInfo(alias="maxLength", default=None)
    """Maximum length of string. Only set if `type` is set to `Text` or `Textarea`."""

    max_value: Union[str, float, None] = FieldInfo(alias="maxValue", default=None)
    """Maximum value of the field.

    Only set if field type is `Date` or `Number`. For `Date` type field, the value
    will be in ISO8601 string format. For `Number` type field, it will be a numeric
    value.
    """

    min_length: Optional[float] = FieldInfo(alias="minLength", default=None)
    """Minimum length of string. Only set if `type` is set to `Text` or `Textarea`."""

    min_value: Union[str, float, None] = FieldInfo(alias="minValue", default=None)
    """Minimum value of the field.

    Only set if field type is `Date` or `Number`. For `Date` type field, the value
    will be in ISO8601 string format. For `Number` type field, it will be a numeric
    value.
    """

    select_options: Optional[List[Union[str, float, bool]]] = FieldInfo(alias="selectOptions", default=None)
    """An array of allowed values when field type is `SingleSelect` or `MultiSelect`."""


class CustomMetadataField(BaseModel):
    """Object containing details of a custom metadata field."""

    id: str
    """Unique identifier for the custom metadata field. Use this to update the field."""

    label: str
    """Human readable name of the custom metadata field.

    This name is displayed as form field label to the users while setting field
    value on the asset in the media library UI.
    """

    name: str
    """API name of the custom metadata field.

    This becomes the key while setting `customMetadata` (key-value object) for an
    asset using upload or update API.
    """

    schema_: Schema = FieldInfo(alias="schema")
    """An object that describes the rules for the custom metadata field value."""

    description: Optional[str] = None
    """Optional description of the custom metadata field.

    Only present when a description has been set. Shown as a hint to the users while
    setting the field's value on an asset in the media library UI.
    """

    reserved: Optional[bool] = None
    """Present and set to `true` when the field is reserved, i.e.

    created and managed by ImageKit rather than by you. Omitted for regular fields.

    Currently the only reserved field is `_internal_original_created_datetime`
    (label "Original creation date", type `Date`). ImageKit creates it when you
    enable the original creation date setting under the Custom Metadata tab of the
    media library settings in the dashboard. Use it to preserve the original
    creation date of assets migrated from another system: set its value through the
    `customMetadata` object in the upload or update file details API, then sort with
    `ASC_ORIGINAL_CREATION_DATE` or `DESC_ORIGINAL_CREATION_DATE` in the list and
    search assets API, or filter with
    `"customMetadata._internal_original_created_datetime"` in `searchQuery`.

    Reserved fields cannot be deleted, and their name cannot be reused when creating
    a new field.
    """
