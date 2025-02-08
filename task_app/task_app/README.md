# Task App - Frappe Backend

## Overview
This is a Frappe-based backend application that provides a Task Management system with RESTful APIs for CRUD operations. It follows SOLID principles, includes error handling, and optimizations such as caching. The system allows users to create, update, delete, and retrieve tasks while ensuring authentication and validation.

## Features
- **Task Management**: Create, Read, Update, and Delete tasks.
- **Authentication**: Secure API endpoints.
- **Database Schema**: Normalized DocType relationships.
- **Performance Optimization**: Caching for frequently accessed data.
- **Error Handling**: Custom exceptions and validation.
- **Unit Testing**: Coverage for API and business logic.

## Prerequisites
Ensure you have the following installed:
- Python 3.8+
- Frappe Framework
- Redis (for caching)
- Node.js (for Frappe assets)
- MariaDB or PostgreSQL
- Bench CLI

## Installation
### Step 1: Set up Frappe and Bench
```bash
# Install Bench
pip install frappe-bench

# Initialize a new Bench instance
bench init frappe-bench && cd frappe-bench

# Create a new Frappe site
bench new-site mysite.local
```

### Step 2: Install the Task App
```bash
# Create a new Frappe application
bench new-app task_app

# Install the app on the site
bench --site mysite.local install-app task_app
```

## Running the Application
```bash
bench start
```

## API Endpoints
| Method | Endpoint | Description |
|--------|---------|-------------|
| POST | `/api/method/task_app.api.create_task` | Create a new task |
| GET | `/api/method/task_app.api.get_task?task_id=<id>` | Get a task by ID |
| PUT | `/api/method/task_app.api.update_task` | Update a task |
| DELETE | `/api/method/task_app.api.delete_task?task_id=<id>` | Delete a task |

## Running Tests
To execute unit tests:
```bash
bench --site mysite.local run-tests --app task_app
```

## Project Structure
```
frappe_app/
│── task_app/
│   ├── task/
│   │   ├── doctype/
│   │   │   ├── task/
│   │   │   │   ├── task.py  # Model definition
│   │   ├── api.py  # API implementation
│   │   ├── services.py  # Business logic
│   │   ├── validators.py  # Validation logic
│   │   ├── exceptions.py  # Custom exceptions
│   │   ├── utils.py  # Utility functions
│   │   ├── test_task.py  # Unit tests
│── config/
│── tests/
│   ├── test_api.py  # Unit tests for API
│   ├── test_services.py  # Unit tests for services
│   ├── test_validators.py  # Unit tests for validation
```

## Contribution Guidelines
1. Fork the repository.
2. Create a new branch: `git checkout -b feature-branch`
3. Commit your changes: `git commit -m 'Add new feature'`
4. Push to the branch: `git push origin feature-branch`
5. Submit a pull request.

## License
This project is licensed under the MIT License.

