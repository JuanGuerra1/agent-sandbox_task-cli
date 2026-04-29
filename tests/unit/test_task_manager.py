import os
import json
import pytest
from src.core.task_manager import TaskManager
from src.models.task import Task

@pytest.fixture
def temp_json_file(tmp_path):
    return str(tmp_path / "test_tasks.json")

def test_load_empty_file(temp_json_file):
    tm = TaskManager(temp_json_file)
    data = tm._load()
    assert data == {"metadata": {"next_id": 1}, "tasks": []}

def test_save_and_load_tasks(temp_json_file):
    tm = TaskManager(temp_json_file)
    data = {"metadata": {"next_id": 3}, "tasks": [
        Task.create(1, "Test 1").to_dict(),
        Task.create(2, "Test 2").to_dict(),
    ]}
    tm._save(data)

    assert os.path.exists(temp_json_file)

    loaded = tm._load()
    assert len(loaded["tasks"]) == 2
    assert loaded["tasks"][0]["id"] == 1
    assert loaded["tasks"][1]["description"] == "Test 2"
    assert loaded["metadata"]["next_id"] == 3

def test_load_corrupt_file(temp_json_file):
    with open(temp_json_file, "w") as f:
        f.write("{ invalid json")

    tm = TaskManager(temp_json_file)
    with pytest.raises(SystemExit) as exc_info:
        tm._load()
    assert exc_info.value.code == 1

def test_add_task(temp_json_file):
    tm = TaskManager(temp_json_file)
    task = tm.add_task("New task")
    assert task.id == 1
    assert task.description == "New task"
    assert task.status == "todo"

    tasks = tm.list_tasks()
    assert len(tasks) == 1
    assert tasks[0].id == 1

def test_list_tasks_filtered(temp_json_file):
    tm = TaskManager(temp_json_file)
    tm.add_task("Task 1")
    t2 = tm.add_task("Task 2")
    tm.update_task_status(t2.id, "done")

    assert len(tm.list_tasks()) == 2
    assert len(tm.list_tasks("todo")) == 1
    assert len(tm.list_tasks("done")) == 1

def test_update_task(temp_json_file):
    tm = TaskManager(temp_json_file)
    t1 = tm.add_task("Task 1")
    
    tm.update_task_description(t1.id, "Updated 1")
    tasks = tm.list_tasks()
    assert tasks[0].description == "Updated 1"

    tm.update_task_status(t1.id, "in-progress")
    tasks = tm.list_tasks()
    assert tasks[0].status == "in-progress"

def test_delete_task(temp_json_file):
    tm = TaskManager(temp_json_file)
    t1 = tm.add_task("Task 1")
    assert len(tm.list_tasks()) == 1

    res = tm.delete_task(t1.id)
    assert res is True
    assert len(tm.list_tasks()) == 0

    res2 = tm.delete_task(999)
    assert res2 is False
