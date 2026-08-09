# Athena — AI Computer Agent

> An open-source Python AI computer-use project with a safe public web demo.

Athena explores how an AI system can understand a task, plan computer actions, execute them in a controlled environment, and verify the result.

## Public web deployment

The current web demo is designed for **Vercel's free Hobby plan**. It runs the FastAPI application as a Python serverless function and does **not** control a visitor's physical computer.

### Deploy from GitHub

1. Create/sign in to a Vercel account.
2. Import `MohammedKhidhrC/Athena-repository`.
3. Keep the project root at the repository root.
4. Deploy. Vercel detects `api/index.py` and the FastAPI `app` automatically.

Vercel's current documentation supports FastAPI on its Python runtime with Git-based deployment. The Hobby plan is free for personal, non-commercial use; usage is subject to Vercel's limits and terms.

## Local development

```bash
pip install -r requirements.txt
uvicorn webapp.app:app --host 0.0.0.0 --port 8000
```

Then open `http://127.0.0.1:8000`.

## Project structure

```text
api/index.py          # Vercel FastAPI entry point
webapp/app.py         # FastAPI application
webapp/static/        # Public Athena browser interface
athena/               # Core Athena components
vision/               # Vision/OCR components
planner/              # Planning components
tests/                # Automated tests
```

## Safety

The public demo must never expose the host machine's mouse/keyboard, files, credentials, or operating-system shell to arbitrary visitors. Any future AI execution should operate inside a sandbox or virtual environment.

## Roadmap

- [x] Safe browser simulation
- [x] Python/FastAPI backend
- [x] Screen/OCR foundation
- [x] Guarded local computer-control layer
- [x] Vercel deployment entry point
- [ ] Open-source LLM planning
- [ ] Sandboxed virtual computer
- [ ] Vision-grounded actions
- [ ] Public AI computer-use demo

## Author

**Mohammed Khidhr C**

GitHub: https://github.com/MohammedKhidhrC
