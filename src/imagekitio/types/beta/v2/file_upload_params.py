# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, List, Union, Iterable
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._types import FileTypes, SequenceNotStr
from ...._utils import PropertyInfo
from ...shared_params.extensions import Extensions

__all__ = [
    "FileUploadParams",
    "Transformation",
    "TransformationPost",
    "TransformationPostTransformation",
    "TransformationPostGifToVideo",
    "TransformationPostThumbnail",
    "TransformationPostAbs",
]


class FileUploadParams(TypedDict, total=False):
    file: Required[FileTypes]
    """The API accepts any of the following:

    - **Binary data** – send the raw bytes as `multipart/form-data`.
    - **HTTP / HTTPS URL** – a publicly reachable URL that ImageKit’s servers can
      fetch.
    - **Base64 string** – the file encoded as a Base64 data URI or plain Base64.

    When supplying a URL, the server must receive the response headers within 8
    seconds; otherwise the request fails with 400 Bad Request.
    """

    file_name: Required[Annotated[str, PropertyInfo(alias="fileName")]]
    """The name with which the file has to be uploaded."""

    token: str
    """This is the client-generated JSON Web Token (JWT).

    The ImageKit.io server uses it to authenticate and check that the upload request
    parameters have not been tampered with after the token has been generated. Learn
    how to create the token on the page below. This field is only required for
    authentication when uploading a file from the client side.

    **Note**: Sending a JWT that has been used in the past will result in a
    validation error. Even if your previous request resulted in an error, you should
    always send a new token.

    **⚠️Warning**: JWT must be generated on the server-side because it is generated
    using your account's private API key. This field is required for authentication
    when uploading a file from the client-side.
    """

    checks: str
    """
    Server-side checks to run on the asset. Read more about
    [Upload API checks](/docs/api-reference/upload-file/upload-file-v2#upload-api-checks).
    """

    custom_coordinates: Annotated[str, PropertyInfo(alias="customCoordinates")]
    """Define an important area in the image.

    This is only relevant for image type files.

    - To be passed as a string with the x and y coordinates of the top-left corner,
      and width and height of the area of interest in the format `x,y,width,height`.
      For example - `10,10,100,100`
    - Can be used with fo-customtransformation.
    - If this field is not specified and the file is overwritten, then
      customCoordinates will be removed.
    """

    custom_metadata: Annotated[Dict[str, object], PropertyInfo(alias="customMetadata")]
    """JSON key-value pairs to associate with the asset.

    Create the custom metadata fields before setting these values.
    """

    description: str
    """Optional text to describe the contents of the file."""

    extensions: Extensions
    """Array of extensions to be applied to the asset.

    Each extension can be configured with specific parameters based on the extension
    type.
    """

    folder: str
    """The folder path in which the image has to be uploaded.

    If the folder(s) didn't exist before, a new folder(s) is created. Using multiple
    `/` creates a nested folder.
    """

    is_private_file: Annotated[bool, PropertyInfo(alias="isPrivateFile")]
    """Whether to mark the file as private or not.

    If `true`, the file is marked as private and is accessible only using named
    transformation or signed URL.
    """

    is_published: Annotated[bool, PropertyInfo(alias="isPublished")]
    """Whether to upload file as published or not.

    If `false`, the file is marked as unpublished, which restricts access to the
    file only via the media library. Files in draft or unpublished state can only be
    publicly accessed after being published.

    The option to upload in draft state is only available in custom enterprise
    pricing plans.
    """

    overwrite_ai_tags: Annotated[bool, PropertyInfo(alias="overwriteAITags")]
    """
    If set to `true` and a file already exists at the exact location, its AITags
    will be removed. Set `overwriteAITags` to `false` to preserve AITags.
    """

    overwrite_custom_metadata: Annotated[bool, PropertyInfo(alias="overwriteCustomMetadata")]
    """
    If the request does not have `customMetadata`, and a file already exists at the
    exact location, existing customMetadata will be removed.
    """

    overwrite_file: Annotated[bool, PropertyInfo(alias="overwriteFile")]
    """
    If `false` and `useUniqueFileName` is also `false`, and a file already exists at
    the exact location, upload API will return an error immediately.
    """

    overwrite_tags: Annotated[bool, PropertyInfo(alias="overwriteTags")]
    """
    If the request does not have `tags`, and a file already exists at the exact
    location, existing tags will be removed.
    """

    response_fields: Annotated[
        List[
            Literal[
                "tags",
                "customCoordinates",
                "isPrivateFile",
                "embeddedMetadata",
                "isPublished",
                "customMetadata",
                "metadata",
                "selectedFieldsSchema",
            ]
        ],
        PropertyInfo(alias="responseFields"),
    ]
    """Array of response field keys to include in the API response body."""

    tags: SequenceNotStr[str]
    """Set the tags while uploading the file. Provide an array of tag strings (e.g.

    `["tag1", "tag2", "tag3"]`). The combined length of all tag characters must not
    exceed 500, and the `%` character is not allowed. If this field is not specified
    and the file is overwritten, the existing tags will be removed.
    """

    transformation: Transformation
    """Configure pre-processing (`pre`) and post-processing (`post`) transformations.

    - `pre` — applied before the file is uploaded to the Media Library.
      Useful for reducing file size or applying basic optimizations upfront (e.g.,
      resize, compress).

    - `post` — applied immediately after upload.
      Ideal for generating transformed versions (like video encodes or thumbnails)
      in advance, so they're ready for delivery without delay.

    You can mix and match any combination of post-processing types.
    """

    use_unique_file_name: Annotated[bool, PropertyInfo(alias="useUniqueFileName")]
    """Whether to use a unique filename for this file or not.

    If `true`, ImageKit.io will add a unique suffix to the filename parameter to get
    a unique filename.

    If `false`, then the image is uploaded with the provided filename parameter, and
    any existing file with the same name is replaced.
    """

    webhook_url: Annotated[str, PropertyInfo(alias="webhookUrl")]
    """
    The final status of extensions after they have completed execution will be
    delivered to this endpoint as a POST request.
    [Learn more](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#webhook-payload-structure)
    about the webhook payload structure.
    """


