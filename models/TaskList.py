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
        if name in self.tasks:
            return "Cette tâche existe déjà."
        self.tasks[name] = Task(name, description, tags)
        return "Tâche ajoutée avec succès."

    def complete_task(self, name):
        """
        Marks a task as complete.
        
        :param name: The name of the task to complete.
        :type name: str
        
        :returns: A message indicating success or failure.
        :rtype: str
        """
        if name not in self.tasks:
            return "Cette tâche n'existe pas."
        self.tasks[name].mark_completed()
        return "Tâche marquée comme complétée."

    def remove_task(self, name):
        """
        Removes a task from the task list.
        
        :param name: The name of the task to remove.
        :type name: str
        
        :returns: A message indicating success or failure.
        :rtype: str
        """
        if name not in self.tasks:
            return "Cette tâche n'existe pas."
        del self.tasks[name]
        return "Tâche supprimée avec succès."

    def display_tasks(self):
        """
        Displays all tasks in the task list.
        
        :returns: None
        """
        if not self.tasks:
            print("Aucune tâche à afficher.")
            return
        for name, task in self.tasks.items():
            print(task)
