from datetime import datetime
from todolist.config.db_config import db
from todolist.models.Task import Task
from todolist.utils.loggers import debug_logger, general_logger
from todolist.utils.exception_perso import TaskAlreadyExistsError, TaskNotFoundError


class TaskList:
    """
    A class to manage a list of Task objects.

    :ivar tasks: A dictionary to hold Task objects.
    """

    def __init__(self, titre: str):
        """
        Initializes an empty dictionary to hold Task objects.

        :returns: None
        """
        self.titre = titre
        self.collection = db.tasks

    def add_task(self, name: str, description: str):
        """
        Adds a new task to the task list.

        :param name: The name of the task.
        :type name: str
        :param description: The description of the task.
        :type description: str

        :returns: A message indicating success or failure.
        :rtype: str
        """
        try :
            if not isinstance(name, str):
                debug_logger.debug(
                    "add_task: name n'est pas un string: %s.", type(name))
                raise TypeError(
                    "Le nom doit être une chaîne de caractères.")

            elif not name:
                debug_logger.debug("add_task: name est vide: %s.", name)
                raise ValueError("Le nom ne peut pas être vide.")
            
            elif self.collection.find_one({"name": name}):
                debug_logger.debug("add_task: La tâche existe déjà: %s.", name)
                general_logger.info(
                    "Tentative d'ajout d'une tâche existante : %s", name)
                raise TaskAlreadyExistsError("La tâche '%s' existe déjà." % name)

            else:
                general_logger.info("Ajout d'une nouvelle tâche : %s", name)
                task = Task(name, description)
                self.collection.insert_one(task.to_dict())
        except TypeError as e:
            print(e)
        except ValueError as e:
            print(e)
        except TaskAlreadyExistsError as e:
            print(e)

    def complete_task(self, name: str):
        """
        Marks a task as complete.

        :param name: The name of the task to complete.
        :type name: str

        :returns: A message indicating success or failure.
        :rtype: str
        """
        Task.completed(self.collection, name)

    def remove_all(self):
        """
        Removes all tasks from the task list.

        :returns: A message indicating success or failure.
        :rtype: str
        """
        self.collection.delete_many({})

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

        else:
            general_logger.info("Suppression d'une tâche : %s", name)
            self.collection.delete_one({"name": name})

    def update_task(self, name: str, new_name: str = None, new_description: str = None):
        """
        Updates a task in the task list.
        """
        Task.update(self.collection, name, new_name, new_description)

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

        else:
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

        else:
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

        else:
            general_logger.info(
                "Affichage d'une liste de tâches non terminées.")
            for task_data in tasks:
                task = Task.from_dict(task_data)
                print(task)
