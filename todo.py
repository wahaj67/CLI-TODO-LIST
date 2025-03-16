import click  
import json   
import os     

TODO_FILE = "todo.json"


def load_task():
    if not os.path.exists(TODO_FILE):  
        return []
    with open(TODO_FILE, "r") as file:
        return json.load(file)


def save_task(tasks):
    with open(TODO_FILE, "w") as file:
        json.dump(tasks, file, indent=4)

@click.group()
def cli():
    """Simple Todo List Manager"""
    pass

@click.command()
@click.argument("task")
def add(task):
    """Add a new task to the list"""
    tasks = load_task()
    tasks.append({"task": task, "done": False})
    save_task(tasks)
    click.echo(f"Task Added: {task}")


@click.command()
def list():
    """List All Tasks"""
    tasks = load_task()
    if not tasks:
        click.echo('No tasks found')
        return
    for index, task in enumerate(tasks , 1):
        status = "✅" if task["done"] else "❌"
        click.echo(f"{index}. {task['task']} {status}")


@click.command()
@click.argument("task_number",type=int)
def complete(task_number):
    """Mark a task as complete"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks[task_number - 1]["done"] = True
        save_task(tasks)
        click.echo(f"Task {task_number} marked as complete")

@click.command()
@click.argument("task_number",type=int)
def clear(task_number):
    """Remove Task from a List"""
    tasks = load_task()
    if 0 < task_number <= len(tasks):
        tasks.pop(task_number - 1)
        save_task(tasks)
        click.echo(f"Task {task_number} removed from the list")
    else:
        click.echo("Invalid task number")

cli.add_command(add)
cli.add_command(list)
cli.add_command(complete)
cli.add_command(clear)


if __name__ == "__main__":
    cli()
