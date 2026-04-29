import argparse
import sys
from src.core.task_manager import TaskManager

def print_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    
    print(f"{'ID':<5} | {'Status':<12} | {'Created At':<22} | {'Description'}")
    print("-" * 80)
    for t in tasks:
        print(f"{t.id:<5} | {t.status:<12} | {t.createdAt:<22} | {t.description}")

def main():
    parser = argparse.ArgumentParser(description="Task CLI - Manage your tasks locally.")
    subparsers = parser.add_subparsers(dest="command", required=True)

    # add
    parser_add = subparsers.add_parser("add", help="Add a new task")
    parser_add.add_argument("description", type=str, help="Description of the task")

    # update
    parser_update = subparsers.add_parser("update", help="Update task description")
    parser_update.add_argument("id", type=int, help="Task ID")
    parser_update.add_argument("description", type=str, help="New description")

    # delete
    parser_delete = subparsers.add_parser("delete", help="Delete a task")
    parser_delete.add_argument("id", type=int, help="Task ID")

    # mark-in-progress
    parser_mip = subparsers.add_parser("mark-in-progress", help="Mark a task as in-progress")
    parser_mip.add_argument("id", type=int, help="Task ID")

    # mark-done
    parser_md = subparsers.add_parser("mark-done", help="Mark a task as done")
    parser_md.add_argument("id", type=int, help="Task ID")

    # list
    parser_list = subparsers.add_parser("list", help="List all tasks or filter by status")
    parser_list.add_argument("status", type=str, nargs="?", choices=["todo", "in-progress", "done"], help="Filter by status")

    args = parser.parse_args()
    tm = TaskManager()

    if args.command == "add":
        task = tm.add_task(args.description)
        print(f"Task added successfully (ID: {task.id})")
    
    elif args.command == "update":
        task = tm.update_task_description(args.id, args.description)
        if task:
            print(f"Task {args.id} updated successfully.")
        else:
            print(f"Error: Task {args.id} not found.", file=sys.stderr)
            sys.exit(1)

    elif args.command == "delete":
        success = tm.delete_task(args.id)
        if success:
            print(f"Task {args.id} deleted successfully.")
        else:
            print(f"Error: Task {args.id} not found.", file=sys.stderr)
            sys.exit(1)

    elif args.command == "mark-in-progress":
        task = tm.update_task_status(args.id, "in-progress")
        if task:
            print(f"Task {args.id} marked as in-progress.")
        else:
            print(f"Error: Task {args.id} not found.", file=sys.stderr)
            sys.exit(1)

    elif args.command == "mark-done":
        task = tm.update_task_status(args.id, "done")
        if task:
            print(f"Task {args.id} marked as done.")
        else:
            print(f"Error: Task {args.id} not found.", file=sys.stderr)
            sys.exit(1)

    elif args.command == "list":
        tasks = tm.list_tasks(args.status)
        print_tasks(tasks)

if __name__ == "__main__":
    main()
