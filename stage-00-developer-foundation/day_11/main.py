from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app =FastAPI(
    title = "Agent toolkit",
    description = "A toolkit for building and managing AI agents",
)

class Task(BaseModel):
    id: int
    title: str
    completed: bool

tasks = [
    Task(id=1, title="Learn APIs", completed=False),
    Task(id=2, title="Build an AI tool", completed=False),
    Task(id=3, title="Deploy the tool", completed=False)
]

@app.get("/tasks")
def get_tasks():
    return tasks


# one task 

@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(
        status_code = 404,
        detail = f"Task with {task_id} not found"
    )

# create a new task

@app.post("/tasks")
def create_task(task : Task):
    new_task = Task(
        id=len(tasks) + 1,
        title=task.title,
        completed=task.completed
    )
    tasks.append(new_task)
    return tasks


# task update 

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task: Task):
    for task in tasks:
        if task.id == task_id:
            task.title = task.title
            task.completed = task.completed
            return task
    raise HTTPException(
        status_code = 404,
        detail = f"Task with {task_id} not found"
    )

# delete a task

@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)
            return {"message": f"Task with {task_id} deleted successfully"}
    raise HTTPException(
        status_code = 404,
        detail = f"Task with {task_id} not found")