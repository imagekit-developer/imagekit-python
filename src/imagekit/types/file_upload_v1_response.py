# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .gps import Gps
from .._models import BaseModel
from .thumbnail import Thumbnail
from .exif_image import ExifImage
from .exif_details import ExifDetails
from .interoperability import Interoperability

__all__ = [
    "FileUploadV1Response",
    "AITag",
    "EmbeddedMetadata",
    "ExtensionStatus",
    "Metadata",
    "MetadataExif",
    "VersionInfo",
]


class AITag(BaseModel):
    confidence: Optional[float] = None
    """Confidence score of the tag."""

    name: Optional[str] = None
    """Name of the tag."""

    source: Optional[str] = None
    """Array of `AITags` associated with the image.

    If no `AITags` are set, it will be null. These tags can be added using the
    `google-auto-tagging` or `aws-auto-tagging` extensions.
    """


class EmbeddedMetadata(BaseModel):
    about_cv_term_cv_id: Optional[str] = FieldInfo(alias="AboutCvTermCvId", default=None)

    about_cv_term_id: Optional[str] = FieldInfo(alias="AboutCvTermId", default=None)

    about_cv_term_name: Optional[str] = FieldInfo(alias="AboutCvTermName", default=None)

    about_cv_term_refined_about: Optional[str] = FieldInfo(alias="AboutCvTermRefinedAbout", default=None)

    additional_model_information: Optional[str] = FieldInfo(alias="AdditionalModelInformation", default=None)

    application_record_version: Optional[int] = FieldInfo(alias="ApplicationRecordVersion", default=None)

    artist: Optional[str] = FieldInfo(alias="Artist", default=None)

    artwork_circa_date_created: Optional[str] = FieldInfo(alias="ArtworkCircaDateCreated", default=None)

    artwork_content_description: Optional[str] = FieldInfo(alias="ArtworkContentDescription", default=None)

    artwork_contribution_description: Optional[str] = FieldInfo(alias="ArtworkContributionDescription", default=None)

    artwork_copyright_notice: Optional[str] = FieldInfo(alias="ArtworkCopyrightNotice", default=None)

    artwork_copyright_owner_id: Optional[str] = FieldInfo(alias="ArtworkCopyrightOwnerID", default=None)

    artwork_copyright_owner_name: Optional[str] = FieldInfo(alias="ArtworkCopyrightOwnerName", default=None)

    artwork_creator: Optional[List[str]] = FieldInfo(alias="ArtworkCreator", default=None)

    artwork_creator_id: Optional[List[str]] = FieldInfo(alias="ArtworkCreatorID", default=None)

    artwork_date_created: Optional[datetime] = FieldInfo(alias="ArtworkDateCreated", default=None)

    artwork_licensor_id: Optional[str] = FieldInfo(alias="ArtworkLicensorID", default=None)

    artwork_licensor_name: Optional[str] = FieldInfo(alias="ArtworkLicensorName", default=None)

    artwork_physical_description: Optional[str] = FieldInfo(alias="ArtworkPhysicalDescription", default=None)

    artwork_source: Optional[str] = FieldInfo(alias="ArtworkSource", default=None)

    artwork_source_inventory_no: Optional[str] = FieldInfo(alias="ArtworkSourceInventoryNo", default=None)

    artwork_source_inv_url: Optional[str] = FieldInfo(alias="ArtworkSourceInvURL", default=None)

    artwork_style_period: Optional[List[str]] = FieldInfo(alias="ArtworkStylePeriod", default=None)

    artwork_title: Optional[str] = FieldInfo(alias="ArtworkTitle", default=None)

    authors_position: Optional[str] = FieldInfo(alias="AuthorsPosition", default=None)

    byline: Optional[str] = FieldInfo(alias="Byline", default=None)

    byline_title: Optional[str] = FieldInfo(alias="BylineTitle", default=None)

    caption: Optional[str] = FieldInfo(alias="Caption", default=None)

    caption_abstract: Optional[str] = FieldInfo(alias="CaptionAbstract", default=None)

    caption_writer: Optional[str] = FieldInfo(alias="CaptionWriter", default=None)

    city: Optional[str] = FieldInfo(alias="City", default=None)

    color_space: Optional[str] = FieldInfo(alias="ColorSpace", default=None)

    components_configuration: Optional[str] = FieldInfo(alias="ComponentsConfiguration", default=None)

    copyright: Optional[str] = FieldInfo(alias="Copyright", default=None)

    copyright_notice: Optional[str] = FieldInfo(alias="CopyrightNotice", default=None)

    copyright_owner_id: Optional[List[str]] = FieldInfo(alias="CopyrightOwnerID", default=None)

    copyright_owner_name: Optional[List[str]] = FieldInfo(alias="CopyrightOwnerName", default=None)

    country: Optional[str] = FieldInfo(alias="Country", default=None)

    country_code: Optional[str] = FieldInfo(alias="CountryCode", default=None)

    country_primary_location_code: Optional[str] = FieldInfo(alias="CountryPrimaryLocationCode", default=None)

    country_primary_location_name: Optional[str] = FieldInfo(alias="CountryPrimaryLocationName", default=None)

    creator: Optional[str] = FieldInfo(alias="Creator", default=None)

    creator_address: Optional[str] = FieldInfo(alias="CreatorAddress", default=None)

    creator_city: Optional[str] = FieldInfo(alias="CreatorCity", default=None)

    creator_country: Optional[str] = FieldInfo(alias="CreatorCountry", default=None)

    creator_postal_code: Optional[str] = FieldInfo(alias="CreatorPostalCode", default=None)

    creator_region: Optional[str] = FieldInfo(alias="CreatorRegion", default=None)

    creator_work_email: Optional[str] = FieldInfo(alias="CreatorWorkEmail", default=None)

    creator_work_telephone: Optional[str] = FieldInfo(alias="CreatorWorkTelephone", default=None)

    creator_work_url: Optional[str] = FieldInfo(alias="CreatorWorkURL", default=None)

    credit: Optional[str] = FieldInfo(alias="Credit", default=None)

    date_created: Optional[datetime] = FieldInfo(alias="DateCreated", default=None)

    date_time_created: Optional[datetime] = FieldInfo(alias="DateTimeCreated", default=None)

    date_time_original: Optional[datetime] = FieldInfo(alias="DateTimeOriginal", default=None)

    description: Optional[str] = FieldInfo(alias="Description", default=None)

    digital_image_guid: Optional[str] = FieldInfo(alias="DigitalImageGUID", default=None)

    digital_source_type: Optional[str] = FieldInfo(alias="DigitalSourceType", default=None)

    embedded_encoded_rights_expr: Optional[str] = FieldInfo(alias="EmbeddedEncodedRightsExpr", default=None)

    embedded_encoded_rights_expr_lang_id: Optional[str] = FieldInfo(
        alias="EmbeddedEncodedRightsExprLangID", default=None
    )

    embedded_encoded_rights_expr_type: Optional[str] = FieldInfo(alias="EmbeddedEncodedRightsExprType", default=None)

    event: Optional[str] = FieldInfo(alias="Event", default=None)

    exif_version: Optional[str] = FieldInfo(alias="ExifVersion", default=None)

    flashpix_version: Optional[str] = FieldInfo(alias="FlashpixVersion", default=None)

    genre_cv_id: Optional[str] = FieldInfo(alias="GenreCvId", default=None)

    genre_cv_term_id: Optional[str] = FieldInfo(alias="GenreCvTermId", default=None)

    genre_cv_term_name: Optional[str] = FieldInfo(alias="GenreCvTermName", default=None)

    genre_cv_term_refined_about: Optional[str] = FieldInfo(alias="GenreCvTermRefinedAbout", default=None)

    headline: Optional[str] = FieldInfo(alias="Headline", default=None)

    image_creator_id: Optional[str] = FieldInfo(alias="ImageCreatorID", default=None)

    image_creator_image_id: Optional[str] = FieldInfo(alias="ImageCreatorImageID", default=None)

    image_creator_name: Optional[str] = FieldInfo(alias="ImageCreatorName", default=None)

    image_description: Optional[str] = FieldInfo(alias="ImageDescription", default=None)

    image_region_boundary_h: Optional[List[float]] = FieldInfo(alias="ImageRegionBoundaryH", default=None)

    image_region_boundary_rx: Optional[List[float]] = FieldInfo(alias="ImageRegionBoundaryRx", default=None)

    image_region_boundary_shape: Optional[List[str]] = FieldInfo(alias="ImageRegionBoundaryShape", default=None)

    image_region_boundary_unit: Optional[List[str]] = FieldInfo(alias="ImageRegionBoundaryUnit", default=None)

    image_region_boundary_vertices_x: Optional[List[float]] = FieldInfo(
        alias="ImageRegionBoundaryVerticesX", default=None
    )

    image_region_boundary_vertices_y: Optional[List[float]] = FieldInfo(
        alias="ImageRegionBoundaryVerticesY", default=None
    )

    image_region_boundary_w: Optional[List[float]] = FieldInfo(alias="ImageRegionBoundaryW", default=None)

    image_region_boundary_x: Optional[List[float]] = FieldInfo(alias="ImageRegionBoundaryX", default=None)

    image_region_boundary_y: Optional[List[float]] = FieldInfo(alias="ImageRegionBoundaryY", default=None)

    image_region_ctype_identifier: Optional[List[str]] = FieldInfo(alias="ImageRegionCtypeIdentifier", default=None)

    image_region_ctype_name: Optional[List[str]] = FieldInfo(alias="ImageRegionCtypeName", default=None)

    image_region_id: Optional[List[str]] = FieldInfo(alias="ImageRegionID", default=None)

    image_region_name: Optional[List[str]] = FieldInfo(alias="ImageRegionName", default=None)

    image_region_organisation_in_image_name: Optional[List[str]] = FieldInfo(
        alias="ImageRegionOrganisationInImageName", default=None
    )

    image_region_person_in_image: Optional[List[str]] = FieldInfo(alias="ImageRegionPersonInImage", default=None)

    image_region_role_identifier: Optional[List[str]] = FieldInfo(alias="ImageRegionRoleIdentifier", default=None)

    image_region_role_name: Optional[List[str]] = FieldInfo(alias="ImageRegionRoleName", default=None)

    image_supplier_id: Optional[str] = FieldInfo(alias="ImageSupplierID", default=None)

    image_supplier_image_id: Optional[str] = FieldInfo(alias="ImageSupplierImageID", default=None)

    image_supplier_name: Optional[str] = FieldInfo(alias="ImageSupplierName", default=None)

    instructions: Optional[str] = FieldInfo(alias="Instructions", default=None)

    intellectual_genre: Optional[str] = FieldInfo(alias="IntellectualGenre", default=None)

    keywords: Optional[List[str]] = FieldInfo(alias="Keywords", default=None)

    licensor_city: Optional[List[str]] = FieldInfo(alias="LicensorCity", default=None)

    licensor_country: Optional[List[str]] = FieldInfo(alias="LicensorCountry", default=None)

    licensor_email: Optional[List[str]] = FieldInfo(alias="LicensorEmail", default=None)

    licensor_extended_address: Optional[List[str]] = FieldInfo(alias="LicensorExtendedAddress", default=None)

    licensor_id: Optional[List[str]] = FieldInfo(alias="LicensorID", default=None)

    licensor_name: Optional[List[str]] = FieldInfo(alias="LicensorName", default=None)

    licensor_postal_code: Optional[List[str]] = FieldInfo(alias="LicensorPostalCode", default=None)

    licensor_region: Optional[List[str]] = FieldInfo(alias="LicensorRegion", default=None)

    licensor_street_address: Optional[List[str]] = FieldInfo(alias="LicensorStreetAddress", default=None)

    licensor_telephone1: Optional[List[str]] = FieldInfo(alias="LicensorTelephone1", default=None)

    licensor_telephone2: Optional[List[str]] = FieldInfo(alias="LicensorTelephone2", default=None)

    licensor_url: Optional[List[str]] = FieldInfo(alias="LicensorURL", default=None)

    linked_encoded_rights_expr: Optional[str] = FieldInfo(alias="LinkedEncodedRightsExpr", default=None)

    linked_encoded_rights_expr_lang_id: Optional[str] = FieldInfo(alias="LinkedEncodedRightsExprLangID", default=None)

    linked_encoded_rights_expr_type: Optional[str] = FieldInfo(alias="LinkedEncodedRightsExprType", default=None)

    location: Optional[str] = FieldInfo(alias="Location", default=None)

    location_created_city: Optional[str] = FieldInfo(alias="LocationCreatedCity", default=None)

    location_created_country_code: Optional[str] = FieldInfo(alias="LocationCreatedCountryCode", default=None)

    location_created_country_name: Optional[str] = FieldInfo(alias="LocationCreatedCountryName", default=None)

    location_created_gps_altitude: Optional[str] = FieldInfo(alias="LocationCreatedGPSAltitude", default=None)

    location_created_gps_latitude: Optional[str] = FieldInfo(alias="LocationCreatedGPSLatitude", default=None)

    location_created_gps_longitude: Optional[str] = FieldInfo(alias="LocationCreatedGPSLongitude", default=None)

    location_created_location_id: Optional[str] = FieldInfo(alias="LocationCreatedLocationId", default=None)

    location_created_location_name: Optional[str] = FieldInfo(alias="LocationCreatedLocationName", default=None)

    location_created_province_state: Optional[str] = FieldInfo(alias="LocationCreatedProvinceState", default=None)

    location_created_sublocation: Optional[str] = FieldInfo(alias="LocationCreatedSublocation", default=None)

    location_created_world_region: Optional[str] = FieldInfo(alias="LocationCreatedWorldRegion", default=None)

    location_shown_city: Optional[List[str]] = FieldInfo(alias="LocationShownCity", default=None)

    location_shown_country_code: Optional[List[str]] = FieldInfo(alias="LocationShownCountryCode", default=None)

    location_shown_country_name: Optional[List[str]] = FieldInfo(alias="LocationShownCountryName", default=None)

    location_shown_gps_altitude: Optional[List[str]] = FieldInfo(alias="LocationShownGPSAltitude", default=None)

    location_shown_gps_latitude: Optional[List[str]] = FieldInfo(alias="LocationShownGPSLatitude", default=None)

    location_shown_gps_longitude: Optional[List[str]] = FieldInfo(alias="LocationShownGPSLongitude", default=None)

    location_shown_location_id: Optional[List[str]] = FieldInfo(alias="LocationShownLocationId", default=None)

    location_shown_location_name: Optional[List[str]] = FieldInfo(alias="LocationShownLocationName", default=None)

    location_shown_province_state: Optional[List[str]] = FieldInfo(alias="LocationShownProvinceState", default=None)

    location_shown_sublocation: Optional[List[str]] = FieldInfo(alias="LocationShownSublocation", default=None)

    location_shown_world_region: Optional[List[str]] = FieldInfo(alias="LocationShownWorldRegion", default=None)

    max_avail_height: Optional[float] = FieldInfo(alias="MaxAvailHeight", default=None)

    max_avail_width: Optional[float] = FieldInfo(alias="MaxAvailWidth", default=None)

    api_model_age: Optional[List[float]] = FieldInfo(alias="ModelAge", default=None)

    api_model_release_id: Optional[List[str]] = FieldInfo(alias="ModelReleaseID", default=None)

    object_attribute_reference: Optional[str] = FieldInfo(alias="ObjectAttributeReference", default=None)

    object_name: Optional[str] = FieldInfo(alias="ObjectName", default=None)

    offset_time_original: Optional[str] = FieldInfo(alias="OffsetTimeOriginal", default=None)

    organisation_in_image_code: Optional[List[str]] = FieldInfo(alias="OrganisationInImageCode", default=None)

    organisation_in_image_name: Optional[List[str]] = FieldInfo(alias="OrganisationInImageName", default=None)

    orientation: Optional[str] = FieldInfo(alias="Orientation", default=None)

    original_transmission_reference: Optional[str] = FieldInfo(alias="OriginalTransmissionReference", default=None)

    person_in_image: Optional[List[str]] = FieldInfo(alias="PersonInImage", default=None)

    person_in_image_cv_term_cv_id: Optional[List[str]] = FieldInfo(alias="PersonInImageCvTermCvId", default=None)

    person_in_image_cv_term_id: Optional[List[str]] = FieldInfo(alias="PersonInImageCvTermId", default=None)

    person_in_image_cv_term_name: Optional[List[str]] = FieldInfo(alias="PersonInImageCvTermName", default=None)

    person_in_image_cv_term_refined_about: Optional[List[str]] = FieldInfo(
        alias="PersonInImageCvTermRefinedAbout", default=None
    )

    person_in_image_description: Optional[List[str]] = FieldInfo(alias="PersonInImageDescription", default=None)

    person_in_image_id: Optional[List[str]] = FieldInfo(alias="PersonInImageId", default=None)

    person_in_image_name: Optional[List[str]] = FieldInfo(alias="PersonInImageName", default=None)

    product_in_image_description: Optional[List[str]] = FieldInfo(alias="ProductInImageDescription", default=None)

    product_in_image_gtin: Optional[List[float]] = FieldInfo(alias="ProductInImageGTIN", default=None)

    product_in_image_name: Optional[List[str]] = FieldInfo(alias="ProductInImageName", default=None)

    property_release_id: Optional[List[str]] = FieldInfo(alias="PropertyReleaseID", default=None)

    province_state: Optional[str] = FieldInfo(alias="ProvinceState", default=None)

    rating: Optional[int] = FieldInfo(alias="Rating", default=None)

    registry_entry_role: Optional[List[str]] = FieldInfo(alias="RegistryEntryRole", default=None)

    registry_item_id: Optional[List[str]] = FieldInfo(alias="RegistryItemID", default=None)

    registry_organisation_id: Optional[List[str]] = FieldInfo(alias="RegistryOrganisationID", default=None)

    resolution_unit: Optional[str] = FieldInfo(alias="ResolutionUnit", default=None)

    rights: Optional[str] = FieldInfo(alias="Rights", default=None)

    scene: Optional[List[str]] = FieldInfo(alias="Scene", default=None)

    source: Optional[str] = FieldInfo(alias="Source", default=None)

    special_instructions: Optional[str] = FieldInfo(alias="SpecialInstructions", default=None)

    state: Optional[str] = FieldInfo(alias="State", default=None)

    subject: Optional[List[str]] = FieldInfo(alias="Subject", default=None)

    subject_code: Optional[List[str]] = FieldInfo(alias="SubjectCode", default=None)

    subject_reference: Optional[List[str]] = FieldInfo(alias="SubjectReference", default=None)

    sublocation: Optional[str] = FieldInfo(alias="Sublocation", default=None)

    time_created: Optional[str] = FieldInfo(alias="TimeCreated", default=None)

    title: Optional[str] = FieldInfo(alias="Title", default=None)

    transmission_reference: Optional[str] = FieldInfo(alias="TransmissionReference", default=None)

    usage_terms: Optional[str] = FieldInfo(alias="UsageTerms", default=None)

    web_statement: Optional[str] = FieldInfo(alias="WebStatement", default=None)

    writer: Optional[str] = FieldInfo(alias="Writer", default=None)

    writer_editor: Optional[str] = FieldInfo(alias="WriterEditor", default=None)

    x_resolution: Optional[float] = FieldInfo(alias="XResolution", default=None)

    y_resolution: Optional[float] = FieldInfo(alias="YResolution", default=None)


