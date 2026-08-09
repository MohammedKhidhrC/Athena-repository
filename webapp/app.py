from pathlib import Path
from fastapi import FastAPI, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Athena Web Simulator")
app.mount("/static", StaticFiles(directory=BASE_DIR / "static"), name="static")

class TaskRequest(BaseModel):
    task: str

@app.get("/", response_class=HTMLResponse)
def home() -> str:
    return (BASE_DIR / "static" / "index.html").read_text(encoding="utf-8")

@app.post("/api/simulate")
def simulate(payload: TaskRequest):
    task = payload.task.strip()
    if not task:
        return {"ok": False, "error": "Enter a task."}

    lower = task.lower()
    actions = []
    if "notepad" in lower or "text editor" in lower:
        actions.append({"action": "open", "target": "notepad"})
    if "type" in lower:
        text = task.split("type", 1)[1].strip() if "type" in lower else ""
        if text:
            actions.append({"action": "type", "text": text})
    if "click" in lower:
        actions.append({"action": "click", "target": "simulated button"})
    if not actions:
        actions = [{"action": "observe", "target": "virtual desktop"}]

    return {
        "ok": True,
        "task": task,
        "steps": [
            {"stage": "understand", "message": "Task received"},
            {"stage": "observe", "message": "Inspecting the virtual desktop"},
            {"stage": "plan", "message": f"Planned {len(actions)} action(s)"},
            {"stage": "execute", "message": "Executing in safe simulation mode"},
            {"stage": "verify", "message": "Simulation completed"},
        ],
        "actions": actions,
        "live": False,
    }
