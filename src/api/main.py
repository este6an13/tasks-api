from fastapi import FastAPI

from src.api.routes import tasks_routes
from src.api.version import API_VERSION

app = FastAPI(
    title="Tasks API",
    description="API for managing user tasks",
    version=API_VERSION,
)

app.include_router(tasks_routes.router)
