# Function Definitions
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b

# Main Program Loop
while True:
    print("\n===== CALCULATOR =====")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("\nChoose an option (1-5): ")

    if choice == "5":
        print("Goodbye!")
        break

    if choice in ["1", "2", "3", "4"]:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue

        if choice == "1":
            result = add(num1, num2)
            print(f"Result: {num1} + {num2} = {result}")

        elif choice == "2":
            result = subtract(num1, num2)
            print(f"Result: {num1} - {num2} = {result}")

        elif choice == "3":
            result = multiply(num1, num2)
            print(f"Result: {num1} * {num2} = {result}")

        elif choice == "4":
            result = divide(num1, num2)
            print(f"Result: {num1} / {num2} = {result}")

    else:
        print("Invalid option! Please enter a number between 1 and 5.")