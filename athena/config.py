"""Configuration for the Athena agent."""

from dataclasses import dataclass


@dataclass(frozen=True)
class AthenaConfig:
    """Runtime configuration with safe defaults."""

    model: str = "qwen3:4b"
    dry_run: bool = True
    screenshot_dir: str = "screenshots"
    max_actions: int = 20


DEFAULT_CONFIG = AthenaConfig()
