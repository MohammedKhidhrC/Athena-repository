"""Main Athena agent loop."""

from .actions import ActionExecutor
from .config import AthenaConfig, DEFAULT_CONFIG
from .planner import plan
from .vision import observe_screen


def run(task: str, config: AthenaConfig = DEFAULT_CONFIG) -> int:
    """Observe, plan, and execute a task within configured limits."""
    observation = observe_screen(config.screenshot_dir + "/observation.png")
    print(f"[VISION] {observation.width}x{observation.height} -> {observation.image_path}")

    actions = plan(task)
    if not actions:
        print("No safe plan available for this task yet.")
        return 0

    if len(actions) > config.max_actions:
        raise ValueError("Planner produced too many actions")

    executor = ActionExecutor(dry_run=config.dry_run)
    for action in actions:
        executor.execute(action)

    return len(actions)
