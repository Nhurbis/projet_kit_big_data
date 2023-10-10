from datetime import datetime

class Task:
    def __init__(self:str, name:str, description):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.completed = False
        self.last_modified = datetime.now()

    def mark_completed(self):
        self.completed = True

    def update_task(self, new_name=None, new_description=None):
        if new_name:
            self.name = new_name
        if new_description:
            self.description = new_description
        self.last_modified = datetime.now()

    def __str__(self):
        return f"{self.name} - {self.description} (Completed: {self.completed})"

