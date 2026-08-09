"""Command-line entry point for Athena."""

import argparse

from .agent import run


def main() -> None:
    parser = argparse.ArgumentParser(description="Athena AI computer-use agent")
    parser.add_argument("task", nargs="?", default="type hello in notepad")
    args = parser.parse_args()
    run(args.task)


if __name__ == "__main__":
    main()
