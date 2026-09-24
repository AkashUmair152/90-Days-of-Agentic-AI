# Day 6 — Stage 0: Python Files, JSON, Exceptions, and Data Persistence

## 1. Day 6 Overview

Every program you've written so far loses its data the moment it closes — variables only exist in memory (RAM) while the program is running. Today changes that: you learn how to **save data to files** so it survives after the program ends, how to **safely handle errors** with exceptions so bad input or missing files don't crash your program, and how to use **JSON** — the standard format for structured data exchange — to store and load that data cleanly. This matters enormously for Agentic AI because tool inputs/outputs, API payloads, and agent state are almost always JSON, and a production-quality tool must handle errors gracefully instead of crashing.

## 2. Files

- **What files are:** Storage on disk that keeps data even after your program stops running (unlike variables, which live only in memory/RAM while the program runs).
- **Why programs need files:**
```
Program running
      ↓
RAM / memory
      ↓
Program closes
      ↓
Data disappears
```
Without files, every run starts from scratch. With files:
```
Program
   ↓
File
   ↓
Data remains
```

- **`open()`:** The built-in function that opens a file.
```python
file = open("hello.txt", "r")
```
- **`with open()`:** The preferred, standard way to open files (explained in Section 4).

- **Read mode (`"r"`):**
```python
with open("hello.txt", "r") as file:
    content = file.read()
print(content)
```
- **Write mode (`"w"`):**
```python
with open("hello.txt", "w") as file:
    file.write("Hello Akash")
```
- **Append mode (`"a"`):**
```python
with open("hello.txt", "a") as file:
    file.write("\nNew line")
```
- **Create mode (`"x"`):** Creates a new file (listed in the lesson's file modes table).

- **`read()`:** Reads the entire file content as one string.
- **`readlines()`:** Reads all lines into a list.
```python
with open("hello.txt", "r") as file:
    lines = file.readlines()
print(lines)
# ["Hello Akash\n", "Welcome to Python\n"]
```
- **Looping through a file:**
```python
with open("hello.txt", "r") as file:
    for line in file:
        print(line.strip())
```

## 3. File Modes

| Mode | Meaning |
|---|---|
| `"r"` | Read |
| `"w"` | Write (overwrite) |
| `"a"` | Append |
| `"x"` | Create new file |

**`"w"` can overwrite existing content:** If `hello.txt` already contains `"Hello\nWelcome"`, running:
```python
with open("hello.txt", "w") as file:
    file.write("New content")
```
completely replaces the old content — the file now only contains `"New content"`. This is different from `"a"`, which adds to the end without deleting what's already there.

Mental model:
```
w = replace
a = add to end
```

## 4. with open()

`with open(...) as file:` is preferred over plain `open()` because it **automatically handles closing the file** for you once the block finishes — you don't need to manually call `file.close()`. This is the standard pattern you'll see constantly in real Python code.

## 5. Exceptions

- **What exceptions are:** Errors that occur while your program is running (as opposed to syntax errors caught before running).
```python
number = 10 / 0   # raises ZeroDivisionError
```
```python
with open("missing.txt") as file:   # raises FileNotFoundError
    ...
```

- **Why applications need exception handling:**
```
Without handling:
Program → Error → 💥 Program crashes

With handling:
Program → Error → except → Handle problem → Continue / give useful message
```

- **`try`/`except`:**
```python
try:
    number = 10 / 0
except ZeroDivisionError:
    print("You cannot divide by zero.")
```

- **`else`:** Runs only when no exception occurred inside `try`.
```python
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number.")
else:
    print("You entered:", number)
```

- **`finally`:** Runs whether an exception occurred or not.
```python
try:
    number = int(input("Number: "))
except ValueError:
    print("Invalid number.")
finally:
    print("Program finished.")
```

- **`raise`:** Lets you create/trigger an exception yourself, typically for validation.
```python
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount
```
Handling your own raised exception:
```python
try:
    result = withdraw(1000, -50)
except ValueError as error:
    print(error)
```
Output: `Amount must be greater than zero.`

**Mental model:**
```
try     → "I'll try this operation."
except  → "If something goes wrong, handle it."
else    → "If everything worked, do this."
finally → "Do this no matter what."
```
```
try
 ↓
Did error happen?
 ↙       ↘
YES       NO
 ↓         ↓
except    else
```

## 6. Common Exceptions

*(Today's lesson explicitly covered `ZeroDivisionError`, `ValueError`, and `FileNotFoundError`. `KeyError` and `IndexError` weren't part of today's material, but since they're closely related beginner-level exceptions from structures you already know — dictionaries and lists — they're included here briefly as useful, practical reference.)*

| Exception | Example that triggers it |
|---|---|
| `ValueError` | `int("abc")` — text that can't be converted to a number |
| `ZeroDivisionError` | `10 / 0` |
| `FileNotFoundError` | `open("missing.txt", "r")` on a file that doesn't exist |
| `KeyError` | `user["email"]` when the dictionary has no `"email"` key |
| `IndexError` | `names[10]` on a list with fewer than 11 items |

## 7. Specific Exception Handling

**Prefer specific exceptions over a bare `except:`.**
```python
try:
    number = int(input("Enter number: "))
    result = 100 / number
except ValueError:
    print("Please enter a valid number.")
except ZeroDivisionError:
    print("Number cannot be zero.")
```
A bare `except:` catches almost everything and can hide real problems, making bugs harder to find:
```python
try:
    ...
except:      # ⚠️ Avoid — catches too much, hides the real error
    ...
```
Naming the exact exception (`except ValueError:`, `except FileNotFoundError:`) keeps your error handling precise and your program's behavior predictable.

## 8. JSON

- **What JSON is:** JavaScript Object Notation — a common, language-independent text format for exchanging structured data. You don't need to know JavaScript to use it.
```json
{
  "name": "Akash",
  "age": 29,
  "city": "Lahore"
}
```
- **JSON objects:** Key/value structures wrapped in `{ }` — look just like Python dictionaries.
- **JSON arrays:** Ordered lists wrapped in `[ ]` — look just like Python lists.
```json
["Learn Python", "Learn FastAPI", "Learn AI"]
```
- **JSON strings:** Text values in double quotes, e.g. `"Akash"`.
- **JSON numbers:** Plain numeric values, e.g. `29`.
- **JSON booleans:** `true` / `false` — note the **lowercase**, unlike Python's `True`/`False`.
- **`null`:** JSON's equivalent of Python's `None`.

- **Python vs JSON differences:**

| Python | JSON |
|---|---|
| `True` / `False` | `true` / `false` |
| `None` | `null` |
| dictionary (in-memory Python object) | text-based data format |

They look nearly identical in shape, but a Python dictionary is a live object in memory, while JSON is a text format used for storing/exchanging data — Python's `json` module converts between the two.

## 9. json.dump() and json.load()

```
Python
  ↓
json.dump()
  ↓
JSON file
```
```
JSON file
  ↓
json.load()
  ↓
Python
```

**`json.dump()`** — writes Python data into a JSON file:
```python
import json

user = {
    "name": "Akash",
    "age": 29,
    "skills": ["Python", "FastAPI"]
}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)
```
Result (`user.json`):
```json
{
    "name": "Akash",
    "age": 29,
    "skills": [
        "Python",
        "FastAPI"
    ]
}
```
`indent=4` is used purely for readability — without it, the JSON would likely be written as one unformatted line.

**`json.load()`** — reads JSON back into Python data:
```python
import json

with open("user.json", "r") as file:
    user = json.load(file)

print(user)
```

**Memorize:**
```
dump → Python → JSON file
load → JSON file → Python
```
(Note: `json.dumps()` and `json.loads()` also exist, working with strings instead of files — the lesson mentions these exist but says they'll be covered soon, not today.)

**JSON objects + arrays combined:**
```json
{
    "name": "Akash",
    "tasks": [
        {"id": 1, "title": "Learn Python", "completed": true},
        {"id": 2, "title": "Learn FastAPI", "completed": false}
    ]
}
```
This kind of nested shape is very similar to the data you'll eventually send and receive through real APIs.

## 10. Data Persistence

- **Memory vs persistent storage:** Memory (RAM) only holds data while the program runs; persistent storage (files) keeps data after the program closes.
- **Why data disappears when only stored in variables:**
```
Program starts → data → program stops → data disappears
```
- **How files allow persistence:**
```
Program starts → load data → modify data → save data → program stops → data remains
```
This **load → modify → save** cycle is the core workflow behind any persistent application, including today's Todo app.

## 11. Persistent Todo Application

**Project structure:**
```
day-06/
│
├── main.py
├── storage.py
└── tasks.json
```

**Responsibility of each file:**

- **`storage.py`** — handles reading and writing data to `tasks.json`:
```python
import json

def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
```
`load_tasks()` opens `tasks.json` for reading and converts its JSON content into Python data; if the file doesn't exist yet, it safely returns an empty list instead of crashing. `save_tasks(tasks)` writes the current Python list back into `tasks.json` as formatted JSON.

- **`main.py`** — contains the application logic and menu, using `storage.py`'s functions:
```python
from storage import load_tasks, save_tasks

def add_task(tasks, title):
    task = {"id": len(tasks) + 1, "title": title, "completed": False}
    tasks.append(task)
```
The overall architecture:
```
main.py
   ↓
load_tasks()
   ↓
tasks
   ↓
user action
   ↓
modify tasks
   ↓
save_tasks()
   ↓
tasks.json
```

- **`tasks.json`** — the actual persistent data file, e.g.:
```json
[
    {"id": 1, "title": "Learn Python", "completed": false}
]
```

**Important improvement:** Raw input like `task_id = int(input("Task ID: "))` will crash with `ValueError` if the user types something like `abc`. Wrapping it in `try`/`except` prevents the crash:
```python
try:
    task_id = int(input("Task ID: "))
except ValueError:
    print("Please enter a valid number.")
    continue
```

## 12. Agentic AI Connection

Today's tools map directly onto how tools and agents communicate:

- **Tool inputs/outputs:** A tool might receive `{"city": "Lahore"}` and return `{"temperature": 31, "condition": "Sunny"}` — both JSON-shaped.
- **API payloads:** Requests and responses to LLM APIs and other services are commonly JSON.
- **Agent state:** As seen in earlier lessons, agent state is often represented as a dictionary — which maps naturally to JSON for saving/loading.
- **Conversation history:** A list of message dictionaries, just like the JSON arrays-of-objects shape from Section 8.
- **Configuration:** Settings for an application are frequently stored as JSON files.
- **Persistence:** Tool results, task lists, or agent memory can be saved to disk using `json.dump()`/`json.load()`, exactly like today's Todo app.
- **Database interaction:** Real databases eventually replace simple JSON files, but the data itself is still commonly represented and exchanged as JSON along the way.

```
LLM
 ↓
Tool
 ↓
Function
 ↓
JSON
 ↓
Storage
```

**Important:** JSON is a data format used for structured communication between components (LLM ↔ tool ↔ storage) — it is **not** itself an AI agent. It's the "shape" the data takes as it moves through the system, not the reasoning or decision-making itself.

## 13. Mental Models

- File = a persistent place to store data.
- `r` = read.
- `w` = write/replace (overwrites existing content).
- `a` = append (adds to the end).
- `with open()` = automatically closes the file for you.
- `try` = attempt something that might fail.
- `except` = handle a specific error if it happens.
- `else` (in try/except) = runs only if no error occurred.
- `finally` = runs no matter what.
- `raise` = intentionally report a problem/error.
- Bare `except:` = catches too much, hides real bugs — avoid it.
- JSON object `{ }` ≈ Python dictionary; JSON array `[ ]` ≈ Python list.
- JSON booleans are lowercase (`true`/`false`); Python's are capitalized (`True`/`False`).
- `dump` = Python → JSON file.
- `load` = JSON file → Python.
- Persistence = load → modify → save, so data survives after the program closes.

## 14. Common Beginner Mistakes

- **Forgetting to close files** — avoided entirely by using `with open()`, which closes automatically.
- **Using `"w"` when `"a"` is needed** — accidentally wiping out existing file content instead of adding to it.
- **Catching every exception with a bare `except:`** — hides the real error and makes debugging harder; use specific exception types instead.
- **Not handling a missing file** — forgetting `except FileNotFoundError:` when a file might not exist yet (like `tasks.json` on first run).
- **Confusing JSON with a Python dictionary** — they look alike, but JSON is a text-based data format, while a dictionary is a Python object in memory.
- **Forgetting that JSON booleans are lowercase** — writing `True`/`False` by hand in a `.json` file (instead of `true`/`false`) produces invalid JSON.
- **Forgetting to save changed data** — modifying a list in memory (e.g., `tasks.append(...)`) but never calling `save_tasks(tasks)`, so the change is lost when the program closes.
- **Assuming variables persist after the program closes** — without explicitly saving to a file, all in-memory data disappears once the program ends.

## 15. Practical Code Examples

```python
# Reading a file
with open("hello.txt", "r") as file:
    content = file.read()
print(content)

# Reading lines
with open("hello.txt", "r") as file:
    for line in file:
        print(line.strip())

# Writing (overwrite)
with open("hello.txt", "w") as file:
    file.write("Hello Akash")

# Appending
with open("hello.txt", "a") as file:
    file.write("\nNew line")

# try/except/else/finally
try:
    number = int(input("Enter number: "))
except ValueError:
    print("Invalid number.")
else:
    print("You entered:", number)
finally:
    print("Program finished.")

# raise
def withdraw(balance, amount):
    if amount <= 0:
        raise ValueError("Amount must be greater than zero.")
    if amount > balance:
        raise ValueError("Insufficient balance.")
    return balance - amount

try:
    withdraw(1000, -50)
except ValueError as error:
    print(error)

# JSON dump/load
import json

user = {"name": "Akash", "age": 29, "skills": ["Python", "FastAPI"]}

with open("user.json", "w") as file:
    json.dump(user, file, indent=4)

with open("user.json", "r") as file:
    loaded_user = json.load(file)
print(loaded_user)

# Persistent storage pattern
def load_tasks():
    try:
        with open("tasks.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open("tasks.json", "w") as file:
        json.dump(tasks, file, indent=4)
```

## 16. Interview Questions

1. **Q: What is the difference between memory and persistent storage?**
   A: Memory (RAM) only holds data while the program is running; persistent storage (files) keeps data even after the program closes.

2. **Q: What does `with open("data.txt", "r") as file:` do?**
   A: Opens `data.txt` in read mode and automatically closes the file when the block finishes.

3. **Q: What's the difference between `"r"`, `"w"`, and `"a"`?**
   A: `"r"` reads a file, `"w"` writes and overwrites existing content, `"a"` appends without deleting what's already there.

4. **Q: Why is `with open()` preferred over plain `open()`?**
   A: It automatically closes the file for you, even if an error occurs, without needing to manually call `file.close()`.

5. **Q: What happens when `"w"` is used on a file that already has content?**
   A: The existing content is completely replaced/overwritten.

6. **Q: What is an exception?**
   A: An error that occurs while a program is running, such as dividing by zero or opening a missing file.

7. **Q: What does `try` do?**
   A: Marks a block of code that might raise an error, so Python can attempt it safely.

8. **Q: What does `except` do?**
   A: Catches and handles a specific type of error if it occurs inside the `try` block.

9. **Q: When does `else` run in a try/except block?**
   A: Only when no exception occurred in the `try` block.

10. **Q: When does `finally` run?**
    A: Always — whether an exception occurred or not.

11. **Q: What does `raise` do?**
    A: Lets you intentionally trigger an exception, often to signal invalid input or a validation failure.
```python
raise ValueError("Amount must be greater than zero.")
```

12. **Q: What is JSON?**
    A: A text-based format for representing structured data (objects and arrays), commonly used to exchange data between systems like APIs.

13. **Q: What's the difference between `json.dump()` and `json.load()`?**
    A: `json.dump()` writes Python data into a JSON file; `json.load()` reads JSON data from a file back into Python.

14. **Q: Why is JSON extremely common in APIs?**
    A: It's a simple, structured, language-independent format that closely mirrors dictionaries/lists, making it easy for different systems (including LLMs and tools) to exchange data.

15. **Q: Explain this architecture:**
```
LLM → Tool → Function → JSON data → Storage
```
    A: The LLM decides to use a tool, the tool calls a Python function, that function's input/output is represented as JSON, and the JSON can be persisted to storage (like a file).

16. **Q: Why should you generally avoid a bare `except:`?**
    A: It catches almost every kind of error indiscriminately, which can hide bugs and make debugging much harder; catching specific exceptions is clearer and safer.

17. **Q: What happens if you try to open a file that doesn't exist in read mode?**
    A: Python raises a `FileNotFoundError`.

18. **Q: What's the difference between a Python dictionary and JSON?**
    A: They look nearly identical, but a Python dictionary is a live object in memory, while JSON is a text-based data format used for storage/exchange; `True`/`False`/`None` in Python become `true`/`false`/`null` in JSON.

19. **Q: Why does `load_tasks()` use `try`/`except FileNotFoundError`?**
    A: So that on the very first run (when `tasks.json` doesn't exist yet), the program safely returns an empty list instead of crashing.

20. **Q: What is `indent=4` used for in `json.dump()`?**
    A: Purely for readability — it formats the JSON output with indentation instead of writing it as one unformatted line.

## 17. Flashcards

Q: What does `"r"` mode do?
A: Opens a file for reading.

Q: What does `"w"` mode do?
A: Opens a file for writing, overwriting existing content.

Q: What does `"a"` mode do?
A: Opens a file for appending, adding to the end without deleting existing content.

Q: What does `with open()` do automatically?
A: Closes the file for you.

Q: What does `file.read()` return?
A: The entire file content as one string.

Q: What does `file.readlines()` return?
A: A list of lines from the file.

Q: What is an exception?
A: An error that occurs while a program is running.

Q: What does `try` do?
A: Attempts code that might raise an error.

Q: What does `except` do?
A: Handles a specific error if it occurs.

Q: When does `else` run in try/except?
A: Only if no exception occurred.

Q: When does `finally` run?
A: Always, regardless of whether an error occurred.

Q: What does `raise` do?
A: Intentionally triggers an exception.

Q: What error does `10 / 0` raise?
A: `ZeroDivisionError`.

Q: What error does `int("abc")` raise?
A: `ValueError`.

Q: What error does opening a missing file raise?
A: `FileNotFoundError`.

Q: Why avoid a bare `except:`?
A: It catches too much and can hide real bugs.

Q: What is JSON?
A: A text-based format for structured data exchange.

Q: What does a JSON object look like?
A: Key/value pairs in `{ }`, like a Python dictionary.

Q: What does a JSON array look like?
A: An ordered list in `[ ]`, like a Python list.

Q: How are JSON booleans written?
A: Lowercase — `true`/`false`.

Q: What is JSON's equivalent of Python's `None`?
A: `null`.

Q: What does `json.dump()` do?
A: Writes Python data into a JSON file.

Q: What does `json.load()` do?
A: Reads JSON data from a file into Python.

Q: What does "persistence" mean?
A: Data survives after the program stops running.

Q: What's the core persistence workflow?
A: Load data → modify data → save data.

Q: Is JSON itself an AI agent?
A: No — it's a data format used for structured communication, not the reasoning/decision-making itself.

## 18. Code Output Practice

Predict the output or exception for each (no answers given — verify yourself):

1.
```python
with open("notes.txt", "w") as file:
    file.write("Hello")

with open("notes.txt", "r") as file:
    print(file.read())
```

2.
```python
with open("notes.txt", "w") as file:
    file.write("First")

with open("notes.txt", "w") as file:
    file.write("Second")

with open("notes.txt", "r") as file:
    print(file.read())
```

3.
```python
with open("notes.txt", "w") as file:
    file.write("Line1")

with open("notes.txt", "a") as file:
    file.write("\nLine2")

with open("notes.txt", "r") as file:
    print(file.read())
```

4.
```python
try:
    x = 10 / 0
except ValueError:
    print("Value error")
```
(What happens, given the exception type doesn't match?)

5.
```python
try:
    number = int("hello")
except ValueError:
    print("Not a number")
else:
    print("Converted:", number)
```

6.
```python
try:
    print("Trying")
finally:
    print("Always runs")
```

7.
```python
def check(age):
    if age < 0:
        raise ValueError("Invalid age")
    return age

try:
    check(-5)
except ValueError as e:
    print(e)
```

8.
```python
import json

data = {"a": True, "b": None}
with open("test.json", "w") as file:
    json.dump(data, file)

with open("test.json", "r") as file:
    print(file.read())
```

9.
```python
def load_data():
    try:
        with open("missing.json", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

print(load_data())
```

10.
```python
tasks = []
tasks.append({"id": 1, "title": "Test"})
print(tasks)
# Program ends here without saving to a file — what happens if you run the program again and read tasks.json?
```

## 19. Debugging Practice

Each snippet has a bug — identify and fix it:

1.
```python
file = open("data.txt", "r")
content = file.read
print(content)
```

2.
```python
with open("output.txt", "w") as file:
    file.write("Saving progress")

with open("output.txt", "w") as file:
    file.write("\nMore progress")
```
(This is meant to *add* a second line without losing the first.)

3.
```python
try:
    number = int(input("Enter number: "))
except:
    print("Something went wrong")
```
(This should specifically catch invalid number input.)

4.
```python
try:
    result = 10 / number
except ZeroDivisionError:
    print("Cannot divide by zero")
print(result)
```
(Assume `number` is `0` — what's wrong with using `result` after the except block?)

5.
```python
def withdraw(balance, amount):
    if amount <= 0:
        return ValueError("Invalid amount")
    return balance - amount
```
(This should actually raise the error, not return it.)

6.
```python
import json

user = {"name": "Akash"}
with open("user.json", "w") as file:
    json.dump(file, user)
```
(Arguments are in the wrong order.)

7.
```python
def load_tasks():
    with open("tasks.json", "r") as file:
        return json.load(file)
```
(This crashes the first time the program runs, before `tasks.json` exists — fix it.)

8.
```python
tasks = [{"id": 1, "title": "Learn Python", "completed": False}]

def complete_task(tasks, task_id):
    for task in tasks:
        if task["id"] = task_id:
            task["completed"] = True
```

9.
```python
try:
    age = int(input("Age: "))
except ValueError:
    print("Invalid age")
else:
    print("Age accepted")
finally
    print("Done")
```

10.
```python
data = {"active": True}
with open("data.json", "w") as file:
    json.dump(data, file)
```
Then someone manually edits `data.json` to say `"active": True` (capital T) instead of `true`. What's wrong with that edit, and what would happen if you tried `json.load()` on it?

## 20. Knowledge Test (No Answers)

1. Why does data stored only in a variable disappear when the program closes?
2. What is the practical difference between `"w"` and `"a"` file modes, and when would you choose each?
3. Why does `with open()` help prevent bugs related to files being left open?
4. What is the difference between a syntax error and an exception, based on how exceptions were described today?
5. Why is it generally better to catch a specific exception (like `ValueError`) instead of using a bare `except:`?
6. When does the `else` block in a try/except statement execute, and why is that useful?
7. What is the purpose of `finally`, and give an example of when you might want code to always run regardless of errors?
8. How does `raise` differ from Python automatically raising an exception (like `ZeroDivisionError`)?
9. What's the difference between a JSON object and a JSON array, in terms of Python equivalents?
10. Why are JSON booleans written differently (`true`/`false`) than Python's (`True`/`False`)?
11. What does `json.dump(data, file, indent=4)` actually do, step by step?
12. Why does `load_tasks()` need a `try`/`except FileNotFoundError` block specifically?
13. Describe the full "persistence workflow" (load → modify → save) in your own words, using the Todo app as an example.
14. Scenario: A user enters `"five"` when your program expects a task ID number. What exception occurs, and how would you handle it gracefully?
15. Scenario: You call `save_tasks(tasks)` before appending a new task instead of after. What would go wrong?
16. Why is JSON described as "not itself an AI agent," even though it appears constantly in agent architectures?
17. Scenario: Your `tools/weather.py` function returns a dictionary. Why might you use `json.dump()` before saving that result to disk?
18. What would happen if you used `"w"` mode inside `save_tasks()` but only ever called it with a partial list of tasks, forgetting to include existing ones?
19. Why might a developer choose to store agent state as JSON rather than just leaving it in a Python variable during a long-running agent process?
20. Scenario: Two different exceptions — `ValueError` and `FileNotFoundError` — could occur in the same `try` block. How would you structure the `except` clauses to handle both distinctly?

## 21. Five-Minute Revision Sheet

- **Persistence:** memory (RAM) disappears on program close; files keep data — workflow is load → modify → save.
- **File modes:** `"r"` read, `"w"` write/overwrite, `"a"` append, `"x"` create new.
- **`with open()`:** preferred — auto-closes the file.
- **`try`/`except`/`else`/`finally`:** try = attempt; except = handle a specific error; else = runs if no error; finally = always runs.
- **`raise`:** intentionally trigger an exception, e.g. for validation.
- **Avoid bare `except:`** — catch specific exceptions instead (`ValueError`, `ZeroDivisionError`, `FileNotFoundError`).
- **JSON:** text-based structured data format; objects `{}` ≈ dicts, arrays `[]` ≈ lists; booleans lowercase (`true`/`false`); `null` ≈ `None`.
- **`json.dump()`:** Python → JSON file. **`json.load()`:** JSON file → Python.
- **Todo app architecture:** `storage.py` (load_tasks/save_tasks) handles persistence; `main.py` handles app logic; `tasks.json` holds the actual data.
- **Agentic AI link:** LLM → Tool → Function → JSON → Storage; JSON is the data format, not the agent itself.

## 22. What I Must Remember

1. Data stored only in variables disappears when the program closes — persistence requires saving to files.
2. `with open()` is the preferred way to work with files because it automatically closes them.
3. `"w"` overwrites existing file content entirely, while `"a"` appends without deleting what's already there.
4. Exceptions are runtime errors; `try`/`except` lets your program handle them gracefully instead of crashing.
5. `else` in a try/except block runs only when no exception occurred; `finally` always runs regardless.
6. `raise` lets you intentionally create your own exceptions, commonly for validation logic.
7. Prefer specific exceptions (`ValueError`, `FileNotFoundError`, `ZeroDivisionError`) over a bare `except:`, which hides real problems.
8. JSON is a text-based format for structured data that closely mirrors Python dictionaries/lists, but with lowercase booleans (`true`/`false`) and `null` instead of `None`.
9. `json.dump()` writes Python data to a JSON file; `json.load()` reads JSON data back into Python.
10. The persistence pattern for real applications is: load data → modify it in memory → save it back to the file.
11. JSON is central to Agentic AI because tool inputs/outputs, API payloads, agent state, and conversation history are all commonly represented as JSON — but JSON itself is just a data format, not the agent's reasoning.
12. A robust application always anticipates missing files (`FileNotFoundError`) and invalid user input (`ValueError`) rather than assuming everything will go right.