class TransformationPostTransformation(TypedDict, total=False):
    type: Required[Literal["transformation"]]
    """Transformation type."""

    value: Required[str]
    """Transformation string (e.g.

    `w-200,h-200`).
    Same syntax as ImageKit URL-based transformations.
    """


class TransformationPostGifToVideo(TypedDict, total=False):
    type: Required[Literal["gif-to-video"]]
    """Converts an animated GIF into an MP4."""

    value: str
    """Optional transformation string to apply to the output video.

    **Example**: `q-80`
    """


class TransformationPostThumbnail(TypedDict, total=False):
    type: Required[Literal["thumbnail"]]
    """Generates a thumbnail image."""

    value: str
    """Optional transformation string.

    **Example**: `w-150,h-150`
    """


class TransformationPostAbs(TypedDict, total=False):
    protocol: Required[Literal["hls", "dash"]]
    """Streaming protocol to use (`hls` or `dash`)."""

    type: Required[Literal["abs"]]
    """Adaptive Bitrate Streaming (ABS) setup."""

    value: Required[str]
    """
    List of different representations you want to create separated by an underscore.
    """


TransformationPost: TypeAlias = Union[
    TransformationPostTransformation, TransformationPostGifToVideo, TransformationPostThumbnail, TransformationPostAbs
]


class Transformation(TypedDict, total=False):
    """Configure pre-processing (`pre`) and post-processing (`post`) transformations.

    - `pre` — applied before the file is uploaded to the Media Library.
      Useful for reducing file size or applying basic optimizations upfront (e.g., resize, compress).

    - `post` — applied immediately after upload.
      Ideal for generating transformed versions (like video encodes or thumbnails) in advance, so they're ready for delivery without delay.

    You can mix and match any combination of post-processing types.
    """

    post: Iterable[TransformationPost]
    """List of transformations to apply _after_ the file is uploaded.

    Each item must match one of the following types: `transformation`,
    `gif-to-video`, `thumbnail`, `abs`.
    """

    pre: str
    """Transformation string to apply before uploading the file to the Media Library.

    Useful for optimizing files at ingestion.
    """
