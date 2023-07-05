import json

import responses
from responses import matchers

from imagekitio.constants.url import URL
from imagekitio.exceptions.BadRequestException import BadRequestException
from imagekitio.exceptions.ForbiddenException import ForbiddenException
from imagekitio.exceptions.NotFoundException import NotFoundException
from imagekitio.exceptions.UnknownException import UnknownException
from imagekitio.models.CreateCustomMetadataFieldsRequestOptions import (
    CreateCustomMetadataFieldsRequestOptions,
)
from imagekitio.models.CustomMetaDataTypeEnum import CustomMetaDataTypeEnum
from imagekitio.models.CustomMetadataFieldsSchema import CustomMetadataFieldsSchema
from imagekitio.models.UpdateCustomMetadataFieldsRequestOptions import (
    UpdateCustomMetadataFieldsRequestOptions,
)
from imagekitio.utils.formatter import camel_dict_to_snake_dict
from tests.helpers import (
    ClientTestCase,
    create_headers_for_test,
)


class TestCustomMetadataFields(ClientTestCase):
    """
    TestCustomMetadataFields class used to test CRUD methods of custom metadata fields
    """

    field_id = "field_id"

    @responses.activate
    def test_get_custom_metadata_fields_fails_on_unauthenticated_request(self):
        """
        Tests if the unauthenticated request restricted
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.GET,
                url,
                status=403,
                body="""{"message": "Your account cannot be authenticated."
                                    , "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.get_custom_metadata_fields(True)
            self.assertRaises(ForbiddenException)
        except UnknownException as e:
            self.assertEqual(e.message, "Your account cannot be authenticated.")
            self.assertEqual(403, e.response_metadata.http_status_code)

    @responses.activate
    def test_get_custom_metadata_fields_succeeds(self):
        """
        Tests if get_custom_metadata_fields succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""[{
                        "id": "62a9d5f6db485107347bb7f2",
                        "name": "test10",
                        "label": "test10",
                        "schema": {
                            "type": "Number",
                            "isValueRequired": false,
                            "minValue": 10,
                            "maxValue": 1000
                        }
                    }, {
                        "id": "62aab2cfdb4851833b8f5e64",
                        "name": "test11",
                        "label": "test11",
                        "schema": {
                            "type": "Number",
                            "isValueRequired": false,
                            "minValue": 10,
                            "maxValue": 1000
                        }
                    }]""",
            match=[matchers.query_string_matcher("includeDeleted=false")],
            headers=headers,
        )
        resp = self.client.get_custom_metadata_fields()

        mock_response_metadata = {
            "raw": [
                {
                    "id": "62a9d5f6db485107347bb7f2",
                    "name": "test10",
                    "label": "test10",
                    "schema": {
                        "type": "Number",
                        "isValueRequired": False,
                        "minValue": 10,
                        "maxValue": 1000,
                    },
                },
                {
                    "id": "62aab2cfdb4851833b8f5e64",
                    "name": "test11",
                    "label": "test11",
                    "schema": {
                        "type": "Number",
                        "isValueRequired": False,
                        "minValue": 10,
                        "maxValue": 1000,
                    },
                },
            ],
            "httpStatusCode": 200,
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("62a9d5f6db485107347bb7f2", resp.list[0].id)
        self.assertEqual("62aab2cfdb4851833b8f5e64", resp.list[1].id)
        self.assertEqual(
            "http://test.com/v1/customMetadataFields?includeDeleted=false",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_get_custom_metadata_fields_succeeds_with_include_deleted_true(self):
        """
        Tests if get_custom_metadata_fields succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""[{
                        "id": "62a9d5f6db485107347bb7f2",
                        "name": "test10",
                        "label": "test10",
                        "schema": {
                            "type": "Number",
                            "isValueRequired": false,
                            "minValue": 10,
                            "maxValue": 1000
                        }
                    }, {
                        "id": "62aab2cfdb4851833b8f5e64",
                        "name": "test11",
                        "label": "test11",
                        "schema": {
                            "type": "Number",
                            "isValueRequired": false,
                            "minValue": 10,
                            "maxValue": 1000
                        }
                    }]""",
            match=[matchers.query_string_matcher("includeDeleted=true")],
            headers=headers,
        )
        resp = self.client.get_custom_metadata_fields(include_deleted=True)

        mock_response_metadata = {
            "raw": [
                {
                    "id": "62a9d5f6db485107347bb7f2",
                    "name": "test10",
                    "label": "test10",
                    "schema": {
                        "type": "Number",
                        "isValueRequired": False,
                        "minValue": 10,
                        "maxValue": 1000,
                    },
                },
                {
                    "id": "62aab2cfdb4851833b8f5e64",
                    "name": "test11",
                    "label": "test11",
                    "schema": {
                        "type": "Number",
                        "isValueRequired": False,
                        "minValue": 10,
                        "maxValue": 1000,
                    },
                },
            ],
            "httpStatusCode": 200,
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("62a9d5f6db485107347bb7f2", resp.list[0].id)
        self.assertEqual("62aab2cfdb4851833b8f5e64", resp.list[1].id)
        self.assertEqual(
            "http://test.com/v1/customMetadataFields?includeDeleted=true",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_get_custom_metadata_fields_succeeds_with_additional_attributes_in_response(self):
        """
        Tests if get_custom_metadata_fields succeeds with additional responses
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = create_headers_for_test()
        responses.add(
            responses.GET,
            url,
            body="""[{
                        "id": "62a9d5f6db485107347bb7f2",
                        "name": "test10",
                        "label": "test10",
                        "schema": {
                            "type": "Number",
                            "isValueRequired": false,
                            "minValue": 10,
                            "maxValue": 1000,
                            "currentValue":100
                        }
                    }, {
                        "id": "62aab2cfdb4851833b8f5e64",
                        "name": "test11",
                        "label": "test11",
                        "schema": {
                            "type": "Number",
                            "isValueRequired": false,
                            "minValue": 10,
                            "maxValue": 1000,
                            "currentValue":1000
                        }
                    }]""",
            match=[matchers.query_string_matcher("includeDeleted=true")],
            headers=headers,
        )
        resp = self.client.get_custom_metadata_fields(include_deleted=True)

        mock_response_metadata = {
            "raw": [
                {
                    "id": "62a9d5f6db485107347bb7f2",
                    "name": "test10",
                    "label": "test10",
                    "schema": {
                        "type": "Number",
                        "isValueRequired": False,
                        "minValue": 10,
                        "maxValue": 1000,
                        "currentValue":100
                    },
                },
                {
                    "id": "62aab2cfdb4851833b8f5e64",
                    "name": "test11",
                    "label": "test11",
                    "schema": {
                        "type": "Number",
                        "isValueRequired": False,
                        "minValue": 10,
                        "maxValue": 1000,
                        "currentValue":1000
                    },
                },
            ],
            "httpStatusCode": 200,
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(resp.list[0].schema.current_value,100)
        self.assertEqual(resp.list[1].schema.current_value,1000)
        self.assertEqual(resp.list[0].random,None)

    @responses.activate
    def test_delete_custom_metadata_fields_succeeds(self):
        """
        Tests if delete_custom_metadata_fields succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, self.field_id)
        headers = create_headers_for_test()
        responses.add(responses.DELETE, url, status=204, headers=headers, body="{}")
        resp = self.client.delete_custom_metadata_field(self.field_id)

        mock_response_metadata = {
            "raw": None,
            "httpStatusCode": 204,
            "headers": {
                "Content-Type": "text/plain",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/customMetadataFields/field_id",
            responses.calls[0].request.url,
        )

    @responses.activate
    def test_delete_custom_metadata_fields_fails_with_404(self):
        """
        Tests if delete_custom_metadata_fields succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, self.field_id)
        try:
            headers = create_headers_for_test()
            responses.add(
                responses.DELETE,
                url,
                status=404,
                headers=headers,
                body="""{"message": "No such custom metadata field exists",
                                 "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.delete_custom_metadata_field(self.field_id)
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No such custom metadata field exists", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_create_custom_metadata_fields_fails_with_400(self):
        """
        Tests if create_custom_metadata_fields fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        try:
            responses.add(
                responses.POST,
                url,
                status=400,
                body="""{"message": "A custom metadata field with this name already exists"
                                    , "help": "For support kindly contact us at support@imagekit.io ."}""",
            )
            self.client.create_custom_metadata_fields(
                options=CreateCustomMetadataFieldsRequestOptions(
                    name="test",
                    label="test",
                    schema=CustomMetadataFieldsSchema(
                        type=CustomMetaDataTypeEnum.Number, min_value=100, max_value=200
                    ),
                )
            )
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual(
                "A custom metadata field with this name already exists", e.message
            )
            self.assertEqual(400, e.response_metadata.http_status_code)

    @responses.activate
    def test_create_custom_metadata_fields_succeeds_with_type_number(self):
        """
        Tests if create_custom_metadata_fields succeeds with type number
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=201,
            headers=headers,
            body="""{
                "id": "62dfc03b1b02a58936efca37",
                "name": "test",
                "label": "test",
                "schema": {
                    "type": "Number",
                    "minValue": 100,
                    "maxValue": 200
                }
            }""",
        )
        resp = self.client.create_custom_metadata_fields(
            options=CreateCustomMetadataFieldsRequestOptions(
                name="test",
                label="test",
                schema=CustomMetadataFieldsSchema(
                    type=CustomMetaDataTypeEnum.Number, min_value=100, max_value=200
                ),
            )
        )

        mock_response_metadata = {
            "raw": {
                "id": "62dfc03b1b02a58936efca37",
                "name": "test",
                "label": "test",
                "schema": {"type": "Number", "minValue": 100, "maxValue": 200},
            },
            "httpStatusCode": 201,
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }

        request_body = json.dumps(
            json.loads(
                """{
                "name": "test",
                "label": "test",
                "schema": {
                    "type": "Number",
                    "minValue": 100,
                    "maxValue": 200
                }
            }"""
            )
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/customMetadataFields", responses.calls[0].request.url
        )
        self.assertMultiLineEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_create_custom_metadata_fields_succeeds_with_type_textarea(self):
        """
        Tests if create_custom_metadata_fields succeeds with type textarea
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=201,
            headers=headers,
            body="""{
                "id": "62e0d7ae1b02a589360dc1fd",
                "name": "test",
                "label": "test",
                "schema": {
                    "isValueRequired": true,
                    "defaultValue": "The",
                    "type": "Textarea",
                    "minLength": 3,
                    "maxLength": 200
                }
            }""",
        )
        resp = self.client.create_custom_metadata_fields(
            options=CreateCustomMetadataFieldsRequestOptions(
                name="test",
                label="test",
                schema=CustomMetadataFieldsSchema(
                    is_value_required=True,
                    default_value="The",
                    type=CustomMetaDataTypeEnum.Textarea,
                    min_length=3,
                    max_length=200,
                ),
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 201,
            "raw": {
                "id": "62e0d7ae1b02a589360dc1fd",
                "label": "test",
                "name": "test",
                "schema": {
                    "defaultValue": "The",
                    "isValueRequired": True,
                    "maxLength": 200,
                    "minLength": 3,
                    "type": "Textarea",
                },
            },
        }

        request_body = json.dumps(
            json.loads(
                """{
                "name": "test",
                "label": "test",
                "schema": {
                    "type": "Textarea",
                    "defaultValue": "The",
                    "isValueRequired": true,
                    "minLength": 3,
                    "maxLength": 200
                }
            }"""
            )
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/customMetadataFields", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_create_custom_metadata_fields_succeeds_with_type_date(self):
        """
        Tests if create_custom_metadata_fields succeeds with type date
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=201,
            headers=headers,
            body="""{
                "id": "62dfc9f41b02a58936f0d284",
                "name": "test-date",
                "label": "test-date",
                "schema": {
                    "type": "Date",
                    "minValue": "2022-11-29T10:11:10+00:00",
                    "maxValue": "2022-11-30T10:11:10+00:00"
                }
            }""",
        )
        resp = self.client.create_custom_metadata_fields(
            options=CreateCustomMetadataFieldsRequestOptions(
                name="test-date",
                label="test-date",
                schema=CustomMetadataFieldsSchema(
                    type=CustomMetaDataTypeEnum.Date,
                    min_value="2022-11-29T10:11:10+00:00",
                    max_value="2022-11-30T10:11:10+00:00",
                ),
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 201,
            "raw": {
                "id": "62dfc9f41b02a58936f0d284",
                "label": "test-date",
                "name": "test-date",
                "schema": {
                    "maxValue": "2022-11-30T10:11:10+00:00",
                    "minValue": "2022-11-29T10:11:10+00:00",
                    "type": "Date",
                },
            },
        }

        request_body = json.dumps(
            json.loads(
                """{
                "name": "test-date",
                "label": "test-date",
                "schema": {
                    "type": "Date",
                    "minValue": "2022-11-29T10:11:10+00:00",
                    "maxValue": "2022-11-30T10:11:10+00:00"
                }
            }"""
            )
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/customMetadataFields", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_create_custom_metadata_fields_succeeds_with_type_boolean(self):
        """
        Tests if create_custom_metadata_fields succeeds with type boolean
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=201,
            headers=headers,
            body="""{
                "id": "62dfcb801b02a58936f0fc39",
                "name": "test-boolean",
                "label": "test-boolean",
                "schema": {
                    "type": "Boolean",
                    "isValueRequired": true,
                    "defaultValue": true
                }
            }""",
        )
        resp = self.client.create_custom_metadata_fields(
            options=CreateCustomMetadataFieldsRequestOptions(
                name="test-boolean",
                label="test-boolean",
                schema=CustomMetadataFieldsSchema(
                    type=CustomMetaDataTypeEnum.Boolean,
                    is_value_required=True,
                    default_value=True,
                ),
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 201,
            "raw": {
                "id": "62dfcb801b02a58936f0fc39",
                "label": "test-boolean",
                "name": "test-boolean",
                "schema": {
                    "defaultValue": True,
                    "isValueRequired": True,
                    "type": "Boolean",
                },
            },
        }

        request_body = json.dumps(
            json.loads(
                """{
                "name": "test-boolean",
                "label": "test-boolean",
                "schema": {
                    "type": "Boolean",
                    "defaultValue": true,
                    "isValueRequired": true
                }
            }"""
            )
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/customMetadataFields", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_create_custom_metadata_fields_succeeds_with_type_single_select(self):
        """
        Tests if create_custom_metadata_fields succeeds with type SingleSelect
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=201,
            headers=headers,
            body="""{
                "id": "62dfcdb21b02a58936f14c97",
                "name": "test",
                "label": "test",
                "schema": {
                    "type": "SingleSelect",
                    "selectOptions": ["small", "medium", "large", 30, 40, true]
                }
            }""",
        )
        resp = self.client.create_custom_metadata_fields(
            options=CreateCustomMetadataFieldsRequestOptions(
                name="test",
                label="test",
                schema=CustomMetadataFieldsSchema(
                    type=CustomMetaDataTypeEnum.SingleSelect,
                    select_options=["small", "medium", "large", 30, 40, True],
                ),
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 201,
            "raw": {
                "id": "62dfcdb21b02a58936f14c97",
                "label": "test",
                "name": "test",
                "schema": {
                    "selectOptions": ["small", "medium", "large", 30, 40, True],
                    "type": "SingleSelect",
                },
            },
        }

        request_body = json.dumps(
            json.loads(
                """{
                "name": "test",
               "label": "test",
               "schema":
                   {
                       "type": "SingleSelect",
                       "selectOptions": ["small", "medium", "large", 30, 40,
                                         true]
                   }
               }"""
            )
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/customMetadataFields", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_create_custom_metadata_fields_succeeds_with_type_multi_select(self):
        """
        Tests if create_custom_metadata_fields succeeds with type MultiSelect
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields".format(URL.API_BASE_URL)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.POST,
            url,
            status=201,
            headers=headers,
            body="""{
                "id": "62dfcf001b02a58936f17808",
                "name": "test",
                "label": "test",
                "schema": {
                    "type": "MultiSelect",
                    "isValueRequired": true,
                    "defaultValue": ["small", 30, true],
                    "selectOptions": ["small", "medium", "large", 30, 40, true]
                }
            }""",
        )
        resp = self.client.create_custom_metadata_fields(
            options=CreateCustomMetadataFieldsRequestOptions(
                name="test",
                label="test",
                schema=CustomMetadataFieldsSchema(
                    type=CustomMetaDataTypeEnum.MultiSelect,
                    is_value_required=True,
                    default_value=["small", 30, True],
                    select_options=["small", "medium", "large", 30, 40, True],
                ),
            )
        )

        mock_response_metadata = {
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
            "httpStatusCode": 201,
            "raw": {
                "id": "62dfcf001b02a58936f17808",
                "label": "test",
                "name": "test",
                "schema": {
                    "defaultValue": ["small", 30, True],
                    "isValueRequired": True,
                    "selectOptions": ["small", "medium", "large", 30, 40, True],
                    "type": "MultiSelect",
                },
            },
        }

        request_body = json.dumps(
            json.loads(
                """{
                "name": "test",
                "label": "test",
                "schema": {
                    "type": "MultiSelect",
                    "selectOptions": ["small", "medium", "large", 30, 40, true],
                    "defaultValue": ["small", 30, true],
                    "isValueRequired": true
                }
            }"""
            )
        )
        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual(
            "http://test.com/v1/customMetadataFields", responses.calls[0].request.url
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_update_custom_metadata_fields_succeeds(self):
        """
        Tests if update_custom_metadata_fields succeeds
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, self.field_id)
        headers = {"Content-Type": "application/json"}
        headers.update(create_headers_for_test())
        responses.add(
            responses.PATCH,
            url,
            headers=headers,
            body="""{
                "id": "62a9d5f6db485107347bb7f2",
                "name": "test",
                "label": "test-update",
                "schema": {
                    "minValue": 100,
                    "maxValue": 200,
                    "type": "Number"
                }
            }""",
        )

        resp = self.client.update_custom_metadata_fields(
            self.field_id,
            options=UpdateCustomMetadataFieldsRequestOptions(
                label="test-update",
                schema=CustomMetadataFieldsSchema(min_value=100, max_value=200),
            ),
        )

        mock_response_metadata = {
            "raw": {
                "id": "62a9d5f6db485107347bb7f2",
                "name": "test",
                "label": "test-update",
                "schema": {"minValue": 100, "maxValue": 200, "type": "Number"},
            },
            "httpStatusCode": 200,
            "headers": {
                "Content-Type": "text/plain, application/json",
                "Accept-Encoding": "gzip, deflate",
                "Authorization": "Basic ZmFrZTEyMjo=",
            },
        }

        request_body = json.dumps(
            json.loads(
                """{
                "label": "test-update",
                "schema": {
                    "minValue": 100,
                    "maxValue": 200
                }
            }"""
            )
        )

        self.assertEqual(
            camel_dict_to_snake_dict(mock_response_metadata),
            resp.response_metadata.__dict__,
        )
        self.assertEqual("62a9d5f6db485107347bb7f2", resp.id)
        self.assertEqual(
            "http://test.com/v1/customMetadataFields/field_id",
            responses.calls[0].request.url,
        )
        self.assertEqual(request_body, responses.calls[0].request.body)

    @responses.activate
    def test_update_custom_metadata_fields_fails_with_404(self):
        """
        Tests if update_custom_metadata_fields fails with 404
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, self.field_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=404,
                body="""{
                    "message": "No such custom metadata field exists",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
            )

            self.client.update_custom_metadata_fields(
                self.field_id,
                options=UpdateCustomMetadataFieldsRequestOptions(
                    label="test-update",
                    schema=CustomMetadataFieldsSchema(min_value=100, max_value=200),
                ),
            )
            self.assertRaises(NotFoundException)
        except NotFoundException as e:
            self.assertEqual("No such custom metadata field exists", e.message)
            self.assertEqual(404, e.response_metadata.http_status_code)

    @responses.activate
    def test_update_custom_metadata_fields_fails_with_400(self):
        """
        Tests if update_custom_metadata_fields fails with 400
        """
        URL.API_BASE_URL = "http://test.com"
        url = "{}/v1/customMetadataFields/{}".format(URL.API_BASE_URL, self.field_id)
        try:
            responses.add(
                responses.PATCH,
                url,
                status=400,
                body="""{
                    "message": "Your request contains invalid ID parameter.",
                    "help": "For support kindly contact us at support@imagekit.io ."
                }""",
            )

            self.client.update_custom_metadata_fields(
                self.field_id,
                options=UpdateCustomMetadataFieldsRequestOptions(
                    label="test-update",
                    schema=CustomMetadataFieldsSchema(min_value=100, max_value=200),
                ),
            )
            self.assertRaises(BadRequestException)
        except BadRequestException as e:
            self.assertEqual("Your request contains invalid ID parameter.", e.message)
            self.assertEqual(400, e.response_metadata.http_status_code)
