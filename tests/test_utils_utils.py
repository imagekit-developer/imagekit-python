import unittest

from imagekitio.utils.utils import convert_to_response_object
from imagekitio.models.results.UploadFileResult import UploadFileResult

from requests.models import Response

import responses        

class TestUtilsUtils(unittest.TestCase):
    

    @responses.activate()
    def test_convert_to_response_object(self):
        response = Response()
        response.status_code = 200
        response._content = b'{"fileId":"abc123","name":"file.jpg","size":812557,"versionInfo":{"id":"abc123","name":"Version 1"},"filePath":"/file.jpg","url":"http://test.com","fileType":"image","height":398,"width":1000,"thumbnailUrl":"https://test.com","AITags":null,"embeddedMetadata":{"XResolution":1,"YResolution":1,"DateCreated":"2023-06-22T09:06:21.151Z","DateTimeCreated":"2023-06-22T09:06:21.151Z"}}'
        u =  convert_to_response_object(response,UploadFileResult)
        expectedUploadFileResponse = {'file_id': 'abc123', 'name': 'file.jpg', 'size': 812557, 'version_info': {'id': 'abc123', 'name': 'Version 1'}, 'file_path': '/file.jpg', 'url': 'http://test.com', 'file_type': 'image', 'height': 398, 'width': 1000, 'thumbnail_url': 'https://test.com', 'ai_tags': None, 'embedded_metadata': {'x_resolution': 1, 'y_resolution': 1, 'date_created': '2023-06-22T09:06:21.151Z', 'date_time_created': '2023-06-22T09:06:21.151Z'}}
        expectedUploadFileResult  = UploadFileResult(**expectedUploadFileResponse)

        self.assertEqual(u.file_id,expectedUploadFileResult.file_id)
        self.assertEqual(u.name,expectedUploadFileResult.name)
        self.assertEqual(u.url,expectedUploadFileResult.url)
        self.assertEqual(u.thumbnail_url,expectedUploadFileResult.thumbnail_url)
        self.assertEqual(u.height,expectedUploadFileResult.height)
        self.assertEqual(u.width,expectedUploadFileResult.width)
        self.assertEqual(u.size,expectedUploadFileResult.size)
        self.assertEqual(u.file_path,expectedUploadFileResult.file_path)
        self.assertEqual(u.tags,expectedUploadFileResult.tags)

        for tag1,tag2 in zip(u.ai_tags,expectedUploadFileResult.ai_tags):
            self.assertEqual(tag1.confidence,tag2.confidence)
            self.assertEqual(tag1.name,tag2.name)
            self.assertEqual(tag1.source,tag2.source)
            
        self.assertEqual(u.version_info.id,expectedUploadFileResult.version_info.id)
        self.assertEqual(u.version_info.name,expectedUploadFileResult.version_info.name)
        self.assertEqual(u.is_private_file,expectedUploadFileResult.is_private_file)
        self.assertEqual(u.custom_coordinates,expectedUploadFileResult.custom_coordinates)
        self.assertEqual(u.custom_metadata,expectedUploadFileResult.custom_metadata)
        self.assertEqual(u.embedded_metadata.x_resolution,expectedUploadFileResult.embedded_metadata.x_resolution)
        self.assertEqual(u.embedded_metadata.y_resolution,expectedUploadFileResult.embedded_metadata.y_resolution)
        self.assertEqual(u.embedded_metadata.date_time_created,expectedUploadFileResult.embedded_metadata.date_time_created)
        self.assertEqual(u.embedded_metadata.date_created,expectedUploadFileResult.embedded_metadata.date_created)
        self.assertEqual(u.extension_status,expectedUploadFileResult.extension_status)
        self.assertEqual(u.file_type,expectedUploadFileResult.file_type)
        self.assertEqual(u.orientation,expectedUploadFileResult.orientation)
