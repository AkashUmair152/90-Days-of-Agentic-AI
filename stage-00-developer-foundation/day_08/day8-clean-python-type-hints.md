# Day 8 — Stage 0: Clean Python, Type Hints, *args, **kwargs, Comprehensions, Lambda, enumerate(), and zip()

## 1. Day 8 Overview

Today's features — type hints, `*args`/`**kwargs`, comprehensions, `lambda`, `enumerate()`, and `zip()` — aren't random trivia. They appear constantly in FastAPI, API/SDK code, LLM libraries, agent frameworks, tool definitions, and Pydantic models. The goal by the end of today is to be able to look at code like:
```python
def process_tools(
    tools: list[str],
    config: dict[str, str] | None = None
) -> list[str]:
    ...
```
and actually understand what it means — because real-world AI code frequently looks exactly like this. Writing cleaner, more explicit Python now means you'll read and write professional-grade code comfortably once you reach FastAPI and agent frameworks.

## 2. Type Hints

Without type hints, a function like `def add(a, b): return a + b` gives no clue what `a` and `b` should be — a number, a string, a list? Python won't stop you from misusing it. **Type hints** let you communicate the expected types:
```python
def add(a: int, b: int) -> int:
    return a + b
```

**Common type hints:**
```python
age: int = 29
name: str = "Akash"
price: float = 99.99
is_active: bool = True
```
- **Lists:** `numbers: list[int] = [1, 2, 3]`, `names: list[str] = ["Ali", "Ahmed", "Akash"]`
- **Dictionaries:** `user: dict[str, str] = {"name": "Akash", "city": "Lahore"}` — meaning keys and values are both expected to be strings; another example: `scores: dict[str, int] = {"Python": 90, "FastAPI": 85}`.
- **`None`** as a return type: `def print_message(message: str) -> None:` means "this function doesn't return a meaningful value."
- **`str | None`:** Means the value can be *either* a string *or* `None`.
```python
name: str | None = None

def find_user(user_id: int) -> str | None:
    ...
```

**Important — type hints don't normally enforce types:** Writing `def add(a: int, b: int) -> int:` does **not** stop you from calling `add("Hello", "World")` — Python will happily run it and return `"HelloWorld"`. Type hints exist primarily for humans, editors, static type checkers (like `mypy` or `pyright`, which you don't need to worry about yet), documentation, and a better development experience — not automatic runtime enforcement.

**Why this matters for Agentic AI:** A function like `def search_web(query: str) -> list[str]:` immediately communicates its input (a string) and output (a list of strings) — this becomes especially valuable when working with tools, APIs, Pydantic models, FastAPI, and LLM structured outputs.

## 3. Function Type Hints

The general shape:
```python
def function(
    parameter: type
) -> return_type:
    ...
```

**Examples:**
```python
def greet(name: str) -> str:
    return f"Hello {name}"
```
Read it as: `greet()` takes a string and returns a string.

```python
def calculate_average(numbers: list[float]) -> float:
    if not numbers:
        raise ValueError("Numbers cannot be empty.")
    return sum(numbers) / len(numbers)
```
This immediately tells you: input is a list of floats, output is a float, and an empty list raises a `ValueError`.

## 4. *args

Suppose `def add(a, b): return a + b` only conveniently handles two arguments — but you want `add(1, 2, 3, 4, 5)`. `*args` collects any number of extra **positional** arguments.
```python
def add(*args):
    print(args)

add(1, 2, 3)   # (1, 2, 3)
```
**`args` becomes a tuple.** The name `args` isn't magical — `def add(*numbers):` works identically and may even be clearer:
```python
def add(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add(1, 2))          # 3
print(add(1, 2, 3))       # 6
print(add(1, 2, 3, 4, 5)) # 15
```

**Remember:**
```
*args
 ↓
Extra positional arguments
 ↓
Tuple
```

## 5. **kwargs

`**kwargs` collects extra **keyword** (named) arguments.
```python
def show_user(**kwargs):
    print(kwargs)

show_user(name="Akash", age=29, city="Lahore")
```
Output:
```python
{"name": "Akash", "age": 29, "city": "Lahore"}
```
**`kwargs` becomes a dictionary.**

## 6. *args vs **kwargs

