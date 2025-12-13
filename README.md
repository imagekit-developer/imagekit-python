# ImageKit.io Python SDK

<!-- prettier-ignore -->
[![PyPI version](https://img.shields.io/pypi/v/imagekitio.svg?label=pypi%20(stable))](https://pypi.org/project/imagekitio/)

The ImageKit Python SDK provides convenient access to the ImageKit REST API from any Python 3.9+ application. It offers powerful tools for URL generation and transformation, signed URLs for secure content delivery, webhook verification, file uploads, and more. The library includes type definitions for all request params and response fields, and offers both synchronous and asynchronous clients powered by [httpx](https://github.com/encode/httpx).

The REST API documentation can be found on [imagekit.io](https://imagekit.io/docs/api-reference). The full API of this library can be found in [api.md](api.md).

## Table of Contents

- [Installation](#installation)
- [Requirements](#requirements)
- [Usage](#usage)
  - [Using types](#using-types)
  - [Nested params](#nested-params)
  - [Async usage](#async-usage)
- [URL generation](#url-generation)
  - [Basic URL generation](#basic-url-generation)
  - [URL generation with transformations](#url-generation-with-transformations)
  - [URL generation with image overlay](#url-generation-with-image-overlay)
  - [URL generation with text overlay](#url-generation-with-text-overlay)
  - [URL generation with multiple overlays](#url-generation-with-multiple-overlays)
  - [Signed URLs for secure delivery](#signed-urls-for-secure-delivery)
  - [Using Raw transformations for undocumented features](#using-raw-transformations-for-undocumented-features)
- [Authentication parameters for client-side uploads](#authentication-parameters-for-client-side-uploads)
- [Webhook verification](#webhook-verification)
- [Advanced Usage](#advanced-usage)
  - [File uploads](#file-uploads)
  - [Handling errors](#handling-errors)
  - [Retries](#retries)
  - [Timeouts](#timeouts)
  - [Logging](#logging)
  - [Accessing raw response data](#accessing-raw-response-data-eg-headers)
  - [Making custom/undocumented requests](#making-customundocumented-requests)
  - [Configuring the HTTP client](#configuring-the-http-client)
  - [Managing HTTP resources](#managing-http-resources)
- [Versioning](#versioning)
- [Contributing](#contributing)

## Installation

```sh
# install from PyPI
pip install imagekitio
```

## Usage

The full API of this library can be found in [api.md](api.md).

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),  # This is the default and can be omitted
)

# Upload a file
with open("/path/to/your/image.jpg", "rb") as f:
    file_data = f.read()

response = client.files.upload(
    file=file_data,
    file_name="uploaded-image.jpg",
)
print(response.file_id)
print(response.url)
```

While you can provide a `private_key` keyword argument,
we recommend using [python-dotenv](https://pypi.org/project/python-dotenv/)
to add `IMAGEKIT_PRIVATE_KEY="My Private Key"` to your `.env` file
so that your Private Key is not stored in source control.


### Using types

Nested request parameters are [TypedDicts](https://docs.python.org/3/library/typing.html#typing.TypedDict). Responses are [Pydantic models](https://docs.pydantic.dev) which also provide helper methods for things like:

- Serializing back into JSON, `model.to_json()`
- Converting to a dictionary, `model.to_dict()`

Typed requests and responses provide autocomplete and documentation within your editor. If you would like to see type errors in VS Code to help catch bugs earlier, set `python.analysis.typeCheckingMode` to `basic`.

### Nested params

Nested parameters are dictionaries, typed using `TypedDict`, for example:

```python
from imagekitio import ImageKit

client = ImageKit()

# Read file into memory and upload
with open("/path/to/file.jpg", "rb") as f:
    file_data = f.read()

response = client.files.upload(
    file=file_data,
    file_name="fileName",
    transformation={
        "post": [
            {
                "type": "thumbnail",
                "value": "w-150,h-150",
            },
            {
                "protocol": "dash",
                "type": "abs",
                "value": "sr-240_360_480_720_1080",
            },
        ]
    },
)
print(response.file_id)
```

### Async usage

Simply import `AsyncImageKit` instead of `ImageKit` and use `await` with each API call:

```python
import os
import asyncio
from imagekitio import AsyncImageKit

client = AsyncImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),  # This is the default and can be omitted
)


async def main() -> None:
    # Read file into memory and upload
    with open("/path/to/your/image.jpg", "rb") as f:
        file_data = f.read()
    
    response = await client.files.upload(
        file=file_data,
        file_name="file-name.jpg",
    )
    print(response.file_id)
    print(response.url)


asyncio.run(main())
```

Functionality between the synchronous and asynchronous clients is otherwise identical.

#### With aiohttp

By default, the async client uses `httpx` for HTTP requests. However, for improved concurrency performance you may also use `aiohttp` as the HTTP backend.

You can enable this by installing `aiohttp`:

```sh
# install from PyPI
pip install imagekitio[aiohttp]
```

Then you can enable it by instantiating the client with `http_client=DefaultAioHttpClient()`:

```python
import os
import asyncio
from imagekitio import DefaultAioHttpClient
from imagekitio import AsyncImageKit


async def main() -> None:
    async with AsyncImageKit(
        private_key=os.environ.get(
            "IMAGEKIT_PRIVATE_KEY"
        ),  # This is the default and can be omitted
        http_client=DefaultAioHttpClient(),
    ) as client:
        # Read file into memory and upload
        with open("/path/to/your/image.jpg", "rb") as f:
            file_data = f.read()
        
        response = await client.files.upload(
            file=file_data,
            file_name="file-name.jpg",
        )
        print(response.file_id)
        print(response.url)


asyncio.run(main())
```

## URL generation

The ImageKit SDK provides a powerful `helper.build_url()` method for generating optimized image and video URLs with transformations. Here are examples ranging from simple URLs to complex transformations with overlays and signed URLs.

### Basic URL generation

Generate a simple URL without any transformations:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# Basic URL without transformations
url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/path/to/image.jpg",
)
print(url)
# Result: https://ik.imagekit.io/your_imagekit_id/path/to/image.jpg
```

### URL generation with transformations

Apply common transformations like resizing, cropping, and format conversion:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# URL with basic transformations
url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/path/to/image.jpg",
    transformation=[
        {
            "width": 400,
            "height": 300,
            "crop": "maintain_ratio",
            "quality": 80,
            "format": "webp",
        }
    ],
)
print(url)
# Result: https://ik.imagekit.io/your_imagekit_id/path/to/image.jpg?tr=w-400,h-300,c-maintain_ratio,q-80,f-webp
```

### URL generation with image overlay

Add image overlays to your base image:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# URL with image overlay
url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/path/to/base-image.jpg",
    transformation=[
        {
            "width": 500,
            "height": 400,
            "overlay": {
                "type": "image",
                "input": "/path/to/overlay-logo.png",
                "position": {
                    "x": 10,
                    "y": 10,
                },
                "transformation": [
                    {
                        "width": 100,
                        "height": 50,
                    }
                ],
            },
        }
    ],
)
print(url)
# Result: URL with image overlay positioned at x:10, y:10
```

### URL generation with text overlay

Add customized text overlays:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# URL with text overlay
url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/path/to/base-image.jpg",
    transformation=[
        {
            "width": 600,
            "height": 400,
            "overlay": {
                "type": "text",
                "text": "Sample Text Overlay",
                "position": {
                    "x": 50,
                    "y": 50,
                    "focus": "center",
                },
                "transformation": [
                    {
                        "font_size": 40,
                        "font_family": "Arial",
                        "font_color": "FFFFFF",
                        "typography": "b",  # bold
                    }
                ],
            },
        }
    ],
)
print(url)
# Result: URL with bold white Arial text overlay at center position
```

### URL generation with multiple overlays

Combine multiple overlays for complex compositions:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# URL with multiple overlays (text + image)
url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/path/to/base-image.jpg",
    transformation=[
        {
            "width": 800,
            "height": 600,
            "overlay": {
                "type": "text",
                "text": "Header Text",
                "position": {
                    "x": 20,
                    "y": 20,
                },
                "transformation": [
                    {
                        "font_size": 30,
                        "font_color": "000000",
                    }
                ],
            },
        },
        {
            "overlay": {
                "type": "image",
                "input": "/watermark.png",
                "position": {
                    "focus": "bottom_right",
                },
                "transformation": [
                    {
                        "width": 100,
                        "opacity": 70,
                    }
                ],
            },
        },
    ],
)
print(url)
# Result: URL with text overlay at top-left and semi-transparent watermark at bottom-right
```

### Signed URLs for secure delivery

Generate signed URLs that expire after a specified time for secure content delivery:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# Generate a signed URL that expires in 1 hour (3600 seconds)
url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/private/secure-image.jpg",
    transformation=[
        {
            "width": 400,
            "height": 300,
            "quality": 90,
        }
    ],
    signed=True,
    expires_in=3600,  # URL expires in 1 hour
)
print(url)
# Result: URL with signature parameters (?ik-t=timestamp&ik-s=signature)

# Generate a signed URL that doesn't expire
permanent_signed_url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/private/secure-image.jpg",
    signed=True,
    # No expires_in means the URL won't expire
)
print(permanent_signed_url)
# Result: URL with signature parameter (?ik-s=signature)
```

### Using Raw transformations for undocumented features

ImageKit frequently adds new transformation parameters that might not yet be documented in the SDK. You can use the `raw` parameter to access these features or create custom transformation strings:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# Using Raw transformation for undocumented or new parameters
url = client.helper.build_url(
    url_endpoint="https://ik.imagekit.io/your_imagekit_id",
    src="/path/to/image.jpg",
    transformation=[
        {
            # Combine documented transformations with raw parameters
            "width": 400,
            "height": 300,
        },
        {
            # Use raw for undocumented transformations or complex parameters
            "raw": "something-new",
        },
    ],
)
print(url)
# Result: https://ik.imagekit.io/your_imagekit_id/path/to/image.jpg?tr=w-400,h-300:something-new
```

## Authentication parameters for client-side uploads

Generate authentication parameters for secure client-side file uploads:

```python
import os
from imagekitio import ImageKit

client = ImageKit(
    private_key=os.environ.get("IMAGEKIT_PRIVATE_KEY"),
)

# Generate authentication parameters for client-side uploads
auth_params = client.helper.get_authentication_parameters()
print(auth_params)
# Result: {'expire': <timestamp>, 'signature': '<hmac-signature>', 'token': '<uuid-token>'}

# Generate with custom token and expiry
custom_auth_params = client.helper.get_authentication_parameters(
    token="my-custom-token",
    expire=1800
)
print(custom_auth_params)
# Result: {'expire': 1800, 'signature': '<hmac-signature>', 'token': 'my-custom-token'}
```

These authentication parameters can be used in client-side upload forms to securely upload files without exposing your private API key.

## Webhook verification

The ImageKit SDK provides utilities to verify webhook signatures for secure event handling. This ensures that webhook requests are actually coming from ImageKit and haven't been tampered with.

For detailed information about webhook setup, signature verification, and handling different webhook events, refer to the [ImageKit webhook documentation](https://imagekit.io/docs/webhooks#verify-webhook-signature).

## Advanced Usage

### File uploads

Request parameters that correspond to file uploads can be passed as `bytes`, a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, an `IO[bytes]` file object, or a tuple of `(filename, contents, media type)`.

Here are common file upload patterns:

```python
from pathlib import Path
from imagekitio import ImageKit
import io

client = ImageKit()

# Method 1: Upload from bytes
# Read file into memory first, then upload
with open("/path/to/your/image.jpg", "rb") as f:
    file_data = f.read()

response = client.files.upload(
    file=file_data,
    file_name="uploaded-image.jpg",
)

# Method 2: Upload from file stream (for large files)
# Pass file object directly - SDK reads it
with open("/path/to/your/image.jpg", "rb") as file_stream:
    response = client.files.upload(
        file=file_stream,
        file_name="uploaded-image.jpg",
    )

# Method 3: Upload using Path object (SDK reads automatically)
response = client.files.upload(
    file=Path("/path/to/file.jpg"),
    file_name="fileName.jpg",
)

# Method 4: Upload from BytesIO (for programmatically generated content)
content = b"your binary data"
bytes_io = io.BytesIO(content)
response = client.files.upload(
    file=bytes_io,
    file_name="binary-upload.jpg",
)

# Method 5: Upload with custom content type using tuple format
image_data = b"your binary data"
response = client.files.upload(
    file=("custom.jpg", image_data, "image/jpeg"),
    file_name="custom-upload.jpg",
)
```

The async client uses the exact same interface. If you pass a [`PathLike`](https://docs.python.org/3/library/os.html#os.PathLike) instance, the file contents will be read asynchronously automatically.

**Note:** URL strings (e.g., `"https://example.com/image.jpg"`) are not supported by the Python SDK. To upload from a URL, download the content first:

```python
import urllib.request

# Download from URL and upload to ImageKit
url = "https://example.com/image.jpg"
with urllib.request.urlopen(url) as response:
    url_content = response.read()

# Upload the downloaded content
upload_response = client.files.upload(
    file=url_content,
    file_name="downloaded-image.jpg",
)
```

### Handling errors

When the library is unable to connect to the API (for example, due to network connection problems or a timeout), a subclass of `imagekitio.APIConnectionError` is raised.

When the API returns a non-success status code (that is, 4xx or 5xx
response), a subclass of `imagekitio.APIStatusError` is raised, containing `status_code` and `response` properties.

All errors inherit from `imagekitio.APIError`.

```python
import imagekitio
from imagekitio import ImageKit

client = ImageKit()

try:
    # Read file into memory and upload
    with open("/path/to/your/image.jpg", "rb") as f:
        file_data = f.read()
    
    response = client.files.upload(
        file=file_data,
        file_name="file-name.jpg",
    )
except imagekitio.APIConnectionError as e:
    print("The server could not be reached")
    print(e.__cause__)  # an underlying Exception, likely raised within httpx.
except imagekitio.RateLimitError as e:
    print("A 429 status code was received; we should back off a bit.")
except imagekitio.APIStatusError as e:
    print("Another non-200-range status code was received")
    print(e.status_code)
    print(e.response)
```

Error codes are as follows:

| Status Code | Error Type                 |
| ----------- | -------------------------- |
| 400         | `BadRequestError`          |
| 401         | `AuthenticationError`      |
| 403         | `PermissionDeniedError`    |
| 404         | `NotFoundError`            |
| 422         | `UnprocessableEntityError` |
| 429         | `RateLimitError`           |
| >=500       | `InternalServerError`      |
| N/A         | `APIConnectionError`       |

### Retries

Certain errors are automatically retried 2 times by default, with a short exponential backoff.
Connection errors (for example, due to a network connectivity problem), 408 Request Timeout, 409 Conflict,
429 Rate Limit, and >=500 Internal errors are all retried by default.

You can use the `max_retries` option to configure or disable retry settings:

```python
from imagekitio import ImageKit

# Configure the default for all requests:
client = ImageKit(
    # default is 2
    max_retries=0,
)

# Or, configure per-request:
with open("/path/to/your/image.jpg", "rb") as f:
    file_data = f.read()

client.with_options(max_retries=5).files.upload(
    file=file_data,
    file_name="file-name.jpg",
)
```

### Timeouts

By default requests time out after 1 minute. You can configure this with a `timeout` option,
which accepts a float or an [`httpx.Timeout`](https://www.python-httpx.org/advanced/timeouts/#fine-tuning-the-configuration) object:

```python
from imagekitio import ImageKit

# Configure the default for all requests:
client = ImageKit(
    # 20 seconds (default is 1 minute)
    timeout=20.0,
)

# More granular control:
client = ImageKit(
    timeout=httpx.Timeout(60.0, read=5.0, write=10.0, connect=2.0),
)

# Override per-request:
with open("/path/to/your/image.jpg", "rb") as f:
    file_data = f.read()

client.with_options(timeout=5.0).files.upload(
    file=file_data,
    file_name="file-name.jpg",
)
```

On timeout, an `APITimeoutError` is thrown.

Note that requests that time out are [retried twice by default](#retries).

### Logging

We use the standard library [`logging`](https://docs.python.org/3/library/logging.html) module.

You can enable logging by setting the environment variable `IMAGE_KIT_LOG` to `info`.

```shell
$ export IMAGE_KIT_LOG=info
```

Or to `debug` for more verbose logging.

### How to tell whether `None` means `null` or missing

In an API response, a field may be explicitly `null`, or missing entirely; in either case, its value is `None` in this library. You can differentiate the two cases with `.model_fields_set`:

```py
if response.my_field is None:
  if 'my_field' not in response.model_fields_set:
    print('Got json like {}, without a "my_field" key present at all.')
  else:
    print('Got json like {"my_field": null}.')
```

### Accessing raw response data (e.g. headers)

The "raw" Response object can be accessed by prefixing `.with_raw_response.` to any HTTP method call, e.g.,

```py
from imagekitio import ImageKit

client = ImageKit()

# Read file into memory and upload
with open("/path/to/your/image.jpg", "rb") as f:
    file_data = f.read()

response = client.files.with_raw_response.upload(
    file=file_data,
    file_name="file-name.jpg",
)
print(response.headers.get('X-My-Header'))

file = response.parse()  # get the object that `files.upload()` would have returned
print(file.file_id)
```

These methods return an [`APIResponse`](https://github.com/imagekit-developer/imagekit-python/tree/master/src/imagekitio/_response.py) object.

The async client returns an [`AsyncAPIResponse`](https://github.com/imagekit-developer/imagekit-python/tree/master/src/imagekitio/_response.py) with the same structure, the only difference being `await`able methods for reading the response content.

#### `.with_streaming_response`

The above interface eagerly reads the full response body when you make the request, which may not always be what you want.

To stream the response body, use `.with_streaming_response` instead, which requires a context manager and only reads the response body once you call `.read()`, `.text()`, `.json()`, `.iter_bytes()`, `.iter_text()`, `.iter_lines()` or `.parse()`. In the async client, these are async methods.

```python
# Read file into memory and upload
with open("/path/to/your/image.jpg", "rb") as f:
    file_data = f.read()

with client.files.with_streaming_response.upload(
    file=file_data,
    file_name="file-name.jpg",
) as response:
    print(response.headers.get("X-My-Header"))

    for line in response.iter_lines():
        print(line)
```

The context manager is required so that the response will reliably be closed.

### Making custom/undocumented requests

This library is typed for convenient access to the documented API.

If you need to access undocumented endpoints, params, or response properties, the library can still be used.

#### Undocumented endpoints

To make requests to undocumented endpoints, you can make requests using `client.get`, `client.post`, and other
http verbs. Options on the client will be respected (such as retries) when making this request.

```py
import httpx

response = client.post(
    "/foo",
    cast_to=httpx.Response,
    body={"my_param": True},
)

print(response.headers.get("x-foo"))
```

#### Undocumented request params

If you want to explicitly send an extra param, you can do so with the `extra_query`, `extra_body`, and `extra_headers` request
options.

#### Undocumented response properties

To access undocumented response properties, you can access the extra fields like `response.unknown_prop`. You
can also get all the extra fields on the Pydantic model as a dict with
[`response.model_extra`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_extra).

### Configuring the HTTP client

You can directly override the [httpx client](https://www.python-httpx.org/api/#client) to customize it for your use case, including:

- Support for [proxies](https://www.python-httpx.org/advanced/proxies/)
- Custom [transports](https://www.python-httpx.org/advanced/transports/)
- Additional [advanced](https://www.python-httpx.org/advanced/clients/) functionality

```python
import httpx
from imagekitio import ImageKit, DefaultHttpxClient

client = ImageKit(
    # Or use the `IMAGE_KIT_BASE_URL` env var
    base_url="http://my.test.server.example.com:8083",
    http_client=DefaultHttpxClient(
        proxy="http://my.test.proxy.example.com",
        transport=httpx.HTTPTransport(local_address="0.0.0.0"),
    ),
)
```

You can also customize the client on a per-request basis by using `with_options()`:

```python
client.with_options(http_client=DefaultHttpxClient(...))
```

### Managing HTTP resources

By default the library closes underlying HTTP connections whenever the client is [garbage collected](https://docs.python.org/3/reference/datamodel.html#object.__del__). You can manually close the client using the `.close()` method if desired, or with a context manager that closes when exiting.

```py
from imagekitio import ImageKit

with ImageKit() as client:
  # make requests here
  ...

# HTTP client is now closed
```

## Versioning

This package generally follows [SemVer](https://semver.org/spec/v2.0.0.html) conventions, though certain backwards-incompatible changes may be released as minor versions:

1. Changes that only affect static types, without breaking runtime behavior.
2. Changes to library internals which are technically public but not intended or documented for external use. _(Please open a GitHub issue to let us know if you are relying on such internals.)_
3. Changes that we do not expect to impact the vast majority of users in practice.

We take backwards-compatibility seriously and work hard to ensure you can rely on a smooth upgrade experience.

We are keen for your feedback; please open an [issue](https://www.github.com/imagekit-developer/imagekit-python/issues) with questions, bugs, or suggestions.

### Determining the installed version

If you've upgraded to the latest version but aren't seeing any new features you were expecting then your python environment is likely still using an older version.

You can determine the version that is being used at runtime with:

```py
import imagekitio
print(imagekitio.__version__)
```

## Requirements

Python 3.9 or higher.

## Contributing

See [the contributing documentation](./CONTRIBUTING.md).
