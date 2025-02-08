import frappe
from .exceptions import NotFoundError
from .validators import TaskValidator

class TaskService:
    @staticmethod
    def create_task(title, description):
        """Business logic for creating a task with validation."""
        TaskValidator.validate_title(title)
        TaskValidator.validate_description(description)

        task = frappe.get_doc({
            "doctype": "Task",
            "title": title,
            "description": description
        })
        task.insert()
        return task.as_dict()

    @staticmethod
    def get_task(task_id):
        """Retrieve a task after validating task ID."""
        TaskValidator.validate_task_id(task_id)

        task = frappe.get_doc("Task", task_id)
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found")
        return task.as_dict()

    @staticmethod
    def update_task(task_id, title=None, description=None):
        """Update a task after validating input."""
        TaskValidator.validate_task_id(task_id)

        task = frappe.get_doc("Task", task_id)
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found")

        if title:
            TaskValidator.validate_title(title)
            task.title = title
        if description:
            TaskValidator.validate_description(description)
            task.description = description

        task.save()
        return task.as_dict()

    @staticmethod
    def delete_task(task_id):
        """Delete a task after validating task ID."""
        TaskValidator.validate_task_id(task_id)

        task = frappe.get_doc("Task", task_id)
        if not task:
            raise NotFoundError(f"Task with ID {task_id} not found")
        task.delete()
