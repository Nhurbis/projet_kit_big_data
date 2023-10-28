import pytest
from unittest.mock import patch, MagicMock
from controller.task_controller import TaskController
from model.tasklist import TaskList
from model.task import Task
import mongomock

# Initialisation de la base de données en mémoire


@pytest.fixture
def mongo():
    with mongomock.patch(servers=(('server.example', 27017),)):
        yield

# Test de la création d'une liste de tâches


def test_create_tasklist(mongo):
    title = "Ma liste de tâches"
    response = TaskController.create_tasklist(title)
    assert title in response
    assert "Tasklist 'Ma liste de tâches' added successfully!" in response

# Test de l'ajout d'une tâche à une liste de tâches


def test_add_task_to_tasklist(mongo):
    tasklist = TaskList(title="Ma liste")
    tasklist.save()

    response = TaskController.add_task_to_tasklist(
        str(tasklist._id), "Ma tâche", "Description")
    assert "Tâche ajoutée avec succès" in response

    # Vérifiez que la tâche a été ajoutée
    updated_tasklist = TaskList.get_tasklist_by_id(str(tasklist._id))
    assert len(updated_tasklist.tasks) == 1

# Test de la complétion d'une tâche


def test_complete_task(mongo):
    task = Task("Ma tâche", "Description")
    tasklist = TaskList(title="Ma liste", tasks=[task])
    tasklist.save()

    response = TaskController.complete_task(str(tasklist._id), str(task._id))
    assert "Tâche complétée avec succès" in response

    # Vérifiez que la tâche est marquée comme complète
    updated_tasklist = TaskList.get_tasklist_by_id(str(tasklist._id))
    assert updated_tasklist.tasks[0].completed

# Test de la suppression d'une tâche


def test_delete_task(mongo):
    task = Task("Ma tâche", "Description")
    tasklist = TaskList(title="Ma liste", tasks=[task])
    tasklist.save()

    response = TaskController.delete_task(str(tasklist._id), str(task._id))
    assert "Tâche supprimée avec succès" in response

    # Vérifiez que la tâche a été supprimée
    updated_tasklist = TaskList.get_tasklist_by_id(str(tasklist._id))
    assert len(updated_tasklist.tasks) == 0

# Test de l'affichage des tâches incomplètes


def test_show_incomplete_tasks(mongo, capsys):
    task = Task("Ma tâche", "Description")
    tasklist = TaskList(title="Ma liste", tasks=[task])
    tasklist.save()

    TaskController.show_incomplete_tasks(str(tasklist._id))
    captured = capsys.readouterr()
    assert "Ma tâche" in captured.out

# Test de la récupération des tâches incomplètes


def test_get_incomplete_tasks(mongo):
    task = Task("Ma tâche", "Description")
    tasklist = TaskList(title="Ma liste", tasks=[task])
    tasklist.save()

    response = TaskController.get_incomplete_tasks(str(tasklist._id))
    assert "Ma tâche" in response
