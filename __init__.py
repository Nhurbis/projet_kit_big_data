from todolist.models.TaskList import TaskList


if __name__ == "__main__":
    task_list = TaskList('liste_test_1')
    task_list2 = TaskList('liste_test_2')

    # Ajouter une tâche
    task_list.add_task("Manger des pâtes", "bolognaise ou carbonara")

    # Afficher les tâches
    print("------- Tâches incomplètes -------")
    task_list.display_todo_tasks()

    # Marquer une tâche comme terminée
    task_list.complete_task("Manger des pâtes")

    #changer la description d'une tâche
    task_list.update_task('Manger des pâtes', new_description='carbonara en fait')

    # Afficher les tâches terminées
    print("------- Tâches complétées -------")
    task_list.display_done_tasks()

    # Supprimer une tâche
    task_list.remove_task("Manger des pâtes")

    #Afficher toutes les tâches
    print("-------- Tâches ------- :")
    task_list.display_all_tasks()

    # Ajouter une tâche
    task_list2.add_task("Bonjour liste 2","juste un test")
    
    # On l'affiche
    print("-------- Tâches 2 ------- :")
    task_list2.display_all_tasks()