class ExtensionStatus(BaseModel):
    aws_auto_tagging: Optional[Literal["success", "pending", "failed"]] = FieldInfo(
        alias="aws-auto-tagging", default=None
    )

    google_auto_tagging: Optional[Literal["success", "pending", "failed"]] = FieldInfo(
        alias="google-auto-tagging", default=None
    )

    remove_bg: Optional[Literal["success", "pending", "failed"]] = FieldInfo(alias="remove-bg", default=None)


class MetadataExif(BaseModel):
    exif: Optional[ExifDetails] = None
    """Object containing Exif details."""

    gps: Optional[Gps] = None
    """Object containing GPS information."""

    image: Optional[ExifImage] = None
    """Object containing EXIF image information."""

    interoperability: Optional[Interoperability] = None
    """JSON object."""

    makernote: Optional[Dict[str, object]] = None

    thumbnail: Optional[Thumbnail] = None
    """Object containing Thumbnail information."""


class Metadata(BaseModel):
    audio_codec: Optional[str] = FieldInfo(alias="audioCodec", default=None)
    """The audio codec used in the video (only for video)."""

    bit_rate: Optional[int] = FieldInfo(alias="bitRate", default=None)
    """The bit rate of the video in kbps (only for video)."""

    density: Optional[int] = None
    """The density of the image in DPI."""

    duration: Optional[int] = None
    """The duration of the video in seconds (only for video)."""

    exif: Optional[MetadataExif] = None

    format: Optional[str] = None
    """The format of the file (e.g., 'jpg', 'mp4')."""

    has_color_profile: Optional[bool] = FieldInfo(alias="hasColorProfile", default=None)
    """Indicates if the image has a color profile."""

    has_transparency: Optional[bool] = FieldInfo(alias="hasTransparency", default=None)
    """Indicates if the image contains transparent areas."""

    height: Optional[int] = None
    """The height of the image or video in pixels."""

    p_hash: Optional[str] = FieldInfo(alias="pHash", default=None)
    """Perceptual hash of the image."""

    quality: Optional[int] = None
    """The quality indicator of the image."""

    size: Optional[int] = None
    """The file size in bytes."""

    video_codec: Optional[str] = FieldInfo(alias="videoCodec", default=None)
    """The video codec used in the video (only for video)."""

    width: Optional[int] = None
    """The width of the image or video in pixels."""


