from todolist.config.db_config import db
from datetime import datetime
from todolist.models.Task import Task

class TaskList:
    """
    A class to manage a list of Task objects.
    
    :ivar tasks: A dictionary to hold Task objects.
    """

    def __init__(self):
        """
        Initializes an empty dictionary to hold Task objects.
        
        :returns: None
        """
        self.tasks = {}

    def add_task(self, name, description, tags=None):
        """
        Adds a new task to the task list.
        
        :param name: The name of the task.
        :type name: str
        :param description: The description of the task.
        :type description: str
        :param tags: A list of tags for the task. Defaults to None.
        :type tags: list, optional
        
        :returns: A message indicating success or failure.
        :rtype: str
        """
        if self.collection.find_one({"name": name}):
            print("Cette tâche existe déjà.")
            return
        task = Task(name, description, tags)
        self.collection.insert_one(task.to_dict())

    def complete_task(self, name):
        """
        Marks a task as complete.
        
        :param name: The name of the task to complete.
        :type name: str
        
        :returns: A message indicating success or failure.
        :rtype: str
        """
        if not self.collection.find_one({"name": name}):
            print("Cette tâche n'existe pas.")
            return
        self.collection.update_one(
            {"name": name}, {"$set": {"completed": True, "completion_date": datetime.now()}})

    def remove_task(self, name):
        """
        Removes a task from the task list.
        
        :param name: The name of the task to remove.
        :type name: str
        
        :returns: A message indicating success or failure.
        :rtype: str
        """
        if not self.collection.find_one({"name": name}):
            print("Cette tâche n'existe pas.")
            return
        self.collection.delete_one({"name": name})

    def display_tasks(self):
        """
        Displays all tasks in the task list.
        
        :returns: None
        """
        tasks = self.collection.find()
        if not tasks:
            print("Aucune tâche à afficher.")
            return
        for task_data in tasks:
            task = Task.from_dict(task_data)
            print(task)