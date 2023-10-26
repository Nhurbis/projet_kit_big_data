import pymongo
from bson import ObjectId
import logging
from utils.loggers import debug_logger, errors_logger
from config.db_config import db
from utils.exception_perso import TaskNotFoundError

logging.basicConfig(level=logging.INFO)

class TaskModel:
    def __init__(self) -> None:
        try:
            self.collection = db["tasks"]
            self.completed: bool = False
            self.description: str = ""
            logging.info("Connected to MongoDB")
        except pymongo.errors.ConnectionError as e:
            logging.error(f"Could not connect to MongoDB: {str(e)}")
            raise
    
    def save_task(self, title: str, status: str, description: str) -> str:
        try:
            task_id: str = self.collection.insert_one({"title": title, "status": status, "description": description}).inserted_id
            logging.info(f"Task saved with ID: {task_id}")
            return task_id
        except Exception as e:
            logging.error(f"Error saving task: {str(e)}")
            return None
    
    def get_all_tasks(self) -> list:
        try:
            tasks: list = list(self.collection.find())
            logging.info("Fetched all tasks")
            return tasks
        except Exception as e:
            logging.error(f"Error fetching tasks: {str(e)}")
            return None
    
    def update_task(self, task_id: str, new_title: str, new_description: str) -> None:
        try:
            if not isinstance(task_id, str):
                debug_logger.debug("update: name n'est pas un string: %s.", type(task_id))
                raise TypeError(
                    "Le nom de la task à modifier doit être des chaînes de caractères.")

            elif not new_description and not new_title:
                debug_logger.debug("update: new_description et new_name sont vides: %s.", task_id)
                raise ValueError("Le nom et la description ne peuvent pas être vides.")

            elif not self.collection.find_one({"name": task_id}):
                errors_logger.debug("update: La tâche n'existe pas: %s.", task_id)
                debug_logger.info("Tentative de modification d'une tache inexistante : %s", task_id)
                raise TaskNotFoundError("La tache '%s' n'existe pas." % task_id)
        except TypeError as e:
            print(e)
            return
        except ValueError as e:
            print(e)
            return
        except TaskNotFoundError as e:
            print(e)
            return
        
        if new_description:
            if not isinstance(new_description, str):
                errors_logger.debug("update: new_description n'est pas un string: %s.", type(new_description))
                debug_logger.info("Tentative de modification de la description d'une tache avec une description non string : %s", new_description)
            else:
                errors_logger.info("Update de la tâche %s avec nouvelle description %s e", name, new_description)
                self.collection.update_one({"name": name}, {"$set": {"description": new_description}})
                
        if new_title:
            if not isinstance(new_name, str):
                errors_logger.debug("update: new_name n'est pas un string: %s.", type(new_name))
                debug_logger.info("Tentative de modification du nom d'une tache avec un nom non string : %s", new_name)
            else:
                debug_logger.info("Update de la tâche %s avec nouveau nom %s e", name, new_name)
                self.collection.update_one({"name": name}, {"$set": {"name": new_name}})
    
    def delete_task(self, task_id: str) -> None:
        try:
            self.collection.delete_one({"_id": ObjectId(task_id)})
            logging.info(f"Task {task_id} deleted")
        except Exception as e:
            logging.error(f"Error deleting task {task_id}: {str(e)}")
