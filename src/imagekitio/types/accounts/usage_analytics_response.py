# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import TYPE_CHECKING, Dict, List
from datetime import date, datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from .request_bandwidth_entry import RequestBandwidthEntry

__all__ = [
    "UsageAnalyticsResponse",
    "Browser",
    "BrowserByBandwidth",
    "BrowserByRequest",
    "Cache",
    "Country",
    "CountryByBandwidth",
    "CountryByRequest",
    "Device",
    "DeviceByBandwidth",
    "DeviceByRequest",
    "ErrorReason",
    "Extension",
    "Format",
    "FormatByBandwidth",
    "FormatByRequest",
    "StatusCode",
    "Top404Asset",
    "TopImages",
    "TopImagesByBandwidth",
    "TopImagesByRequest",
    "TopImageTransforms",
    "TopImageTransformsByBandwidth",
    "TopImageTransformsByRequest",
    "TopOtherAssets",
    "TopOtherAssetsByBandwidth",
    "TopOtherAssetsByRequest",
    "TopReferrers",
    "TopReferrersByBandwidth",
    "TopReferrersByRequest",
    "TopUserAgents",
    "TopUserAgentsByBandwidth",
    "TopUserAgentsByRequest",
    "TopVideos",
    "TopVideosByBandwidth",
    "TopVideosByRequest",
    "TopVideoTransforms",
    "TopVideoTransformsByBandwidth",
    "TopVideoTransformsByRequest",
    "URLEndpoints",
    "URLEndpointsByBandwidth",
    "URLEndpointsByRequest",
    "VideoProcessing",
]


class BrowserByBandwidth(RequestBandwidthEntry):
    name: str
    """Browser name (e.g. `Chrome`)."""


class BrowserByRequest(RequestBandwidthEntry):
    name: str
    """Browser name (e.g. `Chrome`)."""


