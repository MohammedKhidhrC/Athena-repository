"""Command-line entry point for Athena."""

import argparse

from .agent import run
from .config import AthenaConfig


def main() -> None:
    parser = argparse.ArgumentParser(description="Athena AI computer-use agent")
    parser.add_argument("task", nargs="?", default="type hello in notepad")
    parser.add_argument(
        "--live",
        action="store_true",
        help="enable real mouse/keyboard execution; dry-run is the default",
    )
    parser.add_argument(
        "--screenshot-dir",
        default="screenshots",
        help="directory for screen observations",
    )
    args = parser.parse_args()

    config = AthenaConfig(dry_run=not args.live, screenshot_dir=args.screenshot_dir)
    run(args.task, config)


if __name__ == "__main__":
    main()
