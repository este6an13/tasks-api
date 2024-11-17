# Tasks API

Tasks API is a simple application for managing tasks, providing endpoints to create, retrieve, update, and delete tasks. It's built with **FastAPI** and uses **SQLAlchemy** for database operations.

## Prerequisites

Make sure you have **Poetry** installed on your system. If not, you can install it by following the [Poetry installation guide](https://python-poetry.org/docs/#installation).

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/tasks-api.git
   cd tasks-api
   ```

2. Install the dependencies:

   ```bash
   poetry install
   ```

## Running the Application

To start the API server, run the following command:

```bash
poetry run uvicorn src.api.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.

## Running Tests

To run the test suite, add `pytest` to your development dependencies and execute the tests:

1. Add `pytest`:

   ```bash
   poetry add pytest --group dev
   ```

2. Run the tests:

   ```bash
   poetry run pytest
   ```

## Endpoints

- **POST /tasks**: Create a new task
- **GET /tasks**: List all tasks
- **PUT /tasks/{task_id}**: Update a task by ID
- **DELETE /tasks/{task_id}**: Delete a task by ID

## License

This project is licensed under the MIT License.
