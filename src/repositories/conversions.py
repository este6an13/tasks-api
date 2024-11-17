from sqlalchemy.orm import Session
from src.domain.models import Task as TaskSchema
from src.db.models import Task as DBTask, TaskStatus
from uuid import UUID, uuid4
from fastapi import HTTPException
from typing import List


# Convert DB object to Schema object (SQLAlchemy to Pydantic)
def db_to_schema(task: DBTask) -> TaskSchema:

    return TaskSchema(
        id=UUID(task.id),
        title=task.title,
        description=task.description,
        status=task.status.value,
    )


# Convert Schema object to DB object (Pydantic to SQLAlchemy)
def schema_to_db(task: TaskSchema) -> DBTask:

    return DBTask(
        id=str(task.id),
        title=task.title,
        description=task.description,
        status=TaskStatus(task.status),
    )
