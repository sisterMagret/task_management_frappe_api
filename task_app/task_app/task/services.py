import frappe
from task_app.exceptions import NotFoundError, ValidationError

class TaskService:
    @staticmethod
    def create_task(title, description):
        """Business logic for creating a task"""
        if not title:
            raise ValidationError("Title is required")

        task = frappe.get_doc({
            "doctype": "Task",
            "title": title,
            "description": description
        })
        task.insert()
        return task.as_dict()

    @staticmethod
    def get_task(task_id):
        """Retrieve a task"""
        task = frappe.get_doc("Task", task_id)
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found")
        return task.as_dict()

    @staticmethod
    def update_task(task_id, title=None, description=None):
        """Update a task"""
        task = frappe.get_doc("Task", task_id)
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found")

        if title:
            task.title = title
        if description:
            task.description = description

        task.save()
        return task.as_dict()

    @staticmethod
    def delete_task(task_id):
        """Delete a task"""
        task = frappe.get_doc("Task", task_id)
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found")
        task.delete()
