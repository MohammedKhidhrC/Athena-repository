# Athena — AI Computer Agent

> An open-source Windows AI computer-use agent built around local AI, screen perception, planning, and guarded mouse/keyboard control.

**Status:** 🚧 Early development — perception and guarded computer control are now implemented.

## What is Athena?

Athena explores how a local AI system can understand what is visible on a Windows computer, decide what to do next, perform an action, and verify the result.

```text
Task → Observe screen → Plan → Validate → Act → Observe again → Verify
```

## Current capabilities

- Capture the primary Windows monitor
- Create a `ScreenObservation` with image path and dimensions
- Represent computer actions as structured Python objects
- Dry-run every action by default
- Optional live Windows control through PyAutoGUI
- Guard `open` actions with an explicit allow-list
- Support click, type, press, wait, and safe application-open actions
- Enforce a maximum action count
- Automated tests for executor safety and planner behavior

## Quick start

Use Python 3.12+ on Windows.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
```

### Safe dry-run

```powershell
python -m athena "type hello in notepad"
```

Athena captures a screen observation and prints the planned actions without sending mouse or keyboard input.

### Explicit live mode

```powershell
python -m athena "type hello in notepad" --live
```

Live mode is opt-in. PyAutoGUI fail-safe is enabled; moving the mouse to the top-left corner can abort PyAutoGUI operations.

> **Important:** Live mode is experimental. Do not use it for credentials, financial actions, account changes, destructive commands, or other sensitive operations.

## Repository structure

```text
Athena-repository/
├── athena/
│   ├── __init__.py
│   ├── __main__.py
│   ├── actions.py
│   ├── agent.py
│   ├── capture.py
│   ├── config.py
│   ├── planner.py
│   └── vision.py
├── tests/
│   ├── test_actions.py
│   └── test_planner.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Roadmap

- [x] Initial repository structure
- [x] Configuration layer
- [x] Screen-capture abstraction
- [x] Screen observation module
- [x] Structured action model
- [x] Guarded Windows action executor
- [x] Dry-run agent loop
- [ ] OCR integration
- [ ] Ollama planner integration
- [ ] Vision-language model integration
- [ ] Action verification
- [ ] Retry and recovery
- [ ] Task history and logs
- [ ] More example computer-use tasks
- [ ] Automated CI

## Safety principles

Athena is being developed with conservative defaults:

1. Dry-run is the default.
2. Live execution requires an explicit `--live` flag.
3. Application launching is allow-listed.
4. Action counts are bounded.
5. Sensitive or destructive workflows should require explicit confirmation.
6. Vision and planning should be separated from execution so each layer can be tested independently.

## Contributing

Small, focused improvements are welcome. Start with documentation, tests, bug fixes, isolated adapters, or examples before changing the core agent loop.

## Author

**Mohammed Khidhr C**

GitHub: https://github.com/MohammedKhidhrC
