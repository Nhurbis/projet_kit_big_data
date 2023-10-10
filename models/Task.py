from datetime import datetime

class Task:
    def __init__(self:str, name:str, description, tags=None):
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.completed = False
        self.last_modified = datetime.now()
        self.completion_date = None
        self.tags = tags if tags else []

    def mark_completed(self):
        self.completed = True
        self.completion_date = datetime.now()

    def update_task(self, new_name=None, new_description=None):
        if new_name:
            self.name = new_name
        if new_description:
            self.description = new_description
        self.last_modified = datetime.now()

    def add_tag(self, tag):
        if tag not in self.tags:
            self.tags.append(tag)
            self.last_modified = datetime.now()

    def remove_tag(self, tag):
        if tag in self.tags:
            self.tags.remove(tag)
            self.last_modified = datetime.now()

    def __str__(self):
        return f"{self.name} - {self.description} (Completed: {self.completed})"

