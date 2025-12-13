# File manually created for helper functions - not generated from OpenAPI spec

from __future__ import annotations

import re
import hmac
import time
import uuid
import base64
import hashlib
from typing import Any, Dict, List, Union, Iterable, Optional, Sequence, cast
from urllib.parse import quote, parse_qs, urlparse, urlunparse
from typing_extensions import Unpack

from .._resource import SyncAPIResource, AsyncAPIResource
from ..types.shared_params.overlay import Overlay
from ..types.shared_params.src_options import SrcOptions
from ..types.shared_params.transformation import Transformation
from ..types.shared_params.text_overlay_transformation import TextOverlayTransformation
from ..types.shared_params.subtitle_overlay_transformation import SubtitleOverlayTransformation
from ..types.shared_params.solid_color_overlay_transformation import SolidColorOverlayTransformation

# Type alias for any transformation type (main or overlay-specific)
AnyTransformation = Union[
    Transformation, TextOverlayTransformation, SubtitleOverlayTransformation, SolidColorOverlayTransformation
]

__all__ = ["HelperResource", "AsyncHelperResource"]

# Constants
TRANSFORMATION_PARAMETER = "tr"
SIGNATURE_PARAMETER = "ik-s"
TIMESTAMP_PARAMETER = "ik-t"
DEFAULT_TIMESTAMP = 9999999999
SIMPLE_OVERLAY_PATH_REGEX = re.compile(r"^[a-zA-Z0-9-._/ ]*$")
SIMPLE_OVERLAY_TEXT_REGEX = re.compile(r"^[a-zA-Z0-9-._ ]*$")

# Transformation key mapping
SUPPORTED_TRANSFORMS = {
    # Basic sizing & layout
    "width": "w",
    "height": "h",
    "aspect_ratio": "ar",
    "background": "bg",
    "border": "b",
    "crop": "c",
    "crop_mode": "cm",
    "dpr": "dpr",
    "focus": "fo",
    "quality": "q",
    "x": "x",
    "x_center": "xc",
    "y": "y",
    "y_center": "yc",
    "format": "f",
    "video_codec": "vc",
    "audio_codec": "ac",
    "radius": "r",
    "rotation": "rt",
    "blur": "bl",
    "named": "n",
    "default_image": "di",
    "flip": "fl",
    "original": "orig",
    "start_offset": "so",
    "end_offset": "eo",
    "duration": "du",
    "streaming_resolutions": "sr",
    # AI & advanced effects
    "grayscale": "e-grayscale",
    "ai_upscale": "e-upscale",
    "ai_retouch": "e-retouch",
    "ai_variation": "e-genvar",
    "ai_drop_shadow": "e-dropshadow",
    "ai_change_background": "e-changebg",
    "ai_remove_background": "e-bgremove",
    "ai_remove_background_external": "e-removedotbg",
    "ai_edit": "e-edit",
    "contrast_stretch": "e-contrast",
    "shadow": "e-shadow",
    "sharpen": "e-sharpen",
    "unsharp_mask": "e-usm",
    "gradient": "e-gradient",
    # Other flags & finishing
    "progressive": "pr",
    "lossless": "lo",
    "color_profile": "cp",
    "metadata": "md",
    "opacity": "o",
    "trim": "t",
    "zoom": "z",
    "page": "pg",
    # Text overlay transformations
    "font_size": "fs",
    "font_family": "ff",
    "font_color": "co",
    "inner_alignment": "ia",
    "padding": "pa",
    "alpha": "al",
    "typography": "tg",
    "line_height": "lh",
    # Subtitles transformations
    "font_outline": "fol",
    "font_shadow": "fsh",
    "color": "co",
    # Raw pass-through
    "raw": "raw",
}

CHAIN_TRANSFORM_DELIMITER = ":"
TRANSFORM_DELIMITER = ","
TRANSFORM_KEY_VALUE_DELIMITER = "-"

# RFC 3986 section 3.3 defines 'pchar' (path characters) that are safe to use unencoded:
# pchar = unreserved / pct-encoded / sub-delims / ":" / "@"
# unreserved = ALPHA / DIGIT / "-" / "." / "_" / "~"
# sub-delims = "!" / "$" / "&" / "'" / "(" / ")" / "*" / "+" / "," / ";" / "="
# This matches what Node.js URL.pathname uses and ensures compatibility across SDKs
RFC3986_PATH_SAFE_CHARS = "/:@!$&'()*+,;=-._~"


