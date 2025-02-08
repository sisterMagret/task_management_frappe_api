import unittest
import frappe
from task_app.utils import CacheManager
from task_app.services import TaskService

class TestCacheManager(unittest.TestCase):
    def setUp(self):
        """Create a task and cache it"""
        self.task = TaskService.create_task("Cached Task", "Testing caching")
        CacheManager.get_cached_task(self.task["name"])

    def test_cache_retrieval(self):
        """Test if task is retrieved from cache"""
        cached_task = CacheManager.get_cached_task(self.task["name"])
        self.assertEqual(cached_task["title"], self.task["title"])

    def test_cache_invalidates_on_delete(self):
        """Test cache invalidation after task deletion"""
        TaskService.delete_task(self.task["name"])
        CacheManager.invalidate_cache(self.task["name"])
        with self.assertRaises(frappe.DoesNotExistError):
            CacheManager.get_cached_task(self.task["name"])

if __name__ == "__main__":
    unittest.main()
