# Athena — AI Computer Agent

> An open-source Windows AI computer-use agent built around local AI, vision, planning, and verified mouse/keyboard control.

**Status:** 🚧 Early development

## What is Athena?

Athena explores how a local AI system can understand what is visible on a Windows computer, decide what to do next, perform the action, and verify the result.

```text
Screen → Capture → Vision/OCR → Local LLM Planner → Action Validator → Mouse/Keyboard → Verification → Next action
```

## Goals

- Capture the Windows screen reliably
- Understand screen content with vision/OCR
- Convert natural-language tasks into structured actions
- Control the mouse and keyboard
- Verify actions instead of blindly continuing
- Recover from failed actions
- Run locally where practical
- Keep dangerous or destructive actions behind confirmation

## Technology

- Python
- Ollama / local LLMs
- Screen capture
- OCR / computer vision
- Windows mouse and keyboard automation

## Repository structure

```text
Athena-repository/
├── athena/
│   ├── __init__.py
│   ├── config.py
│   ├── capture.py
│   ├── planner.py
│   ├── actions.py
│   └── agent.py
├── tests/
├── requirements.txt
├── .gitignore
└── README.md
```

## Quick start

Use Python 3.12+ on Windows.

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python -m athena
```

The first version provides a small, inspectable foundation. Model calls and computer control are kept behind explicit modules rather than hidden inside one script.

## Roadmap

- [x] Initial repository structure
- [x] Configuration layer
- [x] Screen-capture abstraction
- [x] Structured action model
- [x] Dry-run agent loop
- [ ] Ollama planner integration
- [ ] Vision/OCR integration
- [ ] Windows mouse/keyboard adapter
- [ ] Action verification
- [ ] Retry and recovery
- [ ] Task history and logs
- [ ] Example computer-use tasks
- [ ] Automated tests and CI

## Safety

Athena should not execute destructive, financial, credential-changing, or other sensitive actions without explicit confirmation. Development should prefer dry-run mode while capabilities are being tested.

## Contributing

Small, focused improvements are welcome. Start with documentation, tests, bug fixes, or isolated modules before changing the core agent loop.

## Author

**Mohammed Khidhr C**

GitHub: https://github.com/MohammedKhidhrC