class Browser(BaseModel):
    """CDN traffic grouped by browser."""

    by_bandwidth: List[BrowserByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top browsers sorted by bandwidth utilized."""

    by_requests: List[BrowserByRequest] = FieldInfo(alias="byRequests")
    """Top browsers sorted by request count."""


class Cache(BaseModel):
    """CDN cache hit, miss and error counts for the date range."""

    error_count: float = FieldInfo(alias="errorCount")
    """
    Number of requests where the CDN encountered a cache error or exceeded capacity
    while serving the response.
    """

    hit_count: float = FieldInfo(alias="hitCount")
    """Number of requests served from cache, including full hits and revalidated hits."""

    miss_count: float = FieldInfo(alias="missCount")
    """
    Number of requests that were not found in cache and had to be fetched from
    origin.
    """


class CountryByBandwidth(RequestBandwidthEntry):
    code: str
    """ISO country code."""

    name: str
    """Country name."""


class CountryByRequest(RequestBandwidthEntry):
    code: str
    """ISO country code."""

    name: str
    """Country name."""


class Country(BaseModel):
    """CDN traffic grouped by country."""

    by_bandwidth: List[CountryByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top requesting countries sorted by total bandwidth utilized."""

    by_requests: List[CountryByRequest] = FieldInfo(alias="byRequests")
    """Top requesting countries sorted by request count."""


class DeviceByBandwidth(RequestBandwidthEntry):
    name: str
    """Device category combined with operating system or vendor (e.g.

    `Desktop - Windows PC`).
    """


class DeviceByRequest(RequestBandwidthEntry):
    name: str
    """Device category combined with operating system or vendor (e.g.

    `Desktop - Windows PC`).
    """


class Device(BaseModel):
    """CDN traffic grouped by device and operating system (e.g.

    `Desktop - Apple Mac`, `Smartphone - Apple iPhone`).
    """

    by_bandwidth: List[DeviceByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top device/OS combinations sorted by bandwidth utilized."""

    by_requests: List[DeviceByRequest] = FieldInfo(alias="byRequests")
    """Top device/OS combinations sorted by request count."""


class ErrorReason(BaseModel):
    name: str
    """Description of the error reason."""

    request_count: float = FieldInfo(alias="requestCount")
    """Number of requests that failed with this error reason."""


class Extension(BaseModel):
    name: str
    """Extension identifier."""

    operation_count: float = FieldInfo(alias="operationCount")
    """Number of times this extension ran during the date range."""


class FormatByBandwidth(RequestBandwidthEntry):
    name: str
    """MIME type (e.g. `image/webp`)."""


class FormatByRequest(RequestBandwidthEntry):
    name: str
    """MIME type (e.g. `image/webp`)."""


class Format(BaseModel):
    """CDN traffic grouped by response `Content-Type`."""

    by_bandwidth: List[FormatByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top content types sorted by bandwidth utilized."""

    by_requests: List[FormatByRequest] = FieldInfo(alias="byRequests")
    """Top content types sorted by request count."""


class StatusCode(BaseModel):
    name: str
    """HTTP status code."""

    request_count: float = FieldInfo(alias="requestCount")
    """Number of requests that received this status code."""


class Top404Asset(BaseModel):
    name: str
    """URL that returned a 404 response."""

    request_count: float = FieldInfo(alias="requestCount")
    """Number of requests to this URL that returned a 404 response."""


class TopImagesByBandwidth(RequestBandwidthEntry):
    name: str
    """URL of the image asset."""


class TopImagesByRequest(RequestBandwidthEntry):
    name: str
    """URL of the image asset."""


class TopImages(BaseModel):
    """Top image assets by traffic."""

    by_bandwidth: List[TopImagesByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top image assets sorted by bandwidth utilized."""

    by_requests: List[TopImagesByRequest] = FieldInfo(alias="byRequests")
    """Top image assets sorted by request count."""


class TopImageTransformsByBandwidth(RequestBandwidthEntry):
    name: str
    """Image transformation string (e.g. `tr:w-400,h-400`)."""


class TopImageTransformsByRequest(RequestBandwidthEntry):
    name: str
    """Image transformation string (e.g. `tr:w-400,h-400`)."""


class TopImageTransforms(BaseModel):
    """Top image transformation strings by traffic."""

    by_bandwidth: List[TopImageTransformsByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top image transformation strings sorted by bandwidth utilized."""

    by_requests: List[TopImageTransformsByRequest] = FieldInfo(alias="byRequests")
    """Top image transformation strings sorted by request count."""


class TopOtherAssetsByBandwidth(RequestBandwidthEntry):
    name: str
    """URL of the non-image, non-video asset."""


class TopOtherAssetsByRequest(RequestBandwidthEntry):
    name: str
    """URL of the non-image, non-video asset."""


class TopOtherAssets(BaseModel):
    """Top non-image, non-video assets by traffic."""

    by_bandwidth: List[TopOtherAssetsByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top non-image, non-video assets sorted by bandwidth utilized."""

    by_requests: List[TopOtherAssetsByRequest] = FieldInfo(alias="byRequests")
    """Top non-image, non-video assets sorted by request count."""


class TopReferrersByBandwidth(RequestBandwidthEntry):
    name: str
    """Referrer URL."""


class TopReferrersByRequest(RequestBandwidthEntry):
    name: str
    """Referrer URL."""


class TopReferrers(BaseModel):
    """Top HTTP referrers by traffic."""

    by_bandwidth: List[TopReferrersByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top HTTP referrers sorted by bandwidth utilized."""

    by_requests: List[TopReferrersByRequest] = FieldInfo(alias="byRequests")
    """Top HTTP referrers sorted by request count."""


class TopUserAgentsByBandwidth(RequestBandwidthEntry):
    name: str
    """User agent string."""


class TopUserAgentsByRequest(RequestBandwidthEntry):
    name: str
    """User agent string."""


class TopUserAgents(BaseModel):
    """Top user agents by traffic."""

    by_bandwidth: List[TopUserAgentsByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top user agents sorted by bandwidth utilized."""

    by_requests: List[TopUserAgentsByRequest] = FieldInfo(alias="byRequests")
    """Top user agents sorted by request count."""


class TopVideosByBandwidth(RequestBandwidthEntry):
    name: str
    """URL of the video asset."""


class TopVideosByRequest(RequestBandwidthEntry):
    name: str
    """Full URL of the video asset (e.g. `https://ik.imagekit.io/demo/clip.mp4`)."""


class TopVideos(BaseModel):
    """Top video assets by traffic."""

    by_bandwidth: List[TopVideosByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top video assets sorted by bandwidth utilized."""

    by_requests: List[TopVideosByRequest] = FieldInfo(alias="byRequests")
    """Top video assets sorted by request count."""


class TopVideoTransformsByBandwidth(RequestBandwidthEntry):
    name: str
    """Video transformation string (e.g. `tr:h-720,f-mp4`)."""


class TopVideoTransformsByRequest(RequestBandwidthEntry):
    name: str
    """Video transformation string (e.g. `tr:h-720,f-mp4`)."""


class TopVideoTransforms(BaseModel):
    """Top video transformation strings by traffic."""

    by_bandwidth: List[TopVideoTransformsByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top video transformation strings sorted by bandwidth utilized."""

    by_requests: List[TopVideoTransformsByRequest] = FieldInfo(alias="byRequests")
    """Top video transformation strings sorted by request count."""


class URLEndpointsByBandwidth(RequestBandwidthEntry):
    name: str
    """
    URL endpoint name, or `Default` for traffic that does not match a named
    endpoint.
    """


class URLEndpointsByRequest(RequestBandwidthEntry):
    name: str
    """
    URL endpoint name, or `Default` for traffic that does not match a named
    endpoint.
    """


class URLEndpoints(BaseModel):
    """CDN traffic grouped by configured URL endpoint.

    Traffic that does not match any named URL endpoint pattern is grouped under `Default`.
    """

    by_bandwidth: List[URLEndpointsByBandwidth] = FieldInfo(alias="byBandwidth")
    """Top URL endpoints sorted by bandwidth utilized."""

    by_requests: List[URLEndpointsByRequest] = FieldInfo(alias="byRequests")
    """Top URL endpoints sorted by request count."""


class VideoProcessing(BaseModel):
    codec: str
    """Video codec used for the output (e.g. `h264`, `av1`)."""

    duration_seconds: float = FieldInfo(alias="durationSeconds")
    """Total output duration, in seconds, for this resolution and codec combination."""

    resolution: str
    """Output resolution tier (e.g. `SD`, `HD`, `4K`)."""


class UsageAnalyticsResponse(BaseModel):
    bandwidth_bytes: float = FieldInfo(alias="bandwidthBytes")
    """Total bandwidth, in bytes, utilized during the specified date range."""

    browser: Browser
    """CDN traffic grouped by browser."""

    cache: Cache
    """CDN cache hit, miss and error counts for the date range."""

    country: Country
    """CDN traffic grouped by country."""

    device: Device
    """CDN traffic grouped by device and operating system (e.g.

    `Desktop - Apple Mac`, `Smartphone - Apple iPhone`).
    """

    end_date: date = FieldInfo(alias="endDate")
    """End date of the computed analytics data."""

    error_reasons: List[ErrorReason] = FieldInfo(alias="errorReasons")
    """Request count grouped by origin error reason.

    This covers failed origin fetches, such as an asset not found at origin or an
    origin timeout. It is not the HTTP status code returned to the client, see
    `statusCodes` for that.
    """

    extensions: List[Extension]
    """Raw per-extension operation counts for the date range.

    These are raw operation counts, not billable extension units. For billable
    usage, use the `/v1/accounts/usage` endpoint.
    """

    format: Format
    """CDN traffic grouped by response `Content-Type`."""

    generated_at: datetime = FieldInfo(alias="generatedAt")
    """Date and time when the analytics data was computed.

    Use this to gauge how fresh the returned data is. The date and time is in
    ISO8601 format.
    """

    request_count: float = FieldInfo(alias="requestCount")
    """Total number of requests made during the specified date range."""

    start_date: date = FieldInfo(alias="startDate")
    """Start date of the computed analytics data."""

    status_codes: List[StatusCode] = FieldInfo(alias="statusCodes")
    """Request count grouped by HTTP status code."""

    top404_assets: List[Top404Asset] = FieldInfo(alias="top404Assets")
    """Top URLs that returned a 404 response."""

    top_images: TopImages = FieldInfo(alias="topImages")
    """Top image assets by traffic."""

    top_image_transforms: TopImageTransforms = FieldInfo(alias="topImageTransforms")
    """Top image transformation strings by traffic."""

    top_other_assets: TopOtherAssets = FieldInfo(alias="topOtherAssets")
    """Top non-image, non-video assets by traffic."""

    top_referrers: TopReferrers = FieldInfo(alias="topReferrers")
    """Top HTTP referrers by traffic."""

    top_user_agents: TopUserAgents = FieldInfo(alias="topUserAgents")
    """Top user agents by traffic."""

    top_videos: TopVideos = FieldInfo(alias="topVideos")
    """Top video assets by traffic."""

    top_video_transforms: TopVideoTransforms = FieldInfo(alias="topVideoTransforms")
    """Top video transformation strings by traffic."""

    url_endpoints: URLEndpoints = FieldInfo(alias="urlEndpoints")
    """CDN traffic grouped by configured URL endpoint.

    Traffic that does not match any named URL endpoint pattern is grouped under
    `Default`.
    """

    video_processing: List[VideoProcessing] = FieldInfo(alias="videoProcessing")
    """
    Raw observed video transcode output duration, in seconds, grouped by resolution
    and codec. These are raw seconds, not billable Video Processing Units (VPU). For
    billable VPU totals, use the `/v1/accounts/usage` endpoint.
    """

    if TYPE_CHECKING:
        # Some versions of Pydantic <2.8.0 have a bug and don’t allow assigning a
        # value to this field, so for compatibility we avoid doing it at runtime.
        __pydantic_extra__: Dict[str, object] = FieldInfo(init=False)  # pyright: ignore[reportIncompatibleVariableOverride]

        # Stub to indicate that arbitrary properties are accepted.
        # To access properties that are not valid identifiers you can use `getattr`, e.g.
        # `getattr(obj, '$type')`
        def __getattr__(self, attr: str) -> object: ...
    else:
        __pydantic_extra__: Dict[str, object]
