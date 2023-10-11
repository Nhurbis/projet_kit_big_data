from datetime import datetime

class TagError(Exception):
    pass

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
        if not isinstance(name, str) or not isinstance(description, str):
            debug_logger.debug("Le nom et la description doivent être des chaînes de caractères.")
            raise TypeError("Le nom et la description doivent être des chaînes de caractères.")
                    
        if not name or not description:
            debug_logger.debug("Le nom et la description ne peuvent pas être vides.")
            raise ValueError("Le nom et la description ne peuvent pas être vides.")
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
        if self.completed:
            debug_logger.debug("La tâche est déjà marquée comme complétée.")
            raise TaskAlreadyCompletedError("La tâche est déjà marquée comme complétée.")
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
            if not isinstance(new_name, str):
                debug_logger.debug("Le nouveau nom doit être une chaîne de caractères.")
                raise TypeError("Le nouveau nom doit être une chaîne de caractères.")
                        
            general_logger.info("Modification du nom d'une tâche : " + self.name + " -> " + new_name)
            self.name = new_name
            self.last_modified = datetime.now()

        if new_description:
            if not isinstance(new_description, str):
                debug_logger.debug("La nouvelle description doit être une chaîne de caractères.")
                raise TypeError("La nouvelle description doit être une chaîne de caractères.")
                        
            general_logger.info("Modification de la description d'une tâche : " + self.name + " -> " + new_description)
            self.description = new_description
            self.last_modified = datetime.now()
        if not new_name and not new_description:
            debug_logger.debug("Aucun paramètre de modification n'a été fourni.")
            raise ValueError("Aucun paramètre de modification n'a été fourni.")

    def add_tag(self, tag:str):
        """
        Adds a tag to the task if it doesn't already exist and updates the last_modified date.
        
        :param tag: The tag to add.
        :type tag: str
        
        :returns: None
        """
        if not isinstance(tag, str):
            debug_logger.debug("Le tag doit être une chaîne de caractères.")
            raise TypeError("Le tag doit être une chaîne de caractères.")
        
        if tag in self.tags:
            debug_logger.debug(f"Le tag '{tag}' existe déjà pour cette tâche.")
            raise TagError(f"Le tag '{tag}' existe déjà pour cette tâche.")
            
        if tag not in self.tags:
            general_logger.info("Ajout d'un tag à une tâche : " + self.name + " -> " + tag)
            self.tags.append(tag)
            self.last_modified = datetime.now()

    def remove_tag(self, tag):
        """
        Removes a tag from the task if it exists and updates the last_modified date.
        
        :param tag: The tag to remove.
        :type tag: str
        
        :returns: None
        """
        if tag not in self.tags:
            debug_logger.debug(f"Le tag '{tag}' n'existe pas pour cette tâche.")
            raise TagError(f"Le tag '{tag}' n'existe pas pour cette tâche.")
        if tag in self.tags:
            general_logger.info("Suppression d'un tag à une tâche : " + self.name + " -> " + tag)
            self.tags.remove(tag)
            self.last_modified = datetime.now()

    def __str__(self):
        """
        Returns a string representation of the Task object.
        
        :returns: A string representing the task.
        :rtype: str
        """
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