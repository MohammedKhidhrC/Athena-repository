from pathlib import Path
import asyncio
from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse

BASE_DIR = Path(__file__).resolve().parent
app = FastAPI(title="Athena Live Demo")

@app.get("/", response_class=HTMLResponse)
async def home():
    return (BASE_DIR / "static" / "live.html").read_text(encoding="utf-8")


def plan_task(task: str):
    lower = task.lower()
    actions = []
    if "notepad" in lower or "text editor" in lower:
        actions.append(("OPEN", "notepad"))
    if "type" in lower:
        marker = lower.find("type")
        text = task[marker + 4:].strip()
        if text:
            actions.append(("TYPE", text))
    if "click" in lower:
        actions.append(("CLICK", "virtual button"))
    if not actions:
        actions.append(("OBSERVE", "virtual desktop"))
    return actions


@app.websocket("/ws/demo")
async def demo(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            data = await websocket.receive_json()
            task = str(data.get("task", "")).strip()
            if not task:
                await websocket.send_json({"type": "error", "message": "Enter a task."})
                continue

            commands = plan_task(task)
            await websocket.send_json({"type": "reset"})
            events = [
                ("brain", "python -m athena.demo --task " + repr(task)),
                ("log", "[Python] Athena process started"),
                ("log", "[Vision] Capturing virtual desktop..."),
                ("terminal", "$ python -m athena.demo"),
                ("log", "[Planner] Converting task into safe actions..."),
            ]
            for kind, message in events:
                await websocket.send_json({"type": kind, "message": message})
                await asyncio.sleep(0.45)

            for action, value in commands:
                await websocket.send_json({"type": "action", "action": action, "value": value})
                await asyncio.sleep(0.8)

            await websocket.send_json({"type": "log", "message": "[Verify] Checking simulated result..."})
            await asyncio.sleep(0.6)
            await websocket.send_json({"type": "done", "message": "Demo complete — host computer untouched."})
    except WebSocketDisconnect:
        return