| | `*args` | `**kwargs` |
|---|---|---|
| **Collects** | Extra positional arguments | Extra keyword (named) arguments |
| **Becomes** | A tuple | A dictionary |
| **Example call** | `add(1, 2, 3)` | `show_user(name="Akash", age=29)` |

**Combined example:**
```python
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(10, 20, name="Akash", age=29)
```
Output:
```python
(10, 20)
{"name": "Akash", "age": 29}
```

**Why this matters for AI:** These patterns appear constantly in libraries, frameworks, decorators, wrappers, and SDKs — for example, `def run_agent(*args, **kwargs): ...`. When you see this, just think: `*args` = extra positional values, `**kwargs` = extra named values.

## 7. List Comprehensions ⭐⭐⭐

Given `numbers = [1, 2, 3, 4, 5]`, wanting `[2, 4, 6, 8, 10]`:

**Normal loop:**
```python
result = []
for number in numbers:
    result.append(number * 2)
```

**List comprehension (shorter):**
```python
result = [number * 2 for number in numbers]
```

**How to read it:** `[expression for item in collection]` reads as "Give me `number * 2` for every `number` in `numbers`."

**With a condition:**
```python
numbers = [1, 2, 3, 4, 5, 6]

even_numbers = [
    number
    for number in numbers
    if number % 2 == 0
]
# [2, 4, 6]
```

**When not to use comprehensions:** Something like `result = [x * 2 if x % 2 == 0 else x + 1 for x in numbers]` is technically valid, but if a comprehension becomes hard to read, prefer a normal loop instead. Good Python is readable Python.

## 8. Dictionary Comprehensions

```python
numbers = [1, 2, 3, 4]

squares = {
    number: number ** 2
    for number in numbers
}
# {1: 1, 2: 4, 3: 9, 4: 16}
```

**Why comprehensions matter for AI:**
```python
titles = [doc["title"] for doc in documents]
tool_names = [tool.name for tool in tools]
active_tools = [tool for tool in tools if tool.enabled]
```
Patterns like these show up constantly when processing documents, tools, and search results.

## 9. Lambda Functions

A **lambda** is a small, anonymous (unnamed) function.
```python
def square(x):
    return x * x

square = lambda x: x * x   # equivalent

print(square(5))   # 25
```
**Mental model:** `lambda x: x * x` roughly means `def something(x): return x * x`. Lambdas are useful for small, temporary functions — but simple, named, readable functions are often clearer, especially as logic grows more complex. Don't turn every function into a lambda just because you can.

## 10. map() and filter()

**`map()`** applies a function to every item in a collection:
```python
numbers = [1, 2, 3, 4]
result = map(lambda x: x * x, numbers)
result = list(result)   # [1, 4, 9, 16]
```
**`filter()`** keeps only items that pass a condition:
```python
numbers = [1, 2, 3, 4, 5, 6]
result = filter(lambda x: x % 2 == 0, numbers)
result = list(result)   # [2, 4, 6]
```
**Compared with list comprehensions:** A comprehension is usually easier to read for the same task:
```python
result = [x * x for x in numbers]           # instead of map()
result = [x for x in numbers if x % 2 == 0] # instead of filter()
```
For now, prefer the more readable comprehension version.

## 11. enumerate()

Given `tools = ["calculator", "weather", "search"]`, and wanting both index and value:

**Less clean:**
```python
for i in range(len(tools)):
    print(i, tools[i])
```

**Better, with `enumerate()`:**
```python
for index, tool in enumerate(tools):
    print(index, tool)
```
Output:
```
0 calculator
1 weather
2 search
```

**Why it matters:** You'll use `enumerate()` constantly when processing messages, documents, tools, tasks, and search results:
```python
for index, message in enumerate(messages):
    print(f"{index}: {message}")
```

## 12. zip()

Given two related lists:
```python
names = ["Akash", "Ali", "Ahmed"]
ages = [29, 25, 30]

for name, age in zip(names, ages):
    print(name, age)
```
Output:
```
Akash 29
Ali 25
Ahmed 30
```

**Why it matters for AI:** When you have two related collections — e.g., `documents` and `embeddings` — that need to be processed *together*:
```python
for document, embedding in zip(documents, embeddings):
    ...
```
This pattern appears often in data processing tasks.

