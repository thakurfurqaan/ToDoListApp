# ToDoListApp
Creating this app as an Interview Assessment project for NewsReels. A simple ToDo List Application using Flask, Flask-SQLAlchemy, and SQLite. The application exposes a RESTful API to manage tasks.

## Prerequisites

- Python 3.9 or later
- Docker and Docker Compose

## Running the Application

### Local Development

1. Install the required Python packages:

    ```
    pip install -r requirements.txt
    ```

2. Run the application:

    ```
    python app.py
    ```

    The application will be accessible at `http://localhost:5000/`.

### Using Docker

1. Build the Docker image:

    ```
    docker build -t todo-list-app .
    ```

2. Run the Docker container:

    ```
    docker run -p 5000:5000 todo-list-app
    ```

    The application will be accessible at `http://localhost:5000/`.

### Using Docker Compose

1. Build and run the application using Docker Compose:

    ```
    docker-compose up --build --no-deps
    ```

    The application will be accessible at `http://localhost:5000/`.

## API Endpoints

- `GET /tasks`: Retrieve a list of all tasks.
- `POST /tasks`: Add a new task. Requires a JSON payload with the `name` key.
- `PUT /tasks/<int:task_id>/complete`: Mark a task with the specified `task_id` as complete.

## Running Tests

1. Install the required Python packages for testing:

    ```
    pip install -r requirements.txt
    ```

2. Run the tests:

    ```
    python tests.py
    ```

## Maintainer
- [Furqaan Thakur](thakurfurqaan@gmail.com)
