import base64
import sys

sys.path.append("..")

# #### set your private_key public_key, url_endpoint, url ### ##
private_key = ""
public_key = ""
url_endpoint = ""
# dummy image url
url = "https://file-examples.com/wp-content/uploads/2017/10/file_example_JPG_100kB.jpg"

if __name__ == "__main__":
    from imagekitio.client import ImageKit

    imagekit = ImageKit(
        private_key=private_key, public_key=public_key, url_endpoint=url_endpoint,
    )

    # URL generation using image path and image hostname
    # 1
    print(imagekit.ik_request.private_key)
    print("-------------------------------------")

    image_url = imagekit.url(
        {
            "path": "default-image.jpg",
            "url_endpoint": url_endpoint,
            "transformation": [{"height": "300", "width": "400"}],
        }
    )

    print("url", image_url, end="\n\n")
    print("-------------------------------------")

    # 2 Using full image URL
    image_url = imagekit.url(
        {
            "src": url_endpoint.rstrip("/") + "/default-image.jpg",
            "transformation": [{"height": "300", "width": "400"}],
        }
    )

    print("Url using full image url", image_url, end="\n\n")

    # chained Transformations as a query parameter
    print("-------------------------------------")

    image_url = imagekit.url(
        {
            "path": "/default-image.jpg",
            "url_endpoint": "example.com",
            "transformation": [{"height": "300", "width": "400"}, {"rotation": 90}],
            "transformation_position": "query",
        }
    )

    print("chained transformation-", image_url, end="\n\n")
    # 4. Sharpening and contrast transforms and a progressive JPG image
    print("-------------------------------------")

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

    print("Sharpening and contrast transforms-", image_url, end="\n\n")

    # 3. Signed url
    print("-------------------------------------")
    image_url = imagekit.url(
        {
            "path": "/default-image.jpg",
            "query_parameters": {"v": "123"},
            "transformation": [{"height": "300", "width": "400"}],
            "signed": True,
            "expire_seconds": 300,
        }
    )

    print("Signed url-", image_url, end="\n\n")

    print("-------------------------------------")
    list_files = imagekit.list_files({"skip": 0, "limit": 5})
    bulk_ids = [
        list_files["response"][3]["fileId"],
        list_files["response"][4]["fileId"],
    ]
    print("List files-", "\n", list_files)

    upload = imagekit.upload_file(
        file=open("sample.jpg", "rb"),
        file_name="testing",
        options={
            "response_fields": ["is_private_file", "tags"],
            "tags": ["abc", "def"],
            "use_unique_file_name": False,
        },
    )
    print("-------------------------------------")

    print("Upload with binary-", upload, end="\n\n")
    file_id = upload["response"]["fileId"]

    upload = imagekit.upload_file(
        file=url,
        file_name="testing",
        options={
            "response_fields": ["is_private_file"],
            "is_private_file": True,
            "tags": ["abc", "def"],
        },
    )

    print("Upload with url-------------", upload)

    with open("sample.jpg", mode="rb") as img:
        imgstr = base64.b64encode(img.read())

    upload_base64 = imagekit.upload_file(
        file=imgstr,
        file_name="test64",
        options={
            "response_fields": ["is_private_file", "metadata", "tags"],
            "is_private_file": True,
            "tags": ["abc", "def"],
        },
    )

    print("Upload  base64", upload_base64)

    url_uploaded_id = upload["response"]["fileId"]
    image_url = upload["response"]["url"]
    print("Upload with url -", upload, "\n\n")

    print("-------------------------------------")

    updated_detail = imagekit.update_file_details(
        list_files["response"][0]["fileId"],
        {"tags": ["image_tag"], "custom_coordinates": "10,10,100,100"},
    )
    print("Updated detail-", updated_detail, end="\n\n")

    details = imagekit.get_file_details(url_uploaded_id)
    print("File detail with  binary upload-", details, end="\n\n")

    print("-------------------------------------")

    details = imagekit.get_file_details(upload["response"]["fileId"])
    print("File detail with url upload-", details, end="\n\n")

    print("-------------------------------------")
    file_metadata = imagekit.get_file_metadata(list_files["response"][0]['fileId'])

    print("-------------------------------------")
    delete = imagekit.delete_file(list_files["response"][1]["fileId"], )

    print("Delete File-", delete)

    print("-------------------------------------")
    purge_cache = imagekit.purge_file_cache(file_url=image_url)
    print("Purge cache-", purge_cache)

    request_id = purge_cache["response"]["request_id"]
    purge_cache_status = imagekit.get_purge_file_cache_status(request_id)

    print("-------------------------------------")

    print("Cache status-", purge_cache_status)

    print("-------------------------------------")

    auth_params = imagekit.get_authentication_parameters()
    print("Auth params-", auth_params)

    print("-------------------------------------")
    print(
        "Phash distance-",
        imagekit.phash_distance("f06830ca9f1e3e90", "f06830ca9f1e3e90"),
    )

    print("-------------------------------------")

    print("Bulk File delete-", imagekit.bulk_file_delete(bulk_ids))

    print("-----------------------------")

    remote_file_url = upload["response"]["url"]
    print("Get metadata-", imagekit.get_remote_file_url_metadata(remote_file_url))