## 13. Writing Clean Functions

- **Descriptive names:** `process(x)` says nothing about what it does; `calculate_final_price(price)` does.
```python
# Not ideal
def process(x):
    a = x * 2
    b = a + 10
    c = b / 2
    return c

# Better
def calculate_final_price(price: float) -> float:
    doubled_price = price * 2
    price_with_fee = doubled_price + 10
    final_price = price_with_fee / 2
    return final_price
```
- **Type hints:** Communicate expected inputs/outputs, as in Sections 2–3.
- **Simple logic:** Break complex operations into clear, small steps rather than one dense line.
- **Readable variables:** `doubled_price` beats `a`.
- **Small functions:** Each function does one clear thing.
- **Useful exceptions:** Raise clear errors for invalid input (e.g., `raise ValueError("Numbers cannot be empty.")`), as covered in `calculate_average()`.

Good code should communicate intent — a reader shouldn't have to guess what a function is for.

## 14. Combining Concepts

Bringing type hints, classes, methods, and comprehensions together:
```python
class Tool:
    def __init__(self, name: str):
        self.name = name

tools = [
    Tool("calculator"),
    Tool("weather"),
    Tool("search")
]

tool_names: list[str] = [
    tool.name
    for tool in tools
]
# ["calculator", "weather", "search"]
```
This is exactly the kind of Python you'll use while building an agent's tool registry — type hints clarify what's expected, and comprehensions cleanly extract the data you need.

## 15. Agentic AI Connection

```
Tool
  ↓
Tool Registry
  ↓
Agent
  ↓
LLM
```

These concepts show up throughout real AI systems:
- **Tool systems / tool registries:** Type-hinted `Tool` classes, and comprehensions to extract names, filter enabled tools, etc.
- **Agent frameworks:** `*args`/`**kwargs` appear frequently in flexible, configurable functions (e.g., `def run_agent(*args, **kwargs):`).
- **APIs / FastAPI:** Type hints on function parameters and return values describe request/response shapes clearly.
- **Structured data:** Comprehensions are a natural fit for transforming lists of documents, messages, or search results.
- **LLM applications:** Clean, well-typed functions make tool definitions and API wrappers far easier to read and maintain.

## 16. Tool Registry Example

```python
class Tool:
    def __init__(self, name: str, description: str):
        self.name = name
        self.description = description

    def run(self):
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

tools: list[Tool] = [
    CalculatorTool(),
    TextTool()
]

tool_names = [tool.name for tool in tools]
print(tool_names)   # ['calculator', 'text']
```

**Finding a tool by name** (combining type hints + `str | None`):
```python
def find_tool(tools: list[Tool], name: str) -> Tool | None:
    for tool in tools:
        if tool.name == name:
            return tool
    return None

tool = find_tool(tools, "calculator")
if tool:
    print(tool.run(20, 30))   # 50
```
Type hints make the function's contract immediately clear: it takes a list of `Tool` objects and a name, and returns either a matching `Tool` or `None`. List comprehensions clean up the process of extracting just the names once you have the tools.

## 17. Mental Models

- Type hint = communication — "what type should this be?"
- `-> str` = "this function returns a string."
- Type hints don't enforce types at runtime — they're for humans, editors, and static checkers.
- `str | None` = "this can be a string, or nothing."
- `*args` = extra positional values → becomes a tuple.
- `**kwargs` = extra named values → becomes a dictionary.
- List comprehension = compact way to build/filter a list.
- Dictionary comprehension = compact way to build a dictionary.
- `lambda` = a small, temporary, anonymous function.
- `map()` = apply a function to every item.
- `filter()` = keep only items that pass a condition.
- `enumerate()` = index + item, together.
- `zip()` = combine items from multiple collections, pairwise.
- Clean Python = readable → predictable → maintainable → easier to build AI systems.
- Not every function needs to be a lambda, and not every piece of logic needs to be a class.

## 18. Common Beginner Mistakes

