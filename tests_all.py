from fastapi.testclient import TestClient
from task_service.main import app as t_app
from notification_service.main import app as n_app

def test_create_task():
    r = TestClient(t_app).post("/api/tasks", json={"title": "Test"})
    assert r.status_code == 201
    assert r.json()["status"] == "new"
    assert r.json()["title"] == "Test"

def test_webhook():
    r = TestClient(n_app).post("/api/webhooks/task_created", json={
        "id": "1", "title": "t", "description": "",
        "status": "new", "created_at": "2025-01-01T00:00:00Z",
    })
    assert r.status_code == 200
    assert r.json() == {"status": "ok"}