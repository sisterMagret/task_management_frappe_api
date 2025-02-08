import unittest
from ..services import TaskService
from ..exceptions import NotFoundError

class TestTaskService(unittest.TestCase):
    def test_create_task(self):
        task = TaskService.create_task("New Task", "This is a test task")
        self.assertIsNotNone(task)
        self.assertEqual(task["title"], "New Task")

    def test_get_task(self):
        task = TaskService.create_task("Sample Task", "Another task")
        fetched_task = TaskService.get_task(task["name"])
        self.assertEqual(fetched_task["title"], "Sample Task")

    def test_update_task(self):
        task = TaskService.create_task("Update Me", "Before update")
        updated_task = TaskService.update_task(task["name"], title="Updated Task")
        self.assertEqual(updated_task["title"], "Updated Task")

    def test_delete_task(self):
        task = TaskService.create_task("Delete Me", "Will be deleted")
        TaskService.delete_task(task["name"])
        with self.assertRaises(NotFoundError):
            TaskService.get_task(task["name"])

if __name__ == "__main__":
    unittest.main()
