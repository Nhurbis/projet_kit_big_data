
class TaskAlreadyExistsError(Exception):
    """
    Exception raised when a task already exists.
    """
    pass


class TaskNotFoundError(Exception):
    """
    Exception raised when a task is not found.
    """
    pass
