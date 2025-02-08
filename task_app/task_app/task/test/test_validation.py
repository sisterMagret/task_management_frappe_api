import unittest
from task_app.validators import validate_task
from task_app.exceptions import ValidationError

class TestTaskValidation(unittest.TestCase):
    def test_valid_task(self):
        """Test valid task inputs"""
        self.assertIsNone(validate_task("Valid Task", "This is a valid task."))

    def test_missing_title(self):
        """Test missing title validation"""
        with self.assertRaises(ValidationError):
            validate_task("", "Missing title should raise error")

    def test_title_length(self):
        """Test overly long title validation"""
        long_title = "A" * 300
        with self.assertRaises(ValidationError):
            validate_task(long_title, "Title too long")

if __name__ == "__main__":
    unittest.main()
