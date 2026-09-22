tasks = []

while True:
    print("\n===== TODO APP =====")
    print("1. Add task")
    print("2. View tasks")
    print("3. Delete task")
    print("4. Exit")

    choice = input("\nChoose an option (1-4): ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print(f"Task '{task}' added!")

    elif choice == "2":
        if len(tasks) == 0:
            print("\nNo tasks found.")
        else:
            print("\nTasks:")
            for i in range(len(tasks)):
                print(f"{i + 1}. {tasks[i]}")

    elif choice == "3":
        if len(tasks) == 0:
            print("\nNo tasks to delete.")
        else:
            task_num = int(input("Enter task number to delete: "))
            if 1 <= task_num <= len(tasks):
                removed = tasks.pop(task_num - 1)
                print(f"Deleted task: {removed}")
            else:
                print("Invalid task number.")

    elif choice == "4":
        print("Exiting app. Goodbye!")
        break

    else:
        print("Invalid choice. Please select 1, 2, 3, or 4.")