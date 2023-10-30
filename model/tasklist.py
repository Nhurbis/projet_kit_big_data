from typing import List, Optional, Dict
from config.db_config import db
import uuid
from utils.loggers import errors_logger
from model.task import Task


class TaskList:
    """A class to represent a TaskList.

    Attributes:
        _id (str): Unique identifier for the task list.
        title (str): Title of the task list.
        tasks (List[Task]): List of tasks in the task list.

    """

    def __init__(self, title: str, tasks: Optional[List[Task]] = None, _id: Optional[str] = None) -> None:
        """Initialize a TaskList instance.

        Args:
            title (str): Title of the task list.
            tasks (List[Task], optional): List of tasks. Defaults to an empty list.
            _id (str, optional): Unique identifier. Defaults to a new UUID.

        """
        self._id: str = _id if _id is not None else str(uuid.uuid4())
        self.title: str = title
        self.tasks: List[Task] = tasks if tasks is not None else []

    def save(self) -> None:
        """Save TaskList to the database."""
        try:
            tasklist_data = {
                "title": self.title,
                "tasks": [task.to_dict() for task in self.tasks],
            }
            db.tasklists.update_one(
                {"_id": self._id}, {"$set": tasklist_data}, upsert=True)
        except Exception as e:
            errors_logger.error(
                f"An error occurred while saving TaskList: {str(e)}")
            raise

    @staticmethod
    def get_tasklist_by_id(tasklist_id: str) -> Optional['TaskList']:
        """Retrieve a TaskList from the database by its ID.

        Args:
            tasklist_id (str): Unique identifier of the task list.

        Returns:
            Optional[TaskList]: A TaskList instance if found, None otherwise.

        """
        try:
            data = db.tasklists.find_one({"_id": tasklist_id})
            if data:
                tasks = [Task.from_dict(task_data)
                         for task_data in data.get('tasks', [])]
                return TaskList(title=data['title'], tasks=tasks, _id=data['_id'])
        except Exception as e:
            errors_logger.error(
                f"An error occurred while retrieving TaskList: {str(e)}")
        return None
    
    @staticmethod
    def get_all_tasklists() -> List['TaskList']:
        """Retrieve all TaskLists from the database.

        Returns:
            List[TaskList]: A list of TaskList instances.

        """
        try:
            data = db.tasklists.find()
            tasklists = []
            for tasklist_data in data:
                tasklists.append(TaskList.from_dict(tasklist_data))
            return tasklists
        except Exception as e:
            errors_logger.error(
                f"An error occurred while retrieving TaskLists: {str(e)}")
            raise
 
    def to_dict(self) -> Dict:
        """Convert TaskList object to dictionary."""
        return {
            "_id": self._id,
            "title": self.title,
            "tasks": [task.to_dict() for task in self.tasks],
        }

    @classmethod
    def from_dict(cls, data: Dict) -> "TaskList":
        """Create a TaskList object from a dictionary.

        Args:
            data (Dict[str, Union[List[Task], str]]): Dictionary to create a TaskList from.

        Returns:
            TaskList: A TaskList instance created from the provided dictionary.

        """
        tasks = [Task.from_dict(task) for task in data.get("tasks", [])]
        _id = data.get("_id")
        return cls(title=data["title"], tasks=tasks, _id=_id)
