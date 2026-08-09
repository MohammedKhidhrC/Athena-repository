"""Planning boundary for Athena.

The first version intentionally uses a tiny deterministic planner. A local
LLM adapter can later implement the same interface without changing the agent loop.
"""

from .actions import Action


def plan(task: str) -> list[Action]:
    """Turn a small demo task into structured actions.

    This is deliberately conservative. Unknown tasks produce no actions until
    a real planner is connected and validated.
    """
    normalized = task.strip().lower()
    if normalized == "type hello in notepad":
        return [
            Action("open", target="notepad"),
            Action("type", target="text editor", text="hello"),
        ]
    return []
