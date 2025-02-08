## **Frappe Task App**
A **Frappe-based** backend application for managing tasks with **CRUD operations**, authentication, performance optimization, and error handling.

---

## **Table of Contents**
- [Features](#features)
- [Project Structure](#project-structure)
- [Setup Instructions](#setup-instructions)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Authentication](#authentication)
- [Testing](#testing)
- [Deployment](#deployment)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)

---

## **Features**
**Frappe Framework-based REST API**  
**CRUD operations on "Task" DocType**   
**User authentication with role-based access**  
**Data validation & error handling**  
**Performance optimization with caching**  
**Unit tests with `unittest`**  

---

## **Project Structure**
```
frappe-bench/
│── apps/
│   ├── task_app/
│   │   ├── task/
│   │   │   ├── doctype/
│   │   │   │   ├── task/
│   │   │   │   │   ├── task.py  # Task Model
│   │   │   │   │   ├── task.json  # Metadata
│   │   │   ├── api.py  # API Endpoints
│   │   │   ├── services.py  # Business Logic
│   │   │   ├── validators.py  # Validation Logic
│   │   │   ├── exceptions.py  # Custom Exceptions
│   │   │   ├── utils.py  # Utility Functions (Caching)
│   │   │   ├── test_task.py  # Unit Tests
│   ├── README.md  # Documentation
│── config/
│── tests/
│   ├── test_api.py  # Unit Tests for API
│   ├── test_services.py  # Unit Tests for Business Logic
│   ├── test_validators.py  # Unit Tests for Validation
```

---

## **Setup Instructions**
### **Step 1: Install Frappe**
Ensure **Python 3.10+** is installed, then install Frappe.
```bash
pip install frappe-bench
bench init frappe-bench
cd frappe-bench
```

### **Step 2: Create a New Site**
```bash
bench new-site mysite.local
```

### **Step 3: Install the Task App**
```bash
bench get-app task_app https://github.com/your-username/frappe-task-app.git
bench --site mysite.local install-app task_app
```

### **Step 4: Start the Server**
```bash
bench start
```

---

## **Running the Application**
1. Open **http://localhost:8000**
2. Login with **admin credentials**:
   - **Username:** `Administrator`
   - **Password:** Set during site creation.

---

## **API Endpoints**
### **Create a Task**
```http
POST /api/method/task_app.api.create_task
```
#### **Request Body:**
```json
{
  "title": "New Task",
  "description": "This is a test task"
}
```
#### **Response:**
```json
{
  "message": "Task created successfully",
  "task_id": "TASK-0001"
}
```

---

### **Get a Task**
```http
GET /api/method/task_app.api.get_task?task_id=TASK-0001
```
#### **Response:**
```json
{
  "task_id": "TASK-0001",
  "title": "New Task",
  "description": "This is a test task"
}
```

---

### ** Update a Task**
```http
PUT /api/method/task_app.api.update_task
```
#### **Request Body:**
```json
{
  "task_id": "TASK-0001",
  "title": "Updated Task"
}
```
#### **Response:**
```json
{
  "message": "Task updated successfully"
}
```

---

### **Delete a Task**
```http
DELETE /api/method/task_app.api.delete_task?task_id=TASK-0001
```
#### **Response:**
```json
{
  "message": "Task deleted successfully"
}
```

---

## **Authentication**
### **Login (Get API Key & Secret)**
1. **Login as Administrator**.
2. Go to **User Settings** > **API Access**.
3. Generate **API Key & Secret**.

### **Use API Key & Secret**
Include in **headers**:
```http
Authorization: token <api_key>:<api_secret>
```

---

## **Testing**
### **Run Unit Tests**
```bash
bench --site mysite.local run-tests --app task_app
```

### **Test Services (`test_services.py`)**
```python
import unittest
from task_app.services import TaskService

class TestTaskService(unittest.TestCase):
    def test_create_task(self):
        task = TaskService.create_task("New Task", "Test task")
        self.assertEqual(task["title"], "New Task")

if __name__ == "__main__":
    unittest.main()
```

---

## **Deployment**
### **Push to GitHub**
```bash
git init
git add .
git commit -m "Initial commit"
git remote add origin https://github.com/your-username/frappe-task-app.git
git branch -M main
git push -u origin main
```

## **Troubleshooting**
### **Database Migration Issues**
```bash
bench --site mysite.local migrate
```

### **Frappe Not Running?**
Check logs:
```bash
bench --site mysite.local logs
```

### **Clear Cache Issues**
```bash
bench clear-cache
```

