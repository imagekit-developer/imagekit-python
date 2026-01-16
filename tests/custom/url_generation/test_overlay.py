"""Overlay transformation tests imported from Ruby SDK."""

import pytest

from imagekitio import ImageKit


class TestOverlay:
    """Test overlay functionality matching Ruby SDK overlay_test.rb."""

    @pytest.fixture(autouse=True)
    def setup(self):
        """Setup client for each test."""
        self.client = ImageKit(private_key="My Private API Key")

    # Basic overlay tests
    def test_should_ignore_overlay_when_type_property_is_missing(self):
        """Test that overlay is ignored when type is missing."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"width": 300}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:w-300/base-image.jpg"
        assert url == expected

    def test_should_ignore_text_overlay_when_text_property_is_missing(self):
        """Test that text overlay is ignored when text is empty."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "text", "text": ""}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/base-image.jpg"
        assert url == expected

    def test_should_ignore_image_overlay_when_input_property_is_missing(self):
        """Test that image overlay is ignored when input is empty."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "image", "input": ""}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/base-image.jpg"
        assert url == expected

    def test_should_ignore_video_overlay_when_input_property_is_missing(self):
        """Test that video overlay is ignored when input is empty."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "video", "input": ""}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/base-image.jpg"
        assert url == expected

    def test_should_ignore_subtitle_overlay_when_input_property_is_missing(self):
        """Test that subtitle overlay is ignored when input is empty."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "subtitle", "input": ""}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/base-image.jpg"
        assert url == expected

    def test_should_ignore_solid_color_overlay_when_color_property_is_missing(self):
        """Test that solid color overlay is ignored when color is empty."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "solidColor", "color": ""}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/base-image.jpg"
        assert url == expected

    # Basic overlay functionality tests
    def test_should_generate_url_with_text_overlay_using_url_encoding(self):
        """Test text overlay with URL encoding."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "text", "text": "Minimal Text"}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-text,i-Minimal%20Text,l-end/base-image.jpg"
        assert url == expected

    def test_should_generate_url_with_image_overlay_from_input_file(self):
        """Test image overlay from input file."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "image", "input": "logo.png"}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-image,i-logo.png,l-end/base-image.jpg"
        assert url == expected

    def test_should_generate_url_with_video_overlay_from_input_file(self):
        """Test video overlay from input file."""
        url = self.client.helper.build_url(
            src="/base-video.mp4",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "video", "input": "play-pause-loop.mp4"}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-video,i-play-pause-loop.mp4,l-end/base-video.mp4"
        assert url == expected

    def test_should_generate_url_with_subtitle_overlay_from_input_file(self):
        """Test subtitle overlay from input file."""
        url = self.client.helper.build_url(
            src="/base-video.mp4",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "subtitle", "input": "subtitle.srt"}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-subtitle,i-subtitle.srt,l-end/base-video.mp4"
        assert url == expected

    def test_should_generate_url_with_solid_color_overlay_using_background_color(self):
        """Test solid color overlay."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[{"overlay": {"type": "solidColor", "color": "FF0000"}}],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-image,i-ik_canvas,bg-FF0000,l-end/base-image.jpg"
        assert url == expected

    def test_should_generate_url_with_multiple_complex_overlays_including_nested_transformations(self):
        """Test complex overlays with nested transformations."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[
                # Text overlay
                {
                    "overlay": {
                        "type": "text",
                        "text": "Every thing",
                        "position": {"x": "10", "y": "20", "focus": "center"},
                        "timing": {"start": 5.0, "duration": "10", "end": 15.0},
                        "transformation": [
                            {
                                "width": "bw_mul_0.5",
                                "font_size": 20.0,
                                "font_family": "Arial",
                                "font_color": "0000ff",
                                "inner_alignment": "left",
                                "padding": 5.0,
                                "alpha": 7.0,
                                "typography": "b",
                                "background": "red",
                                "radius": 10.0,
                                "rotation": "N45",
                                "flip": "h",
                                "line_height": 20.0,
                            }
                        ],
                    }
                },
                # Image overlay
                {
                    "overlay": {
                        "type": "image",
                        "input": "logo.png",
                        "position": {"x": "10", "y": "20", "focus": "center"},
                        "timing": {"start": 5.0, "duration": "10", "end": 15.0},
                        "transformation": [
                            {
                                "width": "bw_mul_0.5",
                                "height": "bh_mul_0.5",
                                "rotation": "N45",
                                "flip": "h",
                                "overlay": {"type": "text", "text": "Nested text overlay"},
                            }
                        ],
                    }
                },
                # Video overlay
                {
                    "overlay": {
                        "type": "video",
                        "input": "play-pause-loop.mp4",
                        "position": {"x": "10", "y": "20", "focus": "center"},
                        "timing": {"start": 5.0, "duration": "10", "end": 15.0},
                        "transformation": [
                            {"width": "bw_mul_0.5", "height": "bh_mul_0.5", "rotation": "N45", "flip": "h"}
                        ],
                    }
                },
                # Subtitle overlay
                {
                    "overlay": {
                        "type": "subtitle",
                        "input": "subtitle.srt",
                        "position": {"x": "10", "y": "20", "focus": "center"},
                        "timing": {"start": 5.0, "duration": "10", "end": 15.0},
                        "transformation": [
                            {
                                "background": "red",
                                "color": "0000ff",
                                "font_family": "Arial",
                                "font_outline": "2_A1CCDD50",
                                "font_shadow": "A1CCDD_3",
                            }
                        ],
                    }
                },
                # Solid color overlay
                {
                    "overlay": {
                        "type": "solidColor",
                        "color": "FF0000",
                        "position": {"x": "10", "y": "20", "focus": "center"},
                        "timing": {"start": 5.0, "duration": "10", "end": 15.0},
                        "transformation": [
                            {
                                "width": "bw_mul_0.5",
                                "height": "bh_mul_0.5",
                                "alpha": 0.5,
                                "background": "red",
                                "gradient": True,
                                "radius": "max",
                            }
                        ],
                    }
                },
            ],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-text,i-Every%20thing,lx-10,ly-20,lfo-center,lso-5,leo-15,ldu-10,w-bw_mul_0.5,fs-20,ff-Arial,co-0000ff,ia-left,pa-5,al-7,tg-b,bg-red,r-10,rt-N45,fl-h,lh-20,l-end:l-image,i-logo.png,lx-10,ly-20,lfo-center,lso-5,leo-15,ldu-10,w-bw_mul_0.5,h-bh_mul_0.5,rt-N45,fl-h,l-text,i-Nested%20text%20overlay,l-end,l-end:l-video,i-play-pause-loop.mp4,lx-10,ly-20,lfo-center,lso-5,leo-15,ldu-10,w-bw_mul_0.5,h-bh_mul_0.5,rt-N45,fl-h,l-end:l-subtitle,i-subtitle.srt,lx-10,ly-20,lfo-center,lso-5,leo-15,ldu-10,bg-red,co-0000ff,ff-Arial,fol-2_A1CCDD50,fsh-A1CCDD_3,l-end:l-image,i-ik_canvas,bg-FF0000,lx-10,ly-20,lfo-center,lso-5,leo-15,ldu-10,w-bw_mul_0.5,h-bh_mul_0.5,al-0.5,bg-red,e-gradient,r-max,l-end/base-image.jpg"
        assert url == expected

    # Overlay encoding tests
    def test_should_use_plain_encoding_for_simple_image_paths_with_slashes_converted_to_double_at(self):
        """Test plain encoding for simple image paths."""
        url = self.client.helper.build_url(
            src="/medium_cafe_B1iTdD0C.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "image", "input": "/customer_logo/nykaa.png"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-image,i-customer_logo@@nykaa.png,l-end/medium_cafe_B1iTdD0C.jpg"
        assert url == expected

    def test_should_use_base64_encoding_for_image_paths_containing_special_characters(self):
        """Test base64 encoding for image paths with special characters."""
        url = self.client.helper.build_url(
            src="/medium_cafe_B1iTdD0C.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "image", "input": "/customer_logo/Ñykaa.png"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-image,ie-Y3VzdG9tZXJfbG9nby%2FDkXlrYWEucG5n,l-end/medium_cafe_B1iTdD0C.jpg"
        assert url == expected

    def test_should_use_plain_encoding_for_simple_text_overlays(self):
        """Test plain encoding for simple text."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "text", "text": "HelloWorld"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-text,i-HelloWorld,l-end/sample.jpg"
        assert url == expected

    def test_should_convert_slashes_to_double_at_in_font_family_paths_for_custom_fonts(self):
        """Test font family path conversion."""
        url = self.client.helper.build_url(
            src="/medium_cafe_B1iTdD0C.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[
                {
                    "overlay": {
                        "type": "text",
                        "text": "Manu",
                        "transformation": [{"font_family": "nested-path/Poppins-Regular_Q15GrYWmL.ttf"}],
                    }
                }
            ],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-text,i-Manu,ff-nested-path@@Poppins-Regular_Q15GrYWmL.ttf,l-end/medium_cafe_B1iTdD0C.jpg"
        assert url == expected

    def test_should_use_url_encoding_for_text_overlays_with_spaces_and_safe_characters(self):
        """Test URL encoding for text with spaces."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "text", "text": "Hello World"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-text,i-Hello%20World,l-end/sample.jpg"
        assert url == expected

    def test_should_use_base64_encoding_for_text_overlays_with_special_unicode_characters(self):
        """Test base64 encoding for Unicode text."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "text", "text": "हिन्दी"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-text,ie-4KS54KS%2F4KSo4KWN4KSm4KWA,l-end/sample.jpg"
        assert url == expected

    def test_should_use_plain_encoding_when_explicitly_specified_for_text_overlay(self):
        """Test explicit plain encoding for text."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "text", "text": "HelloWorld", "encoding": "plain"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-text,i-HelloWorld,l-end/sample.jpg"
        assert url == expected

    def test_should_use_base64_encoding_when_explicitly_specified_for_text_overlay(self):
        """Test explicit base64 encoding for text."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "text", "text": "HelloWorld", "encoding": "base64"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-text,ie-SGVsbG9Xb3JsZA%3D%3D,l-end/sample.jpg"
        assert url == expected

    def test_should_use_plain_encoding_when_explicitly_specified_for_image_overlay(self):
        """Test explicit plain encoding for image."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "image", "input": "/customer/logo.png", "encoding": "plain"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-image,i-customer@@logo.png,l-end/sample.jpg"
        assert url == expected

    def test_should_use_base64_encoding_when_explicitly_specified_for_image_overlay(self):
        """Test explicit base64 encoding for image."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "image", "input": "/customer/logo.png", "encoding": "base64"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-image,ie-Y3VzdG9tZXIvbG9nby5wbmc%3D,l-end/sample.jpg"
        assert url == expected

    def test_should_use_base64_encoding_when_explicitly_specified_for_video_overlay(self):
        """Test explicit base64 encoding for video."""
        url = self.client.helper.build_url(
            src="/sample.mp4",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "video", "input": "/path/to/video.mp4", "encoding": "base64"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-video,ie-cGF0aC90by92aWRlby5tcDQ%3D,l-end/sample.mp4"
        assert url == expected

    def test_should_use_base64_encoding_when_explicitly_specified_for_subtitle_overlay(self):
        """Test explicit base64 encoding for subtitle."""
        url = self.client.helper.build_url(
            src="/sample.mp4",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "subtitle", "input": "sub.srt", "encoding": "base64"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-subtitle,ie-c3ViLnNydA%3D%3D,l-end/sample.mp4"
        assert url == expected

    def test_should_use_plain_encoding_when_explicitly_specified_for_subtitle_overlay(self):
        """Test explicit plain encoding for subtitle overlay."""
        url = self.client.helper.build_url(
            src="/sample.mp4",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="path",
            transformation=[{"overlay": {"type": "subtitle", "input": "/sub.srt", "encoding": "plain"}}],
        )
        expected = "https://ik.imagekit.io/demo/tr:l-subtitle,i-sub.srt,l-end/sample.mp4"
        assert url == expected

    def test_should_properly_encode_overlay_text_when_transformations_are_in_query_parameters(self):
        """Test text overlay encoding with query position."""
        url = self.client.helper.build_url(
            src="/sample.jpg",
            url_endpoint="https://ik.imagekit.io/demo",
            transformation_position="query",
            transformation=[{"overlay": {"type": "text", "text": "Minimal Text"}}],
        )
        expected = "https://ik.imagekit.io/demo/sample.jpg?tr=l-text,i-Minimal%20Text,l-end"
        assert url == expected

    # Layer mode tests
    def test_should_handle_layer_mode_multiply_in_overlay(self):
        """Test layer mode multiply in image overlay."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[
                {
                    "overlay": {
                        "type": "image",
                        "input": "overlay.png",
                        "layer_mode": "multiply",
                    }
                }
            ],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-image,i-overlay.png,lm-multiply,l-end/base-image.jpg"
        assert url == expected

    def test_should_handle_layer_mode_cutter_in_overlay(self):
        """Test layer mode cutter in image overlay."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[
                {
                    "overlay": {
                        "type": "image",
                        "input": "overlay.png",
                        "layer_mode": "cutter",
                    }
                }
            ],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-image,i-overlay.png,lm-cutter,l-end/base-image.jpg"
        assert url == expected

    def test_should_handle_layer_mode_cutout_in_overlay(self):
        """Test layer mode cutout in image overlay."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[
                {
                    "overlay": {
                        "type": "image",
                        "input": "overlay.png",
                        "layer_mode": "cutout",
                    }
                }
            ],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-image,i-overlay.png,lm-cutout,l-end/base-image.jpg"
        assert url == expected

    def test_should_handle_layer_mode_displace_in_overlay(self):
        """Test layer mode displace in image overlay."""
        url = self.client.helper.build_url(
            src="/base-image.jpg",
            url_endpoint="https://ik.imagekit.io/test_url_endpoint",
            transformation_position="path",
            transformation=[
                {
                    "overlay": {
                        "type": "image",
                        "input": "overlay.png",
                        "layer_mode": "displace",
                    }
                }
            ],
        )
        expected = "https://ik.imagekit.io/test_url_endpoint/tr:l-image,i-overlay.png,lm-displace,l-end/base-image.jpg"
        assert url == expected

