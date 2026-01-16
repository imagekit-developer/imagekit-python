"""Advanced URL generation tests imported from Ruby SDK."""

import pytest

from imagekitio import ImageKit


class TestAdvancedURLGeneration:
    """Test advanced URL generation matching Ruby SDK advanced_url_generation_test.rb."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup client for each test."""
        self.client = ImageKit(private_key="My Private API Key")

    # AI Transformation Tests
    def test_should_generate_the_correct_url_for_ai_background_removal_when_set_to_true(self):
        """Test AI background removal transformation."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"ai_remove_background": True}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=e-bgremove"
        assert url == expected

    def test_should_generate_the_correct_url_for_external_ai_background_removal_when_set_to_true(self):
        """Test external AI background removal transformation."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"ai_remove_background_external": True}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=e-removedotbg"
        assert url == expected

    def test_should_generate_the_correct_url_when_ai_drop_shadow_transformation_is_set_to_true(self):
        """Test AI drop shadow transformation."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"ai_drop_shadow": True}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=e-dropshadow"
        assert url == expected

    def test_should_generate_the_correct_url_when_gradient_transformation_is_set_to_true(self):
        """Test gradient transformation."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"gradient": True}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=e-gradient"
        assert url == expected

    def test_should_not_apply_ai_background_removal_when_value_is_not_true(self):
        """Test that AI background removal is not applied when not true."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg"
        assert url == expected

    def test_should_not_apply_external_ai_background_removal_when_value_is_not_true(self):
        """Test that external AI background removal is not applied when not true."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg"
        assert url == expected

    def test_should_handle_ai_transformations_with_parameters(self):
        """Test AI transformations with custom parameters."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"ai_drop_shadow": "custom-shadow-params"}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=e-dropshadow-custom-shadow-params"
        assert url == expected

    def test_should_handle_gradient_with_parameters(self):
        """Test gradient with custom parameters."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"gradient": "ld-top_from-green_to-00FF0010_sp-1"}],
        )
        expected = (
            "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=e-gradient-ld-top_from-green_to-00FF0010_sp-1"
        )
        assert url == expected

    def test_should_combine_ai_transformations_with_regular_transformations(self):
        """Test combining AI and regular transformations."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"width": 300, "height": 200, "ai_remove_background": True}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=w-300,h-200,e-bgremove"
        assert url == expected

    def test_should_handle_multiple_ai_transformations(self):
        """Test multiple AI transformations."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"ai_remove_background": True, "ai_drop_shadow": True}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=e-bgremove,e-dropshadow"
        assert url == expected

    # Parameter-specific tests
    def test_should_generate_the_correct_url_for_width_transformation_when_provided_with_a_number_value(self):
        """Test width transformation with number value."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"width": 400}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=w-400"
        assert url == expected

    def test_should_generate_the_correct_url_for_height_transformation_when_provided_with_a_string_value(self):
        """Test height transformation with string value."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"height": "300"}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=h-300"
        assert url == expected

    def test_should_generate_the_correct_url_for_aspect_ratio_transformation_when_provided_with_colon_format(self):
        """Test aspect ratio transformation with colon format."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"aspect_ratio": "4:3"}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=ar-4:3"
        assert url == expected

    def test_should_generate_the_correct_url_for_quality_transformation_when_provided_with_a_number_value(self):
        """Test quality transformation with number value."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"quality": 80}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=q-80"
        assert url == expected

    # Additional parameter validation tests
    def test_should_skip_transformation_parameters_that_are_undefined_or_empty(self):
        """Test that undefined/empty parameters are skipped."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"width": 300}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=w-300"
        assert url == expected

    def test_should_handle_boolean_transformation_values(self):
        """Test boolean transformation values."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"trim": True}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=t-true"
        assert url == expected

    def test_should_handle_transformation_parameter_with_empty_string_value(self):
        """Test transformation with empty string value."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"default_image": ""}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg"
        assert url == expected

    def test_should_handle_complex_transformation_combinations(self):
        """Test complex transformation combinations."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"width": 300, "height": 200, "quality": 85, "border": "5_FF0000"}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=w-300,h-200,q-85,b-5_FF0000"
        assert url == expected

    def test_should_handle_radius_with_complex_corner_values(self):
        """Test radius transformation with complex corner-specific values."""
        url = self.client.helper.build_url(
            src="/test_path1.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[{"radius": "10_20_20_max"}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path1.jpg?tr=r-10_20_20_max"
        assert url == expected

    def test_should_generate_the_correct_url_with_many_transformations_including_video_and_ai_transforms(self):
        """Test many transformations including video and AI."""
        url = self.client.helper.build_url(
            src="/test_path.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="query",
            transformation=[
                {
                    "height": 300,
                    "width": 400,
                    "aspect_ratio": "4-3",
                    "quality": 40,
                    "crop": "force",
                    "crop_mode": "extract",
                    "focus": "left",
                    "format": "jpeg",
                    "radius": 50,
                    "background": "A94D34",
                    "border": "5-A94D34",
                    "rotation": 90,
                    "blur": 10,
                    "named": "some_name",
                    "progressive": True,
                    "lossless": True,
                    "trim": 5,
                    "metadata": True,
                    "color_profile": True,
                    "default_image": "/folder/file.jpg/",
                    "dpr": 3,
                    "x": 10,
                    "y": 20,
                    "x_center": 30,
                    "y_center": 40,
                    "flip": "h",
                    "opacity": 0.8,
                    "zoom": 2,
                    "video_codec": "h264",
                    "audio_codec": "aac",
                    "start_offset": 5,
                    "end_offset": 15,
                    "duration": 10,
                    "streaming_resolutions": ["1440", "1080"],
                    "grayscale": True,
                    "ai_upscale": True,
                    "ai_retouch": True,
                    "ai_variation": True,
                    "ai_drop_shadow": True,
                    "ai_change_background": "prompt-car",
                    "ai_edit": "prompt-make it vintage",
                    "ai_remove_background": True,
                    "contrast_stretch": True,
                    "shadow": "bl-15_st-40_x-10_y-N5",
                    "sharpen": 10,
                    "unsharp_mask": "2-2-0.8-0.024",
                    "gradient": "from-red_to-white",
                    "color_replace": "FF0000_10_0000FF",
                    "distort": "p-10_20_100_20_100_200_10_200",
                    "original": True,
                    "page": "2_4",
                    "raw": "h-200,w-300,l-image,i-logo.png,l-end",
                }
            ],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/test_path.jpg?tr=h-300,w-400,ar-4-3,q-40,c-force,cm-extract,fo-left,f-jpeg,r-50,bg-A94D34,b-5-A94D34,rt-90,bl-10,n-some_name,pr-true,lo-true,t-5,md-true,cp-true,di-folder@@file.jpg,dpr-3,x-10,y-20,xc-30,yc-40,fl-h,o-0.8,z-2,vc-h264,ac-aac,so-5,eo-15,du-10,sr-1440_1080,e-grayscale,e-upscale,e-retouch,e-genvar,e-dropshadow,e-changebg-prompt-car,e-edit-prompt-make it vintage,e-bgremove,e-contrast,e-shadow-bl-15_st-40_x-10_y-N5,e-sharpen-10,e-usm-2-2-0.8-0.024,e-gradient-from-red_to-white,cr-FF0000_10_0000FF,e-distort-p-10_20_100_20_100_200_10_200,orig-true,pg-2_4,h-200,w-300,l-image,i-logo.png,l-end"
        assert url == expected
