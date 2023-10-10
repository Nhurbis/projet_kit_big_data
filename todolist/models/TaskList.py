
class TaskAlreadyExistsError(Exception):
    pass

class TaskNotFoundError(Exception):
    pass

class TaskList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name:str, description:str, tags=None):
        if not isinstance(name, str):
            debug_logger.debug("Le nom doit être des chaînes de caractères.")
            raise TypeError("Le nom et la description doivent être des chaînes de caractères.")
        
        if not name:
            debug_logger.debug("Le nom ne peut pas être vide.")
            raise ValueError("Le nom ne peut pas être vide.")
        
        if name in self.tasks:
            debug_logger.debug("La tâche existe déjà.")
            general_logger.info("Tentative d'ajout d'une tâche existante : " + name)
            raise TaskAlreadyExistsError(f"La tâche '{name}' existe déjà.")

        general_logger.info("Ajout d'une nouvelle tâche : " + name)
        self.tasks[name] = Task(name, description, tags)

    def complete_task(self, name:str):
        if name not in self.tasks:
            debug_logger.debug("La tâche n'existe pas.")
            general_logger.info("Tentative de complétion d'une tâche inexistante : " + name)
            raise TaskNotFoundError(f"La tâche '{name}' n'existe pas.")
        
        general_logger.info("Complétion d'une tâche : " + name)
        self.tasks[name].mark_completed()

    def remove_task(self, name:str):
        if name not in self.tasks:
            debug_logger.debug("La tâche n'existe pas.")
            general_logger.info("Tentative de suppression d'une tâche inexistante : " + name)
            raise TaskNotFoundError(f"La tâche '{name}' n'existe pas.")
        
        general_logger.info("Suppression d'une tâche : " + name)
        del self.tasks[name]

    def display_tasks(self):
        if not self.tasks:
            general_logger.info("Tentative d'affichage d'une liste de tâches vide.")
            print("Aucune tâche à afficher.")
            return
        general_logger.info("Affichage d'une liste de tâches.")
        for name, task in self.tasks.items():
            print(task)
