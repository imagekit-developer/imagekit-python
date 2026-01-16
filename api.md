# Shared Types

```python
from imagekitio.types import (
    BaseOverlay,
    ExtensionConfig,
    Extensions,
    GetImageAttributesOptions,
    ImageOverlay,
    Overlay,
    OverlayPosition,
    OverlayTiming,
    ResponsiveImageAttributes,
    SavedExtension,
    SolidColorOverlay,
    SolidColorOverlayTransformation,
    SrcOptions,
    StreamingResolution,
    SubtitleOverlay,
    SubtitleOverlayTransformation,
    TextOverlay,
    TextOverlayTransformation,
    Transformation,
    TransformationPosition,
    VideoOverlay,
)
```

# CustomMetadataFields

Types:

```python
from imagekitio.types import (
    CustomMetadataField,
    CustomMetadataFieldListResponse,
    CustomMetadataFieldDeleteResponse,
)
```

Methods:

- <code title="post /v1/customMetadataFields">client.custom_metadata_fields.<a href="./src/imagekitio/resources/custom_metadata_fields.py">create</a>(\*\*<a href="src/imagekitio/types/custom_metadata_field_create_params.py">params</a>) -> <a href="./src/imagekitio/types/custom_metadata_field.py">CustomMetadataField</a></code>
- <code title="patch /v1/customMetadataFields/{id}">client.custom_metadata_fields.<a href="./src/imagekitio/resources/custom_metadata_fields.py">update</a>(id, \*\*<a href="src/imagekitio/types/custom_metadata_field_update_params.py">params</a>) -> <a href="./src/imagekitio/types/custom_metadata_field.py">CustomMetadataField</a></code>
- <code title="get /v1/customMetadataFields">client.custom_metadata_fields.<a href="./src/imagekitio/resources/custom_metadata_fields.py">list</a>(\*\*<a href="src/imagekitio/types/custom_metadata_field_list_params.py">params</a>) -> <a href="./src/imagekitio/types/custom_metadata_field_list_response.py">CustomMetadataFieldListResponse</a></code>
- <code title="delete /v1/customMetadataFields/{id}">client.custom_metadata_fields.<a href="./src/imagekitio/resources/custom_metadata_fields.py">delete</a>(id) -> <a href="./src/imagekitio/types/custom_metadata_field_delete_response.py">CustomMetadataFieldDeleteResponse</a></code>

# Files

Types:

```python
from imagekitio.types import (
    File,
    Folder,
    Metadata,
    UpdateFileRequest,
    FileUpdateResponse,
    FileCopyResponse,
    FileMoveResponse,
    FileRenameResponse,
    FileUploadResponse,
)
```

Methods:

- <code title="patch /v1/files/{fileId}/details">client.files.<a href="./src/imagekitio/resources/files/files.py">update</a>(file_id, \*\*<a href="src/imagekitio/types/file_update_params.py">params</a>) -> <a href="./src/imagekitio/types/file_update_response.py">FileUpdateResponse</a></code>
- <code title="delete /v1/files/{fileId}">client.files.<a href="./src/imagekitio/resources/files/files.py">delete</a>(file_id) -> None</code>
- <code title="post /v1/files/copy">client.files.<a href="./src/imagekitio/resources/files/files.py">copy</a>(\*\*<a href="src/imagekitio/types/file_copy_params.py">params</a>) -> <a href="./src/imagekitio/types/file_copy_response.py">FileCopyResponse</a></code>
- <code title="get /v1/files/{fileId}/details">client.files.<a href="./src/imagekitio/resources/files/files.py">get</a>(file_id) -> <a href="./src/imagekitio/types/file.py">File</a></code>
- <code title="post /v1/files/move">client.files.<a href="./src/imagekitio/resources/files/files.py">move</a>(\*\*<a href="src/imagekitio/types/file_move_params.py">params</a>) -> <a href="./src/imagekitio/types/file_move_response.py">FileMoveResponse</a></code>
- <code title="put /v1/files/rename">client.files.<a href="./src/imagekitio/resources/files/files.py">rename</a>(\*\*<a href="src/imagekitio/types/file_rename_params.py">params</a>) -> <a href="./src/imagekitio/types/file_rename_response.py">FileRenameResponse</a></code>
- <code title="post /api/v1/files/upload">client.files.<a href="./src/imagekitio/resources/files/files.py">upload</a>(\*\*<a href="src/imagekitio/types/file_upload_params.py">params</a>) -> <a href="./src/imagekitio/types/file_upload_response.py">FileUploadResponse</a></code>

