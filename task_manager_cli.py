import argparse
from controller.task_controller import TaskController


def main():
    parser = argparse.ArgumentParser(description='Gestionnaire de Tâches CLI')
    subparsers = parser.add_subparsers(dest='command')

    # Commande pour créer une nouvelle liste de tâches
    create_tasklist_parser = subparsers.add_parser(
        'create_tasklist', help='Créer une nouvelle liste de tâches')
    create_tasklist_parser.add_argument(
        'title', type=str, help='Titre de la liste de tâches')

    # Commande pour ajouter une tâche à une liste de tâches
    add_task_parser = subparsers.add_parser(
        'add_task', help='Ajouter une tâche à une liste de tâches')
    add_task_parser.add_argument(
        'tasklist_id', type=str, help="ID de la liste de tâches")
    add_task_parser.add_argument('name', type=str, help="Nom de la tâche")
    add_task_parser.add_argument(
        'description', type=str, help="Description de la tâche")

    # Commande pour marquer une tâche comme complétée
    complete_task_parser = subparsers.add_parser(
        'complete_task', help='Marquer une tâche comme complétée')
    complete_task_parser.add_argument(
        'tasklist_id', type=str, help="ID de la liste de tâches")
    complete_task_parser.add_argument(
        'task_id', type=str, help="ID de la tâche")

    # Commande pour supprimer une tâche
    delete_task_parser = subparsers.add_parser(
        'delete_task', help='Supprimer une tâche')
    delete_task_parser.add_argument(
        'tasklist_id', type=str, help="ID de la liste de tâches")
    delete_task_parser.add_argument('task_id', type=str, help="ID de la tâche")

    # Commande pour afficher les tâches incomplètes
    show_incomplete_tasks_parser = subparsers.add_parser(
        'show_incomplete_tasks', help='Afficher les tâches incomplètes')
    show_incomplete_tasks_parser.add_argument(
        'tasklist_id', type=str, help="ID de la liste de tâches")

    args = parser.parse_args()

    if args.command == 'create_tasklist':
        response = TaskController.create_tasklist(args.title)
        print(response)

    elif args.command == 'add_task':
        response = TaskController.add_task_to_tasklist(
            args.tasklist_id, args.name, args.description)
        print(response)

    elif args.command == 'complete_task':
        response = TaskController.complete_task(args.tasklist_id, args.task_id)
        print(response)

    elif args.command == 'delete_task':
        response = TaskController.delete_task(args.tasklist_id, args.task_id)
        print(response)

    elif args.command == 'show_incomplete_tasks':
        TaskController.show_incomplete_tasks(args.tasklist_id)

    else:
        parser.print_help()


if __name__ == "__main__":
    main()
