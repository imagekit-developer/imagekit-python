# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from datetime import datetime, timezone

import pytest
import standardwebhooks

from imagekitio import ImageKit

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    def test_method_unwrap(self, client: ImageKit) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"id":"id","type":"video.transformation.accepted","created_at":"2019-12-27T18:11:19.117Z","data":{"asset":{"url":"https://example.com"},"transformation":{"type":"video-transformation","options":{"audio_codec":"aac","auto_rotate":true,"format":"mp4","quality":0,"stream_protocol":"HLS","variants":["string"],"video_codec":"h264"}}},"request":{"url":"https://example.com","x_request_id":"x_request_id","user_agent":"user_agent"}}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    def test_method_unwrap(self, client: ImageKit) -> None:
        key = b"secret"
        hook = standardwebhooks.Webhook(key)

        data = """{"id":"id","type":"video.transformation.accepted","created_at":"2019-12-27T18:11:19.117Z","data":{"asset":{"url":"https://example.com"},"transformation":{"type":"video-transformation","options":{"audio_codec":"aac","auto_rotate":true,"format":"mp4","quality":0,"stream_protocol":"HLS","variants":["string"],"video_codec":"h264"}}},"request":{"url":"https://example.com","x_request_id":"x_request_id","user_agent":"user_agent"}}"""
        msg_id = "1"
        timestamp = datetime.now(tz=timezone.utc)
        sig = hook.sign(msg_id=msg_id, timestamp=timestamp, data=data)
        headers = {
            "webhook-id": msg_id,
            "webhook-timestamp": str(int(timestamp.timestamp())),
            "webhook-signature": sig,
        }

        try:
            _ = client.webhooks.unwrap(data, headers=headers, key=key)
        except standardwebhooks.WebhookVerificationError as e:
            raise AssertionError("Failed to unwrap valid webhook") from e

        bad_headers = [
            {**headers, "webhook-signature": hook.sign(msg_id=msg_id, timestamp=timestamp, data="xxx")},
            {**headers, "webhook-id": "bad"},
            {**headers, "webhook-timestamp": "0"},
        ]
        for bad_header in bad_headers:
            with pytest.raises(standardwebhooks.WebhookVerificationError):
                _ = client.webhooks.unwrap(data, headers=bad_header, key=key)
