from todolist.models.TaskList import TaskList


if __name__ == "__main__":
    task_list = TaskList()

    # # Ajouter une tâche
    # task_list.add_task("Faire les courses", "Acheter du lait et du pain")

    # # Afficher les tâches
    # task_list.display_tasks()

    # # Marquer une tâche comme terminée
    # task_list.complete_task("Faire les courses")

    # # Afficher les tâches après avoir marqué une tâche comme terminée
    # task_list.display_tasks()

    # # Supprimer une tâche
    # task_list.remove_task("Faire les courses")

    # Afficher les tâches après suppression
    print("Tâches incomplètes :")
    task_list.display_todo_tasks()
    print("Tâches complétées :")
    task_list.display_done_tasks()