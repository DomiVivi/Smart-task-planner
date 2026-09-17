from fastapi import FastAPI
from uuid import uuid4
from datetime import datetime, timezone
import httpx, logging

logging.basicConfig(level=logging.INFO)
app = FastAPI()
tasks = []


@app.post("/api/tasks", status_code=201)   
async def create_task(data: dict):
    task = {
        "id": str(uuid4()),
        "title": data["title"],
        "description": data.get("description", ""),
        "status": "new",
        "created_at": datetime.now(timezone.utc).isoformat(),
    }
    tasks.append(task)

    for i in range(3):
        try:
            async with httpx.AsyncClient(timeout=3) as c:
                r = await c.post(
                    "http://localhost:8001/api/webhooks/task_created",
                    json=task,
                )
                if r.status_code == 200:
                    break
        except Exception as e:
            logging.warning(f"try {i+1} failed: {e}")
    else:
        logging.error("webhook failed after 3 attempts")

    return task


@app.get("/api/tasks")
async def list_tasks():
    return tasks