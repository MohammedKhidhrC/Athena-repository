"""Structured computer actions used by the planner and executor."""

from dataclasses import dataclass
from typing import Literal

ActionType = Literal["click", "type", "press", "wait", "open"]


@dataclass(frozen=True)
class Action:
    """A single proposed computer action."""

    action: ActionType
    target: str = ""
    text: str = ""

    def describe(self) -> str:
        if self.action == "type":
            return f"type into {self.target!r}: {self.text!r}"
        if self.target:
            return f"{self.action} {self.target!r}"
        return self.action


class ActionExecutor:
    """Dry-run executor; real OS control will be added behind this boundary."""

    def __init__(self, dry_run: bool = True) -> None:
        self.dry_run = dry_run

    def execute(self, action: Action) -> None:
        if self.dry_run:
            print(f"[DRY RUN] {action.describe()}")
            return
        raise NotImplementedError("Live execution is not enabled in Athena 0.1.0")
