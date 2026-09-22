
# 🧪 Exercise 1 — User Input

# Write a program that asks:

# What is your name?
# What is your age?
# What is your city?

name = input("What is your name?")
age = int(input("what is you age?"))
city = input("What is your city?")

print(f"Hello {name}, you are {age} years old and you live in {city}.")

#🧪 Exercise 2 — Shopping List

# Create:
shopping = []
# Ask the user for 3 items and add them using append().
for i in range(3):
    item =input(f"Enter item {i + 1 };")
    shopping.append(item)
# Then print the complete list.
print("Your shopping list is:", shopping)


#🧪 Exercise 3 — List Operations

#Given:

numbers = [10, 20, 30, 40, 50]

#Do the following:

# Print the first item
print("First item:", numbers[0])
# Print the last item
print("Last item:", numbers[-1])
# Change 30 to 35
numbers[2] = 35
# Add 60
numbers.append(60)
# Remove 20
numbers.remove(20)
# Print the length
numbers_length = len(numbers)
print("Length of the list:", numbers_length)
# Print all numbers using a loop
for number in numbers:
    print(number)


# 🧪 Exercise 4 — Dictionary

# Create:

student = { 
    "name": "Zain", 
    "age": 20, 
    "course": "Data Science", 
    "is_active": True 
}

# Then:

# Print the name
print("Name:", student["name"])
# Print the age
print("Age:", student["age"])
# Add "city"
student["city"] = "lahore"
# Change the age
student["age"] = 21
# Loop through all key/value pairs
for key, value in student.items():
    print(f"{key}: {value}")


# 🧪 Exercise 5 — Agent Tools

# Create this list:

tools = [
    {
        "name": "calculator",
        "description": "Perform calculations"
    },
    {
        "name": "weather",
        "description": "Get weather information"
    },
    {
        "name": "search",
        "description": "Search the web"
    }
]

# Use a loop to print:
# Tool: calculator
# Description: Perform calculations
# Tool: weather
# Description: Get weather information
# Tool: search
# Description: Search the web
# This is your first tiny connection to agent architecture.

for tool in tools:
    print(f"Tool: {tool['name']}")
    print(f"Description: {tool['description']}")