## Bulk

Types:

```python
from imagekitio.types.files import (
    BulkDeleteResponse,
    BulkAddTagsResponse,
    BulkRemoveAITagsResponse,
    BulkRemoveTagsResponse,
)
```

Methods:

- <code title="post /v1/files/batch/deleteByFileIds">client.files.bulk.<a href="./src/imagekitio/resources/files/bulk.py">delete</a>(\*\*<a href="src/imagekitio/types/files/bulk_delete_params.py">params</a>) -> <a href="./src/imagekitio/types/files/bulk_delete_response.py">BulkDeleteResponse</a></code>
- <code title="post /v1/files/addTags">client.files.bulk.<a href="./src/imagekitio/resources/files/bulk.py">add_tags</a>(\*\*<a href="src/imagekitio/types/files/bulk_add_tags_params.py">params</a>) -> <a href="./src/imagekitio/types/files/bulk_add_tags_response.py">BulkAddTagsResponse</a></code>
- <code title="post /v1/files/removeAITags">client.files.bulk.<a href="./src/imagekitio/resources/files/bulk.py">remove_ai_tags</a>(\*\*<a href="src/imagekitio/types/files/bulk_remove_ai_tags_params.py">params</a>) -> <a href="./src/imagekitio/types/files/bulk_remove_ai_tags_response.py">BulkRemoveAITagsResponse</a></code>
- <code title="post /v1/files/removeTags">client.files.bulk.<a href="./src/imagekitio/resources/files/bulk.py">remove_tags</a>(\*\*<a href="src/imagekitio/types/files/bulk_remove_tags_params.py">params</a>) -> <a href="./src/imagekitio/types/files/bulk_remove_tags_response.py">BulkRemoveTagsResponse</a></code>

## Versions

Types:

```python
from imagekitio.types.files import VersionListResponse, VersionDeleteResponse
```

Methods:

- <code title="get /v1/files/{fileId}/versions">client.files.versions.<a href="./src/imagekitio/resources/files/versions.py">list</a>(file_id) -> <a href="./src/imagekitio/types/files/version_list_response.py">VersionListResponse</a></code>
- <code title="delete /v1/files/{fileId}/versions/{versionId}">client.files.versions.<a href="./src/imagekitio/resources/files/versions.py">delete</a>(version_id, \*, file_id) -> <a href="./src/imagekitio/types/files/version_delete_response.py">VersionDeleteResponse</a></code>
- <code title="get /v1/files/{fileId}/versions/{versionId}">client.files.versions.<a href="./src/imagekitio/resources/files/versions.py">get</a>(version_id, \*, file_id) -> <a href="./src/imagekitio/types/file.py">File</a></code>
- <code title="put /v1/files/{fileId}/versions/{versionId}/restore">client.files.versions.<a href="./src/imagekitio/resources/files/versions.py">restore</a>(version_id, \*, file_id) -> <a href="./src/imagekitio/types/file.py">File</a></code>

## Metadata

Methods:

- <code title="get /v1/files/{fileId}/metadata">client.files.metadata.<a href="./src/imagekitio/resources/files/metadata.py">get</a>(file_id) -> <a href="./src/imagekitio/types/metadata.py">Metadata</a></code>
- <code title="get /v1/metadata">client.files.metadata.<a href="./src/imagekitio/resources/files/metadata.py">get_from_url</a>(\*\*<a href="src/imagekitio/types/files/metadata_get_from_url_params.py">params</a>) -> <a href="./src/imagekitio/types/metadata.py">Metadata</a></code>

# SavedExtensions

Types:

```python
from imagekitio.types import SavedExtensionListResponse
```

Methods:

