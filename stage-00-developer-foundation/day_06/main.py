

# Exercise 1 — File Reader

def read_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return file.read()
    except FileNotFoundError:
        return f"Error: File '{filename}' not found."

# Test
print(read_file("hello.txt"))


# Exercise 2 — File Writer Python 

def write_file(filename, content):
    with open(filename, "w", encoding="utf-8") as file:
        file.write(content)
    print(f"Content successfully written to {filename}")

# Test
write_file("notes.txt", "Learning Python")

# Exercise 3 — JSON Save Python
import json

def save_json(filename, data):
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)
    print(f"Data saved to {filename}")

# Test
user = {
    "name": "Akash",
    "skills": ["Python", "FastAPI"]
}
save_json("user.json", user)

# Exercise 4 — JSON Load Python
import json

def load_json(filename):
    try:
        with open(filename, "r", encoding="utf-8") as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"File '{filename}' not found. Returning empty structure.")
        return []
    except json.JSONDecodeError:
        print(f"Error decoding JSON from '{filename}'. Returning empty structure.")
        return []

# Test
data = load_json("user.json")
print("Loaded Data:", data)

# Exercise 5 — Exception Practice Python

try:
    user_input = input("Enter a number: ")
    number = float(user_input)
    result = 100 / number
    print(f"100 / {number} = {result}")
except ValueError:
    print("Invalid input! Please enter a valid numerical value.")
except ZeroDivisionError:
    print("Cannot divide by zero!")

# Exercise 6 — User Validation Python

def validate_age(age):
    if age < 0 or age > 120:
        raise ValueError("Age must be between 0 and 120.")
    return True

# Test
try:
    validate_age(25)
    print("Age is valid!")
    validate_age(-5)  # Raises ValueError
except ValueError as e:
    print("Validation Error:", e)

