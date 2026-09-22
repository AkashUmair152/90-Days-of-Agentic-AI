# 🧪 Exercise 1 — Greeting Function
# Use string formatting or f-strings to construct the returned greeting string.


def greet(name):
    return f"Hello, {name}!"

# Test
print(greet("Akash"))
# Output: Hello, Akash!

# 🧪 Exercise 2 — Calculator Functions
# Each function takes two parameters and performs basic arithmetic using +, -, *, and /.

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

# Test
print(add(10, 5))        # 15
print(subtract(10, 5))   # 5
print(multiply(10, 5))   # 50
print(divide(10, 5))     # 2.0


# 🧪 Exercise 3 — Even Number
# Use the modulo operator %. An even number leaves a remainder of 0 when divided by 2.

def is_even(number):
    return number % 2 == 0

# Test
print(is_even(10))  # True
print(is_even(7))   # False


# 🧪 Exercise 4 — Find Maximum (Without max())
# Track the largest number seen so far in a variable highest, updating it whenever a larger number is encountered during the loop.

def find_max(numbers):
    if not numbers:
        return None
    
    highest = numbers[0]
    for num in numbers:
        if num > highest:
            highest = num
    return highest

# Test
numbers_list = [10, 50, 20, 90, 30]
print(find_max(numbers_list))  # 90


# 🧪 Exercise 5 — User Information
# Map the input parameters directly to dictionary key-value pairs.

def create_user(name, age, city):
    return {
        "name": name,
        "age": age,
        "city": city
    }

# Test
user = create_user("Akash", 29, "Lahore")
print(user)
# Output: {'name': 'Akash', 'age': 29, 'city': 'Lahore'}



# 🧪 Exercise 6 — Task Processor
# Iterate over the task list and print a formatted string for each item.


def process_tasks(tasks):
    for task in tasks:
        print(f"Processing: {task}")

# Test
task_list = ["Learn Python", "Learn FastAPI", "Learn AI"]
process_tasks(task_list)


# 🧪 Exercise 7 — Validation
# Use conditional statements (if, elif, else) to validate withdrawal rules sequentially.

def withdraw(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    elif amount > balance:
        return "Insufficient balance"
    else:
        return "Withdrawal successful"

# Test
print(withdraw(100, -50))  # Invalid amount
print(withdraw(100, 150))  # Insufficient balance
print(withdraw(100, 40))   # Withdrawal successful