import base64
import json
import sys

sys.path.append("..")

# #### set your private_key public_key, url_endpoint, url ### ##
private_key = "your_public_api_key"
public_key = "your_private_api_key"
url_endpoint = "https://ik.imagekit.io/your_imagekit_id/"
# dummy image url
url = "https://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg"

if __name__ == "__main__":
    from imagekitio.client import ImageKit

    imagekit = ImageKit(
        private_key=private_key, public_key=public_key, url_endpoint=url_endpoint,
    )

    # The signed url generated for this file doesn't work using the Python SDK

    upload = imagekit.upload_file(
        file=open("sample.jpg", "rb"),
        file_name="testing_upload_binary_signed_private.jpg",
        options={
            "use_unique_file_name": 'false',
            "response_fields": ["is_private_file", "tags"],
            "is_private_file": True,
            "folder": "/testing-python-folder/",
            "tags": ["abc", "def"],
            "extensions": json.dumps(
                ({"name": "remove-bg", "options": {"add_shadow": True, "bg_color": "pink"}},
                 {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10})
            ),
            "webhook_url": "https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
            "overwrite_file": False,
            "overwrite_a_i_tags": False,
            "overwrite_tags": False,
            "overwrite_custom_metadata": True,
            "custom_metadata": json.dumps({"test100": 11})
        },
    )

    print("-------------------------------------")
    print("Upload with binary")
    print("-------------------------------------")
    print(upload)

    upload = imagekit.upload_file(
        file=url,
        file_name="testing-url.jpg",
        options={
            "response_fields": ["is_private_file"],
            "is_private_file": False,
            "tags": ["abc", "def"],
        },
    )

    print("-------------------------------------")
    print("Upload with url")
    print("-------------------------------------")
    print(upload, end="\n\n")

    with open("sample.jpg", mode="rb") as img:
        imgstr = base64.b64encode(img.read())

    upload_base64 = imagekit.upload_file(
        file=imgstr,
        file_name="testing-base64.jpg",
        options={
            "response_fields": ["is_private_file", "metadata", "tags"],
            "is_private_file": False,
            "tags": ["abc", "def"],
        },
    )

    print("-------------------------------------")
    print("Upload with base64")
    print("-------------------------------------")
    print(upload_base64, end="\n\n")

    image_url = imagekit.url(
        {
            "path": upload['response']['filePath'],
            "query_parameters": {"v": "123"},
            "transformation": [{"overlay_image": "/demo1/new_car.jpg", "default_image": "/demo1/default-image.jpg"}],
            "signed": True,
            "expire_seconds": 3000,
        }
    )

    print("-------------------------------------")
    print("Signed url")
    print("-------------------------------------")
    print(image_url, end="\n\n")

    # URL generation using image path and image hostname
    image_url = imagekit.url(
        {
            "path": "default-image.jpg",
            "url_endpoint": url_endpoint,
            "transformation": [{"height": "300", "width": "400"}],
        }
    )

    print("-------------------------------------")
    print("Url using image path")
    print("-------------------------------------")
    print(image_url, end="\n\n")

    # 2 Using full image URL
    image_url = imagekit.url(
        {
            "src": url_endpoint.rstrip("/") + "/default-image.jpg",
            "transformation": [{"height": "300", "width": "400"}],
        }
    )

    print("-------------------------------------")
    print("Url using src")
    print("-------------------------------------")
    print(image_url, end="\n\n")

    image_url = imagekit.url(
        {
            "path": "/default-image.jpg",
            "url_endpoint": "https://ik.imagekit.io/zv3rkhsym/",
            "transformation": [{"height": "300", "width": "400", "raw": "ar-4-3,q-40"}],
        }
    )

    print("-------------------------------------")
    print("Chained transformation")
    print("-------------------------------------")
    print(image_url, end="\n\n")

    image_url = imagekit.url(
        {
            "src": url_endpoint.rstrip("/") + "/default-image.jpg",
            "transformation": [
                {
                    "format": "jpg",
                    "progressive": "true",
                    "effect_sharpen": "-",
                    "effect_contrast": "1",
                }
            ],
        }
    )

    print("-------------------------------------")
    print("Sharpening and contrast transformation")
    print("-------------------------------------")
    print(image_url, end="\n\n")

    list_files = imagekit.list_files({"type": "file", "sort": "ASC_CREATED", "path": "/",
                                      "searchQuery": "createdAt >= '2d' OR size < '2mb' OR format='png'",
                                      "fileType": "all", "limit": 5, "skip": 0,
                                      "tags": "Software, Developer, Engineer"})
    bulk_ids = [
        list_files['response']['list'][0]['file_id'],
        list_files['response']['list'][1]['file_id'],
    ]

    print("-------------------------------------")
    print("List files")
    print("-------------------------------------")
    print(list_files, end="\n\n")

    details = imagekit.get_file_details("file_id")
    print("-------------------------------------")
    print("Get file details")
    print("-------------------------------------")
    print(details, end="\n\n")

    file_versions = imagekit.get_file_versions('62a9c3ccd875ec6fd658c854')
    print("-------------------------------------")
    print("Get file versions")
    print("-------------------------------------")
    print(file_versions, end="\n\n")

    file_versions_details = imagekit.get_file_version_details('62a9c3ccd875ec6fd658c854', '62b97749f63122840530fda9')
    print("-------------------------------------")
    print("Get file version details")
    print("-------------------------------------")
    print(file_versions_details, end="\n\n")

    updated_detail = imagekit.update_file_details(
        "62d92afaef493b90ba8ce296",
        {"remove_a_i_tags": ['floor', 'Fixure'],
         "webhook_url": "https://webhook.site/c78d617f-33bc-40d9-9e61-608999721e2e",
         "extensions": [{"name": "remove-bg", "options": {"add_shadow": True, "bg_color": "red"}},
                        {"name": "google-auto-tagging", "minConfidence": 80, "maxTags": 10}],
         "tags": ["abc", "def"], "custom_coordinates": "10,10,100,100", "custom_metadata": {"test": 11}},
    )

    print("-------------------------------------")
    print("Update file details")
    print("-------------------------------------")
    print(updated_detail, end="\n\n")

    tags = imagekit.add_tags(file_ids=['62d501a785aace394ec4bb10'], tags=['abc', 'def'])
    print("-------------------------------------")
    print("Add tags")
    print("-------------------------------------")
    print(tags, end="\n\n")

    remove_tags = imagekit.remove_tags(file_ids=['62d501a785aace394ec4bb10'], tags=['abc', 'def'])
    print("-------------------------------------")
    print("Remove tags")
    print("-------------------------------------")
    print(remove_tags, end="\n\n")

    remove_ai_tags = imagekit.remove_ai_tags(file_ids=['62a9c3ccd875ec6fd658c854'], a_i_tags=['Plant'])
    print("-------------------------------------")
    print("Remove AI tags")
    print("-------------------------------------")
    print(remove_ai_tags, end="\n\n")

    delete = imagekit.delete_file('62b2bbwed231537b1489706f')
    print("-------------------------------------")
    print("Delete file")
    print("-------------------------------------")
    print(delete, end="\n\n")

    delete_file_version = imagekit.delete_file_version("62a9c3ccd875ec6fd658c854", "62b985cc9f0ad486863282ab")
    print("-------------------------------------")
    print("Delete file version")
    print("-------------------------------------")
    print(delete_file_version, end="\n\n")

    print("-------------------------------------")
    print("Bulk file delete")
    print("-------------------------------------")
    print(imagekit.bulk_file_delete(file_ids=['62ad8a3b514f86178637fdcb']), end="\n\n")

    copy_file = imagekit.copy_file(options={"source_file_path": "/new_car.jpg",
                                            "destination_path": "/test",
                                            "include_file_versions": True})
    print("-------------------------------------")
    print("Copy file")
    print("-------------------------------------")
    print(copy_file, end="\n\n")

    move_file = imagekit.move_file(options={"source_file_path": "/new_car1.jpg",
                                            "destination_path": "/test"})
    print("-------------------------------------")
    print("Move file")
    print("-------------------------------------")
    print(move_file, end="\n\n")

    rename_file = imagekit.rename_file(options={"file_path": "/_testing-binary.jpg",
                                                "new_file_name": "testing-binary.jpg",
                                                "purge_cache": True})
    print("-------------------------------------")
    print("Rename file")
    print("-------------------------------------")
    print(rename_file, end="\n\n")

    restore_file_version = imagekit.restore_file_version("62a9c3ccd875ec6fd658c854", "62a9c3ccd875ec6fd658c854")
    print("-------------------------------------")
    print("Restore file version")
    print("-------------------------------------")
    print(restore_file_version, end="\n\n")

    create_folder = imagekit.create_folder(options={"folder_name": "/demo", "parent_folder_path": "/"})
    print("-------------------------------------")
    print("Create folder")
    print("-------------------------------------")
    print(create_folder, end="\n\n")

    delete_folder = imagekit.delete_folder(options={"folder_path": "/demo1/demo"})
    print("-------------------------------------")
    print("Delete folder")
    print("-------------------------------------")
    print(delete_folder, end="\n\n")

    copy_folder = imagekit.copy_folder(options={"source_folder_path": "/testsssss",
                                                "destination_path": "/test1",
                                                "include_file_versions": True})
    print("-------------------------------------")
    print("Copy folder")
    print("-------------------------------------")
    print(copy_folder, end="\n\n")

    move_folder = imagekit.move_folder(options={"source_folder_path": "/test2",
                                                "destination_path": "/test2"})
    print("-------------------------------------")
    print("Move folder")
    print("-------------------------------------")
    print(move_folder, end="\n\n")

    job_status = imagekit.get_bulk_job_status("62de84fb1b02a58936cc740c")
    print("-------------------------------------")
    print("Bulk job status")
    print("-------------------------------------")
    print(job_status, end="\n\n")

    purge_cache = imagekit.purge_file_cache(
        file_url="https://ik.imagekit.io/your/sample_To_fa4v8vk7.jpg?ik-sdk-version=javascript-1.4.3&updatedAt=1655976201437")
    print("-------------------------------------")
    print("Purge cache")
    print("-------------------------------------")
    print(purge_cache, end="\n\n")

    request_id = "62df7e731b02a5893Ee7e3dd"
    purge_cache_status = imagekit.get_purge_file_cache_status(request_id)

    print("-------------------------------------")
    print("Cache status")
    print("-------------------------------------")
    print(purge_cache_status, end="\n\n")

    file_metadata = imagekit.get_file_metadata("62a9c3ccd875ec6fd658c85W")
    print("-------------------------------------")
    print("File metadata")
    print("-------------------------------------")
    print(file_metadata, end="\n\n")

    print("-------------------------------------")
    print("Get metadata via url")
    print("-------------------------------------")
    print(imagekit.get_remote_file_url_metadata("https://example.com/fakeid/fakeimage.jpg"))

    print("-------------------------------------")
    print("Create custom metadata fields number type")
    print("-------------------------------------")
    print(imagekit.create_custom_metadata_fields(options={"name": "test-py-f",
                                                          "label": "test-py-f",
                                                          "schema":
                                                              {"type": "Number",
                                                               "min_value": 100,
                                                               "max_value": 200}
                                                          }
                                                 ))

    print("-------------------------------------")
    print("Create custom metadata fields textarea type")
    print("-------------------------------------")
    print(imagekit.create_custom_metadata_fields(options={"name": "test-py-ar",
                                                          "label": "test-py-area",
                                                          "schema":
                                                              {
                                                                  "is_value_required": True,
                                                                  "default_value": "The",
                                                                  "type": "Textarea",
                                                                  "min_length": 3,
                                                                  "max_length": 200}
                                                          }
                                                 ))

    print("-------------------------------------")
    print("Create custom metadata fields date type")
    print("-------------------------------------")
    print(imagekit.create_custom_metadata_fields(options={"name": "test-date",
                                                          "label": "test-date",
                                                          "schema":
                                                              {
                                                                  "type": "Date",
                                                                  "min_value": "2022-11-29T10:11:10+00:00",
                                                                  "max_value": "2022-11-30T10:11:10+00:00"}
                                                          }
                                                 ))

    print("-------------------------------------")
    print("Create custom metadata fields boolean type")
    print("-------------------------------------")
    print(imagekit.create_custom_metadata_fields(options={"name": "test-boolean",
                                                          "label": "test-boolean",
                                                          "schema":
                                                              {
                                                                  "type": "Boolean",
                                                                  "is_value_required": True,
                                                                  "default_value": True,
                                                              }
                                                          }
                                                 ))

    print("-------------------------------------")
    print("Create custom metadata fields SingleSelect type")
    print("-------------------------------------")
    print(imagekit.create_custom_metadata_fields(options={"name": "test-sing-sel",
                                                          "label": "test-sing-sel",
                                                          "schema":
                                                              {
                                                                  "type": "SingleSelect",
                                                                  "select_options": ["small", "medium", "large", 30, 40,
                                                                                     True]
                                                              }
                                                          }
                                                 ))

    print("-------------------------------------")
    print("Create custom metadata fields MultiSelect type")
    print("-------------------------------------")
    print(imagekit.create_custom_metadata_fields(options={"name": "test-mul-sel",
                                                          "label": "test-mul-sel",
                                                          "schema":
                                                              {
                                                                  "type": "MultiSelect",
                                                                  "is_value_required": True,
                                                                  "default_value": ["small", 30, True],
                                                                  "select_options": ["small", "medium", "large", 30, 40,
                                                                                     True]
                                                              }
                                                          }
                                                 ))

    print("-------------------------------------")
    print("Get custom metatdata fields")
    print("-------------------------------------")
    print(imagekit.get_custom_metadata_fields())

    print("-------------------------------------")
    print("Update custom metadata fields")
    print("-------------------------------------")
    print(imagekit.update_custom_metadata_fields("if", options={"label": "test-update-number",
                                                                "schema":
                                                                    {
                                                                        "min_value": 100,
                                                                        "max_value": 200
                                                                    }
                                                                }
                                                 ))

    print("-------------------------------------")
    print("Delete custom metatdata fields via custom metatdata fields's id")
    print("-------------------------------------")
    print(imagekit.delete_custom_metadata_field("62a85e97663ef7E5173ba63f"))

    auth_params = imagekit.get_authentication_parameters()
    print("-------------------------------------")
    print("Auth params")
    print("-------------------------------------")
    print(auth_params, end="\n\n")

    print("-------------------------------------")
    print("Phash distance")
    print("-------------------------------------")
    print(imagekit.phash_distance("f06830ca9f1e3e90", "f06830ca9f1e3e90"), end="\n\n")
