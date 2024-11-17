from src.api.version import API_VERSION
from fastapi import APIRouter, Depends, status
from uuid import UUID
from typing import List
from src.domain.models import Task, TaskCreate
from sqlalchemy.orm import Session
from src.repositories.tasks_repository import TasksRepository
from src.db.session import get_db


router = APIRouter(
    prefix=f"/api/{API_VERSION}/tasks",
    tags=["tasks"],
    responses={
        status.HTTP_500_INTERNAL_SERVER_ERROR: {"description": "Internal server error"}
    },
)


@router.post("", response_model=Task)
def create_task(task: TaskCreate, db: Session = Depends(get_db)):
    repository = TasksRepository(db)
    return repository.create_task(task)


@router.get("", response_model=List[Task])
def list_tasks(db: Session = Depends(get_db)):
    repository = TasksRepository(db)
    return repository.list_tasks()


@router.put("/{task_id}", response_model=Task)
def update_task(task_id: UUID, updated_task: TaskCreate, db: Session = Depends(get_db)):
    repository = TasksRepository(db)
    return repository.update_task(task_id, updated_task)


@router.delete("/{task_id}", response_model=Task)
def delete_task(task_id: UUID, db: Session = Depends(get_db)):
    repository = TasksRepository(db)
    return repository.delete_task(task_id)
