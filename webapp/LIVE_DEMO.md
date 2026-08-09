# Athena Live Demo

This is the Python-powered live browser demo for Athena.

## What users see

- A virtual Windows desktop
- A live Python/Command Prompt panel
- Athena's streamed agent events
- A simulated Notepad window
- Mouse movement and action playback

The browser connects to the FastAPI backend over WebSocket at `/ws/demo`.

## Run locally

```powershell
cd webapp
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
uvicorn live_app:app --reload
```

Open `http://127.0.0.1:8000`.

## Docker

```powershell
docker build -t athena-live-demo .
docker run --rm -p 8000:8000 athena-live-demo
```

## Important

The virtual desktop is a browser-rendered simulation. The server does not launch VirtualBox or control a visitor's host computer. A public website cannot safely open VirtualBox on a visitor's machine without local software/permissions. The purpose of this demo is to show Athena's Python agent loop in real time.
