from tools.calculator import add, subtract, multiply, divide
from tools.text import uppercase, lowercase, word_count
from tools.task import add_task, remove_task

tasks = []
 # calcultor tool 
def handle_calculator():
    print("\n--- Calculator Submenu ---")
    print("1. Add\n2. Subtract\n3. Multiply\n4. Divide")
    op = input("Choose operation (1-4): ")
    
    if op in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Must be numbers.")
            return

        if op == "1":
            print(f"Result: {add(num1, num2)}")
        elif op == "2":
            print(f"Result: {subtract(num1, num2)}")
        elif op == "3":
            print(f"Result: {multiply(num1, num2)}")
        elif op == "4":
            res = divide(num1, num2)
            if res is None:
                print("Error: Cannot divide by zero.")
            else:
                print(f"Result: {res}")
    else:
        print("Invalid selection.")

# text tool 
def handle_text_tools():
    print("\n--- Text Tools Submenu ---")
    print("1. Uppercase\n2. Lowercase\n3. Word Count")
    choice = input("Choose tool (1-3): ")
    
    if choice in ["1", "2", "3"]:
        text_input = input("Enter text: ")
        if choice == "1":
            print(f"Result: {uppercase(text_input)}")
        elif choice == "2":
            print(f"Result: {lowercase(text_input)}")
        elif choice == "3":
            print(f"Word Count: {word_count(text_input)}")
    else:
        print("Invalid selection.")
# task tool
def handle_task_tools():
    global tasks
    print("\n--- Task Tools Submenu ---")
    print("1. Add Task\n2. View Tasks\n3. Remove Task")
    choice = input("Choose action (1-3): ")

    if choice == "1":
        task_name = input("Enter new task: ")
        add_task(tasks, task_name)
        print(f"Added task: '{task_name}'")
    elif choice == "2":
        if not tasks:
            print("No tasks available.")
        else:
            print("\nCurrent Tasks:")
            for idx, item in enumerate(tasks):
                print(f"{idx}. {item}")
    elif choice == "3":
        if not tasks:
            print("No tasks to remove.")
            return
        
        for idx, item in enumerate(tasks):
            print(f"{idx}. {item}")
            
        try:
            idx_to_remove = int(input("Enter task index to remove: "))
            success = remove_task(tasks, idx_to_remove)
            if success:
                print("Task removed successfully.")
            else:
                print("Invalid task index.")
        except ValueError:
            print("Please enter a valid numeric index.")
    else:
        print("Invalid selection.")

def main():
    while True:
        print("\n===== TOOL LIBRARY =====")
        print("1. Calculator")
        print("2. Text tools")
        print("3. Task tools")
        print("4. Exit")

        choice = input("\nSelect menu (1-4): ")

        if choice == "1":
            handle_calculator()
        elif choice == "2":
            handle_text_tools()
        elif choice == "3":
            handle_task_tools()
        elif choice == "4":
            print("Exiting Mini Tool Library. Goodbye!")
            break
        else:
            print("Invalid selection. Choose between 1 and 4.")

if __name__ == "__main__":
    main()