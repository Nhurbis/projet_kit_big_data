from todolist.config.db_config import db
from datetime import datetime
from todolist.models.Task import Task


class TaskList:
    def __init__(self):
        self.collection = db.tasks  # Suppose que vous avez une collection nommée "tasks"

    def add_task(self, name, description, tags=None):
        if self.collection.find_one({"name": name}):
            print("Cette tâche existe déjà.")
            return
        task = Task(name, description, tags)
        self.collection.insert_one(task.to_dict())

    def complete_task(self, name):
        if not self.collection.find_one({"name": name}):
            print("Cette tâche n'existe pas.")
            return
        self.collection.update_one(
            {"name": name}, {"$set": {"completed": True, "completion_date": datetime.now()}})

    def remove_task(self, name):
        if not self.collection.find_one({"name": name}):
            print("Cette tâche n'existe pas.")
            return
        self.collection.delete_one({"name": name})

    def display_tasks(self):
        tasks = self.collection.find()
        if not tasks:
            print("Aucune tâche à afficher.")
            return
        for task_data in tasks:
            task = Task.from_dict(task_data)
            print(task)
