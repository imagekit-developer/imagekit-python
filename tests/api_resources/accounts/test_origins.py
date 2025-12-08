# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from imagekitio import ImageKit, AsyncImageKit
from tests.utils import assert_matches_type
from imagekitio.types.accounts import OriginResponse, OriginListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOrigins:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_1(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_1(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_1(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_1(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_2(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_2(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
            s3_force_path_style=True,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_2(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_2(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_3(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_3(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_3(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_3(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_4(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_4(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
            base_url_for_canonical_header="https://cdn.example.com",
            forward_host_header_to_origin=False,
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_4(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_4(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_5(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            name="US S3 Storage",
            type="WEB_PROXY",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_5(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            name="US S3 Storage",
            type="WEB_PROXY",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_5(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            name="US S3 Storage",
            type="WEB_PROXY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_5(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            name="US S3 Storage",
            type="WEB_PROXY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_6(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_6(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="products",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_6(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_6(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_7(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_7(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="uploads",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_7(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_7(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_overload_8(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params_overload_8(self, client: ImageKit) -> None:
        origin = client.accounts.origins.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_overload_8(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_overload_8(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_1(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_1(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_1(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_1(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_1(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                access_key="AKIAIOSFODNN7EXAMPLE",
                bucket="product-images",
                name="US S3 Storage",
                secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                type="S3",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_2(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_2(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
            s3_force_path_style=True,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_2(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_2(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_2(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                access_key="AKIAIOSFODNN7EXAMPLE",
                bucket="product-images",
                endpoint="https://s3.eu-central-1.wasabisys.com",
                name="US S3 Storage",
                secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                type="S3_COMPATIBLE",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_3(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_3(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_3(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_3(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_3(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                access_key="AKIAIOSFODNN7EXAMPLE",
                bucket="product-images",
                name="US S3 Storage",
                secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                type="CLOUDINARY_BACKUP",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_4(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_4(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
            base_url_for_canonical_header="https://cdn.example.com",
            forward_host_header_to_origin=False,
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_4(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_4(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_4(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                base_url="https://images.example.com/assets",
                name="US S3 Storage",
                type="WEB_FOLDER",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_5(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_5(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_5(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_5(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_5(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                name="US S3 Storage",
                type="WEB_PROXY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_6(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_6(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="products",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_6(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_6(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_6(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                bucket="gcs-media",
                client_email="service-account@project.iam.gserviceaccount.com",
                name="US S3 Storage",
                private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
                type="GCS",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_7(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_7(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="uploads",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_7(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_7(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_7(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                account_name="account123",
                container="images",
                name="US S3 Storage",
                sas_token="?sv=2023-01-03&sr=c&sig=abc123",
                type="AZURE_BLOB",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_overload_8(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params_overload_8(self, client: ImageKit) -> None:
        origin = client.accounts.origins.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_overload_8(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_overload_8(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_overload_8(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.update(
                id="",
                base_url="https://akeneo.company.com",
                client_id="akeneo-client-id",
                client_secret="akeneo-client-secret",
                name="US S3 Storage",
                password="strongpassword123",
                type="AKENEO_PIM",
                username="integration-user",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: ImageKit) -> None:
        origin = client.accounts.origins.list()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginListResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: ImageKit) -> None:
        origin = client.accounts.origins.delete(
            "id",
        )
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert origin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_get(self, client: ImageKit) -> None:
        origin = client.accounts.origins.get(
            "id",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_get(self, client: ImageKit) -> None:
        response = client.accounts.origins.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_get(self, client: ImageKit) -> None:
        with client.accounts.origins.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_get(self, client: ImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            client.accounts.origins.with_raw_response.get(
                "",
            )


class TestAsyncOrigins:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_1(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_1(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_1(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_1(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_2(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_2(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
            s3_force_path_style=True,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_2(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_2(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_3(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_3(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_3(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_3(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_4(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_4(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
            base_url_for_canonical_header="https://cdn.example.com",
            forward_host_header_to_origin=False,
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_4(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_4(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_5(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            name="US S3 Storage",
            type="WEB_PROXY",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_5(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            name="US S3 Storage",
            type="WEB_PROXY",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_5(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            name="US S3 Storage",
            type="WEB_PROXY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_5(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            name="US S3 Storage",
            type="WEB_PROXY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_6(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_6(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="products",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_6(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_6(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_7(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_7(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="uploads",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_7(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_7(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_overload_8(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params_overload_8(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_overload_8(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_overload_8(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.create(
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_1(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_1(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_1(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_1(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_1(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                access_key="AKIAIOSFODNN7EXAMPLE",
                bucket="product-images",
                name="US S3 Storage",
                secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                type="S3",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_2(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_2(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
            s3_force_path_style=True,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_2(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_2(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            endpoint="https://s3.eu-central-1.wasabisys.com",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="S3_COMPATIBLE",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_2(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                access_key="AKIAIOSFODNN7EXAMPLE",
                bucket="product-images",
                endpoint="https://s3.eu-central-1.wasabisys.com",
                name="US S3 Storage",
                secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                type="S3_COMPATIBLE",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_3(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_3(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="raw-assets",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_3(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_3(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            access_key="AKIAIOSFODNN7EXAMPLE",
            bucket="product-images",
            name="US S3 Storage",
            secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
            type="CLOUDINARY_BACKUP",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_3(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                access_key="AKIAIOSFODNN7EXAMPLE",
                bucket="product-images",
                name="US S3 Storage",
                secret_key="wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY",
                type="CLOUDINARY_BACKUP",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_4(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_4(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
            base_url_for_canonical_header="https://cdn.example.com",
            forward_host_header_to_origin=False,
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_4(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_4(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            base_url="https://images.example.com/assets",
            name="US S3 Storage",
            type="WEB_FOLDER",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_4(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                base_url="https://images.example.com/assets",
                name="US S3 Storage",
                type="WEB_FOLDER",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_5(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_5(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_5(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_5(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            name="US S3 Storage",
            type="WEB_PROXY",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_5(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                name="US S3 Storage",
                type="WEB_PROXY",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_6(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_6(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="products",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_6(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_6(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            bucket="gcs-media",
            client_email="service-account@project.iam.gserviceaccount.com",
            name="US S3 Storage",
            private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
            type="GCS",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_6(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                bucket="gcs-media",
                client_email="service-account@project.iam.gserviceaccount.com",
                name="US S3 Storage",
                private_key="-----BEGIN PRIVATE KEY-----\\nMIIEv...",
                type="GCS",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_7(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_7(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
            prefix="uploads",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_7(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_7(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            account_name="account123",
            container="images",
            name="US S3 Storage",
            sas_token="?sv=2023-01-03&sr=c&sig=abc123",
            type="AZURE_BLOB",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_7(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                account_name="account123",
                container="images",
                name="US S3 Storage",
                sas_token="?sv=2023-01-03&sr=c&sig=abc123",
                type="AZURE_BLOB",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_overload_8(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params_overload_8(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
            base_url_for_canonical_header="https://cdn.example.com",
            include_canonical_header=False,
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_overload_8(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_overload_8(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.update(
            id="id",
            base_url="https://akeneo.company.com",
            client_id="akeneo-client-id",
            client_secret="akeneo-client-secret",
            name="US S3 Storage",
            password="strongpassword123",
            type="AKENEO_PIM",
            username="integration-user",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_overload_8(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.update(
                id="",
                base_url="https://akeneo.company.com",
                client_id="akeneo-client-id",
                client_secret="akeneo-client-secret",
                name="US S3 Storage",
                password="strongpassword123",
                type="AKENEO_PIM",
                username="integration-user",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.list()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginListResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginListResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.delete(
            "id",
        )
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.delete(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert origin is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.delete(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert origin is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.delete(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_get(self, async_client: AsyncImageKit) -> None:
        origin = await async_client.accounts.origins.get(
            "id",
        )
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_get(self, async_client: AsyncImageKit) -> None:
        response = await async_client.accounts.origins.with_raw_response.get(
            "id",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        origin = await response.parse()
        assert_matches_type(OriginResponse, origin, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncImageKit) -> None:
        async with async_client.accounts.origins.with_streaming_response.get(
            "id",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            origin = await response.parse()
            assert_matches_type(OriginResponse, origin, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_get(self, async_client: AsyncImageKit) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `id` but received ''"):
            await async_client.accounts.origins.with_raw_response.get(
                "",
            )