- **Thinking type hints enforce types automatically** — they don't; Python still runs `add("Hello", "World")` even if `add` is hinted as `int`.
- **Confusing `*args` and `**kwargs`** — `*args` is positional and becomes a tuple; `**kwargs` is keyword-based and becomes a dictionary.
- **Overusing `lambda`** — using lambdas for logic that's too complex to read in one line, when a named function would be clearer.
- **Writing unreadable comprehensions** — cramming too much logic (nested conditions, multiple loops) into one comprehension line instead of using a normal loop.
- **Using `map()`/`filter()` when a comprehension is clearer** — comprehensions are often more readable for the same result.
- **Forgetting return type hints** — omitting `-> type`, leaving the function's output shape unclear.
- **Using vague variable names** — `a`, `b`, `c`, `x` instead of names that describe what the value represents.
- **Overcomplicating functions** — cramming multiple responsibilities into a single function instead of breaking it into small, clearly named steps.

## 19. Practical Code Examples

```python
# Type hints
def add(a: int, b: int) -> int:
    return a + b

def greet(name: str) -> str:
    return f"Hello {name}"

def find_user(user_id: int) -> str | None:
    ...

# *args
def add_all(*numbers):
    total = 0
    for number in numbers:
        total += number
    return total

print(add_all(1, 2, 3, 4, 5))   # 15

# **kwargs
def show_user(**kwargs):
    print(kwargs)

show_user(name="Akash", age=29, city="Lahore")

# *args + **kwargs together
def demo(*args, **kwargs):
    print(args)
    print(kwargs)

demo(10, 20, name="Akash", age=29)

# List comprehension
numbers = [1, 2, 3, 4, 5]
doubled = [n * 2 for n in numbers]

# List comprehension with condition
even_numbers = [n for n in numbers if n % 2 == 0]

# Dictionary comprehension
squares = {n: n ** 2 for n in numbers}

# Lambda
square = lambda x: x * x
print(square(5))   # 25

# map / filter
result = list(map(lambda x: x * x, numbers))
evens = list(filter(lambda x: x % 2 == 0, numbers))

# enumerate
tools = ["calculator", "weather", "search"]
for index, tool in enumerate(tools):
    print(index, tool)

# zip
names = ["Akash", "Ali"]
ages = [29, 25]
for name, age in zip(names, ages):
    print(name, age)

# Combining with classes
class Tool:
    def __init__(self, name: str):
        self.name = name

tools = [Tool("calculator"), Tool("weather")]
tool_names: list[str] = [tool.name for tool in tools]
print(tool_names)
```

## 20. Interview Questions

1. **Q: What is a type hint?**
   A: A way of communicating what type a variable, parameter, or return value is expected to be.

2. **Q: Does a normal Python type hint automatically enforce the type?**
   A: No — Python still runs the code even if the wrong type is passed; type hints are primarily for humans, editors, and static type checkers.

3. **Q: What does `name: str` mean?**
   A: It indicates `name` is expected to hold a string value.

4. **Q: What does `def add(a: int, b: int) -> int:` mean?**
   A: `add` expects two integer parameters and is expected to return an integer.

5. **Q: What does `str | None` mean?**
   A: The value can be either a string or `None`.

6. **Q: What does `*args` collect?**
   A: Extra positional arguments passed to a function.

7. **Q: What data type does `args` become?**
   A: A tuple.

8. **Q: What does `**kwargs` collect?**
   A: Extra keyword (named) arguments passed to a function.

9. **Q: What data type does `kwargs` become?**
   A: A dictionary.

10. **Q: What is a list comprehension?**
    A: A compact syntax for building a list by applying an expression to each item in a collection, optionally with a filter condition.

11. **Q: Convert this into a comprehension:**
```python
result = []
for x in numbers:
    result.append(x * 2)
```
    A: `result = [x * 2 for x in numbers]`.

12. **Q: What does `enumerate()` give you?**
    A: Both the index and the value for each item in a collection, together.

13. **Q: What does `zip()` do?**
    A: Combines multiple collections so you can iterate over their items pairwise.

14. **Q: What is a lambda function?**
    A: A small, anonymous (unnamed) function, typically used for short, temporary logic.

15. **Q: Why shouldn't you make every function into a lambda?**
    A: Complex logic in a lambda becomes hard to read; a named, readable function is often clearer.

16. **Q: Why shouldn't you make every piece of code into a class?**
    A: Simple, standalone actions are often clearer and simpler as plain functions; classes add complexity that isn't always needed.

