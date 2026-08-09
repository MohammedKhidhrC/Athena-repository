---
title: Athena AI Computer Demo
emoji: 🤖
colorFrom: indigo
colorTo: purple
sdk: docker
app_port: 8000
pinned: false
---

# Athena — AI Computer Agent

> An open-source Python AI computer-use project with a safe public web demo.

Athena explores how an AI system can understand a task, plan computer actions, execute them in a controlled environment, and verify the result.

## Public demo

This repository is prepared for deployment as a **Hugging Face Docker Space**. The public demo is sandboxed and does **not** control a visitor's physical computer.

## Local development

```bash
pip install -r requirements.txt
uvicorn app:app --host 0.0.0.0 --port 8000
```

## Core project

The `athena/` package contains screen capture, vision/OCR, planning, and guarded computer-control components. Live Windows control remains opt-in and is intended for local development only.

## Safety

The public demo must never expose the host machine's mouse/keyboard or credentials to arbitrary visitors. Any future AI execution should operate inside a sandbox or virtual environment.

## Author

**Mohammed Khidhr C**

GitHub: https://github.com/MohammedKhidhrC
