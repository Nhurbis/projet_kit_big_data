
class TaskList:
    def __init__(self):
        self.tasks = {}

    def add_task(self, name, description):
        if name in self.tasks:
            print("Cette tâche existe déjà.")
            return
        self.tasks[name] = Task(name, description)

    def complete_task(self, name):
        if name not in self.tasks:
            print("Cette tâche n'existe pas.")
            return
        self.tasks[name].mark_completed()

    def remove_task(self, name):
        if name not in self.tasks:
            print("Cette tâche n'existe pas.")
            return
        del self.tasks[name]

    def display_tasks(self):
        if not self.tasks:
            print("Aucune tâche à afficher.")
            return
        for name, task in self.tasks.items():
            print(task)
