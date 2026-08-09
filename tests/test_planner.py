from athena.planner import plan


def test_demo_task_produces_safe_plan():
    actions = plan("type hello in notepad")
    assert len(actions) == 2
    assert actions[0].action == "open"
    assert actions[1].action == "type"
    assert actions[1].text == "hello"


def test_unknown_task_is_not_executed():
    assert plan("do something dangerous") == []
