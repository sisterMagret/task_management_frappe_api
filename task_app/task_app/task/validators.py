import re
from .exceptions import ValidationError

class TaskValidator:
    """Validator class for Task-related operations."""

    @staticmethod
    def validate_title(title):
        """Ensure the title is not empty and follows a valid format."""
        if not title or not isinstance(title, str):
            raise ValidationError("Task title must be a non-empty string.")
        if len(title) < 3:
            raise ValidationError("Task title must be at least 3 characters long.")

    @staticmethod
    def validate_description(description):
        """Ensure the description is a valid string."""
        if description and not isinstance(description, str):
            raise ValidationError("Task description must be a string.")

    @staticmethod
    def validate_task_id(task_id):
        """Ensure task ID is in correct format (e.g., TASK-XXXX)."""
        if not re.match(r"^TASK-\d{4}$", task_id):
            raise ValidationError("Invalid Task ID format. Expected: TASK-XXXX.")
