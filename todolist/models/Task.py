from datetime import datetime
from todolist.utils.loggers import debug_logger, general_logger
from todolist.utils.exception_perso import TaskAlreadyExistsError, TaskNotFoundError
from todolist.config.db_config import db


class Task:
    """
    A class to represent a Task object.

    :param name: The name of the task.
    :type name: str
    :param description: A description of the task.
    :type description: str

    :ivar name: The name of the task.
    :ivar description: A description of the task.
    :ivar created_at: The time the task was created.
    :ivar completed: Whether the task is completed or not.
    :ivar last_modified: The time the task was last modified.
    :ivar completion_date: The time the task was completed.
    """

    def __init__(self, name, description=""):
        """
        Initializes a Task object with a name and description.

        :param name: The name of the task.
        :type name: str
        :param description: A description of the task.
        :type description: str
        """
        try:
            if not isinstance(name, str):
                debug_logger.debug(
                    "init: name not a string : %s.", type(name))
                raise TypeError(
                    "Le nom doit être une châine de caractères.")

            if not isinstance(description, str):
                debug_logger.debug(
                    "init: description not a string : %s.", type(description))
                raise ValueError(
                    "La description doit être une chaîne de caractère.")
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.completed = False
        self.last_modified = datetime.now()
        self.completion_date = None

    def __str__(self):
        """
        Returns a string representation of the Task object.

        :returns: A string representing the task.
        :rtype: str
        """
        return f"{self.name} - {self.description} (Completed: {self.completed})"

    def to_dict(self):
        """
        Returns a dictionary representation of the Task object.

        :returns: A dictionary representing the task.
        :rtype: dict
        """
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "completed": self.completed,
            "last_modified": self.last_modified,
            "completion_date": self.completion_date,
        }

    @classmethod
    def from_dict(cls, data):
        """
        Creates a Task object from a dictionary.

        :param data: The dictionary to create the Task object from.
        :type data: dict

        :returns: A Task object.
        :rtype: Task
        """
        task = cls(data["name"], data["description"])
        task.created_at = data["created_at"]
        task.completed = data["completed"]
        task.last_modified = data["last_modified"]
        task.completion_date = data["completion_date"]
        return task
    
    @staticmethod
    def completed(collection, name):
        """
        Marks a task as completed.
        """
        try:
            if not collection.find_one({"name": name}):
                debug_logger.debug("completed: task inexisante : ", name)
                general_logger.info(
                    "Tentative de complétion d'une tâche inexistante : %s", name)
                raise TaskNotFoundError("La tâche '%s' n'existe pas." % name)
            
            else :
                general_logger.info("Complétion d'une tâche : %s", name)
                collection.update_one(
                    {"name": name}, {"$set": {"completed": True, "completion_date": datetime.now()}})
        except TaskNotFoundError as e:
            print(e)
    
    @staticmethod
    def update(collection, name, new_name, new_description):
        """
        Updates a task's name and/or description.
        """
        try:
            if not isinstance(name, str):
                debug_logger.debug("update: name n'est pas un string: %s.", type(name))
                raise TypeError(
                    "Le nom de la task à modifier doit être des chaînes de caractères.")

            elif not new_description and not new_name:
                debug_logger.debug("update: new_description et new_name sont vides: %s.", name)
                raise ValueError("Le nom et la description ne peuvent pas être vides.")

            elif not collection.find_one({"name": name}):
                debug_logger.debug("update: La tâche n'existe pas: %s.", name)
                general_logger.info("Tentative de modification d'une tache inexistante : %s", name)
                raise TaskNotFoundError("La tache '%s' n'existe pas." % name)
        except TypeError as e:
            print(e)
            return
        except ValueError as e:
            print(e)
            return
        except TaskNotFoundError as e:
            print(e)
            return
        
        if new_description:
            if not isinstance(new_description, str):
                debug_logger.debug("update: new_description n'est pas un string: %s.", type(new_description))
                general_logger.info("Tentative de modification de la description d'une tache avec une description non string : %s", new_description)
            else:
                general_logger.info("Update de la tâche %s avec nouvelle description %s e", name, new_description)
                collection.update_one({"name": name}, {"$set": {"description": new_description}})
                
        if new_name:
            if not isinstance(new_name, str):
                debug_logger.debug("update: new_name n'est pas un string: %s.", type(new_name))
                general_logger.info("Tentative de modification du nom d'une tache avec un nom non string : %s", new_name)
            else:
                general_logger.info("Update de la tâche %s avec nouveau nom %s e", name, new_name)
                collection.update_one({"name": name}, {"$set": {"name": new_name}})
        