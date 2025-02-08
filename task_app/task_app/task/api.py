import frappe
from task_app.services import TaskService
from task_app.exceptions import NotFoundError, ValidationError

@frappe.whitelist(allow_guest=False)
def create_task(title, description):
    """Create a new task"""
    try:
        return TaskService.create_task(title, description)
    except ValidationError as e:
        frappe.throw(str(e))

@frappe.whitelist()
def get_task(task_id):
    """Get a task by ID"""
    try:
        return TaskService.get_task(task_id)
    except NotFoundError as e:
        frappe.throw(str(e))

@frappe.whitelist()
def update_task(task_id, title=None, description=None):
    """Update an existing task"""
    try:
        return TaskService.update_task(task_id, title, description)
    except NotFoundError as e:
        frappe.throw(str(e))

@frappe.whitelist()
def delete_task(task_id):
    """Delete a task"""
    try:
        TaskService.delete_task(task_id)
        return {"message": "Task deleted"}
    except NotFoundError as e:
        frappe.throw(str(e))
