import subprocess
import os
import pytest
from pathlib import Path

CLI_SCRIPT = "src/cli/main.py"
PROJECT_ROOT = str(Path(__file__).parent.parent.parent)  # raíz del proyecto

@pytest.fixture(autouse=True)
def clean_tasks_file():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    yield
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

def run_cli(*args):
    env = os.environ.copy()
    env["PYTHONPATH"] = PROJECT_ROOT
    return subprocess.run(
        ["python", CLI_SCRIPT, *args],
        capture_output=True,
        text=True,
        env=env
    )


def test_add_and_list():
    res = run_cli("add", "Buy groceries")
    assert res.returncode == 0
    assert "Task added successfully" in res.stdout

    res_list = run_cli("list")
    assert res_list.returncode == 0
    assert "Buy groceries" in res_list.stdout
    assert "todo" in res_list.stdout

def test_update_and_delete():
    run_cli("add", "Task A")
    
    res_update = run_cli("update", "1", "Task B")
    assert res_update.returncode == 0
    
    res_list = run_cli("list")
    assert "Task B" in res_list.stdout
    assert "Task A" not in res_list.stdout

    res_del = run_cli("delete", "1")
    assert res_del.returncode == 0
    
    res_list2 = run_cli("list")
    assert "Task B" not in res_list2.stdout

def test_status_update():
    run_cli("add", "Task C")
    
    res_mip = run_cli("mark-in-progress", "1")
    assert res_mip.returncode == 0
    
    res_list = run_cli("list")
    assert "in-progress" in res_list.stdout

    res_done = run_cli("mark-done", "1")
    assert res_done.returncode == 0
    
    res_list_done = run_cli("list", "done")
    assert "Task C" in res_list_done.stdout

def test_not_found_errors():
    res = run_cli("update", "999", "No task")
    assert res.returncode == 1
    assert "Error: Task 999 not found." in res.stderr

    res_del = run_cli("delete", "999")
    assert res.returncode == 1
    assert "Error: Task 999 not found." in res.stderr
