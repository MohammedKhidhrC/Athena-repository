"""Screen capture utilities."""

from pathlib import Path

import mss
from PIL import Image


def capture_screen(output_path: str | Path = "screenshots/screen.png") -> Path:
    """Capture the primary monitor and save a PNG image."""
    output = Path(output_path)
    output.parent.mkdir(parents=True, exist_ok=True)

    with mss.mss() as camera:
        monitor = camera.monitors[1]
        frame = camera.grab(monitor)
        image = Image.frombytes("RGB", frame.size, frame.rgb)
        image.save(output)

    return output