17. **Q: Why are type hints useful in large projects?**
    A: They make function contracts (expected inputs/outputs) clear at a glance, aiding readability, editor support, and static type checking tools.

18. **Q: Why are type hints useful when working with AI tools?**
    A: Tool functions, APIs, and structured outputs become much easier to understand and integrate when their expected input/output types are explicit.

19. **Q: Explain:**
```python
tool_names = [tool.name for tool in tools]
```
    A: It builds a new list containing the `name` attribute of every `tool` object in the `tools` list.

20. **Q: Explain this architecture:**
```
Tool → Tool Registry → Agent
```
    A: Individual `Tool` objects are collected into a registry (like a list or dictionary); an agent can then look up and use the appropriate tool from that registry based on what it needs to do.

21. **Q: What's the difference between `map()`/`filter()` and a list comprehension doing the same task?**
    A: They achieve similar results, but a list comprehension is generally considered more readable in Python for straightforward transformations/filters.

22. **Q: What does `def print_message(message: str) -> None:` communicate?**
    A: The function takes a string and doesn't return a meaningful value.

23. **Q: What's an example of a mistake caused by assuming type hints enforce types?**
    A: Assuming `add(a: int, b: int)` will reject `add("Hello", "World")`, when in fact Python still executes it and returns `"HelloWorld"`.

24. **Q: Why might `def run_agent(*args, **kwargs):` appear in a framework?**
    A: To let the function accept a flexible, unspecified number of positional and keyword arguments, common in configurable library/framework code.

25. **Q: What's the benefit of combining type hints with list comprehensions in a `Tool` registry, as shown today?**
    A: Type hints make it clear what kind of objects the registry holds (e.g., `list[Tool]`), while comprehensions make it easy and readable to extract or filter data from that registry (e.g., tool names, enabled tools).

## 21. Flashcards

Q: What is a type hint used for?
A: Communicating expected types for variables, parameters, and return values.

Q: Do type hints stop incorrect types at runtime?
A: No — they're mainly for humans, editors, and static checkers.

Q: What does `-> int` mean in a function signature?
A: The function is expected to return an integer.

Q: What does `str | None` represent?
A: A value that can be either a string or `None`.

Q: What does `*args` become inside a function?
A: A tuple of extra positional arguments.

Q: What does `**kwargs` become inside a function?
A: A dictionary of extra keyword arguments.

Q: What's the mental split between `*args` and `**kwargs`?
A: `*args` = positional/tuple; `**kwargs` = keyword/dictionary.

Q: What is the general form of a list comprehension?
A: `[expression for item in collection]`.

Q: How do you add a condition to a list comprehension?
A: `[expression for item in collection if condition]`.

Q: What is a dictionary comprehension?
A: A compact way to build a dictionary, e.g. `{k: v for k in collection}`.

Q: What is a lambda function?
A: A small, anonymous function.

Q: What does `map()` do?
A: Applies a function to every item in a collection.

Q: What does `filter()` do?
A: Keeps only items that satisfy a condition.

Q: Which is usually more readable — `map()`/`filter()` or a list comprehension?
A: A list comprehension, for straightforward cases.

Q: What does `enumerate()` provide during iteration?
A: Both the index and the value of each item.

Q: What does `zip()` do with multiple collections?
A: Combines them so you can iterate over corresponding items together.

Q: Why use descriptive variable names?
A: They communicate intent and make code easier to understand.

Q: What should a function's name communicate?
A: What the function actually does.

Q: When is `raise ValueError(...)` useful in a clean function?
A: To signal invalid input clearly, such as an empty list where data was expected.

Q: What does `list[int]` mean as a type hint?
A: A list where the elements are expected to be integers.

Q: What does `dict[str, str]` mean as a type hint?
A: A dictionary where keys and values are both expected to be strings.

Q: Is a lambda always better than a full function?
A: No — simple/readable named functions are often clearer for anything beyond very small logic.

Q: What's a common mistake with comprehensions?
A: Cramming too much logic into one line, making it hard to read.

Q: How does `find_tool(tools: list[Tool], name: str) -> Tool | None` communicate its contract?
A: It expects a list of `Tool` objects and a name string, and returns either a matching `Tool` or `None`.

