import pymongo
from bson import ObjectId
from utils.loggers import debug_logger, errors_logger
from config.db_config import db
from utils.exception_perso import TaskNotFoundError


class TaskModel:
    def __init__(self) -> None:
        try:
            self.collection = db["tasks"]
            self.completed: bool = False
            self.description: str = ""
            debug_logger.info("Connected to MongoDB")
        except pymongo.errors.ConnectionError as e:
            debug_logger.error(f"Could not connect to MongoDB: {str(e)}")
            raise
    
    def save_task(self, title: str, completed: str, description: str) -> str:
        try:
            task_id: str = self.collection.insert_one({"title": title, "completed": completed, "description": description}).inserted_id
            debug_logger.info(f"Task saved with ID: {task_id}")
            return task_id
        except Exception as e:
            debug_logger.error(f"Error saving task: {str(e)}")
            return None
    
    def get_all_tasks(self) -> list:
        try:
            tasks: list = list(self.collection.find())
            debug_logger.info("Fetched all tasks")
            return tasks
        except Exception as e:
            debug_logger.error(f"Error fetching tasks: {str(e)}")
            return None
    
    def update_task(self, old_title: str, new_title: str, new_description: str, new_completed: bool) -> None:
        updated=False
        try:
            if not isinstance(old_title, str):
                debug_logger.debug("update: task_title n'est pas un string: %s.", type(old_title))
                errors_logger.error("update: task_title n'est pas un string: %s.", type(old_title))
                raise TypeError("Le nom de la task à modifier doit être des chaînes de caractères.")
            elif not self.collection.find_one({"title": old_title}):
                print("update: task inexisante : ", old_title)
                debug_logger.debug("Tentative de modification d'une tache inexistante : %s", old_title)
                raise TaskNotFoundError("La tache '%s' n'existe pas." ,old_title)
            
        except TypeError as e:
            print(e)
            return False
        except ValueError as e:
            print(e)
            return False
        except TaskNotFoundError as e:
            print(e)
            return False
        
        if new_description:
            if not isinstance(new_description, str):
                errors_logger.error("update: new_description n'est pas un string: %s.", type(new_description))
                debug_logger.info("Tentative de modification de la description d'une tache avec une description non string : %s", new_description)
            else:
                debug_logger.info("Update de la tâche %s avec nouvelle description %s e", old_title, new_description)
                self.collection.update_one({"title": old_title}, {"$set": {"description": new_description}})
                updated=True

        if new_completed:
            if not isinstance(new_completed, bool):
                errors_logger.error("update: new_completed n'est pas un bool: %s.", type(new_completed))
                debug_logger.info("Tentative de modification du completed d'une tache avec un completed non bool : %s", new_completed)
            else:
                debug_logger.info("Update de la tâche %s avec nouveau completed %s e", old_title, new_completed)
                self.collection.update_one({"title": old_title}, {"$set": {"completed": new_completed}})
                updated=True

        if new_title:
            if not isinstance(new_title, str):
                errors_logger.error("update: new_title n'est pas un string: %s.", type(new_title))
                debug_logger.info("Tentative de modification du nom d'une tache avec un nom non string : %s", new_title)
            else:
                debug_logger.info("Update de la tâche %s avec nouveau nom %s e", old_title, new_title)
                self.collection.update_one({"title": old_title}, {"$set": {"title": new_title}})
                updated=True        

        return updated

    def delete_task(self, task_title: str) -> None:
        try:
            if not self.collection.find_one({"title": task_title}):
                debug_logger.debug("remove_task: task inexisante : ", task_title)
                debug_logger.info(
                    "Tentative de suppression d'une tâche inexistante : %s", task_title)
                raise TaskNotFoundError("La tâche '%s' n'existe pas." % task_title)

            else:
                debug_logger.info("Suppression d'une tâche : %s", task_title)
                self.collection.delete_one({"title": task_title})
                return True
        except TaskNotFoundError as e:
            debug_logger.debug(f"Task %s non trouvé: {str(e)}", task_title)
            print(e)
            return False
        except Exception as e:
            errors_logger.error(f"Error deleting task: {str(e)}")
            return False