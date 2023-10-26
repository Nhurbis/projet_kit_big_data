from model.task_model import TaskModel
from utils import debug_logger, error_logger


debug_logger.basicConfig(level=debug_logger.INFO)

class TaskController:
    def __init__(self):
        self.model = TaskModel()

    def add_task(self, title, status):
        task_id = self.model.save_task(title, status)
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
            return "\n".join([f"{task['title']} - {task['status']}" for task in tasks])
        else:
            debug_logger.error("Failed to fetch tasks")
            return "Failed to fetch tasks"
            
    def update_task(self, task_id, new_title, new_status, new_description):
        if not task_id or not new_title or not new_status or not new_description:
            debug_logger.error("Invalid input for updating task")
            return "Invalid input"

        new_data = {"title": new_title, "status": new_status}
        updated = self.model.update_task(task_id, new_data)
        if updated:
            debug_logger.info(f"Task {task_id} updated successfully")
            return "Task updated successfully"
        else:
            debug_logger.error(f"Failed to update task {task_id}")
            return "Failed to update task"

    def delete_task(self, task_id):
        if not task_id:
            debug_logger.error("Invalid task ID for deleting task")
            return "Invalid task ID"

        deleted = self.model.delete_task(task_id)
        if deleted:
            debug_logger.info(f"Task {task_id} deleted successfully")
            return "Task deleted successfully"
        else:
            debug_logger.error(f"Failed to delete task {task_id}")
            return "Failed to delete task"
