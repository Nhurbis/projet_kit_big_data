from datetime import datetime
from typing import Optional, Dict
import uuid


class Task:
    """A class to represent a Task.

    Attributes:
        _id (str): Unique identifier for the task.
        name (str): Name of the task.
        description (str): Description of the task.
        created_at (datetime): Creation date and time of the task.
        completed (bool): Status of the task. True if completed, False otherwise.

    """

    def __init__(self, name: str, description: str, completed: bool = False,
                 created_at: Optional[datetime] = None, _id: Optional[str] = None) -> None:
        """Initialize a Task instance.

        Args:
            name (str): Name of the task.
            description (str): Description of the task.
            completed (bool, optional): Status of the task. Defaults to False.
            created_at (datetime, optional): Creation date and time. Defaults to current UTC time.
            _id (str, optional): Unique identifier. Defaults to a new UUID.

        """
        self._id: str = _id if _id is not None else str(uuid.uuid4())
        self.name: str = name
        self.description: str = description
        self.created_at: datetime = created_at if created_at is not None else datetime.utcnow()
        self.completed: bool = completed

    def to_dict(self) -> Dict:
        """Convert Task object to dictionary.

        Returns:
            Dict[str, Union[datetime, str, bool]]: Dictionary representation of the Task instance.

        """
        return {
            "_id": self._id,
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "completed": self.completed,
        }

    @classmethod
    def from_dict(cls, data: Dict) -> 'Task':
        """Create a Task object from a dictionary.

        Args:
            data (Dict[str, Union[datetime, str, bool]]): Dictionary to create a Task from.

        Returns:
            Task: A Task instance created from the provided dictionary.

        """
        _id = data.get('_id')
        name = data.get('name')
        description = data.get('description')
        completed = data.get('completed', False)
        created_at = data.get('created_at')
        if isinstance(created_at, str):
            created_at = datetime.strptime(created_at, "%Y-%m-%d %H:%M:%S")
        elif not isinstance(created_at, datetime):
            created_at = None  
        return cls(name, description, completed, created_at, _id)

    def __str__(self):
        return f"{self.name}: {self.description} (Complétée: {'Oui' if self.completed else 'Non'})"