def _get_transform_key(transform: str) -> str:
    """Get the short transformation key from the long form."""
    if not transform:
        return ""
    return SUPPORTED_TRANSFORMS.get(transform, transform)


def _add_trailing_slash(s: str) -> str:
    """Add trailing slash if not present."""
    if s and not s.endswith("/"):
        return s + "/"
    return s


def _remove_trailing_slash(s: str) -> str:
    """Remove trailing slash if present."""
    if s and s.endswith("/"):
        return s[:-1]
    return s


def _remove_leading_slash(s: str) -> str:
    """Remove leading slash if present."""
    if s and s.startswith("/"):
        return s[1:]
    return s


def _format_number(value: Any) -> str:
    """
    Format a numeric value as a string, removing unnecessary decimal points.

    Examples:
        5.0 -> "5"
        5.5 -> "5.5"
        5 -> "5"
        "5" -> "5"
    """
    if isinstance(value, (int, float)):
        # Check if it's a whole number
        if isinstance(value, float) and value.is_integer():
            return str(int(value))
        return str(value)
    return str(value)


def _path_join(parts: List[str], sep: str = "/") -> str:
    """Join path parts, handling slashes correctly."""
    cleaned_parts: List[str] = []
    for part in parts:
        if part:
            # Remove leading and trailing slashes from parts
            cleaned_part = part.strip("/")
            if cleaned_part:
                cleaned_parts.append(cleaned_part)
    return sep + sep.join(cleaned_parts) if cleaned_parts else ""


def _safe_btoa(s: str) -> str:
    """
    Base64 encode a string and then URL-encode it.
    This matches Node.js behavior: safeBtoa() + encodeURIComponent().

    In Node.js:
    - encodeURIComponent() encodes: / as %2F, + as %2B, = as %3D
    - Python's quote() with default safe='/' doesn't encode /
    - So we need to explicitly set safe='' to encode everything
    """
    encoded = base64.b64encode(s.encode("utf-8")).decode("utf-8")
    # URL encode the entire base64 string (/, +, =, etc.)
    # quote() with safe='' will encode all special characters to match encodeURIComponent
    return quote(encoded, safe="")


def _process_input_path(s: str, encoding: str) -> str:
    """
    Process input path for overlays.
    Returns the full parameter string including the i- or ie- prefix.
    """
    if not s:
        return ""

    # Remove leading and trailing slashes
    s = _remove_trailing_slash(_remove_leading_slash(s))

    if encoding == "plain":
        return f"i-{s.replace('/', '@@')}"

    if encoding == "base64":
        # safeBtoa already encodes = as %3D, no need for further encoding
        return f"ie-{_safe_btoa(s)}"

    # Auto encoding: use plain for simple paths, base64 for special characters
    if SIMPLE_OVERLAY_PATH_REGEX.match(s):
        return f"i-{s.replace('/', '@@')}"
    else:
        # safeBtoa already encodes = as %3D, no need for further encoding
        return f"ie-{_safe_btoa(s)}"


def _process_text(s: str, encoding: str) -> str:
    """
    Process text for overlays.
    Returns the full parameter string including the i- or ie- prefix.
    """
    if not s:
        return ""

    if encoding == "plain":
        return f"i-{quote(s, safe='')}"

    if encoding == "base64":
        # safeBtoa already encodes = as %3D, no need for further encoding
        return f"ie-{_safe_btoa(s)}"

    # Auto encoding: use plain for simple text, base64 for special characters
    if SIMPLE_OVERLAY_TEXT_REGEX.match(s):
        return f"i-{quote(s, safe='')}"

    # safeBtoa already encodes = as %3D, no need for further encoding
    return f"ie-{_safe_btoa(s)}"


