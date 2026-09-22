# Day 4 — Stage 0: Python Functions

## 1. Day 4 Overview

A **function** is a reusable block of logic that you define once and can call as many times as you need. Functions are one of the most important concepts in programming because they let you avoid repeating the same code, organize a program into small understandable pieces, and — crucially for your path — represent a single **action** that something else (like an AI agent) can call. Today's lesson is the direct bridge from "writing Python code" to "building tools an AI agent can use": `Function → Action → Tool → Agent can call it`.

## 2. What Is a Function?

- **Why functions exist:** Without them, repeating a calculation 100 times means writing the same code 100 times. A function lets you write the logic once and reuse it.
```python
a = 10
b = 20
result = a + b
print(result)
```
becomes:
```python
def add(a, b):
    return a + b

result = add(10, 20)
print(result)   # 30
```
- **Reusability:** Once defined, `add()` can be called anywhere, any number of times, with different values.
- **Abstraction:** The caller doesn't need to know *how* `add()` works internally — just that giving it two numbers gives back their sum. This is the same idea as an API: you don't need to know the internals, just the input/output.
- **Function definition:** Writing `def add(a, b): return a + b` — this only *creates* the function; it does **not** run it yet.
- **Function call:** Actually running it: `add(10, 20)`.

**Mental model — function as a machine:**
```
       INPUT
         ↓
   ┌───────────┐
   │ FUNCTION  │
   │  process  │
   └───────────┘
         ↓
       OUTPUT
```
Example: `10 + 20 → add() → 30`

## 3. Function Anatomy

```python
def greet(name):
    return f"Hello, {name}!"
```

| Part | Meaning |
|---|---|
| `def` | Keyword that starts a function definition |
| `greet` | The function's name |
| `(name)` | Parameter — the input the function expects |
| `:` | Starts the function's block |
| (indented lines) | The function's body — code that runs when called |
| `return` | Sends a result back to whoever called the function |

**Important:** Defining a function (`def greet(): print("Hello!")`) only creates it — nothing happens until you *call* it with `greet()`.

## 4. Parameters and Arguments

- **Parameter:** A variable defined in the function's definition — it represents the input the function *expects*.
- **Argument:** The actual value you pass in when *calling* the function.
```python
def greet(name):      # name = parameter
    print(name)

greet("Akash")         # "Akash" = argument
```

- **Positional arguments:** Values matched to parameters by their order/position.
```python
def introduce(name, age, city):
    print(name, age, city)

introduce("Akash", 29, "Lahore")
# "Akash" → name, 29 → age, "Lahore" → city (order matters)
```

- **Keyword arguments:** Values passed by explicitly naming the parameter, so order doesn't matter and the call is easier to read.
```python
introduce(
    name="Akash",
    age=29,
    city="Lahore"
)
```

## 5. return ⭐⭐⭐

- **What it does:** Sends a value back to the code that called the function, so that value can be stored, reused, or passed elsewhere.
```python
def add(a, b):
    return a + b

result = add(10, 20)   # result now holds 30
```
- **Returning values:** As shown above — the caller receives whatever follows `return`.
- **Returning multiple values:** Python allows a function to return more than one value, technically as a tuple:
```python
def get_user():
    return "Akash", 29

name, age = get_user()
# name → "Akash", age → 29
```
- **Early return:** A function stops executing the moment it hits a `return` statement — useful for validation logic:
```python
def withdraw(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    if amount > balance:
        return "Insufficient balance"
    return "Withdrawal successful"
```
- **Why `return` makes functions reusable:** With `return`, the result can be captured in a variable and used further (e.g., `double = result * 2`). Without it, the value only appears on screen and can't be reused in later code.

## 6. print() vs return

| | `print()` | `return` |
|---|---|---|
| **Purpose** | Displays something on screen | Sends a value back to the caller |
| **Reusable afterward?** | No — the value isn't stored anywhere | Yes — can be stored in a variable and reused |
| **Example** | `def add(a, b): print(a + b)` | `def add(a, b): return a + b` |

**Why this matters:**
```python
def add(a, b):
    return a + b

result = add(10, 20)
double = result * 2
print(double)   # 60
```
If `add()` only used `print()` instead of `return`, `result` would not actually hold the sum — you couldn't do `result * 2` with it.

