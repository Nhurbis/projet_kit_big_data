from datetime import datetime
from todolist.config.db_config import db
from todolist.models.Task import Task
from todolist.utils.loggers import debug_logger, general_logger


class TaskAlreadyExistsError(Exception):
    pass


class TaskNotFoundError(Exception):
    pass


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
        self.collection = db.tasks

    def add_task(self, name: str, description: str, tags=None):
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
        if not isinstance(name, str):
            debug_logger.debug("add_task: name n'est pas un string: %s.", type(name))
            raise TypeError(
                "Le nom et la description doivent être des chaînes de caractères.")

        if not name:
            debug_logger.debug("add_task: name est vide: %s.", name)
            raise ValueError("Le nom ne peut pas être vide.")

        if self.collection.find_one({"name": name}):
            debug_logger.debug("add_task: La tâche existe déjà: %s.", name)
            general_logger.info(
                "Tentative d'ajout d'une tâche existante : %s", name)
            raise TaskAlreadyExistsError("La tâche '%s' existe déjà." % name)

        general_logger.info("Ajout d'une nouvelle tâche : %s", name)
        task = Task(name, description, tags)
        self.collection.insert_one(task.to_dict())

    def complete_task(self, name: str):
        """
        Marks a task as complete.

        :param name: The name of the task to complete.
        :type name: str

        :returns: A message indicating success or failure.
        :rtype: str
        """
        if not self.collection.find_one({"name": name}):
            debug_logger.debug("complete_task: task inexisante : ", name)
            general_logger.info(
                "Tentative de complétion d'une tâche inexistante : %s", name)
            raise TaskNotFoundError("La tâche '%s' n'existe pas." % name)

        general_logger.info("Complétion d'une tâche : %s", name)

        self.collection.update_one(
            {"name": name}, {"$set": {"completed": True, "completion_date": datetime.now()}})

    def remove_task(self, name: str):
        """
        Removes a task from the task list.

        :param name: The name of the task to remove.
        :type name: str

        :returns: A message indicating success or failure.
        :rtype: str
        """
        if not self.collection.find_one({"name": name}):
            debug_logger.debug("remove_task: task inexisante : ", name)
            general_logger.info(
                "Tentative de suppression d'une tâche inexistante : %s", name)
            raise TaskNotFoundError("La tâche '%s' n'existe pas." % name)

        general_logger.info("Suppression d'une tâche : %s", name)
        self.collection.delete_one({"name": name})

    def add_tag(self, name: str, tag: str):
        """
        Adds a tag to a task.

        :param name: The name of the task to add the tag to.
        :type name: str
        :param tag: The tag to add to the task.
        :type tag: str

        :returns: A message indicating success or failure.
        :rtype: str
        """
        if not self.collection.find_one({"name": name}):
            debug_logger.debug("add_tag: task inexisante : ", name)
            general_logger.info(
                "Tentative d'ajout d'un tag à une tâche inexistante : ", name)
            raise TaskNotFoundError("La tâche '%s' n'existe pas." % name)
        
        if tag in self.collection.find_one({"name": name})["tags"]:
            debug_logger.debug("add_tag: Le tag existe déjà : ", tag)
            general_logger.info(
                "Tentative d'ajout d'un tag existant à une tâche : %s", name)
            raise TaskAlreadyExistsError("Le tag '%s' existe déjà pour cette tâche." % tag)

        general_logger.info("Ajout d'un tag à une tâche : %s", name)
        self.collection.update_one({"name": name}, {"$push": {"tags": tag}})

    def remove_tag(self, name: str, tag: str):
        """
        Removes a tag from a task.
        Args:
            name (str): _description_
            tag (str): _description_
        """
        if not self.collection.find_one({"name": name}):
            debug_logger.debug("remove_tag: task inexisante : ", name)
            general_logger.info(
                "Tentative de retrait d'un tag à une tâche inexistante : %s", name)
            raise TaskNotFoundError("La tâche '%s' n'existe pas." % name)
        
        if tag not in self.collection.find_one({"name": name})["tags"]:
            debug_logger.debug("remove_tag: Le tag n'existe pas : ", tag)
            general_logger.info(
                "Tentative de retrait d'un tag non existant : %s", name)
            raise TaskAlreadyExistsError("Le tag '%s' n'existe déjà pour cette tâche." % tag)
        
        general_logger.info("Retrait d'un tag à une tâche : %s", name)
        self.collection.update_one({"name": name}, {"$pull": {"tags": tag}})

    def display_all_tasks(self):
        """
        Displays all tasks in the task list.

        :returns: None
        """
        tasks = self.collection.find()
        if not tasks:
            general_logger.info(
                "Tentative d'affichage d'une liste de tâches vide.")
            print("Aucune tâche à afficher.")
            return
        general_logger.info("Affichage d'une liste de tâches.")
        for task_data in tasks:
            task = Task.from_dict(task_data)
            print(task)

    def display_done_tasks(self):
        """
        Displays all completed tasks in the task list.

        :returns: None
        """
        tasks = self.collection.find({"completed": True})
        if not tasks:
            general_logger.info(
                "Tentative d'affichage d'une liste de tâches complétées vide.")
            print("Aucune tâche complétée à afficher.")
            return
        general_logger.info("Affichage d'une liste de tâches complétées.")
        for task_data in tasks:
            task = Task.from_dict(task_data)
            print(task)

    def display_todo_tasks(self):
        """
        Displays all incomplete tasks in the task list.

        :returns: None
        """
        tasks = self.collection.find({"completed": False})
        if not tasks:
            general_logger.info(
                "Tentative d'affichage d'une liste de tâches non terminées vide.")
            print("Aucune tâche incomplète à afficher.")
            return
        general_logger.info("Affichage d'une liste de tâches non terminées.")
        for task_data in tasks:
            task = Task.from_dict(task_data)
            print(task)