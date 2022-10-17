[<img width="250" alt="ImageKit.io" src="https://raw.githubusercontent.com/imagekit-developer/imagekit-javascript/master/assets/imagekit-light-logo.svg"/>](https://imagekit.io)

# ImageKit.io Python SDK

[![Python CI](https://github.com/imagekit-developer/imagekit-python/workflows/Python%20CI/badge.svg)](https://github.com/imagekit-developer/imagekit-python/)
[![imagekitio](https://img.shields.io/pypi/v/imagekitio.svg)](https://pypi.org/project/imagekitio)
[![codecov](https://codecov.io/gh/imagekit-developer/imagekit-python/branch/master/graph/badge.svg?token=CwKWqBIlCu)](https://codecov.io/gh/imagekit-developer/imagekit-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Twitter Follow](https://img.shields.io/twitter/follow/imagekitio?label=Follow&style=social)](https://twitter.com/ImagekitIo)

Python SDK for [ImageKit](https://imagekit.io/) implements the new APIs and interface for different file operations.

ImageKit is complete media storage, optimization, and transformation solution that comes with an [image and video CDN](https://imagekit.io/features/imagekit-infrastructure). It can be integrated with your existing infrastructure - storage like AWS S3, web servers, your CDN, and custom domain names, allowing you to deliver optimized images in minutes with minimal code changes.

Supported Python Versions: >=3.6

Table of contents -

-   [Installation](#installation)
-   [Initialization](#initialization)
-   [Change Log](#change-log)
-   [Usage](#usage)
    -   [URL Generation](#url-generation)
    -   [File Upload](#file-upload)
    -   [File Management](#file-management)
    -   [Utility Functions](#utility-functions)
-   [Handling errors](#handling-errors)
-   [Development](#development)
    -   [Tests](#tests)
    -   [Sample](#sample)
-   [Support](#support)
-   [Links](#links)

## Installation

Go to your terminal and type the following command.

```bash
pip install imagekitio
```

## Initialization

```python
from imagekitio import ImageKit

imagekit = ImageKit(
    private_key='your_private_key',
    public_key='your_public_key',
    url_endpoint='your_url_endpoint'
)
```

## Change log

This document presents a list of changes that break the existing functionality of previous versions. We try to minimize these disruptions, but they are sometimes unavoidable, especially in significant updates. Therefore, versions are marked semantically and tagged as major upgrades whenever such breaking changes occur.

### Breaking History:

Changes from `2.2.8 -> 3.0.0` are listed below

1. Throw an Error:

**What changed**

-   Before the upgrade, an `error` dict was coming in the return object of any function call. Now, SDK throws an exception in case of an error.

**Who is affected?**

-   This affects any development in your software that calls APIs from ImageKit IO and handles errors based on what's returned.

**How should I update my code?**

-   To avoid failures in an application, you could handle errors as [documented here](#handling-errors)

# Usage

You can use this Python SDK for three different kinds of methods:

-   [URL Generation](#url-generation)
-   [File Upload](#file-upload)
-   [File Management](#file-management)
-   [Utility Functions](#utility-functions)

## URL Generation

**1. Using Image path and endpoint (hostname)**

This method allows you to create a URL using the relative file path where the image exists and the URL
endpoint(url_endpoint) you want to use to access the image. You can refer to the documentation
[here](https://docs.imagekit.io/integration/url-endpoints) to read more about URL endpoints
in ImageKit and the section about [image origins](https://docs.imagekit.io/integration/configure-origin) to understand
about paths with different kinds of origins.

The file can be an image, video, or any other static file supported by ImageKit.

```python
imagekit_url = imagekit.url({
    "path": "/default-image.jpg",
    "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
    "transformation": [{
        "height": "300",
        "width": "400",
        "raw": "ar-4-3,q-40"
    }],
})
```

Sample Result URL -

```
https://ik.imagekit.io/your_imagekit_id/endpoint/tr:h-300,w-400,ar-4-3,q-40/default-image.jpg
```

**2. Using full image URL**

This method allows you to add transformation parameters to an absolute URL using the `src` parameter. This method should be
used if you have the complete image URL stored in your database.

```python
image_url = imagekit.url({
    "src": "https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg",
    "transformation": [{
        "height": "300",
        "width": "400",
        "raw": "ar-4-3,q-40"
    }]
})
```

Sample Result URL -

```
https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300%2Cw-400%2Car-4-3%2Cq-40
```

The `.url()` method accepts the following parameters.

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 |
| :---------------------- | :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------ |
| url_endpoint            | Optional. The prepended base URL before the path of the image. If not specified, the URL Endpoint specified during SDK initialization gets used. For example, https://ik.imagekit.io/your_imagekit_id/endpoint/                                                                                                                                                                                                                                                                             |
| path                    | Conditional. A path at which the image exists. For example, `/path/to/image.jpg`. Specify a `path` or `src` parameter for URL generation.                                                                                                                                                                                                                                                                                                                                                   |
| src                     | Conditional. Complete URL of an image already mapped to ImageKit. For example, `https://ik.imagekit.io/your_imagekit_id/endpoint/path/to/image.jpg`. Specify a `path` or `src` parameter for URL generation.                                                                                                                                                                                                                                                                                |
| transformation          | Optional. Specify an array of objects with name and the value in key-value pair to apply transformation params in the URL. Append different steps of a [chained transformation](https://docs.imagekit.io/features/image-transformations/chained-transformations) as different objects of the array. This document includes a complete list of supported transformations in the SDK with some examples. If one uses an unspecified transformation name, it gets applied as it is in the URL. |
| transformation_position | Optional. The default value is `path`, which places the transformation string as a path parameter in the URL. One can also specify it as a query, which adds the transformation string as the query parameter `tr` in the URL. Suppose one uses the `src` parameter to create the URL. In that case, the transformation string is always a query parameter.                                                                                                                                 |
| query_parameters        | Optional. These are the other query parameters that one wants to add to the final URL. These can be any query parameters and are not necessarily related to ImageKit. Especially useful if one wants to add some versioning parameter to their URLs.                                                                                                                                                                                                                                        |
| signed                  | Optional. Boolean. The default is `false`. If set to `true`, the SDK generates a signed image URL adding the image signature to the image URL. One can only use this if they create the URL with the `url_endpoint` and `path` parameters, not the `src` parameter.                                                                                                                                                                                                                         |
| expire_seconds          | Optional. Integer. Used along with the `signed` parameter to specify the time in seconds from `now` when the URL should expire. If specified, the URL contains the expiry timestamp, and the image signature is modified accordingly.                                                                                                                                                                                                                                                       |

## Examples of generating URLs

**1. Chained Transformations as a query parameter**

```python
image_url = imagekit.url({
    "path": "/default-image.jpg",
    "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
    "transformation": [
        {
            "height": "300",
            "width": "400"
        },
        {
            "rotation": 90
        }
    ],
    "transformation_position": "query"
})
```

Sample Result URL -

```
https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300%2Cw-400%3Art-90
```

**2. Sharpening, contrast transform and progressive JPG image**

Add transformations like [Sharpening](https://docs.imagekit.io/features/image-transformations/image-enhancement-and-color-manipulation) to the URL with or without any other value. To use such transforms without specifying a value, set it as "-" in the transformation object. Otherwise, use the value that one wants to add to this transformation.

```python
image_url = imagekit.url({
    "src": "https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg",
    "transformation": [{
        "format": "jpg",
        "progressive": "true",
        "effect_sharpen": "-",
        "effect_contrast": "1"
    }]
})
```

Sample Result URL -

```
# Note that because the `src` parameter is in effect, the transformation string gets added as a query parameter `tr`

https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=f-jpg%2Cpr-true%2Ce-sharpen%2Ce-contrast-1
```

**3. Signed URL that expires in 300 seconds with the default URL endpoint and other query parameters**

```python
image_url = imagekit.url({
    "path": "/default-image.jpg",
    "query_parameters": {
        "p1": "123",
        "p2": "345"
    },
    "transformation": [{
        "height": "300",
        "width": "400"
    }],
    "signed": True,
    "expire_seconds": 300
})
```

Sample Result URL -

```
https://ik.imagekit.io/your_imagekit_id/tr:h-300,w-400/default-image.jpg?p1=123&p2=345&ik-t=1658899345&ik-s=8f03aca28432d4e87f697a48143efb4497bbed9e
```

**List of transformations**

The complete list of transformations supported and their usage in ImageKit is available [here](https://docs.imagekit.io/features/image-transformations/resize-crop-and-other-transformations).
The SDK gives a name to each transformation parameter, making the code simpler, more straightforward, and readable. If a transformation is supported in ImageKit, though it cannot be found in the table below, then use the transformation code from ImageKit docs as the name when using the `URL` function.

If you want to generate transformations in your application and add them to the URL as it is, use the raw parameter.

| Supported Transformation Name | Translates to parameter         |
| ----------------------------- | ------------------------------- |
| height                        | h                               |
| width                         | w                               |
| aspect_ratio                  | ar                              |
| quality                       | q                               |
| crop                          | c                               |
| crop_mode                     | cm                              |
| x                             | x                               |
| y                             | y                               |
| focus                         | fo                              |
| format                        | f                               |
| radius                        | r                               |
| background                    | bg                              |
| border                        | b                               |
| rotation                      | rt                              |
| blur                          | bl                              |
| named                         | n                               |
| overlay_x                     | ox                              |
| overlay_y                     | oy                              |
| overlay_focus                 | ofo                             |
| overlay_height                | oh                              |
| overlay_width                 | ow                              |
| overlay_image                 | oi                              |
| overlay_image_trim            | oit                             |
| overlay_image_aspect_ratio    | oiar                            |
| overlay_image_background      | oibg                            |
| overlay_image_border          | oib                             |
| overlay_image_dpr             | oidpr                           |
| overlay_image_quality         | oiq                             |
| overlay_image_cropping        | oic                             |
| overlay_image_focus           | oifo                            |
| overlay_text                  | ot                              |
| overlay_text_font_size        | ots                             |
| overlay_text_font_family      | otf                             |
| overlay_text_color            | otc                             |
| overlay_text_transparency     | oa                              |
| overlay_alpha                 | oa                              |
| overlay_text_typography       | ott                             |
| overlay_background            | obg                             |
| overlay_text_encoded          | ote                             |
| overlay_text_width            | otw                             |
| overlay_text_background       | otbg                            |
| overlay_text_padding          | otp                             |
| overlay_text_inner_alignment  | otia                            |
| overlay_radius                | or                              |
| progressive                   | pr                              |
| lossless                      | lo                              |
| trim                          | t                               |
| metadata                      | md                              |
| color_profile                 | cp                              |
| default_image                 | di                              |
| dpr                           | dpr                             |
| effect_sharpen                | e-sharpen                       |
| effect_usm                    | e-usm                           |
| effect_contrast               | e-contrast                      |
| effect_gray                   | e-grayscale                     |
| original                      | orig                            |
| raw                           | replaced by the parameter value |

## File Upload

The SDK provides a simple interface using the `.upload_file()` method to upload files to the ImageKit Media library. It
accepts all the parameters supported by
the [ImageKit Upload API](https://docs.imagekit.io/api-reference/upload-file-api/server-side-file-upload).

The `upload_file()` method requires at least the `file` as (URL/Base64/Binary) and the `file_name` parameter to upload a
file. The method returns a dict data in case of success, or it will throw a custom exception in case of failure.
Use the `options` parameter to pass other parameters supported by
the [ImageKit Upload API](https://docs.imagekit.io/api-reference/upload-file-api/server-side-file-upload). Use the same
parameter name as specified in the upload API documentation.

Simple usage

```python
from imagekitio.models.UploadFileRequestOptions import UploadFileRequestOptions

extensions = [
    {
        'name': 'remove-bg',
        'options': {
            'add_shadow': True,
            'bg_color': 'pink'
        }
    },
    {
        'name': 'google-auto-tagging',
        'minConfidence': 80,
        'maxTags': 10
    }
]

options = UploadFileRequestOptions(
    use_unique_file_name=False,
    tags=['abc', 'def'],
    folder='/testing-python-folder/',
    is_private_file=False,
    custom_coordinates='10,10,20,20',
    response_fields=['tags', 'custom_coordinates', 'is_private_file',
                     'embedded_metadata', 'custom_metadata'],
    extensions=extensions,
    webhook_url='https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e',
    overwrite_file=True,
    overwrite_ai_tags=False,
    overwrite_tags=False,
    overwrite_custom_metadata=True,
    custom_metadata={'testss': 12},
)

result = imagekit.upload_file(file='<url|base_64|binary>', # required
                              file_name='my_file_name.jpg', # required
                              options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print that uploaded file's ID
print(result.file_id)
```

If the upload succeeds, the `result` will be the `UploadFileResult` class.

If the upload fails, the custom exception will be thrown with:

-   `response_help` for any kind of help
-   `response_metadata` with `raw`, `http_status_code` and `headers`
-   `message` can be called to get the error message received from ImageKit's servers.

## File Management

The SDK provides a simple interface for all
the [media APIs mentioned here](https://docs.imagekit.io/api-reference/media-api)
to manage your files. This also returns `result`.

**1. List & Search Files**

Accepts an object specifying the parameters used to list and search files. All parameters specified
in
the [documentation here](https://docs.imagekit.io/api-reference/media-api/list-and-search-files#list-and-search-file-api)
can be passed with the correct values to get the results.

```Python
from imagekitio.models.ListAndSearchFileRequestOptions import ListAndSearchFileRequestOptions

options = ListAndSearchFileRequestOptions(
    type='file',
    sort='ASC_CREATED',
    path='/',
    search_query="created_at >= '2d' OR size < '2mb' OR format='png'",
    file_type='all',
    limit=5,
    skip=0,
    tags='Software, Developer, Engineer',
)

result = imagekit.list_files(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the first file's ID
print(result.list[0].file_id)
```

**2. Get File Details**

Accepts the file ID and fetches the details as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/get-file-details)

```python
file_id = "your_file_id"
result = imagekit.get_file_details(file_id=file_id)  # file_id required

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print that file's id
print(result.file_id)
```

**3. Get File Versions**

Accepts the file ID and fetches the details as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/get-file-versions)

```python
file_id = "your_file_id"
result = imagekit.get_file_versions(file_id=file_id)  # file_id required


# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print that file's version id
print(result.list[0].version_info.id)
```

**4. Get File Version details**

Accepts the `file_id` and `version_id` and fetches the details as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/get-file-version-details)

```python
result = imagekit.get_file_version_details(
    file_id='file_id',
    version_id='version_id'
)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print that file's id
print(result.file_id)

# print that file's version id
print(result.version_info.id)
```

**5. Update File Details**

Accepts all the parameters as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/update-file-details).
The first argument to the `update_file_details()` method is the file ID, and a second argument is an object with the
parameters to be
updated.

```python
from imagekitio.models.UpdateFileRequestOptions import UpdateFileRequestOptions

extensions = [
    {
        'name': 'remove-bg',
        'options': {
            'add_shadow': True,
            'bg_color': 'red'
        }
    },
    {
        'name': 'google-auto-tagging',
        'minConfidence': 80,
        'maxTags': 10
    }
]

options = UpdateFileRequestOptions(
    remove_ai_tags=['remove-ai-tag-1', 'remove-ai-tag-2'],
    webhook_url='url',
    extensions=extensions,
    tags=['tag-1', 'tag-2'],
    custom_coordinates='10,10,100,100',
    custom_metadata={'test': 11},
)

result = imagekit.update_file_details(file_id='62cfd39819ca454d82a07182'
        , options=options)  # required

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print that file's id
print(result.file_id)
```

**6. Add tags**

Accepts a list of `file_ids` and `tags` as a parameter to be used to add tags. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/add-tags-bulk) can be passed to
the `.add_tags()` functions to get the results.

```python
result = imagekit.add_tags(file_ids=['file-id-1', 'file-id-2'], tags=['add-tag-1', 'add-tag-2'])

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# list successfully updated file ids
print(result.successfully_updated_file_ids)

# print the first file's id
print(result.successfully_updated_file_ids[0])
```

**7. Remove tags**

Accepts a list of `file_ids` and `tags` as a parameter to be used to remove tags. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/remove-tags-bulk) can be passed to
the `.remove_tags()` functions to get the results.

```python
result = imagekit.remove_tags(file_ids=['file-id-1', 'file-id-2'], tags=['remove-tag-1', 'remove-tag-2'])

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# list successfully updated file ids
print(result.successfully_updated_file_ids)

# print the first file's id
print(result.successfully_updated_file_ids[0])
```

**8. Remove AI tags**

Accepts a list of `file_ids` and `ai_tags` as a parameter to remove AI tags. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/remove-aitags-bulk) can be passed to
the `.remove_ai_tags()` functions to get the results.

```python
result = imagekit.remove_ai_tags(file_ids=['file-id-1', 'file-id-2'], ai_tags=['remove-ai-tag-1', 'remove-ai-tag-2'])

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# list successfully updated file ids
print(result.successfully_updated_file_ids)

# print the first file's id
print(result.successfully_updated_file_ids[0])
```

**9. Delete File**

Delete a file according to the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-file). It accepts the file ID of the File that has to be
deleted.

```python
file_id = "file_id"
result = imagekit.delete_file(file_id=file_id)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)
```

**10. Delete FileVersion**

Delete a file version as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-file-version).
The method accepts the `file_id` and particular version id of the file that has to be deleted.

```python
result = imagekit.delete_file_version(file_id="file_id", version_id="version_id")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)
```

**11. Bulk File Delete by IDs**

Delete a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-files-bulk).
The method accepts a list of file IDs that have to be deleted.

```python
result = imagekit.bulk_file_delete(file_ids=["file_id1", "file_id2"])

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# list successfully deleted file ids
print(result.successfully_deleted_file_ids)

# print the first file's id
print(result.successfully_deleted_file_ids[0])
```

**12. Copy file**

Copy a file according to the [API documentation here](https://docs.imagekit.io/api-reference/media-api/copy-file).
The method accepts `source_file_path`, `destination_path`, and `include_file_versions` of the file that has to be copied.

```python
from imagekitio.models.CopyFileRequestOptions import CopyFileRequestOptions

options = \
    CopyFileRequestOptions(source_file_path='/source_file_path.jpg',
                           destination_path='/destination_path',
                           include_file_versions=True)
result = imagekit.copy_file(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)
```

**13. Move File**

Move a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/move-file).
The method accepts `source_file_path` and `destination_path` of the file that has to be moved.

```python
from imagekitio.models.MoveFileRequestOptions import MoveFileRequestOptions

options = \
    MoveFileRequestOptions(source_file_path='/source_file_path.jpg',
                           destination_path='/destination_path')
result = imagekit.move_file(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)
```

**14. Rename File**

Rename a file per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/rename-file).
The method accepts the `file_path`, `new_file_name`, and `purge_cache` boolean that has to be renamed.

```python
from imagekitio.models.RenameFileRequestOptions import RenameFileRequestOptions

options = RenameFileRequestOptions(file_path='/file_path.jpg',
                                   new_file_name='new_file_name.jpg',
                                   purge_cache=True)
result = imagekit.rename_file(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the purge request id
print(result.purge_request_id)
```

**15. Restore file Version**

Restore a file as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/restore-file-version).
The method accepts the `file_id` and `version_id` of the file that has to be restored.

```python
result = imagekit.restore_file_version(file_id="file_id", version_id="version_id")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print that file's id
print(result.file_id)
```

**16. Create Folder**

Create a folder per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/create-folder).
The method accepts `folder_name` and `parent_folder_path` as options that must be created.

```Python
from imagekitio.models.CreateFolderRequestOptions import CreateFolderRequestOptions

options = CreateFolderRequestOptions(folder_name='test',
                                     parent_folder_path='/')
result = imagekit.create_folder(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)
```

**17. Delete Folder**

Delete a folder as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-folder).
The method accepts `folder_path` as an option that must be deleted.

```python
from imagekitio.models.DeleteFolderRequestOptions import DeleteFolderRequestOptions

options = DeleteFolderRequestOptions(folder_path='/test/demo')
result = imagekit.delete_folder(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)
```

**18. Copy Folder**

Copy a folder as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/copy-folder).
The method accepts the `source_folder_path`, `destination_path`, and `include_file_versions` boolean as options that
have to be copied.

```python
from imagekitio.models.CopyFolderRequestOptions import CopyFolderRequestOptions
options = \
    CopyFolderRequestOptions(source_folder_path='/source_folder_path',
                             destination_path='/destination/path',
                             include_file_versions=True)
result = imagekit.copy_folder(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the job's id
print(result.job_id)
```

**19. Move Folder**

Move a folder as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/move-folder).
The method accepts the `source_folder_path` and `destination_path` of a folder as options that must be moved.

```python
from imagekitio.models.MoveFolderRequestOptions import MoveFolderRequestOptions
options = \
    MoveFolderRequestOptions(source_folder_path='/source_folder_path',
                             destination_path='/destination_path')
result = imagekit.move_folder(options=options)
# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the job's id
print(result.job_id)
```

**20. Get Bulk Job Status**

Accepts the `job_id` to get bulk job status as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/copy-move-folder-status).
The method takes only jobId.

```python
result = imagekit.get_bulk_job_status(job_id="job_id")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the job's id
print(result.job_id)

# print the status
print(result.status)
```

**21. Purge Cache**

Programmatically issue an explicit cache request as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/purge-cache).
Accepts the full URL of the File for which the cache has to be cleared.

```python
result = imagekit.purge_file_cache(file_url="full_url_of_file")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the purge file cache request id
print(result.request_id)
```

**22. Purge Cache Status**

Get the purge cache request status using the `cache_request_id` returned when a purge cache request gets submitted as per the
[API documentation here](https://docs.imagekit.io/api-reference/media-api/purge-cache-status)

```python
result = imagekit.get_purge_file_cache_status(purge_cache_id="cache_request_id")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the purge file cache status
print(result.status)
```

**23. Get File Metadata**

Accepts the `file_id` and fetches the metadata as per
the [API documentation here](https://docs.imagekit.io/api-reference/metadata-api/get-image-metadata-for-uploaded-media-files)

```python
result = imagekit.get_file_metadata(file_id="file_id")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the file metadata fields
print(result.width)
print(result.exif.image.x_resolution)
```

**24. Get File Metadata from remote URL**

Accepts the `remote_file_url` and fetches the metadata as per
the [API documentation here](https://docs.imagekit.io/api-reference/metadata-api/get-image-metadata-from-remote-url)

```python
result = imagekit.get_remote_file_url_metadata(remote_file_url="remote_file_url")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the file metadata fields
print(result.width)
print(result.exif.image.x_resolution)
```

**25. Create CustomMetaDataFields**

Accepts an option specifying the parameters used to create custom metadata fields. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/create-custom-metadata-field)
can be passed as it is with the correct values to get the results.

Check for the [allowed values in the schema](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/create-custom-metadata-field#allowed-values-in-the-schema-object).

**Example:**

```python
# Example for the type number

from imagekitio.models.CreateCustomMetadataFieldsRequestOptions import CreateCustomMetadataFieldsRequestOptions
from imagekitio.models.CustomMetadataFieldsSchema import CustomMetadataFieldsSchema
from imagekitio.models.CustomMetaDataTypeEnum import CustomMetaDataTypeEnum
schema = CustomMetadataFieldsSchema(type=CustomMetaDataTypeEnum.Number,
                                    min_value=100,
                                    max_value=200)
options = CreateCustomMetadataFieldsRequestOptions(name='test',
                                                   label='test',
                                                   schema=schema)
result = imagekit.create_custom_metadata_fields(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the id of created custom metadata fields
print(result.id)

# print the schema's type of created custom metadata fields
print(result.schema.type)

```

```python
# MultiSelect type Example

from imagekitio.models.CreateCustomMetadataFieldsRequestOptions import CreateCustomMetadataFieldsRequestOptions
from imagekitio.models.CustomMetadataFieldsSchema import CustomMetadataFieldsSchema
from imagekitio.models.CustomMetaDataTypeEnum import CustomMetaDataTypeEnum

schema = \
    CustomMetadataFieldsSchema(type=CustomMetaDataTypeEnum.MultiSelect,
                               is_value_required=True,
                               default_value=['small', 30, True],
                               select_options=[
                                    'small',
                                    'medium',
                                    'large',
                                    30,
                                    40,
                                    True,
                                ])
options = \
    CreateCustomMetadataFieldsRequestOptions(name='test-MultiSelect',
        label='test-MultiSelect', schema=schema)
result = imagekit.create_custom_metadata_fields(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the name of created custom metadata fields
print(result.name)

# print the schema's select options of created custom metadata fields
print(result.schema.select_options)

```

```python
# Date type Example

from imagekitio.models.CreateCustomMetadataFieldsRequestOptions import CreateCustomMetadataFieldsRequestOptions
from imagekitio.models.CustomMetadataFieldsSchema import CustomMetadataFieldsSchema
from imagekitio.models.CustomMetaDataTypeEnum import CustomMetaDataTypeEnum

schema = CustomMetadataFieldsSchema(type=CustomMetaDataTypeEnum.Date,
                                    min_value='2022-11-29T10:11:10+00:00',
                                    max_value='2022-11-30T10:11:10+00:00')
options = CreateCustomMetadataFieldsRequestOptions(name='test-date',
                                                   label='test-date',
                                                   schema=schema)
result = imagekit.create_custom_metadata_fields(options=options)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the label of created custom metadata fields
print(result.label)

# print the schema's min value of created custom metadata fields
print(result.schema.min_value)

```

**26. Get CustomMetaDataFields**

Accepts the `include_deleted` boolean as the initial parameter and fetches the metadata as per
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/get-custom-metadata-field)
.

```python
result = imagekit.get_custom_metadata_fields()  # in this case, it will consider includeDeleted as a False

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the first customMetadataField's id
print(result.list[0].id)

# print the first customMetadataField schema's type
print(result.list[0].schema.type)
```

```python
result = imagekit.get_custom_metadata_fields(include_deleted=True)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the first customMetadataField's name
print(result.list[0].name)

# print the first customMetadataField schema's default value
print(result.list[0].schema.default_value)
```

**27. Update CustomMetaDataFields**

Accepts a `field_id` and options for specifying the parameters to be used to edit custom metadata fields
as per
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/update-custom-metadata-field)
.

```python

from imagekitio.models.CustomMetadataFieldsSchema import CustomMetadataFieldsSchema
from imagekitio.models.UpdateCustomMetadataFieldsRequestOptions import UpdateCustomMetadataFieldsRequestOptions

schema = CustomMetadataFieldsSchema(min_value=100, max_value=200)
options = UpdateCustomMetadataFieldsRequestOptions(
    label='test-update',
    schema=schema
)
result = imagekit.update_custom_metadata_fields(
    field_id='id_of_custom_metadata_field',
    options=options
)

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)

# print the label of updated custom metadata fields
print(result.label)

# print the schema's min value of updated custom metadata fields
print(result.schema.min_value)
```

**28. Delete CustomMetaDataFields**

Accepts the id to delete the custom metadata fields as per
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/delete-custom-metadata-field)
.

```python
result = imagekit.delete_custom_metadata_field(field_id="id_of_custom_metadata_field")

# Final Result
print(result)

# Raw Response
print(result.response_metadata.raw)
```

## Utility functions

We have included the following commonly used utility functions in this package.

**Authentication parameter generation**

Suppose one wants to implement client-side file upload. In that case, one will need a token, expiry timestamp, and a valid signature for that upload. The SDK provides a simple method that one can use in their code to generate these authentication parameters.

<em>Note: Any client-side code should never expose The Private API Key. One must always generate these authentications parameters on the server-side</em>

authentication

`authentication_parameters = imagekit.get_authentication_parameters(token, expire)`

Returns

```python
{
    "token": "unique_token",
    "expire": "valid_expiry_timestamp",
    "signature": "generated_signature"
}
```

Both the `token` and `expire` parameters are optional. If not specified, the SDK uses the UUID to generate a random token and internally generates a valid expiry timestamp. The `token` and `expire` used to generate `signature` is part of a response returned by the server.

**Distance calculation between two `pHash` values**

Perceptual hashing allows you to construct a has value that uniquely identifies an input image based on the contents
of an image. [imagekit.io metadata API](https://docs.imagekit.io/api-reference/metadata-api) returns the `pHash`
value of an image in the response. You can use this value
to [find a duplicate or similar image](https://docs.imagekit.io/api-reference/metadata-api#using-phash-to-find-similar-or-duplicate-images)
by calculating the distance between the two images.

This SDK exposes the `phash_distance` function to calculate the distance between two `pHash` values. It accepts two `pHash`
hexadecimal
strings and returns a numeric value indicative of the difference between the two images.

```python
def calculate_distance():
    # fetch metadata of two uploaded image files
    ...
    # extract pHash strings from both: say 'first_hash' and 'second_hash'
    ...
    # calculate the distance between them:

    distance = imagekit.phash_distance(first_hash, second_hash)
    return distance

```

**Distance calculation examples**

```Python
imagekit.phash_distance('f06830ca9f1e3e90', 'f06830ca9f1e3e90')
# output: 0 (same image)

imagekit.phash_distance('2d5ad3936d2e015b', '2d6ed293db36a4fb')
# output: 17 (similar images)

imagekit.phash_distance('a4a65595ac94518b', '7838873e791f8400')
# output: 37 (dissimilar images)
```

**HTTP response metadata of Internal API**

HTTP response metadata of the internal API call can be accessed using the \_response_metadata on the Result object.
Example:

```Python
result = imagekit.upload_file(
    file="<url|base_64|binary>",
    file_name="my_file_name.jpg",
)

# Final Result
print(result)
print(result.response_metadata.raw)
print(result.response_metadata.http_status_code)
print(result.response_metadata.headers)
```

### Sample Code Instruction

To run `sample` code go to the code samples here are hosted on GitHub - https://github.com/imagekit-samples/quickstart/tree/master/python and run.

```shell
python sample.py
```

## Handling errors

Catch and respond to invalid data, internal problems, and more.

ImageKit Python SDK raises exceptions for many reasons, such as not found, invalid parameters, authentication, and
internal server errors. Therefore, we recommend writing code that gracefully handles all possible API exceptions.

#### Example:

```Python
from imagekitio.exceptions.BadRequestException import BadRequestException
from imagekitio.exceptions.UnauthorizedException import UnauthorizedException
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.TooManyRequestsException import TooManyRequestsException
from imagekitio.exceptions.InternalServerException import InternalServerException
from imagekitio.exceptions.PartialSuccessException import PartialSuccessException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.exceptions.UnknownException import UnknownException

try:

    # Use ImageKit's SDK to make requests...
    print('Run image kit api')
except BadRequestException, e:
    # Missing or Invalid parameters were supplied to Imagekit.io's API
    print('Status is: ' + e.response_metadata.http_status_code)
    print('Message is: ' + e.message)
    print('Headers are: ' + e.response_metadata.headers)
    print('Raw body is: ' + e.response_metadata.raw)
except UnauthorizedException, e:
    print(e)
except ForbiddenException, e:
    # No valid API key was provided.
    print(e)
except TooManyRequestsException, e:
    # Can be for the following reasons:
    # ImageKit could not authenticate your account with the keys provided.
    # An expired key (public or private) was used with the request.
    # The account is disabled.
    # If you use the upload API, the total storage limit (or upload limit) is exceeded.
    print(e)
except InternalServerException, e:
    # Too many requests made to the API too quickly
    print(e)
except PartialSuccessException, e:
    # Something went wrong with ImageKit.io API.
    print(e)
except NotFoundException, e:
    # Error cases on partial success.
    print(e)
except UnknownException, e:
    # If any of the field or parameter is not found in the data
    print(e)

# Something else happened, which can be unrelated to ImageKit; the reason will be indicated in the message field
```

## Development

### Tests

Tests are powered by [Tox](https://tox.wiki/en/latest/).

```bash
$ git clone https://github.com/imagekit-developer/imagekit-python && cd imagekit-python
$ pip install tox
$ tox
```

### Sample

#### Get & Install local ImageKit Python SDK

```bash
$ git clone https://github.com/imagekit-developer/imagekit-python && cd imagekit-python
$ pip install -e .
```

#### Get samples

To integrate ImageKit Samples in the Python, the code samples covered here are hosted on GitHub - https://github.com/imagekit-samples/quickstart/tree/master/python.

Open the `python/sample.py` file and replace placeholder credentials with actual values. You can get the value of [URL-endpoint](https://imagekit.io/dashboard#url-endpoints) from your ImageKit dashboard. API keys can be obtained from the [developer](https://imagekit.io/dashboard/developer/api-keys) section in your ImageKit dashboard.

In the `python/sample.py` file, set the following parameters for authentication:

```python
from imagekitio import ImageKit
imagekit = ImageKit(
    private_key='your private_key',
    public_key='your public_key',
    url_endpoint = 'your url_endpoint'
)
```

To install dependencies that are in the `python/requirements.txt` file, can fire this command to install them:

```shell
pip install -r python/requirements.txt
```

Now run `python/sample.py`. If you are using CLI Tool (Terminal/Command prompt), open the project in CLI and execute it.

```shell
# if not installed already
pip install imagekitio

# if installing local sdk
pip install -e <path_to_local_sdk>

# to run sample.py file
python3 python/sample.py
```

## Support

For any feedback or to report any issues or general implementation support, please reach out
to [support@imagekit.io](https://github.com/imagekit-developer/imagekit-python)

## Links

-   [Documentation](https://docs.imagekit.io/)

-   [Main Website](https://imagekit.io/)

## License

Released under the MIT license.
