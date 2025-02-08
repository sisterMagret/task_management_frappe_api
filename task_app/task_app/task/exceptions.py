class NotFoundError(Exception):
    """Exception for missing records"""
    pass

class ValidationError(Exception):
    """Exception for validation failures"""
    pass
