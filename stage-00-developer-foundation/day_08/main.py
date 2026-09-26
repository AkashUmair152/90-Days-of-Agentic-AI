# day-08/main.py


class Tool:

    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def run(self, *args, **kwargs):
        raise NotImplementedError


class CalculatorTool(Tool):

    def __init__(self):
        super().__init__("calculator", "Performs mathematical calculations")

    def run(self, a: int, b: int) -> int:
        return a + b


class TextTool(Tool):

    def __init__(self):
        super().__init__("text", "Converts text to uppercase")

    def run(self, text: str) -> str:
        return text.upper()


# Tool Registry
tools: list[Tool] = [CalculatorTool(), TextTool()]

# Extract tool names
tool_names = [tool.name for tool in tools]
print(tool_names)
# Output: ['calculator', 'text']


# Challenge: Tool Finder
def find_tool(tools: list[Tool], name: str) -> Tool | None:
    """Searches through the tools list and returns the matching Tool instance."""
    for tool in tools:
        if tool.name == name:
            return tool
    return None


# Test Tool Finder
tool = find_tool(tools, "calculator")

if tool:
    print(tool.run(20, 30))
# Expected Output: 50


# 🧪 Exercise 1 — Type Hints


def calculate_total(prices: list[float]) -> float:
    return sum(prices)


# Test
print(calculate_total([10.5, 20.0, 5.5]))
# Expected Output: 36.0

# 🧪 Exercise 2 — *args


def multiply_all(*numbers: int | float) -> int | float:
    result = 1
    for num in numbers:
        result *= num
    return result


# Test
print(multiply_all(2, 3, 4))
# Expected Output: 24


# 🧪 Exercise 3 — **kwargs

def create_profile(**kwargs) -> dict:
    return kwargs


# Test
profile = create_profile(name="Akash", age=29, city="Lahore")
print(profile)
# Expected Output: {'name': 'Akash', 'age': 29, 'city': 'Lahore'}


# 🧪 Exercise 4 — List Comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8]

squares = [num**2 for num in numbers]
print(squares)
# Expected Output: [1, 4, 9, 16, 25, 36, 49, 64]


# 🧪 Exercise 5 — Filter

numbers = [10, 15, 20, 25, 30, 35]

# Using list comprehension:
even_numbers = [num for num in numbers if num % 2 == 0]

print(even_numbers)
# Expected Output: [10, 20, 30]



# 🧪 Exercise 6 — enumerate()

tools = ["calculator", "weather", "search"]

for index, tool_name in enumerate(tools):
    print(f"{index} {tool_name}")

# Expected Output:
# 0 calculator
# 1 weather
# 2 search


# 🧪 Exercise 7 — zip() 

tools = ["calculator", "weather", "search"]
descriptions = ["Math", "Weather", "Internet search"]

for name, desc in zip(tools, descriptions):
    print(f"{name}: {desc}")

# Expected Output:
# calculator: Math
# weather: Weather
# search: Internet search


