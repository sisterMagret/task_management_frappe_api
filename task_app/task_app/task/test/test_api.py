import unittest
import frappe
from task_app.api import create_task, get_task, update_task, delete_task

class TestTaskAPI(unittest.TestCase):
    def setUp(self):
        """Create a test task via API"""
        self.task = create_task("API Task", "Created via API")

    def test_create_task_api(self):
        """Test API task creation"""
        task = create_task("New API Task", "This is a new API task")
        self.assertEqual(task["title"], "New API Task")

    def test_get_task_api(self):
        """Test API get task"""
        fetched = get_task(self.task["name"])
        self.assertEqual(fetched["title"], self.task["title"])

    def test_update_task_api(self):
        """Test API update task"""
        updated_task = update_task(self.task["name"], title="Updated API Task")
        self.assertEqual(updated_task["title"], "Updated API Task")

    def test_delete_task_api(self):
        """Test API delete task"""
        delete_task(self.task["name"])
        with self.assertRaises(frappe.DoesNotExistError):
            get_task(self.task["name"])

if __name__ == "__main__":
    unittest.main()