**Function without `return`:** If a function doesn't explicitly return anything, Python treats the result as `None`:
```python
def greet(name):
    print(f"Hello {name}")

result = greet("Akash")
print(result)
```
Output:
```
Hello Akash
None
```

This distinction is extremely important for APIs and Agentic AI — a tool function needs to `return` its result so the calling code (and eventually the LLM) can actually use it, not just display it.

## 7. Default Parameters

A parameter can have a default value, used only when the caller doesn't provide one.
```python
def greet(name="Guest"):
    print(f"Hello {name}")

greet()          # Hello Guest
greet("Akash")   # Hello Akash
```
This also works when mixing a default with a required parameter:
```python
def create_user(name, country="Pakistan"):
    print(name, country)

create_user("Akash")          # Akash Pakistan
create_user("John", "USA")    # John USA
```

## 8. Scope

- **Local variables:** Variables created inside a function belong only to that function — they can't be accessed from outside it.
```python
def calculate():
    result = 100
    print(result)

calculate()
print(result)   # Error — result doesn't exist outside the function
```
```
Outside
──────────────
name

       ↓

Function
──────────────
result
```

- **Function scope:** If a variable with the same name exists both outside and inside a function, the version *inside* the function is a separate, local variable:
```python
name = "Akash"

def greet():
    name = "John"
    print(name)

greet()
print(name)
```
Output:
```
John
Akash
```
The `name` inside `greet()` doesn't affect the `name` outside it.

- **Global variables (beginner level):** A variable defined outside any function is accessible for reading inside functions, but modifying it from inside a function generally requires the `global` keyword.

- **Why unnecessary global variables should be avoided:** Relying on functions that reach out and modify shared global state (like `global balance`) makes code harder to test and reuse. It's generally better to design functions that *receive* what they need as parameters and *return* their results:
```python
def withdraw(balance, amount):
    if amount > balance:
        return balance, False
    return balance - amount, True
```
This version doesn't depend on any external variable — it's self-contained, easier to test, and easier to reuse.

## 9. Functions + Conditions

Functions can contain any logic from Day 2, including `if`/`elif`/`else`:
```python
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

print(check_age(25))   # Adult
```

## 10. Functions + Loops

Functions can process collections using loops from Day 2/3:
```python
def print_tasks(tasks):
    for task in tasks:
        print(task)

tasks = ["Learn Python", "Learn FastAPI", "Learn AI"]
print_tasks(tasks)
```
This is much cleaner than writing all the logic directly in one large block of code.

## 11. Functions + Dictionaries

