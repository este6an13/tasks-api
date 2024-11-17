from pydantic import BaseModel, Field
from typing import Literal, Optional
from uuid import UUID


# For task creation (input schema)
class TaskCreate(BaseModel):
    title: str = Field(
        ..., min_length=1, max_length=100, description="The title of the task"
    )
    description: str = Field(
        ..., min_length=1, max_length=500, description="A brief description of the task"
    )
    status: Literal["pending", "in progress", "completed"] = Field(
        ..., description="The current status of the task"
    )


# For task response (output schema)
class Task(TaskCreate):
    id: UUID
