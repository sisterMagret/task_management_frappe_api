import unittest
from ..validators import TaskValidator
from ..exceptions import ValidationError

class TestTaskValidator(unittest.TestCase):
    """Unit tests for TaskValidator"""

    def setUp(self):
        """Set up common variables for tests"""
        self.valid_title = "Valid Task"
        self.valid_description = "This is a valid task."

    def test_valid_task(self):
        """Should pass validation for a valid task"""
        self.assertIsNone(TaskValidator.validate_title(self.valid_title))
        self.assertIsNone(TaskValidator.validate_description(self.valid_description))

    def test_missing_title(self):
        """Should raise ValidationError for missing title"""
        with self.assertRaises(ValidationError):
            TaskValidator.validate_title("")

    def test_short_title(self):
        """Should raise ValidationError for a short title"""
        with self.assertRaises(ValidationError):
            TaskValidator.validate_title("Go")

    def test_long_title(self):
        """Should raise ValidationError for an excessively long title"""
        long_title = "A" * 300
        with self.assertRaises(ValidationError):
            TaskValidator.validate_title(long_title)

    def test_invalid_description(self):
        """Should raise ValidationError if description is not a string"""
        with self.assertRaises(ValidationError):
            TaskValidator.validate_description(1234)  # Invalid type

    def test_valid_task_id(self):
        """Should pass validation for a correctly formatted task ID"""
        self.assertIsNone(TaskValidator.validate_task_id("TASK-1234"))

    def test_invalid_task_id(self):
        """Should raise ValidationError for incorrect task ID format"""
        with self.assertRaises(ValidationError):
            TaskValidator.validate_task_id("1234-TASK")

if __name__ == "__main__":
    unittest.main()
