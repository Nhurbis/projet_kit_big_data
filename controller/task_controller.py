from model.task_model import TaskModel
from utils.loggers import debug_logger, errors_logger


class TaskController:
    def __init__(self):
        self.model = TaskModel()

    def add_task(self, title, completed=False,description=""):
        if not title:
            debug_logger.info("Invalid input (no title) for adding task")
            return "Title is necessary to save task"
        completed = True if completed == "True" else False
        task_id = self.model.save_task(title, completed,description)
        if task_id:
            debug_logger.info(f"Task added with ID: {task_id}")
            return f"Task saved with ID: {task_id}"
        else:
            debug_logger.error("Failed to add task")
            return "Failed to save task"

    def show_all_tasks(self):
        tasks = self.model.get_all_tasks()
        if tasks is not None:
            debug_logger.info("Tasks fetched successfully")
            return "\n".join([f'{task["title"]} --- completed {task["completed"]} \n \t-> {task["description"]}' for task in tasks])
        else:
            debug_logger.error("Failed to fetch tasks")
            return "Failed to fetch tasks"
            
    def update_task(self, old_title, new_title, new_completed, new_description):
        new_completed = True if new_completed == "True" else False
        if not old_title :
            debug_logger.info("Invalid input (no old title) for updating task")
            return "Old title is necessary to update task"
        if not new_title and not new_description and not new_completed:
            debug_logger.info("Invalid input (no new title or no new description or no new completed) for updating task")
            return "New title or new description or new completed is necessary to update task"
        
        updated = self.model.update_task(old_title, new_title, new_description, new_completed)
        if updated:
            debug_logger.info(f"Task {old_title} updated successfully")
            return "Task updated successfully"
        else:
            debug_logger.error(f"Failed to update task {old_title}")
            errors_logger.error(f"Failed to update task {old_title}")
            return "Failed to update task"

    def delete_task(self,task_title):
        if not task_title:
            debug_logger.error("Invalid task title for deleting task")
            return "Invalid task title"

        deleted = self.model.delete_task(task_title)
        if deleted:
            debug_logger.info(f"Task {task_title} deleted successfully")
            return "Task deleted successfully"
        else:
            debug_logger.error(f"Failed to delete task {task_title}")
            errors_logger.error(f"Failed to delete task {task_title}")
            return "Failed to delete task"
