"""Screen capture and OCR utilities for Athena."""

from dataclasses import dataclass
from pathlib import Path

from PIL import Image
import pytesseract

from .capture import capture_screen


@dataclass(frozen=True)
class TextRegion:
    """A piece of text detected on screen."""

    text: str
    left: int
    top: int
    width: int
    height: int
    confidence: float


@dataclass(frozen=True)
class ScreenObservation:
    """A snapshot of the visible desktop and recognized text."""

    image_path: Path
    width: int
    height: int
    text: str
    regions: tuple[TextRegion, ...]


def _ocr(image: Image.Image) -> tuple[str, tuple[TextRegion, ...]]:
    """Run Tesseract OCR and return text plus bounding boxes."""
    data = pytesseract.image_to_data(image, output_type=pytesseract.Output.DICT)
    regions: list[TextRegion] = []
    words: list[str] = []

    for i, raw_text in enumerate(data["text"]):
        text = raw_text.strip()
        if not text:
            continue
        try:
            confidence = float(data["conf"][i])
        except (ValueError, TypeError):
            confidence = -1.0
        regions.append(
            TextRegion(
                text=text,
                left=int(data["left"][i]),
                top=int(data["top"][i]),
                width=int(data["width"][i]),
                height=int(data["height"][i]),
                confidence=confidence,
            )
        )
        words.append(text)

    return " ".join(words), tuple(regions)


def observe_screen(output_path: str | Path = "screenshots/observation.png") -> ScreenObservation:
    """Capture the primary monitor and recognize visible text."""
    image_path = capture_screen(output_path)
    with Image.open(image_path) as image:
        image.load()
        width, height = image.size
        text, regions = _ocr(image)
    return ScreenObservation(
        image_path=image_path,
        width=width,
        height=height,
        text=text,
        regions=regions,
    )
