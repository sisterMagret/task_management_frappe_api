import unittest
import frappe
from task_app.services import TaskService
from task_app.exceptions import NotFoundError, ValidationError

class TestTaskService(unittest.TestCase):
    def setUp(self):
        """Set up a test task"""
        self.task = TaskService.create_task("Test Task", "Test Description")

    def test_create_task(self):
        """Test task creation"""
        task = TaskService.create_task("New Task", "This is a new task.")
        self.assertIsNotNone(task)
        self.assertEqual(task["title"], "New Task")

    def test_get_task(self):
        """Test fetching a task"""
        fetched_task = TaskService.get_task(self.task["name"])
        self.assertEqual(fetched_task["title"], self.task["title"])

    def test_update_task(self):
        """Test updating a task"""
        updated_task = TaskService.update_task(self.task["name"], title="Updated Task")
        self.assertEqual(updated_task["title"], "Updated Task")

    def test_delete_task(self):
        """Test deleting a task"""
        TaskService.delete_task(self.task["name"])
        with self.assertRaises(NotFoundError):
            TaskService.get_task(self.task["name"])

if __name__ == "__main__":
    unittest.main()
