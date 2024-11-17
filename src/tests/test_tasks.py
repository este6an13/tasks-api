from src.domain.models import TaskCreate
from src.repositories.tasks_repository import TasksRepository
from src.api.version import API_VERSION

API_URL = f"/api/{API_VERSION}/tasks"


def test_create_task(client):
    payload = {
        "title": "Test Task",
        "description": "A test task description",
        "status": "pending",
    }
    response = client.post(API_URL, json=payload)
    assert response.status_code == 200
    data = response.json()
    assert "id" in data
    assert data["title"] == payload["title"]
    assert data["description"] == payload["description"]
    assert data["status"] == payload["status"]


def test_list_tasks(client, db_session):
    task1 = TaskCreate(title="Task 1", description="Description 1", status="pending")
    task2 = TaskCreate(title="Task 2", description="Description 2", status="completed")

    repo = TasksRepository(db_session)
    repo.create_task(task1)
    repo.create_task(task2)

    response = client.get(API_URL)
    assert response.status_code == 200
    data = response.json()
    assert len(data) == 2


def test_update_task(client, db_session):

    repo = TasksRepository(db_session)

    task_create = TaskCreate(
        title="Update Task", description="Before Update", status="in progress"
    )
    created_task = repo.create_task(task_create)

    update_payload = {
        "title": "Updated Task",
        "description": "After Update",
        "status": "completed",
    }
    response = client.put(f"{API_URL}/{created_task.id}", json=update_payload)
    assert response.status_code == 200
    updated_task = response.json()
    assert updated_task["title"] == update_payload["title"]
    assert updated_task["description"] == update_payload["description"]
    assert updated_task["status"] == update_payload["status"]


def test_delete_task(client, db_session):

    repo = TasksRepository(db_session)
    task_create = TaskCreate(
        title="Delete Task", description="To be deleted", status="pending"
    )
    created_task = repo.create_task(task_create)

    response = client.delete(f"{API_URL}/{created_task.id}")
    assert response.status_code == 200
    assert response.json()["title"] == "Delete Task"

    # Ensure it's gone
    response = client.get(API_URL)
    assert len(response.json()) == 0
