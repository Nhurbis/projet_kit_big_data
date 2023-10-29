import pytest
from datetime import datetime
from model.task import Task


def test_task_init():
    name = "Test Task"
    description = "This is a test task"
    task = Task(name, description)
    assert task.name == name
    assert task.description == description
    assert not task.completed
    assert task.created_at is not None


def test_task_to_dict():
    task = Task("Test", "Test Description")
    task_dict = task.to_dict()
    assert "name" in task_dict
    assert "description" in task_dict
    assert "completed" in task_dict
    assert "created_at" in task_dict
    assert "Test" == task_dict["name"]
    assert "Test Description" == task_dict["description"]


def test_task_from_dict():
    task_data = {
        "name": "Test",
        "description": "Test Description",
        "completed": False,
        "created_at": "2023-10-27 12:34:56",
    }
    task = Task.from_dict(task_data)
    assert task.name == "Test"
    assert task.description == "Test Description"
    assert not task.completed
    assert task.created_at == datetime(2023, 10, 27, 12, 34, 56)
