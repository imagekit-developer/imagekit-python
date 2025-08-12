# CustomMetadataFields

Types:

```python
from imagekit.types import (
    CustomMetadataFieldCreateResponse,
    CustomMetadataFieldUpdateResponse,
    CustomMetadataFieldListResponse,
)
```

Methods:

- <code title="post /v1/customMetadataFields">client.custom_metadata_fields.<a href="./src/imagekit/resources/custom_metadata_fields.py">create</a>(\*\*<a href="src/imagekit/types/custom_metadata_field_create_params.py">params</a>) -> <a href="./src/imagekit/types/custom_metadata_field_create_response.py">CustomMetadataFieldCreateResponse</a></code>
- <code title="patch /v1/customMetadataFields/{id}">client.custom_metadata_fields.<a href="./src/imagekit/resources/custom_metadata_fields.py">update</a>(id, \*\*<a href="src/imagekit/types/custom_metadata_field_update_params.py">params</a>) -> <a href="./src/imagekit/types/custom_metadata_field_update_response.py">CustomMetadataFieldUpdateResponse</a></code>
- <code title="get /v1/customMetadataFields">client.custom_metadata_fields.<a href="./src/imagekit/resources/custom_metadata_fields.py">list</a>(\*\*<a href="src/imagekit/types/custom_metadata_field_list_params.py">params</a>) -> <a href="./src/imagekit/types/custom_metadata_field_list_response.py">CustomMetadataFieldListResponse</a></code>
- <code title="delete /v1/customMetadataFields/{id}">client.custom_metadata_fields.<a href="./src/imagekit/resources/custom_metadata_fields.py">delete</a>(id) -> object</code>

# Files

Types:

```python
from imagekit.types import (
    FileListResponse,
    FileAddTagsResponse,
    FileRemoveAITagsResponse,
    FileRemoveTagsResponse,
    FileRenameResponse,
    FileUploadV1Response,
    FileUploadV2Response,
)
```

Methods:

- <code title="get /v1/files">client.files.<a href="./src/imagekit/resources/files/files.py">list</a>(\*\*<a href="src/imagekit/types/file_list_params.py">params</a>) -> <a href="./src/imagekit/types/file_list_response.py">FileListResponse</a></code>
- <code title="delete /v1/files/{fileId}">client.files.<a href="./src/imagekit/resources/files/files.py">delete</a>(file_id) -> None</code>
- <code title="post /v1/files/addTags">client.files.<a href="./src/imagekit/resources/files/files.py">add_tags</a>(\*\*<a href="src/imagekit/types/file_add_tags_params.py">params</a>) -> <a href="./src/imagekit/types/file_add_tags_response.py">FileAddTagsResponse</a></code>
- <code title="post /v1/files/copy">client.files.<a href="./src/imagekit/resources/files/files.py">copy</a>(\*\*<a href="src/imagekit/types/file_copy_params.py">params</a>) -> object</code>
- <code title="post /v1/files/move">client.files.<a href="./src/imagekit/resources/files/files.py">move</a>(\*\*<a href="src/imagekit/types/file_move_params.py">params</a>) -> object</code>
- <code title="post /v1/files/removeAITags">client.files.<a href="./src/imagekit/resources/files/files.py">remove_ai_tags</a>(\*\*<a href="src/imagekit/types/file_remove_ai_tags_params.py">params</a>) -> <a href="./src/imagekit/types/file_remove_ai_tags_response.py">FileRemoveAITagsResponse</a></code>
- <code title="post /v1/files/removeTags">client.files.<a href="./src/imagekit/resources/files/files.py">remove_tags</a>(\*\*<a href="src/imagekit/types/file_remove_tags_params.py">params</a>) -> <a href="./src/imagekit/types/file_remove_tags_response.py">FileRemoveTagsResponse</a></code>
- <code title="put /v1/files/rename">client.files.<a href="./src/imagekit/resources/files/files.py">rename</a>(\*\*<a href="src/imagekit/types/file_rename_params.py">params</a>) -> <a href="./src/imagekit/types/file_rename_response.py">FileRenameResponse</a></code>
- <code title="post /api/v1/files/upload">client.files.<a href="./src/imagekit/resources/files/files.py">upload_v1</a>(\*\*<a href="src/imagekit/types/file_upload_v1_params.py">params</a>) -> <a href="./src/imagekit/types/file_upload_v1_response.py">FileUploadV1Response</a></code>
- <code title="post /api/v2/files/upload">client.files.<a href="./src/imagekit/resources/files/files.py">upload_v2</a>(\*\*<a href="src/imagekit/types/file_upload_v2_params.py">params</a>) -> <a href="./src/imagekit/types/file_upload_v2_response.py">FileUploadV2Response</a></code>

## Details

Types:

```python
from imagekit.types.files import DetailRetrieveResponse, DetailUpdateResponse
```

Methods:

- <code title="get /v1/files/{fileId}/details">client.files.details.<a href="./src/imagekit/resources/files/details.py">retrieve</a>(file_id) -> <a href="./src/imagekit/types/files/detail_retrieve_response.py">DetailRetrieveResponse</a></code>
- <code title="patch /v1/files/{fileId}/details">client.files.details.<a href="./src/imagekit/resources/files/details.py">update</a>(file_id, \*\*<a href="src/imagekit/types/files/detail_update_params.py">params</a>) -> <a href="./src/imagekit/types/files/detail_update_response.py">DetailUpdateResponse</a></code>

