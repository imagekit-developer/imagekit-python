# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio._utils import parse_date
from imagekitio.types.accounts import UsageGetResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsage:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        usage = client.accounts.usage.get(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.accounts.usage.with_raw_response.get(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = response.parse()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.accounts.usage.with_streaming_response.get(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = response.parse()
            assert_matches_type(UsageGetResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsage:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        usage = await async_client.accounts.usage.get(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.usage.with_raw_response.get(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        usage = await response.parse()
        assert_matches_type(UsageGetResponse, usage, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.usage.with_streaming_response.get(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            usage = await response.parse()
            assert_matches_type(UsageGetResponse, usage, path=["response"])

        assert cast(Any, response.is_closed) is True
