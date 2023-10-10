from datetime import datetime


class Task:
    def __init__(self: str, name: str, description, tags=None):
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

    def to_dict(self):
        return {
            "name": self.name,
            "description": self.description,
            "created_at": self.created_at,
            "completed": self.completed,
            "last_modified": self.last_modified,
            "completion_date": self.completion_date,
            "tags": self.tags
        }

    @classmethod
    def from_dict(cls, data):
        task = cls(data["name"], data["description"], data.get("tags", []))
        task.created_at = data["created_at"]
        task.completed = data["completed"]
        task.last_modified = data["last_modified"]
        task.completion_date = data["completion_date"]
        return task
