import frappe
from frappe.model.document import Document

class Task(Document):
    """Frappe DocType for managing tasks."""
    def before_save(self):
        """Validation before saving"""
        if not self.title:
            frappe.throw("Task title is required")