Q: What's the benefit of combining type hints with classes and comprehensions?
A: It makes the shape and behavior of the data (like a tool registry) explicit and easy to reason about.

Q: What's the architecture: Tool → ? → Agent?
A: Tool → Tool Registry → Agent.

Q: Why do `*args`/`**kwargs` appear often in frameworks/SDKs?
A: They allow flexible functions that accept a variable number of positional and/or keyword arguments.

Q: What's the key idea behind "clean Python"?
A: Readable → predictable → maintainable → easier to build AI systems on top of.

## 22. Code Output Practice

Predict the output of each snippet (no answers given — verify yourself):

1.
```python
def add(a: int, b: int) -> int:
    return a + b

print(add("Hello", "World"))
```

2.
```python
def show(*args):
    print(args)

show(1, 2, 3)
```

3.
```python
def show(**kwargs):
    print(kwargs)

show(a=1, b=2)
```

4.
```python
def demo(*args, **kwargs):
    print(len(args), len(kwargs))

demo(1, 2, 3, x=1, y=2)
```

5.
```python
numbers = [1, 2, 3, 4]
result = [n * 2 for n in numbers if n % 2 == 0]
print(result)
```

6.
```python
numbers = [1, 2, 3]
squares = {n: n * n for n in numbers}
print(squares)
```

7.
```python
square = lambda x: x * x
print(square(4))
```

8.
```python
numbers = [1, 2, 3, 4]
result = list(filter(lambda x: x > 2, numbers))
print(result)
```

9.
```python
tools = ["a", "b", "c"]
for i, t in enumerate(tools):
    print(i, t)
```

10.
```python
names = ["X", "Y"]
values = [10, 20, 30]
for n, v in zip(names, values):
    print(n, v)
```

11.
```python
class Tool:
    def __init__(self, name: str):
        self.name = name

tools = [Tool("a"), Tool("b")]
print([t.name for t in tools])
```

12.
```python
def find_tool(tools, name):
    for tool in tools:
        if tool.name == name:
            return tool
    return None

class Tool:
    def __init__(self, name):
        self.name = name

tools = [Tool("calculator")]
result = find_tool(tools, "weather")
print(result)
```

## 23. Debugging Practice

Each snippet has a bug — identify and fix it:

1.
```python
def add(a: int, b: int) -> int
    return a + b
```

2.
```python
def show(*args):
    print(arg)

show(1, 2, 3)
```

3.
```python
def show_user(**kwargs):
    print(kwargs["name"])

show_user("Akash", age=29)
```

4.
```python
numbers = [1, 2, 3, 4]
result = [n * 2 for n in number]
```

5.
```python
numbers = [1, 2, 3, 4]
even = [n for n in numbers if n % 2 = 0]
```

6.
```python
squares = {n ** 2 for n in numbers}
```
(This is meant to be a dictionary mapping each number to its square, not a set.)

7.
```python
square = lambda x x * x
print(square(5))
```

8.
```python
tools = ["a", "b", "c"]
for tool in enumerate(tools):
    print(index, tool)
```

9.
```python
names = ["A", "B"]
ages = [1, 2, 3]
for name, age in zip(names, ages):
    print(name, age)
```
(Assume the intent is to safely pair only matching entries — what happens here, and is it a bug?)

10.
```python
def find_tool(tools: list[Tool], name: str) -> Tool | None:
    for tool in tools
        if tool.name == name:
            return tool
```

## 24. Knowledge Test (No Answers)