- <code title="post /v1/saved-extensions">client.saved_extensions.<a href="./src/imagekitio/resources/saved_extensions.py">create</a>(\*\*<a href="src/imagekitio/types/saved_extension_create_params.py">params</a>) -> <a href="./src/imagekitio/types/shared/saved_extension.py">SavedExtension</a></code>
- <code title="patch /v1/saved-extensions/{id}">client.saved_extensions.<a href="./src/imagekitio/resources/saved_extensions.py">update</a>(id, \*\*<a href="src/imagekitio/types/saved_extension_update_params.py">params</a>) -> <a href="./src/imagekitio/types/shared/saved_extension.py">SavedExtension</a></code>
- <code title="get /v1/saved-extensions">client.saved_extensions.<a href="./src/imagekitio/resources/saved_extensions.py">list</a>() -> <a href="./src/imagekitio/types/saved_extension_list_response.py">SavedExtensionListResponse</a></code>
- <code title="delete /v1/saved-extensions/{id}">client.saved_extensions.<a href="./src/imagekitio/resources/saved_extensions.py">delete</a>(id) -> None</code>
- <code title="get /v1/saved-extensions/{id}">client.saved_extensions.<a href="./src/imagekitio/resources/saved_extensions.py">get</a>(id) -> <a href="./src/imagekitio/types/shared/saved_extension.py">SavedExtension</a></code>

# Assets

Types:

```python
from imagekitio.types import AssetListResponse
```

Methods:

- <code title="get /v1/files">client.assets.<a href="./src/imagekitio/resources/assets.py">list</a>(\*\*<a href="src/imagekitio/types/asset_list_params.py">params</a>) -> <a href="./src/imagekitio/types/asset_list_response.py">AssetListResponse</a></code>

# Cache

## Invalidation

Types:

```python
from imagekitio.types.cache import InvalidationCreateResponse, InvalidationGetResponse
```

Methods:

- <code title="post /v1/files/purge">client.cache.invalidation.<a href="./src/imagekitio/resources/cache/invalidation.py">create</a>(\*\*<a href="src/imagekitio/types/cache/invalidation_create_params.py">params</a>) -> <a href="./src/imagekitio/types/cache/invalidation_create_response.py">InvalidationCreateResponse</a></code>
- <code title="get /v1/files/purge/{requestId}">client.cache.invalidation.<a href="./src/imagekitio/resources/cache/invalidation.py">get</a>(request_id) -> <a href="./src/imagekitio/types/cache/invalidation_get_response.py">InvalidationGetResponse</a></code>

# Folders

Types:

```python
from imagekitio.types import (
    FolderCreateResponse,
    FolderDeleteResponse,
    FolderCopyResponse,
    FolderMoveResponse,
    FolderRenameResponse,
)
```

Methods:

- <code title="post /v1/folder">client.folders.<a href="./src/imagekitio/resources/folders/folders.py">create</a>(\*\*<a href="src/imagekitio/types/folder_create_params.py">params</a>) -> <a href="./src/imagekitio/types/folder_create_response.py">FolderCreateResponse</a></code>
- <code title="delete /v1/folder">client.folders.<a href="./src/imagekitio/resources/folders/folders.py">delete</a>(\*\*<a href="src/imagekitio/types/folder_delete_params.py">params</a>) -> <a href="./src/imagekitio/types/folder_delete_response.py">FolderDeleteResponse</a></code>
- <code title="post /v1/bulkJobs/copyFolder">client.folders.<a href="./src/imagekitio/resources/folders/folders.py">copy</a>(\*\*<a href="src/imagekitio/types/folder_copy_params.py">params</a>) -> <a href="./src/imagekitio/types/folder_copy_response.py">FolderCopyResponse</a></code>
- <code title="post /v1/bulkJobs/moveFolder">client.folders.<a href="./src/imagekitio/resources/folders/folders.py">move</a>(\*\*<a href="src/imagekitio/types/folder_move_params.py">params</a>) -> <a href="./src/imagekitio/types/folder_move_response.py">FolderMoveResponse</a></code>
- <code title="post /v1/bulkJobs/renameFolder">client.folders.<a href="./src/imagekitio/resources/folders/folders.py">rename</a>(\*\*<a href="src/imagekitio/types/folder_rename_params.py">params</a>) -> <a href="./src/imagekitio/types/folder_rename_response.py">FolderRenameResponse</a></code>

## Job

Types:

```python
from imagekitio.types.folders import JobGetResponse
```

Methods:

- <code title="get /v1/bulkJobs/{jobId}">client.folders.job.<a href="./src/imagekitio/resources/folders/job.py">get</a>(job_id) -> <a href="./src/imagekitio/types/folders/job_get_response.py">JobGetResponse</a></code>

# Accounts

## Usage

Types:

```python
from imagekitio.types.accounts import UsageGetResponse
```

Methods:

- <code title="get /v1/accounts/usage">client.accounts.usage.<a href="./src/imagekitio/resources/accounts/usage.py">get</a>(\*\*<a href="src/imagekitio/types/accounts/usage_get_params.py">params</a>) -> <a href="./src/imagekitio/types/accounts/usage_get_response.py">UsageGetResponse</a></code>

