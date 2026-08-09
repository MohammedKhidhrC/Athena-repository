from PIL import Image

from athena.vision import _ocr


def test_ocr_returns_text_and_regions():
    image = Image.new("RGB", (300, 100), "white")
    # OCR is integration-dependent; this test only verifies the API shape.
    text, regions = _ocr(image)
    assert isinstance(text, str)
    assert isinstance(regions, tuple)
