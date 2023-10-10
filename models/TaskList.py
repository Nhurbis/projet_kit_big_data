class TaskList:
    """
    A class to manage a list of Task objects.
    """
    def __init__(self):
        """
        Initializes an empty dictionary to hold Task objects.
        """
        self.tasks = {}

    def add_task(self, name, description, tags=None):
        """
        Adds a new task to the task list.

        Args:
            name: The name of the task.
            description: The description of the task.
            tags: A list of tags for the task. Defaults to None.

        Returns:
            A message indicating success or failure.
        """
        if name in self.tasks:
            return "Cette tâche existe déjà."
        self.tasks[name] = Task(name, description, tags)
        return "Tâche ajoutée avec succès."

    def complete_task(self, name):
        """
        Marks a task as complete.

        Args:
            name: The name of the task to complete.

        Returns:
            A message indicating success or failure.
        """
        if name not in self.tasks:
            return "Cette tâche n'existe pas."
        self.tasks[name].mark_completed()
        return "Tâche marquée comme complétée."

    def remove_task(self, name):
        """
        Removes a task from the task list.

        Args:
            name: The name of the task to remove.

        Returns:
            A message indicating success or failure.
        """
        if name not in self.tasks:
            return "Cette tâche n'existe pas."
        del self.tasks[name]
        return "Tâche supprimée avec succès."

    def display_tasks(self):
        """
        Displays all tasks in the task list.
        """
        if not self.tasks:
            print("Aucune tâche à afficher.")
            return
        for name, task in self.tasks.items():
            print(task)