def _process_overlay(overlay: Overlay) -> str:
    """Process overlay transformations."""
    if not overlay:
        return ""

    # Extract type, position, timing, and transformation from overlay
    overlay_type: str = cast(str, overlay.get("type", ""))
    position: Dict[str, Any] = cast(Dict[str, Any], overlay.get("position", {}))
    timing: Dict[str, Any] = cast(Dict[str, Any], overlay.get("timing", {}))
    transformation: List[Any] = cast(List[Any], overlay.get("transformation", []))

    if not overlay_type:
        return ""

    parsed_overlay: List[str] = []

    if overlay_type == "text":
        text: str = cast(str, overlay.get("text", ""))
        if not text:
            return ""

        encoding: str = cast(str, overlay.get("encoding", "auto"))
        parsed_overlay.append("l-text")

        # Process the text - returns full string with i- or ie- prefix
        parsed_overlay.append(_process_text(text, encoding))

    elif overlay_type == "image":
        parsed_overlay.append("l-image")

        input_val: str = cast(str, overlay.get("input", ""))
        if not input_val:
            return ""

        img_encoding = cast(str, overlay.get("encoding", "auto"))

        # Process the input path - returns full string with i- or ie- prefix
        parsed_overlay.append(_process_input_path(input_val, img_encoding))

    elif overlay_type == "video":
        parsed_overlay.append("l-video")

        video_input = cast(str, overlay.get("input", ""))
        if not video_input:
            return ""

        video_encoding = cast(str, overlay.get("encoding", "auto"))

        # Process the input path - returns full string with i- or ie- prefix
        parsed_overlay.append(_process_input_path(video_input, video_encoding))

    elif overlay_type == "subtitle":
        parsed_overlay.append("l-subtitle")

        subtitle_input = cast(str, overlay.get("input", ""))
        if not subtitle_input:
            return ""

        subtitle_encoding = cast(str, overlay.get("encoding", "auto"))

        # Process the input path - returns full string with i- or ie- prefix
        parsed_overlay.append(_process_input_path(subtitle_input, subtitle_encoding))

    elif overlay_type == "solidColor":
        parsed_overlay.append("l-image")
        parsed_overlay.append("i-ik_canvas")

        color: str = cast(str, overlay.get("color", ""))
        if not color:
            return ""

        parsed_overlay.append(f"bg-{color}")

    # Handle position properties (x, y, focus)
    # Node.js uses if (x) which skips falsy values like 0, '', false, null, undefined
    x = position.get("x")
    if x:
        parsed_overlay.append(f"lx-{x}")

    y = position.get("y")
    if y:
        parsed_overlay.append(f"ly-{y}")

    focus = position.get("focus")
    if focus:
        parsed_overlay.append(f"lfo-{focus}")

    # Handle timing properties (start, end, duration)
    # Node.js uses if (start) which skips falsy values
    start = timing.get("start")
    if start:
        parsed_overlay.append(f"lso-{_format_number(start)}")

    end = timing.get("end")
    if end:
        parsed_overlay.append(f"leo-{_format_number(end)}")

    duration = timing.get("duration")
    if duration:
        parsed_overlay.append(f"ldu-{duration}")

    # Handle nested transformations for image/video overlays
    if transformation:
        transformation_string: str = _build_transformation_string(transformation)
        if transformation_string and transformation_string.strip():
            parsed_overlay.append(transformation_string)

    # Close overlay
    parsed_overlay.append("l-end")

    return TRANSFORM_DELIMITER.join(parsed_overlay)


def _build_transformation_string(transformation: Optional[Sequence[AnyTransformation]]) -> str:
    """Build transformation string from transformation objects."""
    if not transformation:
        return ""

    parsed_transforms: List[str] = []

    for current_transform in transformation:
        if not current_transform:
            continue

        parsed_transform_step: List[str] = []

        for key, value in current_transform.items():
            if value is None:
                continue

            # Handle overlay separately
            if key == "overlay" and isinstance(value, dict):
                raw_string: str = _process_overlay(cast(Overlay, value))
                if raw_string and raw_string.strip():
                    parsed_transform_step.append(raw_string)
                continue

            # Get the transformation key
            transform_key: str = _get_transform_key(key)
            if not transform_key:
                transform_key = key

            if not transform_key:
                continue

            # Handle boolean transformations that should only output key
            if transform_key in [
                "e-grayscale",
                "e-contrast",
                "e-removedotbg",
                "e-bgremove",
                "e-upscale",
                "e-retouch",
                "e-genvar",
            ]:
                if value is True or value == "-" or value == "true":
                    parsed_transform_step.append(transform_key)
                # Any other value means that the effect should not be applied
                continue

            # Handle transformations that can be true or have values
            if transform_key in ["e-sharpen", "e-shadow", "e-gradient", "e-usm", "e-dropshadow"] and (
                str(value).strip() == "" or value is True or value == "true"
            ):
                parsed_transform_step.append(transform_key)
                continue

            # Handle raw transformation
            if key == "raw":
                if isinstance(value, str) and value.strip():
                    parsed_transform_step.append(value)
                continue

            # Handle default_image and font_family - replace slashes
            if transform_key in ["di", "ff"]:
                value = _remove_trailing_slash(_remove_leading_slash(str(value) if value else ""))
                value = value.replace("/", "@@")

            # Handle streaming_resolutions array
            if transform_key == "sr" and isinstance(value, list):
                value = "_".join(str(v) for v in cast(List[Any], value))

            # Special case for trim with empty string
            if transform_key == "t" and str(value).strip() == "":
                value = "true"

            # Skip false values
            if value is False:
                continue

            # Skip empty strings (except for special keys that allow empty values)
            if isinstance(value, str) and value.strip() == "":
                continue

            # Convert boolean True to lowercase "true"
            if value is True:
                value = "true"

            # Format numeric values to avoid unnecessary .0 for integers
            if isinstance(value, (int, float)):
                value = _format_number(value)

            # Add the transformation
            parsed_transform_step.append(f"{transform_key}{TRANSFORM_KEY_VALUE_DELIMITER}{value}")

        if parsed_transform_step:
            parsed_transforms.append(TRANSFORM_DELIMITER.join(parsed_transform_step))

    return CHAIN_TRANSFORM_DELIMITER.join(parsed_transforms)