Functions can accept and work with dictionaries (Day 3's most important structure):
```python
def get_user(user):
    return user["name"]

user = {"name": "Akash", "age": 29}
name = get_user(user)
print(name)   # Akash
```
This pattern — a function that takes structured data and returns something useful from it — is exactly the shape of many real tool functions.

## 12. Error Handling Inside Functions

A basic `try`/`except` can prevent a function from crashing on a predictable error:
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

print(divide(10, 0))   # Cannot divide by zero
```
`try` runs the code that might fail; `except ZeroDivisionError` catches that specific error and returns a safe fallback message instead of crashing the program. (Deeper error handling will be covered later — this is just the basic pattern.)

## 13. Functions as Actions

A normal Python function can represent a single **action** — something concrete the program (or later, an agent) can *do*:
```python
def calculator(expression):
    ...

def weather(city):
    ...

def search_web(query):
    ...

def send_email(to, message):
    ...
```
Each of these is just a function, but conceptually each one represents an action an agent could eventually choose to perform — for example, an LLM deciding "I need to calculate 25 × 4," then calling `calculator("25 * 4")` to get `100`, and continuing its reasoning with that result.

## 14. Functions → Tools → Agents

This is the key progression from today's lesson:
```
Function
   ↓
Action
   ↓
Tool
   ↓
Agent can select/use the tool
```

**Example — a primitive tool router:**
```python
def calculator(expression):
    return eval(expression)

def weather(city):
    return f"Weather for {city}"

tools = {
    "calculator": calculator,
    "weather": weather
}

tool_name = "calculator"
tool = tools[tool_name]
result = tool("20 + 30")
print(result)
```

**What happens when you write:**
```python
tool = tools["weather"]
result = tool("Lahore")
```
`tools["weather"]` looks up the `weather` function *itself* (not a result — the function object) inside the dictionary and stores it in `tool`. Then `tool("Lahore")` calls that function with `"Lahore"` as the argument, running `weather("Lahore")` and returning `"Weather for Lahore"`.

```
tool name
    ↓
dictionary
    ↓
function
    ↓
execute
    ↓
result
```

Note from the lesson: `eval()` is used above only to demonstrate the function/tool concept quickly — it should not be used on untrusted input in real applications, since it can execute arbitrary code. A safer calculator will be built later.

## 15. Agentic AI Connection

Functions built the way you learned today become the actual actions behind future AI tools:

- **Calculator tools** — a function that evaluates or computes an expression.
- **Web search tools** — a function that queries the web and returns results.
- **Weather tools** — a function that fetches weather data for a location.
- **Database tools** — a function that reads or writes records.
- **APIs** — a function that wraps an external API call, similar to what you did in Lesson 2.
- **File operations** — a function that reads, writes, or processes files.
- **Email tools** — a function like `send_email(to, message)`.
- **RAG retrieval** — a function that searches documents/embeddings and returns relevant chunks.

**Important:** A plain Python function by itself is **not** automatically an AI agent. It's just an action. It only becomes part of an agent once an LLM is choosing *when* and *whether* to call it, as part of a loop that also tracks state — the full picture from Lesson 1 (`Agent = LLM + Tools + Loop + State`).

## 16. Mental Models

- Function = reusable machine.
- Parameter = input slot (defined in the function).
- Argument = the actual value passed in.
- `return` = give the result back so it can be reused.
- `print` = show the result on screen, not reusable afterward.
- Defining a function ≠ running it — you still have to call it.
- Positional arguments = order matters; keyword arguments = names matter.
- Local variables live and die inside their function.
- A function with no `return` gives back `None`.
- Function → Action → Tool → Agent can use it.

## 17. Common Beginner Mistakes

- **Forgetting to call a function** — writing `def greet(): ...` and expecting it to run on its own; you must call `greet()`.
- **Confusing parameter and argument** — the parameter is the placeholder in the definition; the argument is the real value passed at call time.
- **Using `print` instead of `return`** — the result then can't be stored or reused elsewhere in the program.
- **Forgetting `return` entirely** — the function silently gives back `None`, which can cause confusing bugs later.
- **Wrong indentation** — the function body must be indented consistently, just like `if` blocks and loops.
- **Misunderstanding scope** — assuming a variable created inside a function is available outside it, when it isn't.
- **Passing arguments in the wrong order** — with positional arguments, mixing up the order sends the wrong value to the wrong parameter.

## 18. Code Examples

```python
# Basic function
def add(a, b):
    return a + b

result = add(10, 20)
print(result)   # 30

# print vs return
def add_print(a, b):
    print(a + b)

def add_return(a, b):
    return a + b

add_print(10, 20)          # displays 30, but gives nothing back
value = add_return(10, 20) # value now holds 30

# Default parameters
def greet(name="Guest"):
    print(f"Hello {name}")

greet()
greet("Akash")

# Keyword arguments
def introduce(name, age, city):
    print(name, age, city)

introduce(name="Akash", age=29, city="Lahore")

# Scope
name = "Akash"
def greet2():
    name = "John"
    print(name)

greet2()
print(name)

# Functions + conditions
def check_age(age):
    if age >= 18:
        return "Adult"
    else:
        return "Minor"

# Functions + loops
def print_tasks(tasks):
    for task in tasks:
        print(task)

# Functions + dictionaries
def get_user(user):
    return user["name"]

# Multiple return values
def get_user_info():
    return "Akash", 29

name, age = get_user_info()

# Early return
def withdraw(balance, amount):
    if amount <= 0:
        return "Invalid amount"
    if amount > balance:
        return "Insufficient balance"
    return "Withdrawal successful"

# Error handling
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Cannot divide by zero"

# Functions as tools
def calculator(expression):
    return eval(expression)

def weather(city):
    return f"Weather for {city}"

tools = {
    "calculator": calculator,
    "weather": weather
}

tool = tools["weather"]
result = tool("Lahore")
print(result)
```

## 19. Interview Questions

1. **Q: What is a function?**
   A: A reusable block of logic that you define once and can call multiple times with different inputs.

2. **Q: What's the difference between defining a function and calling it?**
   A: Defining (`def`) only creates the function; calling it (`greet()`) actually executes its code.

3. **Q: What's the difference between a parameter and an argument?**
   A: A parameter is the placeholder variable in the function's definition; an argument is the actual value passed when calling the function.

4. **Q: What's the difference between `print()` and `return` in a function?**
   A: `print()` displays a value on screen but gives nothing back to the caller; `return` sends the value back so it can be stored and reused.
   *Deeper:* Without `return`, you can't capture the function's result in a variable for further use.

5. **Q: What does this code return?**
```python
def add(a, b):
    return a + b
```
when called with `add(10, 20)`?
   A: `30`.

6. **Q: What is a default parameter?**
   A: A parameter with a pre-set value that's used automatically when the caller doesn't supply one.
```python
def greet(name="Guest"):
    ...
```

7. **Q: What is a keyword argument?**
   A: An argument passed by explicitly naming its parameter (e.g., `age=29`), so the order in which you pass arguments doesn't matter.

8. **Q: What is variable scope?**
   A: The area of code where a variable is accessible — variables created inside a function are local to it and aren't accessible outside.

9. **Q: Why is returning a result usually more reusable than only printing it?**
   A: A returned value can be stored in a variable and used in further calculations or logic, while a printed value only appears on screen and disappears.

10. **Q: What does this do?**
```python
tools = {
    "calculator": calculator,
    "weather": weather
}
```
    A: It creates a dictionary mapping tool names (strings) to the actual function objects, allowing a specific function to be looked up and called dynamically by name.

11. **Q: What happens here?**
```python
tool = tools["weather"]
result = tool("Lahore")
```
    A: `tools["weather"]` retrieves the `weather` function itself from the dictionary; `tool("Lahore")` then calls that function with `"Lahore"` as the argument and stores its return value in `result`.

12. **Q: Why can functions be considered the foundation of tools in an AI application?**
    A: A tool is essentially a function that performs a specific action (calculation, search, API call); an agent can select and call these functions dynamically, but the underlying action is just a Python function.

13. **Q: What happens if a function has no `return` statement?**
    A: Python returns `None` by default from that function.

14. **Q: What is "early return," and why is it useful?**
    A: Returning before the end of a function (e.g., in a validation check) — it's useful because the function can stop immediately once it knows the final result, without running unnecessary further code.

15. **Q: Can a Python function return more than one value? How?**
    A: Yes — by separating values with a comma after `return` (e.g., `return name, age`), which Python packages as a tuple that can be unpacked into multiple variables.

## 20. Flashcards

Q: What is a function?
A: A reusable block of logic you define once and call as needed.

Q: What keyword defines a function?
A: `def`.

Q: Does defining a function run it?
A: No — you must call it separately.

Q: What is a parameter?
A: The input placeholder defined in a function.

Q: What is an argument?
A: The actual value passed to a function when calling it.

Q: What does `return` do?
A: Sends a value back to the caller so it can be reused.

Q: What does `print()` do inside a function?
A: Displays a value but doesn't make it reusable elsewhere.

Q: What does a function return if it has no `return` statement?
A: `None`.

Q: What is a default parameter?
A: A parameter with a preset value used when no argument is supplied.

Q: What is a positional argument?
A: An argument matched to a parameter by its order.

Q: What is a keyword argument?
A: An argument passed by explicitly naming its parameter.

Q: What is a local variable?
A: A variable that exists only inside the function where it was created.

Q: Can code outside a function access its local variables?
A: No.

Q: Why should unnecessary global variables be avoided?
A: They make functions harder to test and reuse; passing values as parameters is generally better.

Q: What does `try`/`except` do in a function?
A: Lets you catch a specific error and return a safe fallback instead of crashing.

Q: Can a function return multiple values?
A: Yes, as a tuple, which can be unpacked into multiple variables.

Q: What is "early return"?
A: Returning a value before reaching the end of the function, often used for validation.

Q: How do you call a function stored inside a dictionary?
A: Retrieve it by key, then call it with parentheses, e.g. `tools["weather"]("Lahore")`.

Q: Is a Python function automatically an AI agent?
A: No — it's just an action; it becomes part of an agent only when an LLM decides when to call it, within a loop and with state.

Q: What's the mental model for functions and Agentic AI?
A: Function → Action → Tool → Agent can use it.

## 21. Code Output Practice

Predict the output of each snippet before checking (no answers given — verify yourself):

1.
```python
def add(a, b):
    return a + b

print(add(4, 6))
```

2.
```python
def greet(name):
    print(f"Hi {name}")

result = greet("Sara")
print(result)
```

3.
```python
def multiply(a, b=2):
    return a * b

print(multiply(5))
```

4.
```python
def multiply(a, b=2):
    return a * b

print(multiply(5, 3))
```

5.
```python
x = 10

def change():
    x = 20
    print(x)

change()
print(x)
```

6.
```python
def check(age):
    if age >= 18:
        return "Adult"
    return "Minor"

print(check(15))
```

7.
```python
def get_values():
    return 1, 2, 3

a, b, c = get_values()
print(b)
```

8.
```python
def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Error"

print(divide(10, 0))
```

9.
```python
def show(items):
    for item in items:
        print(item)

show(["A", "B"])
```

10.
```python
def get_name(user):
    return user["name"]

print(get_name({"name": "Ali", "age": 20}))
```

## 22. Knowledge Test (No Answers)

1. What is the practical difference between defining a function and calling it?
2. Explain, using your own example, the difference between a parameter and an argument.
3. Why does using `print()` instead of `return` inside a function limit what you can do with its result afterward?
4. What value does a function return if it reaches the end without hitting a `return` statement?
5. What's the difference between calling a function with positional arguments versus keyword arguments?
6. Why might a variable defined inside a function be inaccessible outside of it?
7. Why is it generally considered better practice for a function to receive values as parameters and return results, rather than relying on global variables?
8. What does "early return" mean, and why is it useful in a function like a withdrawal validator?
9. How can a function return more than one value, and how would you capture those values when calling it?
10. What's the purpose of wrapping code in `try`/`except` inside a function like `divide()`?
11. Scenario: You have `tools = {"search": search_function}`. Describe the steps to look up and call the `search` function using the string `"search"`.
12. Scenario: You write a function `def calculate(): result = 5 * 5` with no `return`. What happens if you try to print the value returned by calling this function?
13. Scenario: A function `def introduce(name, age, city)` is called as `introduce(city="Lahore", name="Akash", age=29)`. Will this work? Why or why not?
14. Why is a plain Python function not, by itself, considered an AI agent?
15. Scenario: You're designing a `weather(city)` function meant to eventually become an agent tool. Why does it matter whether this function uses `return` instead of `print()` to give back its result?

## 23. Five-Minute Revision Sheet

- **Function** = reusable block of logic, defined with `def`, run only when *called*.
- **Parameter** = placeholder in the definition; **Argument** = actual value passed at call time.
- **Positional arguments** = matched by order; **Keyword arguments** = matched by name.
- **`return`** sends a value back for reuse; **`print()`** only displays it — no `return` means the function gives back `None`.
- **Default parameters** (`name="Guest"`) are used only when no value is passed.
- **Scope:** variables created inside a function are local — inaccessible outside it; prefer passing values in/returning values out over relying on global variables.
- **Functions can contain** conditions, loops, and dictionary logic just like any other code.
- **`try`/`except`** inside a function lets you catch a specific error and return a safe fallback.
- **Multiple return values** come back as a tuple (`return a, b`) and can be unpacked (`x, y = func()`).
- **Agentic AI link:** Function → Action → Tool → Agent can select/use it — but a function alone is not an agent.

## 24. What I Must Remember

1. A function is a reusable block of logic, defined with `def`, and it only runs when explicitly called.
2. Parameters are placeholders in the function's definition; arguments are the actual values passed when calling it.
3. `return` sends a value back to the caller so it can be reused; `print()` only displays it on screen.
4. A function with no `return` statement implicitly returns `None`.
5. Default parameters provide a fallback value used only when the caller doesn't supply one.
6. Positional arguments are matched by order; keyword arguments are matched by explicit parameter name.
7. Variables created inside a function are local to it and cannot be accessed from outside — prefer passing/returning values over relying on global variables.
8. A function can return multiple values as a tuple, and `try`/`except` inside a function lets it handle predictable errors gracefully.
9. A function can represent a real-world action (calculator, weather, search, email) — this is exactly the shape of a future AI tool.
10. The progression Function → Action → Tool → Agent matters, but a plain function is not automatically an agent — it becomes part of one only when an LLM decides when to call it, within a loop, tracking state.
