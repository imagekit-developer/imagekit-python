# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types.accounts import Webhook, WebhookListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWebhooks:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create(self, client: ImageKit) -> None:
        webhook = client.accounts.webhooks.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: ImageKit) -> None:
        webhook = client.accounts.webhooks.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
            enabled=True,
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: ImageKit) -> None:
        response = client.accounts.webhooks.with_raw_response.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: ImageKit) -> None:
        with client.accounts.webhooks.with_streaming_response.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update(self, client: ImageKit) -> None:
        webhook = client.accounts.webhooks.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: ImageKit) -> None:
        webhook = client.accounts.webhooks.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
            enabled=False,
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "video.transformation.error"],
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: ImageKit) -> None:
        response = client.accounts.webhooks.with_raw_response.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: ImageKit) -> None:
        with client.accounts.webhooks.with_streaming_response.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_update(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        webhook = client.accounts.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.accounts.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.accounts.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        webhook = client.accounts.webhooks.delete(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.accounts.webhooks.with_raw_response.delete(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.accounts.webhooks.with_streaming_response.delete(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        webhook = client.accounts.webhooks.get(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.accounts.webhooks.with_raw_response.get(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.accounts.webhooks.with_streaming_response.get(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.webhooks.with_raw_response.get(
                "",
            )


class TestAsyncWebhooks:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncImageKit) -> None:
        webhook = await async_client.accounts.webhooks.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncImageKit) -> None:
        webhook = await async_client.accounts.webhooks.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
            enabled=True,
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.webhooks.with_raw_response.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.webhooks.with_streaming_response.create(
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "file.created"],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncImageKit) -> None:
        webhook = await async_client.accounts.webhooks.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncImageKit) -> None:
        webhook = await async_client.accounts.webhooks.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
            enabled=False,
            endpoint="https://example.com/imagekit/webhooks",
            events=["video.transformation.ready", "video.transformation.error"],
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.webhooks.with_raw_response.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.webhooks.with_streaming_response.update(
            id="65f1c2a9e4b0a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.webhooks.with_raw_response.update(
                id="",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        webhook = await async_client.accounts.webhooks.list()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.webhooks.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(WebhookListResponse, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.webhooks.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(WebhookListResponse, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        webhook = await async_client.accounts.webhooks.delete(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.webhooks.with_raw_response.delete(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert webhook is None

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.webhooks.with_streaming_response.delete(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert webhook is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.webhooks.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        webhook = await async_client.accounts.webhooks.get(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.webhooks.with_raw_response.get(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        webhook = await response.parse()
        assert_matches_type(Webhook, webhook, path=["response"])

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.webhooks.with_streaming_response.get(
            "65f1c2a9e4b0a1b2c3d4e5f6",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            webhook = await response.parse()
            assert_matches_type(Webhook, webhook, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Mock server tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.webhooks.with_raw_response.get(
                "",
            )