## Origins

Types:

```python
from imagekitio.types.accounts import OriginRequest, OriginResponse, OriginListResponse
```

Methods:

- <code title="post /v1/accounts/origins">client.accounts.origins.<a href="./src/imagekitio/resources/accounts/origins.py">create</a>(\*\*<a href="src/imagekitio/types/accounts/origin_create_params.py">params</a>) -> <a href="./src/imagekitio/types/accounts/origin_response.py">OriginResponse</a></code>
- <code title="put /v1/accounts/origins/{id}">client.accounts.origins.<a href="./src/imagekitio/resources/accounts/origins.py">update</a>(id, \*\*<a href="src/imagekitio/types/accounts/origin_update_params.py">params</a>) -> <a href="./src/imagekitio/types/accounts/origin_response.py">OriginResponse</a></code>
- <code title="get /v1/accounts/origins">client.accounts.origins.<a href="./src/imagekitio/resources/accounts/origins.py">list</a>() -> <a href="./src/imagekitio/types/accounts/origin_list_response.py">OriginListResponse</a></code>
- <code title="delete /v1/accounts/origins/{id}">client.accounts.origins.<a href="./src/imagekitio/resources/accounts/origins.py">delete</a>(id) -> None</code>
- <code title="get /v1/accounts/origins/{id}">client.accounts.origins.<a href="./src/imagekitio/resources/accounts/origins.py">get</a>(id) -> <a href="./src/imagekitio/types/accounts/origin_response.py">OriginResponse</a></code>

## URLEndpoints

Types:

```python
from imagekitio.types.accounts import (
    URLEndpointRequest,
    URLEndpointResponse,
    URLEndpointListResponse,
)
```

Methods:

- <code title="post /v1/accounts/url-endpoints">client.accounts.url_endpoints.<a href="./src/imagekitio/resources/accounts/url_endpoints.py">create</a>(\*\*<a href="src/imagekitio/types/accounts/url_endpoint_create_params.py">params</a>) -> <a href="./src/imagekitio/types/accounts/url_endpoint_response.py">URLEndpointResponse</a></code>
- <code title="put /v1/accounts/url-endpoints/{id}">client.accounts.url_endpoints.<a href="./src/imagekitio/resources/accounts/url_endpoints.py">update</a>(id, \*\*<a href="src/imagekitio/types/accounts/url_endpoint_update_params.py">params</a>) -> <a href="./src/imagekitio/types/accounts/url_endpoint_response.py">URLEndpointResponse</a></code>
- <code title="get /v1/accounts/url-endpoints">client.accounts.url_endpoints.<a href="./src/imagekitio/resources/accounts/url_endpoints.py">list</a>() -> <a href="./src/imagekitio/types/accounts/url_endpoint_list_response.py">URLEndpointListResponse</a></code>
- <code title="delete /v1/accounts/url-endpoints/{id}">client.accounts.url_endpoints.<a href="./src/imagekitio/resources/accounts/url_endpoints.py">delete</a>(id) -> None</code>
- <code title="get /v1/accounts/url-endpoints/{id}">client.accounts.url_endpoints.<a href="./src/imagekitio/resources/accounts/url_endpoints.py">get</a>(id) -> <a href="./src/imagekitio/types/accounts/url_endpoint_response.py">URLEndpointResponse</a></code>

# Beta

## V2

### Files

Types:

```python
from imagekitio.types.beta.v2 import FileUploadResponse
```

Methods:

- <code title="post /api/v2/files/upload">client.beta.v2.files.<a href="./src/imagekitio/resources/beta/v2/files.py">upload</a>(\*\*<a href="src/imagekitio/types/beta/v2/file_upload_params.py">params</a>) -> <a href="./src/imagekitio/types/beta/v2/file_upload_response.py">FileUploadResponse</a></code>

# Webhooks

Types:

```python
from imagekitio.types import (
    BaseWebhookEvent,
    UploadPostTransformErrorEvent,
    UploadPostTransformSuccessEvent,
    UploadPreTransformErrorEvent,
    UploadPreTransformSuccessEvent,
    VideoTransformationAcceptedEvent,
    VideoTransformationErrorEvent,
    VideoTransformationReadyEvent,
    UnsafeUnwrapWebhookEvent,
    UnwrapWebhookEvent,
)
```
