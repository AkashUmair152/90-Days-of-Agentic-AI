def add_task(tasks, task):
    tasks.append(task)
    return tasks

def remove_task(tasks, index):
    if index < 0 or index >= len(tasks):
        return False
    tasks.pop(index)
    return True