def _get_signature_timestamp(seconds: Optional[float]) -> int:
    """Calculate expiry timestamp for URL signing."""
    if not seconds or seconds <= 0:
        return DEFAULT_TIMESTAMP

    # Try to parse as int, return DEFAULT_TIMESTAMP if invalid
    try:
        sec = int(seconds)
        if sec <= 0:
            return DEFAULT_TIMESTAMP
    except (ValueError, TypeError):
        return DEFAULT_TIMESTAMP

    return int(time.time()) + sec


def _get_signature(private_key: str, url: str, url_endpoint: str, expiry_timestamp: int) -> str:
    """Generate HMAC-SHA1 signature for URL signing."""
    if not private_key or not url or not url_endpoint:
        return ""

    # Create the string to sign: relative path + expiry timestamp
    # This matches Node.js: url.replace(addTrailingSlash(urlEndpoint), '') + String(expiryTimestamp)
    url_endpoint_with_slash = _add_trailing_slash(url_endpoint)
    string_to_sign = url.replace(url_endpoint_with_slash, "") + str(expiry_timestamp)

    # Generate HMAC-SHA1 signature
    signature = hmac.new(private_key.encode("utf-8"), string_to_sign.encode("utf-8"), hashlib.sha1).hexdigest()

    return signature


def _get_authentication_parameters(token: str, expire: int, private_key: str) -> Dict[str, Any]:
    """Generate authentication parameters for uploads."""
    auth_parameters = {
        "token": token,
        "expire": expire,
        "signature": "",
    }

    signature = hmac.new(private_key.encode("utf-8"), f"{token}{expire}".encode("utf-8"), hashlib.sha1).hexdigest()

    auth_parameters["signature"] = signature
    return auth_parameters


