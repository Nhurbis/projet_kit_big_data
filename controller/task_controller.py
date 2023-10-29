from typing import Optional, List
from utils.loggers import debug_logger, errors_logger
from model.task import Task
from model.tasklist import TaskList
from config.db_config import db


class TaskController:
    """A class to control the Task and TaskList models."""

    @staticmethod
    def create_tasklist(title: str) -> str:
        """Create a new task list.

        Args:
            title (str): Title of the task list.

        Returns:
            str: A success message with the task list ID or a failure message.
        """
        try:
            tasklist = TaskList(title=title)
            tasklist.save()
            return f"Tasklist '{title}' added successfully! (Voici l'ID qui, en tant normal serait caché, {tasklist._id})"
        except Exception as e:
            errors_logger.error(
                f"An error occurred while creating a TaskList: {str(e)}")
            return "Failed to create TaskList!"

    @staticmethod
    def add_task_to_tasklist(tasklist_id: str, name: str, description: str) -> Optional[str]:
        """Add a task to a task list.

        Args:
            tasklist_id (str): ID of the task list.
            name (str): Name of the task.
            description (str): Description of the task.

        Returns:
            Optional[str]: A success message with the task ID or None if task list is not found.
        """
        try:
            task_list = TaskList.get_tasklist_by_id(tasklist_id)
            if task_list is not None:
                new_task = Task(name, description)
                task_list.tasks.append(new_task)
                db.tasklists.update_one({"_id": tasklist_id}, {
                                        "$push": {"tasks": new_task.to_dict()}})
                debug_logger.info(
                    "Tâche ajoutée avec succès à la liste de tâches.")
                return f"Tâche ajoutée avec succès à la liste de tâches. (Voici l'ID qui, en tant normal serait caché, {new_task._id})"
            else:
                errors_logger.error(
                    "Liste de tâches non trouvée avec l'ID: %s", tasklist_id)
                return None
        except Exception as e:
            errors_logger.exception(
                "Une erreur est survenue lors de l'ajout de la tâche à la liste de tâches.")
            raise RuntimeError(
                "Impossible d'ajouter la tâche à la liste de tâches.") from e

    @staticmethod
    def complete_task(tasklist_id: str, task_id: str) -> str:
        """Mark a task as completed.

        Args:
            tasklist_id (str): ID of the task list.
            task_id (str): ID of the task.

        Returns:
            str: A success message or an error message.
        """
        try:
            task_list = TaskList.get_tasklist_by_id(tasklist_id)
            if task_list is None:
                return "Liste de tâches non trouvée."
            task = next((t for t in task_list.tasks if t._id == task_id), None)
            if task:
                task.completed = True
                task_list.save()
                return "Tâche complétée avec succès."
            else:
                return "Tâche non trouvée."
        except Exception as e:
            errors_logger.error(
                f"Une erreur s'est produite lors de la complétion d'une tâche : {str(e)}")
            raise

    @staticmethod
    def delete_task(tasklist_id: str, task_id: str) -> str:
        """Delete a task from a TaskList.

        Args:
            tasklist_id (str): ID of the task list.
            task_id (str): ID of the task.

        Returns:
            str: A success message or an error message.
        """
        try:
            task_list = TaskList.get_tasklist_by_id(tasklist_id)
            if task_list is None:
                return "Liste de tâches non trouvée."
            task_list.tasks = [t for t in task_list.tasks if t._id != task_id]
            task_list.save()
            return "Tâche supprimée avec succès."
        except Exception as e:
            errors_logger.error(
                f"Une erreur s'est produite lors de la suppression d'une tâche : {str(e)}")
            raise

    @staticmethod
    def show_incomplete_tasks(tasklist_id: str) -> None:
        """Print all incomplete tasks in a TaskList.

        Args:
            tasklist_id (str): ID of the task list.
        """
        try:
            task_list = TaskList.get_tasklist_by_id(tasklist_id)
            if task_list is None:
                print("Liste de tâches non trouvée.")
                return
            for task in [t for t in task_list.tasks if not t.completed]:
                print(task)
        except Exception as e:
            errors_logger.error(
                f"Une erreur s'est produite lors de l'affichage des tâches incomplètes : {str(e)}")
            raise

    @staticmethod
    def get_incomplete_tasks(tasklist_id: str) -> str:
        """Get all incomplete tasks in a TaskList.

        Args:
            tasklist_id (str): ID of the task list.

        Returns:
            str: A list of incomplete tasks or an error message.
        """
        try:
            task_list = TaskList.get_tasklist_by_id(tasklist_id)
            if task_list:
                incomplete_tasks = [
                    task for task in task_list.tasks if not task.completed]
                return "\n".join([f"{task.name}: {task.description}" for task in incomplete_tasks])
            else:
                return "Tasklist not found!"
        except Exception as e:
            errors_logger.error(
                f"An error occurred while getting incomplete tasks: {str(e)}")
            return "Failed to get incomplete tasks!"
