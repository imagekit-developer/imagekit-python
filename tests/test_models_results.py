import unittest

from imagekitio.utils.utils import convert_to_response_object
from imagekitio.models.results.UploadFileResult import UploadFileResult
from imagekitio.models.results.EmbeddedMetadata import EmbeddedMetadata
from imagekitio.models.results.ResponseMetadata import ResponseMetadata
from imagekitio.models.results.VersionInfo import VersionInfo
from imagekitio.models.results.TagsResult import TagsResult
from imagekitio.models.results.MetadataExifThumbnail import MetadataExifThumbnail
from imagekitio.models.results.MetadataExifImage import MetadataExifImage
from imagekitio.models.results.MetadataExifGPS import MetadataExifGPS
from imagekitio.models.results.MetadataExifExif import MetadataExifExif
from imagekitio.models.results.MetadataExif import MetadataExif
from imagekitio.models.results.GetMetadataResult import GetMetadataResult
from imagekitio.models.results.GetBulkJobStatusResult import GetBulkJobStatusResult
from imagekitio.models.results.FolderResult import FolderResult
from imagekitio.models.results.FileResultWithResponseMetadata import FileResultWithResponseMetadata
from imagekitio.models.results.FileResult import FileResult
from imagekitio.models.results.CustomMetadataFieldsResult import CustomMetadataFieldsResult
from imagekitio.models.results.CustomMetadataFieldsResultWithResponseMetadata import CustomMetadataFieldsResultWithResponseMetadata
from imagekitio.models.results.CustomMetadataSchema import CustomMetadataSchema
from imagekitio.models.results.BulkDeleteFileResult import BulkDeleteFileResult
from imagekitio.models.results.AITags import AITags
from imagekitio.models.results.MetadataExifInteroperability import MetadataExifInteroperability


from requests.models import Response

import responses        


