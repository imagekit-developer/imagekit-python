# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from . import shared
from .. import _compat
from .file import File as File
from .folder import Folder as Folder
from .shared import (
    Overlay as Overlay,
    Extensions as Extensions,
    SrcOptions as SrcOptions,
    BaseOverlay as BaseOverlay,
    TextOverlay as TextOverlay,
    ImageOverlay as ImageOverlay,
    VideoOverlay as VideoOverlay,
    OverlayTiming as OverlayTiming,
    Transformation as Transformation,
    OverlayPosition as OverlayPosition,
    SubtitleOverlay as SubtitleOverlay,
    SolidColorOverlay as SolidColorOverlay,
    StreamingResolution as StreamingResolution,
    TransformationPosition as TransformationPosition,
    GetImageAttributesOptions as GetImageAttributesOptions,
    ResponsiveImageAttributes as ResponsiveImageAttributes,
    TextOverlayTransformation as TextOverlayTransformation,
    SubtitleOverlayTransformation as SubtitleOverlayTransformation,
    SolidColorOverlayTransformation as SolidColorOverlayTransformation,
)
from .metadata import Metadata as Metadata
from .file_copy_params import FileCopyParams as FileCopyParams
from .file_move_params import FileMoveParams as FileMoveParams
from .asset_list_params import AssetListParams as AssetListParams
from .base_webhook_event import BaseWebhookEvent as BaseWebhookEvent
from .file_copy_response import FileCopyResponse as FileCopyResponse
from .file_move_response import FileMoveResponse as FileMoveResponse
from .file_rename_params import FileRenameParams as FileRenameParams
from .file_update_params import FileUpdateParams as FileUpdateParams
from .file_upload_params import FileUploadParams as FileUploadParams
from .folder_copy_params import FolderCopyParams as FolderCopyParams
from .folder_move_params import FolderMoveParams as FolderMoveParams
from .asset_list_response import AssetListResponse as AssetListResponse
from .dummy_create_params import DummyCreateParams as DummyCreateParams
from .file_rename_response import FileRenameResponse as FileRenameResponse
from .file_update_response import FileUpdateResponse as FileUpdateResponse
from .file_upload_response import FileUploadResponse as FileUploadResponse
from .folder_copy_response import FolderCopyResponse as FolderCopyResponse
from .folder_create_params import FolderCreateParams as FolderCreateParams
from .folder_delete_params import FolderDeleteParams as FolderDeleteParams
from .folder_move_response import FolderMoveResponse as FolderMoveResponse
from .folder_rename_params import FolderRenameParams as FolderRenameParams
from .unwrap_webhook_event import UnwrapWebhookEvent as UnwrapWebhookEvent
from .custom_metadata_field import CustomMetadataField as CustomMetadataField
from .folder_create_response import FolderCreateResponse as FolderCreateResponse
from .folder_delete_response import FolderDeleteResponse as FolderDeleteResponse
from .folder_rename_response import FolderRenameResponse as FolderRenameResponse
from .update_file_request_param import UpdateFileRequestParam as UpdateFileRequestParam
from .unsafe_unwrap_webhook_event import UnsafeUnwrapWebhookEvent as UnsafeUnwrapWebhookEvent
from .upload_pre_transform_error_event import UploadPreTransformErrorEvent as UploadPreTransformErrorEvent
from .video_transformation_error_event import VideoTransformationErrorEvent as VideoTransformationErrorEvent
from .video_transformation_ready_event import VideoTransformationReadyEvent as VideoTransformationReadyEvent
from .custom_metadata_field_list_params import CustomMetadataFieldListParams as CustomMetadataFieldListParams
from .upload_post_transform_error_event import UploadPostTransformErrorEvent as UploadPostTransformErrorEvent
from .upload_pre_transform_success_event import UploadPreTransformSuccessEvent as UploadPreTransformSuccessEvent
from .custom_metadata_field_create_params import CustomMetadataFieldCreateParams as CustomMetadataFieldCreateParams
from .custom_metadata_field_list_response import CustomMetadataFieldListResponse as CustomMetadataFieldListResponse
from .custom_metadata_field_update_params import CustomMetadataFieldUpdateParams as CustomMetadataFieldUpdateParams
from .upload_post_transform_success_event import UploadPostTransformSuccessEvent as UploadPostTransformSuccessEvent
from .video_transformation_accepted_event import VideoTransformationAcceptedEvent as VideoTransformationAcceptedEvent
from .custom_metadata_field_delete_response import (
    CustomMetadataFieldDeleteResponse as CustomMetadataFieldDeleteResponse,
)

# Rebuild cyclical models only after all modules are imported.
# This ensures that, when building the deferred (due to cyclical references) model schema,
# Pydantic can resolve the necessary references.
# See: https://github.com/pydantic/pydantic/issues/11250 for more context.
if _compat.PYDANTIC_V1:
    shared.src_options.SrcOptions.update_forward_refs()  # type: ignore
    shared.transformation.Transformation.update_forward_refs()  # type: ignore
else:
    shared.src_options.SrcOptions.model_rebuild(_parent_namespace_depth=0)
    shared.transformation.Transformation.model_rebuild(_parent_namespace_depth=0)
