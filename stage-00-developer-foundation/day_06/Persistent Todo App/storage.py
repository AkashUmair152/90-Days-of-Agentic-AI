import json
import os

TASKS_FILE = "tasks.json"

def load_tasks():
    """Loads tasks from tasks.json. Creates an empty file if it doesn't exist."""
    if not os.path.exists(TASKS_FILE):
        save_tasks([])
        return []
        
    try:
        with open(TASKS_FILE, "r", encoding="utf-8") as f:
            return json.load(f)
    except (json.JSONDecodeError, FileNotFoundError):
        return []

def save_tasks(tasks):
    """Saves the tasks list to tasks.json."""
    with open(TASKS_FILE, "w", encoding="utf-8") as f:
        json.dump(tasks, f, indent=4)