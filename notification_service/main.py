from fastapi import FastAPI
import logging

logging.basicConfig(
    filename="notifications.log",
    level=logging.INFO,
    format="%(asctime)s %(message)s",
)
app = FastAPI()

@app.post("/api/webhooks/task_created")
async def task_created(task: dict):
    logging.info(f"NOTIFY: {task['id']} — {task['title']}")
    return {"status": "ok"}