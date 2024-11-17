from sqlalchemy.orm import Session
from src.domain.models import Task as TaskSchema
from src.domain.models import TaskCreate
from src.db.models import Task as DBTask
from uuid import UUID, uuid4
from fastapi import HTTPException
from typing import List
from src.repositories.conversions import db_to_schema, schema_to_db


class TasksRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_task(self, task_create: TaskCreate) -> TaskSchema:
        """Create a new task."""
        task = TaskSchema(id=uuid4(), **task_create.model_dump())
        db_task = schema_to_db(task)
        self.db.add(db_task)
        self.db.commit()
        self.db.refresh(db_task)
        return task

    def list_tasks(self) -> List[TaskSchema]:
        """List all tasks."""
        db_tasks = self.db.query(DBTask).all()
        return [db_to_schema(db_task) for db_task in db_tasks]

    def update_task(self, task_id: UUID, updated_task: TaskCreate) -> TaskSchema:
        """Update an existing task by ID."""
        db_task = self.db.query(DBTask).filter(DBTask.id == str(task_id)).first()
        if not db_task:
            raise HTTPException(status_code=404, detail="Task not found")

        db_task.title = updated_task.title
        db_task.description = updated_task.description
        db_task.status = updated_task.status
        self.db.commit()
        self.db.refresh(db_task)
        task = db_to_schema(db_task)
        return task

    def delete_task(self, task_id: UUID) -> TaskSchema:
        """Delete a task by ID."""
        db_task = self.db.query(DBTask).filter(DBTask.id == str(task_id)).first()
        if not db_task:
            raise HTTPException(status_code=404, detail="Task not found")

        self.db.delete(db_task)
        self.db.commit()
        task = db_to_schema(db_task)
        return task
