import base64
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

    ### The signed url generated for this file doesn't work using the Python SDK
    upload = imagekit.upload_file(
            file=open("sample.jpg", "rb"),
            file_name="testing_upload_binary_signed_private.jpg",
            options={
                "response_fields": ["is_private_file", "tags"],
                "is_private_file": False,
                "folder" : "/testing-python-folder/",
                "tags": ["abc", "def"]
            },
        )
    
    print("-------------------------------------")
    print("Upload with binary")
    print("-------------------------------------")
    print(upload, end="\n\n")

    image_url = imagekit.url(
        {
            "path": upload['response']['filePath'],
            "query_parameters": {"v": "123"},
            "transformation": [{"height": "300", "width": "400"}],
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
            "url_endpoint": "https://www.example.com",
            "transformation": [{"height": "300", "width": "400"}, {"rotation": 90}],
            "transformation_position": "query",
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

    list_files = imagekit.list_files({"skip": 0, "limit": 5})
    bulk_ids = [
        list_files["response"][3]["fileId"],
        list_files["response"][4]["fileId"],
    ]

    print("-------------------------------------")
    print("List files")
    print("-------------------------------------")
    print(list_files, end="\n\n")

    upload = imagekit.upload_file(
        file=open("sample.jpg", "rb"),
        file_name="testing-binary.jpg",
        options={
            "response_fields": ["is_private_file", "tags"],
            "tags": ["abc", "def"],
            "use_unique_file_name": False,
        },
    )
    
    print("-------------------------------------")
    print("Upload with binary")
    print("-------------------------------------")
    print(upload, end="\n\n")
    
    file_id = upload["response"]["fileId"]

    upload = imagekit.upload_file(
        file=url,
        file_name="testing-url.jpg",
        options={
            "response_fields": ["is_private_file"],
            "is_private_file": False,
            "tags": ["abc", "def"],
        },
    )
    image_url = upload["response"]["url"]

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

    updated_detail = imagekit.update_file_details(
        list_files["response"][0]["fileId"],
        {"tags": None, "custom_coordinates": "10,10,100,100"},
    )

    print("-------------------------------------")
    print("Update file details")
    print("-------------------------------------")
    print(updated_detail, end="\n\n")

    details = imagekit.get_file_details(list_files["response"][0]["fileId"])
    print("-------------------------------------")
    print("Get file details")
    print("-------------------------------------")
    print(details, end="\n\n")

    file_metadata = imagekit.get_file_metadata(list_files["response"][0]["fileId"])
    print("-------------------------------------")
    print("File metadata")
    print("-------------------------------------")
    print(file_metadata, end="\n\n")

    
    delete = imagekit.delete_file(list_files["response"][1]["fileId"])
    print("-------------------------------------")
    print("Delete file")
    print("-------------------------------------")
    print(delete, end="\n\n")

    
    purge_cache = imagekit.purge_file_cache(file_url=image_url)
    print("-------------------------------------")
    print("Purge cache")
    print("-------------------------------------")
    print(purge_cache, end="\n\n")

    request_id = purge_cache["response"]["request_id"]
    purge_cache_status = imagekit.get_purge_file_cache_status(request_id)

    print("-------------------------------------")
    print("Cache status")
    print("-------------------------------------")
    print(purge_cache_status, end="\n\n")

    auth_params = imagekit.get_authentication_parameters()
    print("-------------------------------------")
    print("Auth params")
    print("-------------------------------------")
    print(auth_params, end="\n\n")

    print("-------------------------------------")
    print("Phash distance")
    print("-------------------------------------")
    print(imagekit.phash_distance("f06830ca9f1e3e90", "f06830ca9f1e3e90"), end="\n\n")

    

    print("-------------------------------------")
    print("Bulk file delete")
    print("-------------------------------------")
    print(imagekit.bulk_file_delete(bulk_ids), end="\n\n")

    remote_file_url = upload["response"]["url"]
    print("-------------------------------------")
    print("Get metatdata via url")
    print("-------------------------------------")
    print(imagekit.get_remote_file_url_metadata(remote_file_url))
