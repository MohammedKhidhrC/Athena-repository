"""Main Athena agent loop."""

from .actions import ActionExecutor
from .config import AthenaConfig, DEFAULT_CONFIG
from .planner import plan


def run(task: str, config: AthenaConfig = DEFAULT_CONFIG) -> int:
    """Plan and safely execute a task.

    Returns the number of planned actions. The default configuration is dry-run.
    """
    actions = plan(task)
    if not actions:
        print("No safe plan available for this task yet.")
        return 0

    executor = ActionExecutor(dry_run=config.dry_run)
    if len(actions) > config.max_actions:
        raise ValueError("Planner produced too many actions")

    for action in actions:
        executor.execute(action)

    return len(actions)