gps = {
    "GPSVersionId":"1.2"
}
thumbnail ={
    "compression":12,
    "YResolution":1,
    "XResolution":1,
    "resolutionUnit":"DPI",
    "thumbnailOffset":12,
    "thumbnailLength":12,
}
interoperability = {
    "interopVersion":1.1,
    "interopIndex":1.2
}
image = {
    "make":None,
    "model":None,
    "orientation":None,
    "XResolution":None,
    "YResolution":None,
    "resolutionUnit":None,
    "software":None,
    "modifyDate":None,
    "YCbCrPositioning":None,
    "exifOffset":None,
    "gpsInfo":None,
}
exif = {
    "exposureTime":10,
        "FNumber":1,
        "exposureProgram":None,
        "ISO":"2001",
        "exifVersion":1.2,
        "dateTimeOriginal":None,
        "createDate":None,
        "shutterSpeedValue":122,
        "apertureValue":12,
        "exposureCompensation":12,
        "meteringMode":None,
        "flash":"white",
        "focalLength":None,
        "subSecTime":None,
        "subSecTimeOriginal":None,
        "subSecTimeDigitized":None,
        "flashpixVersion":None,
        "colorSpace":None,
        "exifImageWidth":None,
        "exifImageHeight":None,
        "interopOffset":None,
        "focalPlaneXResolution":None,
        "focalPlaneYResolution":None,
        "focalPlaneResolutionUnit":None,
        "customRendered":None,
        "exposureMode":None,
        "whiteBalance":None,
        "sceneCaptureType":None,
}
class TestModelsResults(unittest.TestCase):

    @responses.activate()
    def test_models_results_embedded_metadata_with_variable_attributes(self):
        withVariableAttributes = EmbeddedMetadata(12,12,dpi=14)

        self.assertEqual(withVariableAttributes.x_resolution,12)
        self.assertEqual(withVariableAttributes.y_resolution,12)
        self.assertEqual(withVariableAttributes.date_created,None)
        self.assertEqual(withVariableAttributes.date_time_created,None)
        self.assertEqual(withVariableAttributes.dpi,14)
        self.assertEqual(withVariableAttributes.make,None)

    def test_models_results_response_metadata_with_variable_attributes(self):
        meta = ResponseMetadata(None,200,None,message="Successfully Done")
        
        self.assertEqual(meta.raw,None)
        self.assertEqual(meta.http_status_code,200)
        self.assertEqual(meta.headers,None)
        self.assertEqual(meta.message,"Successfully Done")
        self.assertEqual(meta.a,None)
    
    def test_models_results_version_info_with_variable_attributes(self):
        vi = VersionInfo(123,"0.1.12",description="Testing Purpose")

        self.assertEqual(vi.id,123)
        self.assertEqual(vi.name,"0.1.12")
        self.assertEqual(vi.description,"Testing Purpose")
        self.assertEqual(vi.random,None)
    
    def test_models_results_tags_result_with_variable_attributes(self):
        tr = TagsResult(successfully_updated_file_ids=None,random1="123")

        self.assertEqual(tr.successfully_updated_file_ids,None)
        self.assertEqual(tr.random1,"123")
        self.assertEqual(tr.random2,None)

    def test_models_results_metadata_exif_thumbnail_with_variable_attributes(self):
        met = MetadataExifThumbnail(None,12,12,None,1,200,name="Thumbnail1",)

        self.assertEqual(met.compression,None)
        self.assertEqual(met.x_resolution,12)
        self.assertEqual(met.y_resolution,12)
        self.assertEqual(met.resolution_unit,None)
        self.assertEqual(met.thumbnail_offset,1)
        self.assertEqual(met.thumbnail_length,200)
        self.assertEqual(met.name,"Thumbnail1")
        self.assertEqual(met.random,None)


    def test_models_results_metadata_exif_image_with_variable_attributes(self):
        mei = MetadataExifImage(software="picasso",name="Image1")

        self.assertEqual(mei.software,"picasso")
        self.assertEqual(mei.name,"Image1")
        self.assertEqual(mei.random,None)

    def test_models_results_metadata_exif_gps_with_variable_attributes(self):
        meg = MetadataExifGPS("0.1",longitude="12124.4124",latitude="121523.12312")

        self.assertEqual(meg.gps_version_id,["0",".","1"])
        self.assertEqual(meg.longitude,"12124.4124")
        self.assertEqual(meg.latitude,"121523.12312")
        self.assertEqual(meg.random,None)
    
    def test_models_results_metadata_exif_exif_with_variable_attributes(self):
        mee = MetadataExifExif(12,shutter_speed_value=120,camera_model="canon x")

        self.assertEqual(mee.exposure_time,12)
        self.assertEqual(mee.shutter_speed_value,120)
        self.assertEqual(mee.camera_model,"canon x")
        self.assertEqual(mee.random,None)

    def test_models_results_metadata_exif_with_variable_attributes(self):
        me = MetadataExif(gps=MetadataExifGPS("0.9"),name="exif")

        self.assertEqual(me.gps.gps_version_id,["0",".","9"])
        self.assertEqual(me.name,"exif")
        self.assertEqual(me.random,None)
    
    def test_models_results_get_metadata_result_with_variable_attributes(self):
        getMetadataResult = GetMetadataResult(height=100,width=100,device="canon")

        self.assertEqual(getMetadataResult.width,100)
        self.assertEqual(getMetadataResult.height,100)
        self.assertEqual(getMetadataResult.device,"canon")
        self.assertEqual(getMetadataResult.random,None)

    def test_models_results_get_bulk_job_status_result_with_variable_attributes(self):
        getBulkJobStatusResult = GetBulkJobStatusResult(job_id="123",type="jpg",status="active",num_job=2)

        self.assertEqual(getBulkJobStatusResult.job_id,"123")
        self.assertEqual(getBulkJobStatusResult.type,"jpg")
        self.assertEqual(getBulkJobStatusResult.status,"active")
        self.assertEqual(getBulkJobStatusResult.num_job,2)
        self.assertEqual(getBulkJobStatusResult.random,None)

    def test_folder_results_folder_result_with_variable_attributes(self):
        folderResult = FolderResult("123",address="/abc/home")

        self.assertEqual(folderResult.job_id,"123")
        self.assertEqual(folderResult.address,"/abc/home")
        self.assertEqual(folderResult.random,None)

    def test_file_result_with_response_metadata_with_variable_attributes(self):
        fileResultWithResponseMetadata = FileResultWithResponseMetadata("jpg",name="abc",file_health="healthy")
        self.assertEqual(fileResultWithResponseMetadata.type,"jpg")
        self.assertEqual(fileResultWithResponseMetadata.name,"abc")
        self.assertEqual(fileResultWithResponseMetadata.file_health,"healthy")
        self.assertEqual(fileResultWithResponseMetadata.random,None)

    def test_file_result_with_variable_attributes(self):
        fileResult = FileResult("jpg",name="abc",file_health="healthy")

        self.assertEqual(fileResult.type,"jpg")
        self.assertEqual(fileResult.name,"abc")
        self.assertEqual(fileResult.file_health,"healthy")
        self.assertEqual(fileResult.random,None)

    def test_custom_metadata_scheme_with_variable_attributes(self):
        customMetadataSchema = CustomMetadataSchema("jpg",max_length=1000,name="abc")

        self.assertEqual(customMetadataSchema.max_length,1000)
        self.assertEqual(customMetadataSchema.type,"jpg")
        self.assertEqual(customMetadataSchema.name,"abc")
        self.assertEqual(customMetadataSchema.random,None)

    def test_custom_metadata_fields_result_with_response_metadata_with_variable_attributes(self):
        customMetadataFieldsResultWithResponseMetadata = CustomMetadataFieldsResultWithResponseMetadata(id="1234",label="123",num_fields=5)
        
        self.assertEqual(customMetadataFieldsResultWithResponseMetadata.id,"1234")
        self.assertEqual(customMetadataFieldsResultWithResponseMetadata.label,"123")
        self.assertEqual(customMetadataFieldsResultWithResponseMetadata.num_fields,5)
        self.assertEqual(customMetadataFieldsResultWithResponseMetadata.random,None)

    def test_custom_metadata_fields_result_with_variable_attributes(self):
        customMetadataFieldsResult = CustomMetadataFieldsResult(id="1234",label="123",num_fields=5)
        
        self.assertEqual(customMetadataFieldsResult.id,"1234")
        self.assertEqual(customMetadataFieldsResult.label,"123")
        self.assertEqual(customMetadataFieldsResult.num_fields,5)
        self.assertEqual(customMetadataFieldsResult.random,None)
        
    def test_bulk_delete_file_result_with_variable_attributes(self):
        bulkDeleteFileResult = BulkDeleteFileResult(successfully_deleted_file_ids=["1","2","232"],num_files_deleted=3)

        self.assertEqual(bulkDeleteFileResult.successfully_deleted_file_ids,["1","2","232"])
        self.assertEqual(bulkDeleteFileResult.num_files_deleted,3)
        self.assertEqual(bulkDeleteFileResult.random,None)
    
    def test_ai_tags_with_variable_attributes(self):
        aITags = AITags("abc",confidence="0.96",model="KNN")
        
        self.assertEqual(aITags.name,"abc")
        self.assertEqual(aITags.confidence,"0.96")
        self.assertEqual(aITags.random,None)
    
    def test_metadata_exif_interoperability_with_variable_attributes(self):
        metadataExifInteroperability = MetadataExifInteroperability(1,"0.4.3",ri = 3)

        self.assertEqual(metadataExifInteroperability.interop_index,1)
        self.assertEqual(metadataExifInteroperability.interop_version,"0.4.3")
        self.assertEqual(metadataExifInteroperability.ri,3)
        self.assertEqual(metadataExifInteroperability.random,None)
        


    