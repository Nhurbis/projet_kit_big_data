import pytest
from model.task import Task
from model.tasklist import TaskList


def test_tasklist_init():
    title = "Test TaskList"
    tasklist = TaskList(title)
    assert tasklist.title == title
    assert len(tasklist.tasks) == 0


def test_add_task_to_tasklist():
    tasklist = TaskList("Test")
    task = Task("Test Task", "Test Description")
    tasklist.tasks.append(task)
    assert len(tasklist.tasks) == 1
    assert tasklist.tasks[0].name == "Test Task"


def test_tasklist_to_dict():
    tasklist = TaskList("Test")
    tasklist_dict = tasklist.to_dict()
    assert "title" in tasklist_dict
    assert "tasks" in tasklist_dict
    assert tasklist_dict["title"] == "Test"
    assert isinstance(tasklist_dict["tasks"], list)


def test_tasklist_from_dict():
    task_data = {
        "name": "Test",
        "description": "Test Description",
        "completed": False,
        "created_at": "2023-10-27 12:34:56",
    }
    tasklist_data = {
        "title": "Test TaskList",
        "tasks": [task_data],
    }
    tasklist = TaskList.from_dict(tasklist_data)
    assert tasklist.title == "Test TaskList"
    assert len(tasklist.tasks) == 1
    assert tasklist.tasks[0].name == "Test"
