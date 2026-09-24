from storage import load_tasks, save_tasks

def add_task(tasks):
    title = input("Enter task description: ").strip()
    if not title:
        print("Task cannot be empty!")
        return
    
    new_task = {
        "title": title,
        "completed": False
    }
    tasks.append(new_task)
    save_tasks(tasks)
    print(f"Task '{title}' added!")

def show_tasks(tasks):
    if not tasks:
        print("\nNo tasks found.")
        return

    print("\n===== YOUR TASKS =====")
    for index, task in enumerate(tasks, start=1):
        status = "[✓]" if task["completed"] else "[ ]"
        print(f"{index}. {status} {task['title']}")

def complete_task(tasks):
    if not tasks:
        print("\nNo tasks available to complete.")
        return

    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to mark complete: "))
        if 1 <= task_num <= len(tasks):
            tasks[task_num - 1]["completed"] = True
            save_tasks(tasks)
            print(f"Task {task_num} marked as complete!")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number!")

def delete_task(tasks):
    if not tasks:
        print("\nNo tasks available to delete.")
        return

    show_tasks(tasks)
    try:
        task_num = int(input("\nEnter task number to delete: "))
        if 1 <= task_num <= len(tasks):
            removed = tasks.pop(task_num - 1)
            save_tasks(tasks)
            print(f"Deleted task: '{removed['title']}'")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number!")

def main():
    tasks = load_tasks()

    while True:
        print("\n===== PERSISTENT TODO APP =====")
        print("1. Add task")
        print("2. Show tasks")
        print("3. Complete task")
        print("4. Delete task")
        print("5. Exit")

        choice = input("\nChoose an option (1-5): ").strip()

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            show_tasks(tasks)
        elif choice == "3":
            complete_task(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice! Please select 1, 2, 3, 4, or 5.")

if __name__ == "__main__":
    main()