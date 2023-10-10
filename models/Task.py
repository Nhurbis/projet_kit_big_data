from datetime import datetime

class Task:
    """
    A class to represent a Task object.
    
    :param name: The name of the task.
    :type name: str
    :param description: A description of the task.
    :type description: str
    :param tags: A list of tags associated with the task. Optional.
    :type tags: list, optional
    
    :ivar name: The name of the task.
    :ivar description: A description of the task.
    :ivar created_at: The time the task was created.
    :ivar completed: Whether the task is completed or not.
    :ivar last_modified: The time the task was last modified.
    :ivar completion_date: The time the task was completed.
    :ivar tags: A list of tags associated with the task.
    """

    def __init__(self, name, description, tags=None):
        """
        Initializes a Task object with a name, description, and optional tags.
        
        :param name: The name of the task.
        :type name: str
        :param description: A description of the task.
        :type description: str
        :param tags: A list of tags associated with the task. Defaults to None.
        :type tags: list, optional
        """
        self.name = name
        self.description = description
        self.created_at = datetime.now()
        self.completed = False
        self.last_modified = datetime.now()
        self.completion_date = None
        self.tags = tags if tags else []

    def mark_completed(self):
        """
        Marks a task as completed and updates the completion_date.
        
        :returns: None
        """
        self.completed = True
        self.completion_date = datetime.now()

    def update_task(self, new_name=None, new_description=None):
        """
        Updates the name and/or description of a task and sets the last_modified date.
        
        :param new_name: The new name for the task. Defaults to None.
        :type new_name: str, optional
        :param new_description: The new description for the task. Defaults to None.
        :type new_description: str, optional
        
        :returns: None
        """
        if new_name:
            self.name = new_name
        if new_description:
            self.description = new_description
        self.last_modified = datetime.now()

    def add_tag(self, tag):
        """
        Adds a tag to the task if it doesn't already exist and updates the last_modified date.
        
        :param tag: The tag to add.
        :type tag: str
        
        :returns: None
        """
        if tag not in self.tags:
            self.tags.append(tag)
            self.last_modified = datetime.now()

    def remove_tag(self, tag):
        """
        Removes a tag from the task if it exists and updates the last_modified date.
        
        :param tag: The tag to remove.
        :type tag: str
        
        :returns: None
        """
        if tag in self.tags:
            self.tags.remove(tag)
            self.last_modified = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the Task object.
        
        :returns: A string representing the task.
        :rtype: str
        """
        return f"{self.name} - {self.description} (Completed: {self.completed})"