def _build_url(
    src: str,
    url_endpoint: str,
    transformation_position: str,
    transformation: Any,
    query_parameters: Dict[str, Any],
    signed: bool,
    expires_in: Optional[float],
    private_key: str,
) -> str:
    """
    Internal implementation of build_url.

    Args:
        src: Accepts a relative or absolute path of the resource.
        url_endpoint: Get your urlEndpoint from the ImageKit dashboard.
        transformation_position: By default, the transformation string is added as a query parameter.
        transformation: An array of objects specifying the transformations to be applied in the URL.
        query_parameters: Additional query parameters to add to the final URL.
        signed: Whether to sign the URL or not.
        expires_in: When you want the signed URL to expire, specified in seconds.
        private_key: Private key for signing URLs.

    Returns:
        The constructed source URL.
    """
    if not src:
        return ""

    # Check if src is absolute URL
    is_absolute_url = src.startswith("http://") or src.startswith("https://")

    # Track if src parameter is used for URL (matches Node.js isSrcParameterUsedForURL)
    is_src_parameter_used_for_url = False

    # Parse URL
    try:
        if not is_absolute_url:
            parsed_url = urlparse(url_endpoint)
        else:
            parsed_url = urlparse(src)
            is_src_parameter_used_for_url = True
    except Exception:
        return ""

    # Build query parameters
    query_dict_raw = dict(parse_qs(parsed_url.query))
    # Flatten lists from parse_qs
    query_dict: Dict[str, str] = {k: v[0] if len(v) == 1 else ",".join(v) for k, v in query_dict_raw.items()}

    # Add additional query parameters - convert values to strings like Node.js does
    if query_parameters:
        for k, v in query_parameters.items():
            query_dict[k] = str(v)

    # Build transformation string
    transformation_string = _build_transformation_string(transformation)

    # Determine if transformation should be in query or path
    # Matches Node.js: addAsQuery = transformationUtils.addAsQueryParameter(opts) || isSrcParameterUsedForURL
    add_as_query = transformation_position == "query" or is_src_parameter_used_for_url

    # Placeholder for transformation to avoid URL encoding issues
    TRANSFORMATION_PLACEHOLDER = "PLEASEREPLACEJUSTBEFORESIGN"

    # Build the path
    if not is_absolute_url:
        # For relative URLs
        endpoint_path = urlparse(url_endpoint).path
        path_parts = [endpoint_path] if endpoint_path else []

        # Add transformation in path if needed
        if transformation_string and not add_as_query:
            path_parts.append(f"{TRANSFORMATION_PARAMETER}{CHAIN_TRANSFORM_DELIMITER}{TRANSFORMATION_PLACEHOLDER}")

        # Add src path with RFC 3986 compliant encoding
        # Python's urlunparse() doesn't auto-encode Unicode like Node.js URL does,
        # so we must manually encode the path while preserving RFC 3986 safe chars
        encoded_src = quote(src, safe=RFC3986_PATH_SAFE_CHARS)
        path_parts.append(encoded_src)

        path = _path_join(path_parts)
    else:
        path = parsed_url.path

    # Add transformation to query if needed
    if transformation_string and add_as_query:
        query_dict[TRANSFORMATION_PARAMETER] = TRANSFORMATION_PLACEHOLDER

    # Build the URL
    scheme = parsed_url.scheme or "https"
    netloc = parsed_url.netloc if is_absolute_url else urlparse(url_endpoint).netloc

    # Build query string manually to avoid encoding transformation string
    query_string = ""
    if query_dict:
        query_parts: List[str] = []
        for k, v in query_dict.items():
            query_parts.append(f"{k}={v}")
        query_string = "&".join(query_parts)

    final_url = urlunparse((scheme, netloc, path, "", query_string, ""))

    # Replace placeholder with actual transformation string
    if transformation_string:
        final_url = final_url.replace(TRANSFORMATION_PLACEHOLDER, transformation_string)

    # Sign URL if needed
    if signed or (expires_in and expires_in > 0):
        expiry_timestamp = _get_signature_timestamp(expires_in)

        url_signature = _get_signature(
            private_key=private_key, url=final_url, url_endpoint=url_endpoint, expiry_timestamp=expiry_timestamp
        )

        # Add signature parameters
        parsed_final = urlparse(final_url)
        has_existing_params = bool(parsed_final.query)
        separator = "&" if has_existing_params else "?"

        if expiry_timestamp and expiry_timestamp != DEFAULT_TIMESTAMP:
            final_url += f"{separator}{TIMESTAMP_PARAMETER}={expiry_timestamp}"
            final_url += f"&{SIGNATURE_PARAMETER}={url_signature}"
        else:
            final_url += f"{separator}{SIGNATURE_PARAMETER}={url_signature}"

    return final_url


def _get_authentication_parameters_with_defaults(
    token: Optional[str], expire: Optional[int], private_key: str
) -> Dict[str, Any]:
    """
    Internal implementation of get_authentication_parameters with default value handling.

    Args:
        token: Custom token for the upload session. If not provided, a UUID v4 will be generated automatically.
        expire: Expiration time in seconds from now. If not provided, defaults to 1800 seconds (30 minutes).
        private_key: Private key for generating authentication parameters.

    Returns:
        Authentication parameters object containing token, expire, and signature.
    """
    if not private_key:
        raise ValueError("Private key is required for generating authentication parameters")

    # Generate token if not provided
    if not token:
        token = str(uuid.uuid4())

    # Set default expiry if not provided
    if expire is None:
        expire = int(time.time()) + 1800  # 30 minutes default

    return _get_authentication_parameters(token, expire, private_key)


