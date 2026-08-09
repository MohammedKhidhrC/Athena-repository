# Athena Web Simulator

A Python FastAPI web application that lets users test Athena's computer-use workflow safely in a virtual desktop.

## Run locally

```powershell
cd webapp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn app:app --reload
```

Open http://127.0.0.1:8000

## Safety

This web demo is simulation-only. It never controls the visitor's real mouse, keyboard, browser, or operating system.
