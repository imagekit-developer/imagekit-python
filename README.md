[<img width="250" alt="ImageKit.io" src="https://raw.githubusercontent.com/imagekit-developer/imagekit-javascript/master/assets/imagekit-light-logo.svg"/>](https://imagekit.io)

# ImageKit.io Python SDK

[![Python CI](<https://github.com/imagekit-developer/imagekit-python/workflows/Python%20CI/badge.svg>)](https://github.com/imagekit-developer/imagekit-python/)
[![imagekitio](<https://img.shields.io/pypi/v/imagekitio.svg>)](https://pypi.org/project/imagekitio)
[![codecov](https://codecov.io/gh/imagekit-developer/imagekit-python/branch/master/graph/badge.svg?token=CwKWqBIlCu)](https://codecov.io/gh/imagekit-developer/imagekit-python)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Twitter Follow](https://img.shields.io/twitter/follow/imagekitio?label=Follow&style=social)](https://twitter.com/ImagekitIo)

ImageKit Python SDK allows you to use [image resizing](https://docs.imagekit.io/features/image-transformations)
, [optimization](https://docs.imagekit.io/features/image-optimization)
, [file uploading](https://docs.imagekit.io/api-reference/upload-file-api) and
other [ImageKit APIs](https://docs.imagekit.io/api-reference/api-introduction) from applications written in the Python
language.

Supported Python Versions: >=3.6

Table of contents -

* [Installation](#Installation)
* [Initialization](#Initialization)
* [Change log](#Change log)
* [URL Generation](#URL-generation)
* [File Upload](#File-Upload)
* [File Management](#File-Management)
* [Utility Functions](#Utility-functions)
* [Handling errors](#handling-errors)
* [Support](#Support)
* [Links](#Links)

## Installation

Go to your terminal and type the following command

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

## Usage

You can use this Python SDK for 3 different kinds of methods:

- URL generation
- file upload
- file management

The usage of the SDK has been explained below.

## Change log

This document presents a list of changes that break existing functionality of previous versions. We try our best to minimize these disruptions, but sometimes they are unavoidable and they will be in major versions.

### Breaking History:

Changes from 2.2.8 -> 3.0.0 are listed below

1. Throw an Error:

**What changed**

- In case of failure, the API would throw an exception.

**Who is affected?**

- This affects any development in your application that calls APIs from imagekit IO.

**How should I update my code?**

- To avoid failures in an application, you could handle errors as [documented here](#handling-errors)

## URL generation

**1. Using Image path and image hostname or endpoint**

This method allows you to create an URL using the relative file path where the image exists and the URL
endpoint(url_endpoint) you want to use to access the image. You can refer to the documentation
[here](https://docs.imagekit.io/integration/url-endpoints) to read more about URL endpoints
in ImageKit and the section about [image origins](https://docs.imagekit.io/integration/configure-origin) to understand
about paths with different kinds of origins.
The file can be an image, video, or any other static file supported by ImageKit.

```python
imagekit_url = imagekit.url({
    "path": "/default-image.jpg",
    "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
    "transformation": [{"height": "300", "width": "400", "raw": "ar-4-3,q-40"}],
}
)
```

The result in a URL like

```
https://ik.imagekit.io/your_imagekit_id/endpoint/tr:h-300,w-400,raw-ar-4-3,q-40/default-image.jpg
```

**2. Using full image URL**

This method allows you to add transformation parameters to an absolute URL using `src` parameter. This method should be
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

The results in a URL like

```
https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300%2Cw-400%2Craw-ar-4-3%2Cq-40
```

The ```.url()``` method accepts the following parameters.

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| url_endpoint            | Optional. The base URL to be appended before the path of the image. If not specified, the URL Endpoint specified at the time of SDK initialization is used. For example, https://ik.imagekit.io/your_imagekit_id/endpoint/                                                                                                                                                                                                                                                                                                                                                                |
| path                    | Conditional. This is the path at which the image exists. For example, `/path/to/image.jpg`. Either the `path` or `src` parameter needs to be specified for URL generation.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| src                     | Conditional. This is the complete URL of an image already mapped to ImageKit. For example, `https://ik.imagekit.io/your_imagekit_id/endpoint/path/to/image.jpg`. Either the `path` or `src` parameter needs to be specified for URL generation.                                                                                                                                                                                                                                                                                                                                            |
| transformation          | Optional. An array of objects specifying the transformation to be applied in the URL. The transformation name and the value should be specified as a key-value pair in the object. Different steps of a [chained transformation](https://docs.imagekit.io/features/image-transformations/chained-transformations) can be specified as different objects of the array. The complete list of supported transformations in the SDK and some examples of using them are given later. If you use a transformation name that is not specified in the SDK, it gets applied as it is in the URL. |
| transformation_position | Optional. The default value is `path` that places the transformation string as a path parameter in the URL. It can also be specified as `query`, which adds the transformation string as the query parameter `tr` in the URL. If you use the `src` parameter to create the URL, then the transformation string is always added as a query parameter.                                                                                                                                                                                                                                                  |
| query_parameters        | Optional. These are the other query parameters that you want to add to the final URL. These can be any query parameters and not necessarily related to ImageKit. Especially useful if you want to add some versioning parameter to your URLs.                                                                                                                                                                                                                                                                                                                                            |
| signed                  | Optional. Boolean. Default is `false`. If set to `true`, the SDK generates a signed image URL adding the image signature to the image URL. This can only be used if you are creating the URL with the `url_endpoint` and `path` parameters and not with the `src` parameter.                                                                                                                                                                                                                                                                                                             |
| expire_seconds          | Optional. Integer. Meant to be used along with the `signed` parameter to specify the time in seconds from now when the URL should expire. If specified, the URL contains the expiry timestamp in the URL, and the image signature is modified accordingly.                                                                                                                                                                                                                                                                                                                                 |

## Examples of generating URLs

**1. Chained Transformations as a query parameter**

```python
    image_url = imagekit.url({
    "path": "/default-image.jpg",
    "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
    "transformation": [{
        "height": "300",
        "width": "400"
    },
    {
        "rotation": 90
    }],
    "transformation_position": "query"
})
```

Sample Result URL -

```
https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300%2Cw-400%3Art-90
```

**2. Sharpening and contrast transforms and a progressive JPG image**

There are some transforms
like [Sharpening](https://docs.imagekit.io/features/image-transformations/image-enhancement-and-color-manipulation)
that can be added to the URL with or without any other value. To use such transforms without specifying a value, specify
the value as "-" in the transformation object. Otherwise, specify the value that you want to be added to this
transformation.

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

Note that because `src` parameter was used, the transformation string gets added as a query parameter.

```
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

**Sample Result URL**

```
https://ik.imagekit.io/your_imagekit_id/tr:h-300,w-400/default-image.jpg?p1=123&p2=345&ik-t=1658899345&ik-s=8f03aca28432d4e87f697a48143efb4497bbed9e
```

**List of transformations**

The complete list of transformations supported and their usage in ImageKit can be
found [here](https://docs.imagekit.io/features/image-transformations/resize-crop-and-other-transformations).
The SDK gives a name to each transformation parameter, see the complete list of image and video transformations
supported in ImageKit. The SDK gives a name to each transformation parameter e.g. height for h and width for w
parameter. It makes your code simpler and readable.
If a transformation is supported in ImageKit, If the property does not match any of the following supported options, it
is added as it is.

If you want to generate transformations in your application and add them to the URL as it is, use the raw parameter.

| Supported Transformation Name | Translates to parameter         |
|-------------------------------|---------------------------------|
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
file. The method returns a Dict data in case of success, or it will throw a custom exception in case of failure.
Use the `options` parameter to pass other parameters supported by
the [ImageKit Upload API](https://docs.imagekit.io/api-reference/upload-file-api/server-side-file-upload). Use the same
parameter name as specified in the upload API documentation.

Simple usage

```python
import json

result = imagekit.upload_file(
    file="<url|base_64|binary>",  # required
    file_name="my_file_name.jpg",  # required
    options={
        "folder": "/example-folder/",
        "tags": ["sample-tag"],
        "is_private_file": False,
        "use_unique_file_name": True,
        "response_fields": ["is_private_file", "tags"],
        "extensions": json.dumps(
            ({"name": "remove-bg", "options": {"add_shadow": True, "bg_color": "pink"}},
             {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10})
        ),
        "webhook_url": "url",
        "overwrite_file": True,
        "overwrite_a_i_tags": False,
        "overwrite_tags": False,
        "overwrite_custom_metadata": True,
        "custom_metadata": json.dumps({"test": 10}),
    }
)
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print that uploaded file's ID
print(result.file_id)
```

If the upload succeeds, the `result` will be the `UploadFileResult` class.

If the upload fails, the custom exception will be thrown with:

- `response_help` for any kind of help
- `response_metadata` with `raw`, `http_status_code` and `headers`
- `message` can be called to get the error message received from ImageKit's servers.

## File Management

The SDK provides a simple interface for all
the [media APIs mentioned here](https://docs.imagekit.io/api-reference/media-api)
to manage your files. This also returns `error` and `result`. The error will be `None` if API succeeds.

**1. List & Search Files**

Accepts an object specifying the parameters to be used to list and search files. All parameters specified
in
the [documentation here](https://docs.imagekit.io/api-reference/media-api/list-and-search-files#list-and-search-file-api)
can be passed with the correct values to get the results.

```python
result = imagekit.list_files({"type": "file", "sort": "ASC_CREATED", "path": "/",
                                      "search_query": "created_at >= '2d' OR size < '2mb' OR format='png'",
                                      "file_type": "all", "limit": 5, "skip": 0,
                                      "tags": "Software, Developer, Engineer"})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the first file's ID
print(result.list[0].file_id)
```

**2. Get File Details**

Accepts the file ID and fetches the details as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/get-file-details)

```python
file_id = "your_file_id"
result = imagekit.get_file_details(file_id)  # fileId required
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print that file's id
print(result.file_id)
```

**3. Get File Versions**

Accepts the file ID and fetches the details as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/get-file-versions)

```python
file_id = "your_file_id"
result = imagekit.get_file_versions(file_id)  # fileId required
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print that file's version id
print(result.list[0].version_info.id)
```

**4. Get File Version details**

Accepts the file ID and version ID and fetches the details as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/get-file-version-details)

```python
result = imagekit.get_file_version_details("file_id"  # required
                                           , "version_id")  # required
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print that file's id
print(result.file_id)
# print that file's version id
print(result.version_info.id)
```

**5. Update File Details**

Accepts all the parameters as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/update-file-details).
The first argument to the `update_file_details()` method is the file ID, and the second argument is an object with the
parameters to be
updated.

```python
result = imagekit.update_file_details(
    "62cfd39819ca454d82a07182",  # required
    {
        "remove_a_i_tags": ['remove-ai-tag-1', 'remove-ai-tag-2'],
        "webhook_url": "url",
        "extensions": [{
            "name": "remove-bg",
            "options": {
                "add_shadow": True,
                "bg_color": "red"
            }
        }, {
            "name": "google-auto-tagging",
            "minConfidence": 80,
            "maxTags": 10
        }],
        "tags": ["tag-1", "tag-2"],
        "custom_coordinates": "10,10,100,100",
        "custom_metadata": {
            "test": 11
        }
    }
)
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print that file's id
print(result.file_id)
```

**6. Add tags**

Accepts list of File Ids and Tags as a parameters to be used to add tags. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/add-tags-bulk) can be passed to
the `.add_tags()` functions to get the results.

```python
result = imagekit.add_tags(file_ids=['file-id-1', 'file-id-2'], tags=['add-tag-1', 'add-tag-2'])
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# list successfully updated file ids
print(result.successfully_updated_file_ids)
# print the first file's id
print(result.successfully_updated_file_ids[0])
```

**7. Remove tags**

Accepts list of File Ids and Tags as a parameters to be used to remove tags. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/remove-tags-bulk) can be passed to
the `.remove_tags()` functions to get the results.

```python
result = imagekit.remove_tags(file_ids=['file-id-1', 'file-id-2'], tags=['remove-tag-1', 'remove-tag-2'])
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# list successfully updated file ids
print(result.successfully_updated_file_ids)
# print the first file's id
print(result.successfully_updated_file_ids[0])
```

**8. Remove AI tags**

Accepts list of File Ids and AITags as a parameters to be used to remove AI tags. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/remove-aitags-bulk) can be passed to
the `.remove_ai_tags()` functions to get the results.

```python
result = imagekit.remove_ai_tags(file_ids=['file-id-1', 'file-id-2'], a_i_tags=['remove-ai-tag-1', 'remove-ai-tag-2'])
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# list successfully updated file ids
print(result.successfully_updated_file_ids)
# print the first file's id
print(result.successfully_updated_file_ids[0])
```

**9. Delete File**

Delete a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-file). The
method accepts the file ID of the file that has to be
deleted.

```python
file_id = "file_id"
result = imagekit.delete_file(file_id)
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
```

**10. Delete FileVersion**

Delete a file version as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-file-version).
The method accepts file ID of file and particular version id of that file that has to be deleted.

```python
result = imagekit.delete_file_version("file_id", "version_id")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
```

**11. Bulk File Delete by IDs**

Delete a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-files-bulk).
The method accepts list of file IDs of files that has to be deleted.

```python
result = imagekit.bulk_file_delete(["file_id1", "file_id2"])
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# list successfully deleted file ids
print(result.successfully_deleted_file_ids)
# print the first file's id
print(result.successfully_deleted_file_ids[0])
```

**12. Copy file**

Copy a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/copy-file).
The method accepts sourceFilePath, destinationPath and includeFileVersions of file that has to be copied.

```python
result = imagekit.copy_file(options={"source_file_path": "/source_file_path.jpg",
                                     "destination_path": "/destination_path",
                                     "include_file_versions": True})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
```

**13. Move file**

Move a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/move-file).
The method accepts sourceFilePath and destinationPath of file that has to be moved.

```python
result = imagekit.move_file(options={"source_file_path": "/source_file_path.jpg",
                                     "destination_path": "/destination_path"})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
```

**14. Rename file**

Rename a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/rename-file).
The method accepts filePath and newFileName for file and purgeCache boolean that has to be renamed.

```python
result = imagekit.rename_file(options={"file_path": "/file_path.jpg",
                                       "new_file_name": "new_file_name.jpg",
                                       "purge_cache": True})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the purge request id
print(result.purge_request_id)
```

**15. Restore file Version**

Restore a file as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/restore-file-version).
The method accepts fileId and versionId of file that has to be restored.

```python
result = imagekit.restore_file_version("file_id", "version_id")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print that file's id
print(result.file_id)
```

**16. Create Folder**

Create a folder as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/create-folder).
The method accepts folderName and parentFolderPath as an options that has to be created.

```python
result = imagekit.create_folder(options={"folder_name": "/test", "parent_folder_path": "/"})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
```

**17. Delete Folder**

Delete a folder as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-folder).
The method accepts folderPath as an options that has to be deleted.

```python
result = imagekit.delete_folder(options={"folder_path": "/test/demo"})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
```

**18. Copy Folder**

Copy a folder as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/copy-folder).
The method accepts sourceFolderPath, destinationPath of a folder and includeFileVersions boolean as an options that
has to be copied.

```python
result = imagekit.copy_folder(options={"source_folder_path": "/source_folder_path",
                                       "destination_path": "/destination/path",
                                       "include_file_versions": True})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the job's id
print(result.job_id)
```

**19. Move Folder**

Move a folder as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/move-folder).
The method accepts sourceFolderPath and destinationPath of a folder as an options that has to be moved.

```python
result = imagekit.move_folder(options={"source_folder_path": "/source_folder_path",
                                       "destination_path": "/destination_path"})
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the job's id
print(result.job_id)
```

**20. Get Bulk Job Status**

Accepts the jobId to get bulk job status as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/copy-move-folder-status).
The method accepts only jobId.

```python
result = imagekit.get_bulk_job_status("job_id")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the job's id
print(result.job_id)
# print the status
print(result.status)
```

**21. Purge Cache**

Programmatically issue a cache clear request as per
the [API documentation here](https://docs.imagekit.io/api-reference/media-api/purge-cache).
Accepts the full URL of the file for which the cache has to be cleared.

```python
result = imagekit.purge_file_cache("full_url")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the purge file cache request id
print(result.request_id)
```

**22. Purge Cache Status**

Get the purge cache request status using the request ID returned when a purge cache request gets submitted as per the
[API documentation here](https://docs.imagekit.io/api-reference/media-api/purge-cache-status)

```python
result = imagekit.get_purge_file_cache_status("cache_request_id")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the purge file cache status
print(result.status)
```

**23. Get File Metadata**

Accepts the file ID and fetches the metadata as per
the [API documentation here](https://docs.imagekit.io/api-reference/metadata-api/get-image-metadata-for-uploaded-media-files)

```python
result = imagekit.get_file_metadata("file_id")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the file metadata fields
print(result.width)
print(result.exif.image.x_resolution)
```

**24. Get File Metadata from remote url**

Accepts the remote file url and fetches the metadata as per
the [API documentation here](https://docs.imagekit.io/api-reference/metadata-api/get-image-metadata-from-remote-url)

```python
result = imagekit.get_remote_file_url_metadata("remote_file_url")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the file metadata fields
print(result.width)
print(result.exif.image.x_resolution)
```

**25. Create CustomMetaDataFields**

Accepts an options specifying the parameters to be used to create cusomMetaDataFields. All parameters specified in
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/create-custom-metadata-field)
can be passed as it is with the correct values to get the results.

Check for
the [Allowed Values In The Schema](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/create-custom-metadata-field#allowed-values-in-the-schema-object)
.

**Example:**

```python
result = imagekit.create_custom_metadata_fields(options={"name": "test",
                                                         "label": "test",
                                                         "schema":
                                                             {"type": "Number",
                                                              "min_value": 100,
                                                              "max_value": 200}
                                                         }
                                                )
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the id of created custom metadata fields
print(result.id)
# print the schema's type of created custom metadata fields
print(result.schema.type)
```

**MultiSelect type Example:**

```python
result = imagekit.create_custom_metadata_fields(options={"name": "test-MultiSelect",
                                                         "label": "test-MultiSelect",
                                                         "schema":
                                                             {
                                                                 "type": "MultiSelect",
                                                                 "is_value_required": True,
                                                                 "default_value": ["small", 30, True],
                                                                 "select_options": ["small", "medium", "large", 30, 40,
                                                                                    True]
                                                             }
                                                         }
                                                )
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the name of created custom metadata fields
print(result.name)
# print the schema's select options of created custom metadata fields
print(result.schema.select_options)
```

**Date type Example:**

```python
result = imagekit.create_custom_metadata_fields(options={"name": "test-date",
                                                         "label": "test-date",
                                                         "schema":
                                                             {
                                                                 "type": "Date",
                                                                 "min_value": "2022-11-29T10:11:10+00:00",
                                                                 "max_value": "2022-11-30T10:11:10+00:00"}
                                                         }
                                                )
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the label of created custom metadata fields
print(result.label)
# print the schema's min value of created custom metadata fields
print(result.schema.min_value)
```

**26. Get CustomMetaDataFields**

Accepts the includeDeleted boolean and fetches the metadata as per
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/get-custom-metadata-field)
.

```python
result = imagekit.get_custom_metadata_fields()  # in this case, it will consider includeDeleted as a False
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the first customMetadataField's id
print(result.list[0].id)
# print the first customMetadataField schema's type
print(result.list[0].schema.type)
```

```python
result = imagekit.get_custom_metadata_fields(True)
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the first customMetadataField's name
print(result.list[0].name)
# print the first customMetadataField schema's default value
print(result.list[0].schema.default_value)
```

**27. Update CustomMetaDataFields**

Accepts an ID of customMetaDataField and options for specifying the parameters to be used to edit customMetaDataFields
as per
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/update-custom-metadata-field)
.

```python
result = imagekit.update_custom_metadata_fields("id_of_custom_metadata_field", options={"label": "test-update",
                                                                                        "schema":
                                                                                            {
                                                                                                "min_value": 100,
                                                                                                "max_value": 200
                                                                                            }
                                                                                        }
                                                )
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
# print the label of updated custom metadata fields
print(result.label)
# print the schema's min value of updated custom metadata fields
print(result.schema.min_value)
```

**28. Delete CustomMetaDataFields**

Accepts the id to delete the customMetaDataFields as per
the [API documentation here](https://docs.imagekit.io/api-reference/custom-metadata-fields-api/delete-custom-metadata-field)
.

```python
result = imagekit.delete_custom_metadata_field("id_of_custom_metadata_field")
print("======FINAL RESULT=======")
print("-------------------------------------")
print(result)
print("Raw Response:")
print(result.response_metadata.raw)
```

## Utility functions

We have included the following commonly used utility functions in this package.

**Authentication parameter generation**

In case you are looking to implement client-side file upload, you are going to need a token, expiry timestamp
, and a valid signature for that upload. The SDK provides a simple method that you can use in your code to generate
these
authentication parameters for you.

<em>Note: The Private API Key should never be exposed in any client-side code. You must always generate these
authentications parameters on the server-side</em>

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

Both the `token` and `expire` parameters are optional. If not specified, the SDK uses the UUID to generate a random
token and also generates a valid expiry timestamp internally. The value of the token and expire used to generate the
signature are always returned in the response, no matter if they are provided as an input to this method or not.

**Distance calculation between two pHash values**

Perceptual hashing allows you to construct a has value that uniquely identifies an input image based on the contents
of an image. [imagekit.io metadata API](https://docs.imagekit.io/api-reference/metadata-api) returns the pHash
value of an image in the response. You can use this value
to [find a duplicate or similar image](https://docs.imagekit.io/api-reference/metadata-api#using-phash-to-find-similar-or-duplicate-images)
by calculating the distance between the two images.

This SDK exposes phash_distance function to calculate the distance between two pHash value. It accepts two pHash
hexadecimal
strings and returns a numeric value indicative of the level of difference between the two images.

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

```python
imagekit.phash_distance('f06830ca9f1e3e90', 'f06830ca9f1e3e90')
# output: 0 (ame image)

imagekit.phash_distance('2d5ad3936d2e015b', '2d6ed293db36a4fb')
# output: 17 (similar images)

imagekit.phash_distance('a4a65595ac94518b', '7838873e791f8400')
# output: 37 (dissimilar images)
```

**HTTP response metadata of Internal API**

HTTP response metadata of the internal API call can be accessed using the response_metadata on the Result object.
Example:

```python
result = imagekit.upload_file(
    file="<url|base_64|binary>",
    file_name="my_file_name.jpg",
)
print("======FINAL RESULT=======")
print(result)
print(result.response_metadata.raw)
print(result.response_metadata.http_status_code)
print(result.response_metadata.headers)
```

### Sample Code Instruction

To run `sample` code go to the code samples here are hosted on Github - https://github.com/imagekit-samples/quickstart/tree/master/python and run

```shell
python sample.py
```

## Handling errors

Catch and respond to invalid data, internal problems, and more.

Imagekit Python SDK raise exceptions for many reasons, such as not found, invalid parameters, authentication errors, and
internal server error. We recommend writing code that gracefully handles all possible API exceptions.

#### Example:

```python
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
except BadRequestException as e:
    # Missing or Invalid parameters were supplied to Imagekit.io's API
    print("Status is: " + e.response_metadata.http_status_code)
    print("Message is: " + e.message)
    print("Headers are: " + e.response_metadata.headers)
    print("Raw body is: " + e.response_metadata.raw)
except UnauthorizedException as e:
# No valid API key was provided.
except ForbiddenException as e:
# Can be for the following reasons:
# ImageKit could not authenticate your account with the keys provided.
# An expired key (public or private) was used with the request.
# The account is disabled.
# If you are using the upload API, the total storage limit (or upload limit) is exceeded.
except TooManyRequestsException as e:
# Too many requests made to the API too quickly
except InternalServerException as e:
# Something went wrong with ImageKit.io API.
except PartialSuccessException as e:
# Error cases on partial success.
except NotFoundException as e:
# If any of the field or parameter is not found in data
except UnknownException as e:
# Something else happened, which can be unrelated to imagekit, reason will be indicated in the message field
```

## Support

For any feedback or to report any issues or general implementation support, please reach out
to [support@imagekit.io](https://github.com/imagekit-developer/imagekit-python)

## Links

* [Documentation](https://docs.imagekit.io/)

* [Main Website](https://imagekit.io/)

## License

Released under the MIT license.