class VersionInfo(BaseModel):
    id: Optional[str] = None
    """Unique identifier of the file version."""

    name: Optional[str] = None
    """Name of the file version."""


class FileUploadV1Response(BaseModel):
    ai_tags: Optional[List[AITag]] = FieldInfo(alias="AITags", default=None)
    """An array of tags assigned to the uploaded file by auto tagging."""

    audio_codec: Optional[str] = FieldInfo(alias="audioCodec", default=None)
    """The audio codec used in the video (only for video)."""

    bit_rate: Optional[int] = FieldInfo(alias="bitRate", default=None)
    """The bit rate of the video in kbps (only for video)."""

    custom_coordinates: Optional[str] = FieldInfo(alias="customCoordinates", default=None)
    """
    Value of custom coordinates associated with the image in the format
    `x,y,width,height`. If `customCoordinates` are not defined, then it is `null`.
    Send `customCoordinates` in `responseFields` in API request to get the value of
    this field.
    """

    custom_metadata: Optional[object] = FieldInfo(alias="customMetadata", default=None)
    """A key-value data associated with the asset.

    Use `responseField` in API request to get `customMetadata` in the upload API
    response. Before setting any custom metadata on an asset, you have to create the
    field using custom metadata fields API. Send `customMetadata` in
    `responseFields` in API request to get the value of this field.
    """

    duration: Optional[int] = None
    """The duration of the video in seconds (only for video)."""

    embedded_metadata: Optional[EmbeddedMetadata] = FieldInfo(alias="embeddedMetadata", default=None)
    """Consolidated embedded metadata associated with the file.

    It includes exif, iptc, and xmp data. Send `embeddedMetadata` in
    `responseFields` in API request to get embeddedMetadata in the upload API
    response.
    """

    extension_status: Optional[ExtensionStatus] = FieldInfo(alias="extensionStatus", default=None)
    """
    Extension names with their processing status at the time of completion of the
    request. It could have one of the following status values:

    `success`: The extension has been successfully applied. `failed`: The extension
    has failed and will not be retried. `pending`: The extension will finish
    processing in some time. On completion, the final status (success / failed) will
    be sent to the `webhookUrl` provided.

    If no extension was requested, then this parameter is not returned.
    """

    file_id: Optional[str] = FieldInfo(alias="fileId", default=None)
    """Unique fileId.

    Store this fileld in your database, as this will be used to perform update
    action on this file.
    """

    file_path: Optional[str] = FieldInfo(alias="filePath", default=None)
    """The relative path of the file in the media library e.g.

    `/marketing-assets/new-banner.jpg`.
    """

    file_type: Optional[str] = FieldInfo(alias="fileType", default=None)
    """Type of the uploaded file. Possible values are `image`, `non-image`."""

    height: Optional[float] = None
    """Height of the image in pixels (Only for images)"""

    is_private_file: Optional[bool] = FieldInfo(alias="isPrivateFile", default=None)
    """Is the file marked as private.

    It can be either `true` or `false`. Send `isPrivateFile` in `responseFields` in
    API request to get the value of this field.
    """

    is_published: Optional[bool] = FieldInfo(alias="isPublished", default=None)
    """Is the file published or in draft state.

    It can be either `true` or `false`. Send `isPublished` in `responseFields` in
    API request to get the value of this field.
    """

    metadata: Optional[Metadata] = None
    """Legacy metadata.

    Send `metadata` in `responseFields` in API request to get metadata in the upload
    API response.
    """

    name: Optional[str] = None
    """Name of the asset."""

    size: Optional[float] = None
    """Size of the image file in Bytes."""

    tags: Optional[List[str]] = None
    """The array of tags associated with the asset.

    If no tags are set, it will be `null`. Send `tags` in `responseFields` in API
    request to get the value of this field.
    """

    thumbnail_url: Optional[str] = FieldInfo(alias="thumbnailUrl", default=None)
    """In the case of an image, a small thumbnail URL."""

    url: Optional[str] = None
    """A publicly accessible URL of the file."""

    version_info: Optional[VersionInfo] = FieldInfo(alias="versionInfo", default=None)
    """An object containing the file or file version's `id` (versionId) and `name`."""

    video_codec: Optional[str] = FieldInfo(alias="videoCodec", default=None)
    """The video codec used in the video (only for video)."""

    width: Optional[float] = None
    """Width of the image in pixels (Only for Images)"""
