# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["FileUploadV2Params"]


class FileUploadV2Params(TypedDict, total=False):
    file: Required[str]
    """Pass the HTTP URL or base64 string.

    When passing a URL in the file parameter, please ensure that our servers can
    access the URL. In case ImageKit is unable to download the file from the
    specified URL, a `400` error response is returned. This will also result in a
    `400` error if the file download request is aborted if response headers are not
    received in 8 seconds.
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

    custom_metadata: Annotated[str, PropertyInfo(alias="customMetadata")]
    """Stringified JSON key-value data to be associated with the asset."""

    extensions: str
    """Stringified JSON object with an array of extensions to be applied to the image.

    Refer to extensions schema in
    [update file API request body](/docs/api-reference/digital-asset-management-dam/managing-assets/update-file-details#request-body).
    """

    folder: str
    """The folder path in which the image has to be uploaded.

    If the folder(s) didn't exist before, a new folder(s) is created. Using multiple
    `/` creates a nested folder.
    """

    is_private_file: Annotated[Literal["true", "false"], PropertyInfo(alias="isPrivateFile")]
    """Whether to mark the file as private or not.

    If `true`, the file is marked as private and is accessible only using named
    transformation or signed URL.
    """

    is_published: Annotated[Literal["true", "false"], PropertyInfo(alias="isPublished")]
    """Whether to upload file as published or not.

    If `false`, the file is marked as unpublished, which restricts access to the
    file only via the media library. Files in draft or unpublished state can only be
    publicly accessed after being published.

    The option to upload in draft state is only available in custom enterprise
    pricing plans.
    """

    overwrite_ai_tags: Annotated[Literal["true", "false"], PropertyInfo(alias="overwriteAITags")]
    """
    If set to `true` and a file already exists at the exact location, its AITags
    will be removed. Set `overwriteAITags` to `false` to preserve AITags.
    """

    overwrite_custom_metadata: Annotated[Literal["true", "false"], PropertyInfo(alias="overwriteCustomMetadata")]
    """
    If the request does not have `customMetadata`, and a file already exists at the
    exact location, existing customMetadata will be removed.
    """

    overwrite_file: Annotated[str, PropertyInfo(alias="overwriteFile")]
    """
    If `false` and `useUniqueFileName` is also `false`, and a file already exists at
    the exact location, upload API will return an error immediately.
    """

    overwrite_tags: Annotated[Literal["true", "false"], PropertyInfo(alias="overwriteTags")]
    """
    If the request does not have `tags`, and a file already exists at the exact
    location, existing tags will be removed.
    """

    response_fields: Annotated[str, PropertyInfo(alias="responseFields")]
    """
    Comma-separated values of the fields that you want the API to return in the
    response.

    For example, set the value of this field to
    `tags,customCoordinates,isPrivateFile` to get the value of `tags`,
    `customCoordinates`, and `isPrivateFile` in the response.

    Accepts combination of `tags`, `customCoordinates`, `isPrivateFile`,
    `embeddedMetadata`, `isPublished`, `customMetadata`, and `metadata`.
    """

    tags: str
    """Set the tags while uploading the file.

    Comma-separated value of tags in the format `tag1,tag2,tag3`. The maximum length
    of all characters should not exceed 500. `%` is not allowed.

    If this field is not specified and the file is overwritten then the tags will be
    removed.
    """

    transformation: str
    """Stringified JSON object with properties for pre and post transformations:

    `pre` - Accepts a "string" containing a valid transformation used for requesting
    a pre-transformation for an image or a video file.

    `post` - Accepts an array of objects with properties:

    - `type`: One of `transformation`, `gif-to-video`, `thumbnail`, or `abs`
      (Adaptive bitrate streaming).
    - `value`: A "string" corresponding to the required transformation. Required if
      `type` is `transformation` or `abs`. Optional if `type` is `gif-to-video` or
      `thumbnail`.
    - `protocol`: Either `hls` or `dash`, applicable only if `type` is `abs`.

    Read more about
    [Adaptive bitrate streaming (ABS)](/docs/adaptive-bitrate-streaming).
    """

    use_unique_file_name: Annotated[Literal["true", "false"], PropertyInfo(alias="useUniqueFileName")]
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
