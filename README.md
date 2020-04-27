# Python SDK for ImageKit

[![Python CI](<https://github.com/imagekit-developer/imagekit-python/workflows/Python%20CI/badge.svg>)](https://github.com/imagekit-developer/imagekit-python/)
[![imagekitio](<https://img.shields.io/pypi/v/imagekitio.svg>)](https://pypi.org/project/imagekitio)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Twitter Follow](https://img.shields.io/twitter/follow/imagekitio?label=Follow&style=social)](https://twitter.com/ImagekitIo)

Python SDK for [ImageKit](https://imagekit.io/) that implements the new APIs and interface for performing different file
operations.

ImageKit is a complete image optimization and transformation solution that comes with and
[image CDN](https://imagekit.io/features/imagekit-infrastructure) and media storage. It can be integrated with your
existing infrastructure - storages like AWS s3, web servers, your CDN and custom domain names, allowing you to deliver
optimize images in minutes with minimal code changes.

Table of contents -
 * [Installation](#Installation)
 * [Initialization](#Initialization)
 * [URL Generation](#URL-generation)
 * [File Upload](#File-Upload)
 * [File Management](#File-Management)
 * [Utility Functions](#Utility-functions)
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
    private_key='your private_key',
    public_key='your public_key',
    url_endpoint = 'your url_endpoint'
)
```

## Usage

You can use this Python SDK for 3 different kinds of methods - URL generation, file upload and file management.
The usage of the SDK has been explained below

## URL generation

**1. Using Image path and image hostname or endpoint**

This method allows you to create a URL using the path where the image exists and the URL
endpoint(url_endpoint) you want to use to access the image. You can refer to the documentation
[here](https://docs.imagekit.io/integration/url-endpoints) to read more about URL endpoints
in ImageKit and the section about [image origins](https://docs.imagekit.io/integration/configure-origin) to understand
about paths with different kinds of origins.


```python
imagekit_url = imagekit.url({
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/your_imagekit_id/endpoint/",
            "transformation": [{"height": "300", "width": "400"}],
        }
)
```

The result in a URL like
```
https://ik.imagekit.io/your_imagekit_id/endpoint/tr:h-300,w-400/default-image.jpg
```

**2.Using full image URL**
This method allows you to add transformation parameters to and existing, complete URL that is already mapped to ImageKit
using ```src``` parameter. This method should be used if you have the complete image URL mapped to ImageKit stored in your
database.


```python
image_url = imagekit.url({
    "src": "https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg",
    "transformation" : [{
        "height": "300",
        "width": "400"
    }]
})
```

The results in a URL like

```
https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300%2Cw-400
```


The ```.url()``` method accepts the following parameters

| Option                  | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :---------------------- | :---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| url_endpoint            | Optional. The base URL to be appended before the path of the image. If not specified, the URL Endpoint specified at the time of SDK initialization is used. For example, https://ik.imagekit.io/your_imagekit_id/endpoint/                                                                                                                                                                                                                                                                                                                                                                |
| path                    | Conditional. This is the path at which the image exists. For example, `/path/to/image.jpg`. Either the `path` or `src` parameter need to be specified for URL generation.                                                                                                                                                                                                                                                                                                                                                                                                                 |
| src                     | Conditional. This is the complete URL of an image already mapped to ImageKit. For example, `https://ik.imagekit.io/your_imagekit_id/endpoint/path/to/image.jpg`. Either the `path` or `src` parameter need to be specified for URL generation.                                                                                                                                                                                                                                                                                                                                            |
| transformation          | Optional. An array of objects specifying the transformation to be applied in the URL. The transformation name  and the value should be specified as a key-value pair in the object. Different steps of a [chained transformation](https://docs.imagekit.io/features/image-transformations/chained-transformations) can be specified as different objects of the array. The complete list of supported transformations in the SDK and some examples of using them are given later. If you use a transformation name that is not specified in the SDK, it gets applied as it is in the URL. |
| transformation_position | Optional. Default value is `path` that places the transformation string as a path parameter in the URL. Can also be specified as `query` which adds the transformation string as the query parameter `tr` in the URL. If you use `src` parameter to create the URL, then the transformation string is always added as a query parameter.                                                                                                                                                                                                                                                  |
| query_parameters        | Optional. These are the other query parameters that you want to add to the final URL. These can be any query parameters and not necessarily related to ImageKit. Especially useful, if you want to add some versioning parameter to your URLs.                                                                                                                                                                                                                                                                                                                                            |
| signed                  | Optional. Boolean. Default is `false`. If set to `true`, the SDK generates a signed image URL adding the image signature to the image URL. This can only be used if you are creating the URL with the `url_endpoint` and `path` parameters, and not with the `src` parameter.                                                                                                                                                                                                                                                                                                             |
| expire_seconds          | Optional. Integer. Meant to be used along with the `signed` parameter to specify the time in seconds from now when the URL should expire. If specified, the URL contains the expiry timestamp in the URL and the image signature is modified accordingly.                                                                                                                                                                                                                                                                                                                                 |


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
        "transformation_position ": "query"
    })
```
Sample Result URL -
```
https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=h-300%2Cw-400%3Art-90
```



**2. Sharpening and contrast transforms and a progressive JPG image**

There are some transforms like [Sharpening](https://docs.imagekit.io/features/image-transformations/image-enhancement-and-color-manipulation)
that can be added to the URL with or without any other value. To use such transforms without specifying a value, specify
the value as "-" in the transformation object, otherwise, specify the value that you want to be
added to this transformation.


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

```
//Note that because `src` parameter was used, the transformation string gets added as a query parameter `tr`
https://ik.imagekit.io/your_imagekit_id/endpoint/default-image.jpg?tr=f-jpg%2Cpr-true%2Ce-sharpen%2Ce-contrast-1
```

**3. Signed URL that expires in 300 seconds with the default URL endpoint and other query parameters**

```python
    image_url = imagekit.url({
        "path": "/default-image",
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
https://ik.imagekit.io/your_imagekit_id/tr:h-300,w-400/default-image.jpg?v=123&ik-t=1567358667&ik-s=f2c7cdacbe7707b71a83d49cf1c6110e3d701054
```

**List of transformations**

The complete list of transformations supported and their usage in ImageKit can be found [here](https://docs.imagekit.io/features/image-transformations/resize-crop-and-other-transformations).
The SDK gives a name to each transformation parameter, making the code simpler, making the code simpler and readable.
If a transformation is supported in ImageKit, but a name for it cannot be found in the table below, then use the
transformation code from ImageKit docs as the name when using in the ```url``` function.

| Supported Transformation Name | Translates to parameter |
| ----------------------------- | ----------------------- |
| height                        | h                       |
| width                         | w                       |
| aspect_ratio                  | ar                      |
| quality                       | q                       |
| crop                          | c                       |
| crop_mode                     | cm                      |
| x                             | x                       |
| y                             | y                       |
| focus                         | fo                      |
| format                        | f                       |
| radius                        | r                       |
| background                    | bg                      |
| border                        | bo                      |
| rotation                      | rt                      |
| blur                          | bl                      |
| named                         | n                       |
| overlay_image                 | oi                      |
| overlay_x                     | ox                      |
| overlay_y                     | oy                      |
| overlay_focus                 | ofo                     |
| overlay_height                | oh                      |
| overlay_width                 | ow                      |
| overlay_text                  | ot                      |
| overlay_text_font_size        | ots                     |
| overlay_text_font_family      | otf                     |
| overlay_text_color            | otc                     |
| overlay_alpha                 | oa                      |
| overlay_text_typography       | ott                     |
| overlay_background            | obg                     |
| overlay_image_trim            | oit                     |
| progressive                   | pr                      |
| lossless                      | lo                      |
| trim                          | t                       |
| metadata                      | md                      |
| color_profile                 | cp                      |
| default_image                 | di                      |
| dpr                           | dpr                     |
| effect_sharpen                | e-sharpen               |
| effect_usm                    | e-usm                   |
| effect_contrast               | e-contrast              |
| effect_gray                   | e-grayscale             |
| original                      | orig                    |

## File Upload

The SDK provides a simple interface using the `.upload_file()` method to upload files to the ImageKit Media library. It
accepts all the parameters supported by the [ImageKit Upload API](https://docs.imagekit.io/api-reference/upload-file-api/server-side-file-upload).

The `upload_file()` method requires at least the `file` and the `file_name` parameter to upload a file and returns a Dict with error or success data. Use `options` parameter to pass other parameters supported by the [ImageKit Upload API](https://docs.imagekit.io/api-reference/upload-file-api/server-side-file-upload). Use the same parameter name as specified in the upload API documentation.

Simple usage

```python
imagekit.upload_file(
    file= "<url|base_64|binary>", # required
    file_name= "my_file_name.jpg", # required
    options= {
        "folder" : "/example-folder/",
        "tags": ["sample-tag"],
        "is_private_file": False,
        "use_unique_file_name": True,
        "response_fields": ["is_private_file", "tags"],
    }
)

```

If the upload succeed, `error` will be `null` and the `result` will be the same as what is received from ImageKit's servers.
If the upload fails, `error` will be the same as what is received from ImageKit's servers and the `result` will be null. Learn more from the sample app in this repository.

## File Management

The SDK provides a simple interface for all the [media APIs mentioned here](https://docs.imagekit.io/api-reference/media-api)
to manage your files. This also returns `error` and `result`, error will be `None` if API succeeds.

**1. List & Search Files**

Accepts an object specifying the parameters to be used to list and search files. All parameters specified
in the [documentation here](https://docs.imagekit.io/api-reference/media-api/list-and-search-files#list-and-search-file-api) can be passed as is with the
correct values to get the results.

```python
    imagekit.list_files({
        "skip": 10,
        "limit": 10,
}
    )
```
**2. Get File Details**
Accepts the file ID and fetches the details as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/get-file-details)

```python
imagekit.get_file_details(file_id)
```

**3. Get File Metadata**
Accepts the file ID and fetches the metadata as per the [API documentation here](https://docs.imagekit.io/api-reference/metadata-api/get-image-metadata-for-uploaded-media-files)
```python
imagekit.get_file_metadata(file_id)
```


**3. Get File Metadata from remote url**
Accepts the remote file url and fetches the metadata as per the [API documentation here](https://docs.imagekit.io/api-reference/metadata-api/get-image-metadata-from-remote-url)

```python
imagekit.get_remote_file_url_metadata(remote_file_url)
```

**4. Update File Details**
Update parameters associated with the file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/update-file-details).
The first argument to the `update_field_details` method is the file ID and the second argument is an object with the
parameters to be updated.

```python
imagekit.update_file_details("file_id", {
    "tags": ["image_tag"],
    "custom_coordinates": "10,10,100, 100"
})
```

**6. Delete File**
Delete a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-file). The method accepts the file ID of the file that has to be
deleted.

```python
imagekit.delete_file(file_id)
```

**6. Bulk File Delete by IDs**
Delete a file as per the [API documentation here](https://docs.imagekit.io/api-reference/media-api/delete-files-bulk). The method accepts list of file IDs of  files that has to be
deleted.

```python
imagekit.bulk_file_delete(["file_id1", "file_id2"])
```

**6. Purge Cache**
Programmatically issue a cache clear request as clear request as pet the [API documentation here](https://docs.imagekit.io/api-reference/media-api/purge-cache).
Accepts the full URL of the file for which the cache has to be cleared.
```python
imagekit.purge_file_cache(full_url)
```
**7. Purge Cache Status**

Get the purge cache request status using the request ID returned when a purge cache request gets submitted as pet the
[API documentation here](https://docs.imagekit.io/api-reference/media-api/purge-cache-status)

```python
imagekit.get_purge_file_cache_status(cache_request_id)
```


## Utility functions

We have included following commonly used utility functions in this package.

**Authentication parameter generation**

In case you are looking to implement client-side file upload, you are going to need a token, expiry timestamp
and a valid signature for that upload. The SDK provides a simple method that you can use in your code to generate these
authentication parameters for you.

<em>Note: The Private API Key should never be exposed in any client-side code. You must always generate these authentication
 parameters on the server-side</em>

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

Both the `token` and `expire` parameters are optional. If not specified the SDK uses the uuid to generate a random
token and also generates a valid expiry timestamp internally. The value of the token and expire used to generate the
signature are always returned in the response, no matter if they are provided as an input to this method or not.

**Distance calculation between two pHash values**

Perceptual hashing allows you to constructing a has value that uniquely identifies an input image based on the contents
of an image. [imagekit.io metadata API](https://docs.imagekit.io/api-reference/metadata-api) returns the pHash
value of an image in the response. You can use this value to find duplicate, near duplicate(similar) image by calculating
distance between the two images.


This SDK exposes phash_distance function to calculate distance between two pHash value. It accepts two pHash hexadecimal
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

### Sample Code Instruction
To run `sample` code go to sample directory and run
```python
python sample.py
```
## Support
For any feedback or to report any issues or general implementation support please reach out to [support@imagekit.io]()


## Links

* [Documentation](https://docs.imagekit.io/)

* [Main Website](https://imagekit.io/)


## License
Released under the MIT license.

