"""Structured computer actions and a guarded Windows executor."""

from dataclasses import dataclass
import subprocess
import time
from typing import Literal

import pyautogui

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
    """Execute safe, explicit actions on Windows.

    Dry-run remains the default. Live mode is opt-in and uses PyAutoGUI's
    fail-safe behavior so moving the mouse to the top-left corner can abort.
    """

    def __init__(self, dry_run: bool = True) -> None:
        self.dry_run = dry_run
        pyautogui.PAUSE = 0.15
        pyautogui.FAILSAFE = True

    def execute(self, action: Action) -> None:
        print(f"[ATHENA] {action.describe()}")
        if self.dry_run:
            print("[DRY RUN] no computer input sent")
            return

        if action.action == "click":
            x, y = self._coordinates(action.target)
            pyautogui.click(x, y)
        elif action.action == "type":
            pyautogui.write(action.text, interval=0.01)
        elif action.action == "press":
            if not action.target:
                raise ValueError("press action requires a key target")
            pyautogui.press(action.target)
        elif action.action == "wait":
            seconds = float(action.text or action.target or "1")
            if seconds < 0 or seconds > 30:
                raise ValueError("wait must be between 0 and 30 seconds")
            time.sleep(seconds)
        elif action.action == "open":
            self._open_allowed_target(action.target)
        else:
            raise ValueError(f"Unsupported action: {action.action}")

    @staticmethod
    def _coordinates(target: str) -> tuple[int, int]:
        try:
            x_text, y_text = target.replace(" ", "").split(",", 1)
            x, y = int(x_text), int(y_text)
        except ValueError as exc:
            raise ValueError("click target must be 'x,y'") from exc
        if x < 0 or y < 0:
            raise ValueError("click coordinates cannot be negative")
        return x, y

    @staticmethod
    def _open_allowed_target(target: str) -> None:
        allowed = {
            "notepad": ["notepad.exe"],
            "calculator": ["calc.exe"],
            "explorer": ["explorer.exe"],
        }
        command = allowed.get(target.strip().lower())
        if command is None:
            raise ValueError(
                "open target is not allow-listed; use notepad, calculator, or explorer"
            )
        subprocess.Popen(command)
