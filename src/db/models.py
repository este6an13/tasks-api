from sqlalchemy import Column, String, Enum, Text
from sqlalchemy.orm import validates, declarative_base
import enum

Base = declarative_base()


class TaskStatus(enum.Enum):
    PENDING = "pending"
    IN_PROGRESS = "in progress"
    COMPLETED = "completed"


class Task(Base):
    __tablename__ = "tasks"

    id = Column(String, primary_key=True, unique=True, index=True)
    title = Column(String(100), nullable=False)
    description = Column(Text, nullable=False)
    status = Column(Enum(TaskStatus), nullable=False)

    @validates("status")
    def convert_status(self, key, value):
        if isinstance(value, TaskStatus):
            return value
        return TaskStatus(value)
