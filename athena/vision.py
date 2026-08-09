"""Lightweight screen-vision utilities for Athena.

This module deliberately starts without an external OCR engine. It captures a
screen and returns useful image metadata so the perception boundary can be
tested independently before adding OCR or a vision-language model.
"""

from dataclasses import dataclass
from pathlib import Path

from PIL import Image

from .capture import capture_screen


@dataclass(frozen=True)
class ScreenObservation:
    """A snapshot of the visible desktop."""

    image_path: Path
    width: int
    height: int


def observe_screen(output_path: str | Path = "screenshots/observation.png") -> ScreenObservation:
    """Capture the primary monitor and describe the resulting image."""
    image_path = capture_screen(output_path)
    with Image.open(image_path) as image:
        width, height = image.size
    return ScreenObservation(image_path=image_path, width=width, height=height)