## Batch

Types:

```python
from imagekit.types.files import BatchDeleteResponse
```

Methods:

- <code title="post /v1/files/batch/deleteByFileIds">client.files.batch.<a href="./src/imagekit/resources/files/batch.py">delete</a>(\*\*<a href="src/imagekit/types/files/batch_delete_params.py">params</a>) -> <a href="./src/imagekit/types/files/batch_delete_response.py">BatchDeleteResponse</a></code>

## Versions

Types:

```python
from imagekit.types.files import (
    VersionRetrieveResponse,
    VersionListResponse,
    VersionRestoreResponse,
)
```

Methods:

- <code title="get /v1/files/{fileId}/versions/{versionId}">client.files.versions.<a href="./src/imagekit/resources/files/versions.py">retrieve</a>(version_id, \*, file_id) -> <a href="./src/imagekit/types/files/version_retrieve_response.py">VersionRetrieveResponse</a></code>
- <code title="get /v1/files/{fileId}/versions">client.files.versions.<a href="./src/imagekit/resources/files/versions.py">list</a>(file_id) -> <a href="./src/imagekit/types/files/version_list_response.py">VersionListResponse</a></code>
- <code title="delete /v1/files/{fileId}/versions/{versionId}">client.files.versions.<a href="./src/imagekit/resources/files/versions.py">delete</a>(version_id, \*, file_id) -> object</code>
- <code title="put /v1/files/{fileId}/versions/{versionId}/restore">client.files.versions.<a href="./src/imagekit/resources/files/versions.py">restore</a>(version_id, \*, file_id) -> <a href="./src/imagekit/types/files/version_restore_response.py">VersionRestoreResponse</a></code>

## Purge

Types:

```python
from imagekit.types.files import PurgeExecuteResponse, PurgeStatusResponse
```

Methods:

- <code title="post /v1/files/purge">client.files.purge.<a href="./src/imagekit/resources/files/purge.py">execute</a>(\*\*<a href="src/imagekit/types/files/purge_execute_params.py">params</a>) -> <a href="./src/imagekit/types/files/purge_execute_response.py">PurgeExecuteResponse</a></code>
- <code title="get /v1/files/purge/{requestId}">client.files.purge.<a href="./src/imagekit/resources/files/purge.py">status</a>(request_id) -> <a href="./src/imagekit/types/files/purge_status_response.py">PurgeStatusResponse</a></code>

## Metadata

Types:

```python
from imagekit.types.files import MetadataRetrieveResponse, MetadataFromURLResponse
```

Methods:

- <code title="get /v1/files/{fileId}/metadata">client.files.metadata.<a href="./src/imagekit/resources/files/metadata.py">retrieve</a>(file_id) -> <a href="./src/imagekit/types/files/metadata_retrieve_response.py">MetadataRetrieveResponse</a></code>
- <code title="get /v1/files/metadata">client.files.metadata.<a href="./src/imagekit/resources/files/metadata.py">from_url</a>(\*\*<a href="src/imagekit/types/files/metadata_from_url_params.py">params</a>) -> <a href="./src/imagekit/types/files/metadata_from_url_response.py">MetadataFromURLResponse</a></code>

# Folder

Methods:

- <code title="post /v1/folder">client.folder.<a href="./src/imagekit/resources/folder.py">create</a>(\*\*<a href="src/imagekit/types/folder_create_params.py">params</a>) -> object</code>
- <code title="delete /v1/folder">client.folder.<a href="./src/imagekit/resources/folder.py">delete</a>(\*\*<a href="src/imagekit/types/folder_delete_params.py">params</a>) -> object</code>

# BulkJobs

Types:

```python
from imagekit.types import (
    BulkJobCopyFolderResponse,
    BulkJobMoveFolderResponse,
    BulkJobRetrieveStatusResponse,
)
```

Methods:

- <code title="post /v1/bulkJobs/copyFolder">client.bulk_jobs.<a href="./src/imagekit/resources/bulk_jobs.py">copy_folder</a>(\*\*<a href="src/imagekit/types/bulk_job_copy_folder_params.py">params</a>) -> <a href="./src/imagekit/types/bulk_job_copy_folder_response.py">BulkJobCopyFolderResponse</a></code>
- <code title="post /v1/bulkJobs/moveFolder">client.bulk_jobs.<a href="./src/imagekit/resources/bulk_jobs.py">move_folder</a>(\*\*<a href="src/imagekit/types/bulk_job_move_folder_params.py">params</a>) -> <a href="./src/imagekit/types/bulk_job_move_folder_response.py">BulkJobMoveFolderResponse</a></code>
- <code title="get /v1/bulkJobs/{jobId}">client.bulk_jobs.<a href="./src/imagekit/resources/bulk_jobs.py">retrieve_status</a>(job_id) -> <a href="./src/imagekit/types/bulk_job_retrieve_status_response.py">BulkJobRetrieveStatusResponse</a></code>

# Accounts

Types:

```python
from imagekit.types import AccountGetUsageResponse
```

Methods:

- <code title="get /v1/accounts/usage">client.accounts.<a href="./src/imagekit/resources/accounts.py">get_usage</a>(\*\*<a href="src/imagekit/types/account_get_usage_params.py">params</a>) -> <a href="./src/imagekit/types/account_get_usage_response.py">AccountGetUsageResponse</a></code>
