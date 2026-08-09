import pytest

from athena.actions import Action, ActionExecutor


def test_click_target_parses_coordinates():
    assert ActionExecutor._coordinates("120, 300") == (120, 300)


def test_click_target_rejects_invalid_coordinates():
    with pytest.raises(ValueError):
        ActionExecutor._coordinates("not-a-coordinate")


def test_unknown_open_target_is_rejected():
    with pytest.raises(ValueError):
        ActionExecutor._open_allowed_target("cmd")


def test_dry_run_does_not_execute():
    executor = ActionExecutor(dry_run=True)
    executor.execute(Action("type", text="Athena test"))
