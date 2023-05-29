# Django To-Do List API

This is a simple Django To-Do List API that allows you to perform basic CRUD operations on a task model. The API provides endpoints for creating, reading, updating, and deleting tasks.

## Requirements

- Python 3.7 or higher
- Django 3.1 or higher
- Django Rest Framework 3.12 or higher

## Installation

1. Clone the repository:

```
git clone <repository_url>
```

2. Create and activate a virtual environment:

```
python3 -m venv env
source env/bin/activate
```

3. Install the dependencies:

```
pip install -r requirements.txt
```

4. Run database migrations:

```
python manage.py migrate
```

5. Start the development server:

```
python manage.py runserver
```

The API will be accessible at `http://localhost:8000/`.

## API Endpoints

The following endpoints are available for interacting with the To-Do List API:

- `GET /api/tasks/`: Retrieve a list of all tasks.
- `POST /api/tasks/`: Create a new task.
- `GET /api/tasks/{id}/`: Retrieve a specific task by its ID.
- `PUT /api/tasks/{id}/`: Update a specific task by its ID.
- `DELETE /api/tasks/{id}/`: Delete a specific task by its ID.

## Example Usage

### Retrieve all tasks

Send a GET request to `http://localhost:8000/api/tasks/` to retrieve a list of all tasks:

```
GET /api/tasks/
```

### Create a new task

Send a POST request to `http://localhost:8000/api/tasks/` with the task details in the request body to create a new task:

```
POST /api/tasks/

Request Body:
{
  "title": "Finish project",
  "description": "Complete the project by the end of the week",
  "completed": false
}
```

### Retrieve a specific task

Send a GET request to `http://localhost:8000/api/tasks/{id}/` to retrieve a specific task by its ID:

```
GET /api/tasks/1/
```

### Update a specific task

Send a PUT request to `http://localhost:8000/api/tasks/{id}/` with the updated task details in the request body to update a specific task by its ID:

```
PUT /api/tasks/1/

Request Body:
{
  "title": "Finish project",
  "description": "Complete the project by tomorrow",
  "completed": true
}
```

### Delete a specific task

Send a DELETE request to `http://localhost:8000/api/tasks/{id}/` to delete a specific task by its ID:

```
DELETE /api/tasks/1/
```

## Error Handling

The API handles common error scenarios such as invalid requests and missing resources and returns appropriate error responses with status codes and error messages.

## Conclusion

The Django To-Do List API provides a simple way to manage tasks through basic CRUD operations. Feel free to explore and integrate it into your own applications or projects. If you encounter any issues or have suggestions for improvements, please don't hesitate to contact us.
