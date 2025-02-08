import frappe
from frappe.utils import cache

class CacheManager:
    @staticmethod
    def get_cached_task(task_id):
        cache_key = f"task:{task_id}"
        task = cache.get_value(cache_key)
        if not task:
            task = frappe.get_doc("Task", task_id).as_dict()
            cache.set_value(cache_key, task, expires_in_sec=600)
        return task

    @staticmethod
    def invalidate_cache(task_id):
        cache.delete_value(f"task:{task_id}")