1. Why don't Python type hints stop you from passing the wrong type into a function?
2. What is the practical benefit of type hints if they aren't enforced at runtime?
3. What does `list[str]` communicate about a variable, compared to just `list`?
4. What's the difference between `*args` and `**kwargs` in terms of what kind of arguments they collect?
5. Why does `*args` produce a tuple, while `**kwargs` produces a dictionary?
6. Rewrite, in your own words, the general pattern of a list comprehension.
7. When would you choose a plain `for` loop over a list comprehension, even though the comprehension is shorter?
8. What's the difference between `map()` and a list comprehension performing the same transformation?
9. What's the difference between `filter()` and a list comprehension performing the same filtering?
10. Why is `enumerate()` generally preferred over manually using `range(len(collection))`?
11. What does `zip()` do when the two collections it combines have different lengths? (Think about what "pairing" means here.)
12. Why might a lambda be a poor choice for logic that spans multiple steps or conditions?
13. What makes a function "clean" according to today's lesson (name a few qualities)?
14. Scenario: You have a function with vague variable names like `a`, `b`, `c`. Why could this become a problem in a larger project?
15. Scenario: You write `def search_web(query: str) -> list[str]:` for a future tool. What does this type hint communicate to someone using the tool, even without reading its implementation?
16. Why does `str | None` matter for a function like `find_tool()` that might not find a match?
17. Scenario: You have `tools: list[Tool]` and want just the names of tools that are enabled (`tool.enabled`). Write out, in words, how you'd express this using a list comprehension.
18. Why are `*args`/`**kwargs` common in decorators, wrappers, and SDK functions?
19. Scenario: A teammate uses `map()` and `filter()` heavily, while you prefer list comprehensions. What's the practical trade-off between the two styles?
20. Explain the architecture `Tool → Tool Registry → Agent → LLM` in your own words.
21. Why does combining type hints with comprehensions make a Tool Registry easier to understand for someone new to the codebase?
22. What's the risk of writing an overly complex, hard-to-read list comprehension instead of a normal loop?
23. Scenario: You call `find_tool(tools, "email")` but no tool with that name exists in `tools`. What should the function return, and why does the `Tool | None` type hint matter here?
24. Why might `dict[str, str | int]` type hints eventually be replaced with something like a type alias or a Pydantic model, as hinted at today?
25. Summarize, in one or two sentences, why today's features matter specifically for building AI tools and agents rather than just "general Python cleanliness."

## 25. Five-Minute Revision Sheet

- **Type hints** (`name: str`, `-> int`) communicate expected types but don't enforce them at runtime.
- **`str | None`** = value can be a string or `None`.
- **`*args`** = extra positional arguments → tuple. **`**kwargs`** = extra keyword arguments → dictionary.
- **List comprehension:** `[expression for item in collection if condition]` — compact way to build/filter a list.
- **Dictionary comprehension:** `{key_expr: value_expr for item in collection}`.
- **Lambda:** small anonymous function (`lambda x: x * x`) — best for short, simple logic.
- **`map()`/`filter()`:** apply/filter with a function across a collection — often less readable than an equivalent comprehension.
- **`enumerate()`:** gives index + item together while looping.
- **`zip()`:** pairs up items from multiple collections for parallel iteration.
- **Clean functions:** descriptive names, type hints, simple logic, readable variables, small scope, clear exceptions.
- **Agentic AI link:** Tool → Tool Registry → Agent → LLM; type hints + comprehensions make tool registries clear and maintainable.

## 26. What I Must Remember

1. Type hints communicate expected types for parameters and return values, but Python does not enforce them at runtime.
2. `list[int]`, `dict[str, str]`, and `str | None` describe the shape of a value more precisely than a bare `list`, `dict`, or untyped variable.
3. `*args` collects extra positional arguments as a tuple; `**kwargs` collects extra keyword arguments as a dictionary.
4. List comprehensions (`[expr for item in collection if condition]`) are a compact, often more readable alternative to writing out a full loop.
5. Dictionary comprehensions follow the same idea, but build a dictionary instead of a list.
6. A `lambda` is a small anonymous function best used for short, simple logic — not a replacement for clear, named functions when logic grows complex.
7. `map()` and `filter()` can achieve the same results as comprehensions, but comprehensions are usually considered more readable in Python.
8. `enumerate()` gives you the index and value together while looping; `zip()` lets you iterate over multiple collections in parallel.
9. Clean functions use descriptive names, type hints, simple logic, readable variables, and raise clear exceptions for invalid input.
10. Combining type hints, classes, and comprehensions (as in the Tool Registry example) makes code that models tools/agents far easier to read and maintain.
11. These features appear constantly in FastAPI, APIs, SDKs, LLM libraries, and agent frameworks — understanding them now means reading real AI code will feel natural, not intimidating.
12. The architecture `Tool → Tool Registry → Agent → LLM` is the direction all of Stage 0's building blocks (functions, classes, type hints, comprehensions) have been leading toward.