class HelperResource(SyncAPIResource):
    """
    Helper resource for additional utility functions like URL building and authentication.
    """

    def build_url(self, **options: Unpack[SrcOptions]) -> str:
        """
        Builds a source URL with the given options.

        Args:
            src: Accepts a relative or absolute path of the resource. If a relative path is provided,
                it is appended to the `url_endpoint`. If an absolute path is provided, `url_endpoint` is ignored.
            url_endpoint: Get your urlEndpoint from the ImageKit dashboard.
            transformation: An array of objects specifying the transformations to be applied in the URL.
            transformation_position: By default, the transformation string is added as a query parameter.
                Set to `path` to add it in the URL path instead.
            signed: Whether to sign the URL or not. Set to `true` to generate a signed URL.
            expires_in: When you want the signed URL to expire, specified in seconds.
            query_parameters: Additional query parameters to add to the final URL.

        Returns:
            The constructed source URL.
        """
        return _build_url(
            src=options.get("src", ""),
            url_endpoint=options.get("url_endpoint", ""),
            transformation_position=options.get("transformation_position", "query"),
            transformation=options.get("transformation"),
            query_parameters=options.get("query_parameters", {}),
            signed=options.get("signed", False),
            expires_in=options.get("expires_in"),
            private_key=self._client.private_key,
        )

    def get_authentication_parameters(
        self,
        token: Optional[str] = None,
        expire: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Generates authentication parameters for client-side file uploads using ImageKit's Upload API.

        Args:
            token: Custom token for the upload session. If not provided, a UUID v4 will be generated automatically.
            expire: Expiration time in seconds from now. If not provided, defaults to 1800 seconds (30 minutes).

        Returns:
            Authentication parameters object containing:
            - token: Unique identifier for this upload session
            - expire: Unix timestamp when these parameters expire
            - signature: HMAC-SHA1 signature for authenticating the upload
        """
        return _get_authentication_parameters_with_defaults(
            token=token, expire=expire, private_key=self._client.private_key
        )

    def build_transformation_string(self, transformation: Optional[Iterable[Transformation]] = None) -> str:
        """
        Builds a transformation string from an array of transformation objects.

        Args:
            transformation: List of transformation dictionaries.

        Returns:
            The transformation string in ImageKit format.
        """
        if transformation is None:
            return ""

        # Convert to list if it's an iterable
        if not isinstance(transformation, list):
            transformation = list(transformation)

        return _build_transformation_string(transformation)


class AsyncHelperResource(AsyncAPIResource):
    """
    Async version of helper resource for additional utility functions.
    """

    async def build_url(self, **options: Unpack[SrcOptions]) -> str:
        """
        Async version of build_url.

        Args:
            src: Accepts a relative or absolute path of the resource. If a relative path is provided,
                it is appended to the `url_endpoint`. If an absolute path is provided, `url_endpoint` is ignored.
            url_endpoint: Get your urlEndpoint from the ImageKit dashboard.
            transformation: An array of objects specifying the transformations to be applied in the URL.
            transformation_position: By default, the transformation string is added as a query parameter.
                Set to `path` to add it in the URL path instead.
            signed: Whether to sign the URL or not. Set to `true` to generate a signed URL.
            expires_in: When you want the signed URL to expire, specified in seconds.
            query_parameters: Additional query parameters to add to the final URL.

        Returns:
            The constructed source URL.
        """
        return _build_url(
            src=options.get("src", ""),
            url_endpoint=options.get("url_endpoint", ""),
            transformation_position=options.get("transformation_position", "query"),
            transformation=options.get("transformation"),
            query_parameters=options.get("query_parameters", {}),
            signed=options.get("signed", False),
            expires_in=options.get("expires_in"),
            private_key=self._client.private_key,
        )

    async def get_authentication_parameters(
        self,
        token: Optional[str] = None,
        expire: Optional[int] = None,
    ) -> Dict[str, Any]:
        """
        Async version of get_authentication_parameters.

        Args:
            token: Custom token for the upload session. If not provided, a UUID v4 will be generated automatically.
            expire: Expiration time in seconds from now. If not provided, defaults to 1800 seconds (30 minutes).

        Returns:
            Authentication parameters object containing:
            - token: Unique identifier for this upload session
            - expire: Unix timestamp when these parameters expire
            - signature: HMAC-SHA1 signature for authenticating the upload
        """
        return _get_authentication_parameters_with_defaults(
            token=token, expire=expire, private_key=self._client.private_key
        )

    async def build_transformation_string(self, transformation: Optional[Iterable[Transformation]] = None) -> str:
        """
        Async version of build_transformation_string.

        Args:
            transformation: List of transformation dictionaries.

        Returns:
            The transformation string in ImageKit format.
        """
        if transformation is None:
            return ""

        # Convert to list if it's an iterable
        if not isinstance(transformation, list):
            transformation = list(transformation)

        return _build_transformation_string(transformation)
