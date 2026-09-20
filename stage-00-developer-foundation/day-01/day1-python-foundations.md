# Day 1 — Stage 0: Python Foundations

## 1. Day 1 Overview

Today you learned the absolute basics of Python: how code runs, `print()`, comments, variables, the four core data types (`str`, `int`, `float`, `bool`), `type()`, strings and f-strings, operators, comparisons, `=` vs `==`, and dynamic typing. None of this is AI yet — but it's the ground floor everything else stands on. Every LLM API call, every FastAPI endpoint, every tool function, and every agent you build later is just variables holding values, functions running operations, and conditions comparing things — so getting these fundamentals solid now means you won't be fighting basic syntax later while trying to also learn agent concepts.

## 2. What is Python?

- **What it is:** Python is a high-level, general-purpose programming language — "high-level" means it reads closer to plain English than to machine code, so you focus on logic rather than low-level details.
- **Why it's useful:** One language covers web development (FastAPI/Django), AI/ML (LLMs, agents), automation (scripts, bots), data (analysis/processing), and backend (APIs, databases).
- **Why it matters for Agentic AI:** Your specific path runs:
```
Python
  ↓
FastAPI
  ↓
LLM APIs
  ↓
Tools
  ↓
Agents
  ↓
RAG
  ↓
Production AI
```
Python is the common thread through every stage of that path.

## 3. How Python Code Runs

```
.py file
   ↓
Python Interpreter
   ↓
Execute Code
   ↓
Output
```

- You write code in a `.py` file (e.g., `hello.py`).
- You run it with `python hello.py`.
- The **Python interpreter** is simply the program that reads your `.py` file and executes it — it understands Python syntax and carries out the instructions line by line. You don't need to know its internals yet, just that it's the thing turning your code into actual behavior.

**Example:**
```python
print("Hello World")
```
Running `python hello.py` prints:
```
Hello World
```

## 4. print()

`print()` displays information on the screen.

**Printing strings:**
```python
print("Hello")
print("Python")
print("Agentic AI")
```
Output:
```
Hello
Python
Agentic AI
```

**Printing numbers:**
```python
print(10)
print(25.5)
```
Output:
```
10
25.5
```

**Printing calculations:**
```python
print(10 + 20)
print(50 - 10)
print(5 * 4)
print(20 / 5)
```
Output:
```
30
40
20
4.0
```
Notice `20 / 5` gives `4.0`, not `4` — regular division (`/`) in Python always returns a float, even when the result is a whole number.

## 5. Comments

- **What they are:** Notes for humans, ignored by Python. Written with `#`.
- **Why useful:** They explain *why* something is done, especially for logic that isn't obvious just from reading the code.
- **Good vs unnecessary:**

Unnecessary (comment adds nothing new):
```python
# Create variable
name = "Ali"

# Print name
print(name)
```

Good (explains the *reasoning*, not just the action):
```python
# Price includes a 10% service charge
total = price * 1.10
```

## 6. Variables

- **What a variable is:** A name you give to a value so you can refer to it later.
```python
name = "Ali"
age = 25
```
Simple mental model:
```
name → "Ali"
age  → 25
```

- **More accurate mental model:** Rather than "a variable is a box that stores a value," think of a variable as **a name/reference associated with an object/value**. `name` doesn't physically contain `"Ali"` — it *refers to* the object `"Ali"`. You don't need Python's memory model in depth yet; just remember a variable gives you a name to refer to a value.

- **Changing variables:**
```python
age = 25
print(age)

age = 26
print(age)
```
Output:
```
25
26
```

- **Using variables in calculations:**
```python
price = 100
quantity = 3

total = price * quantity
print(total)
```
Output: `300`. This is clearer than writing `print(100 * 3)` because the variable names tell you what the numbers mean.

## 7. Python Data Types

| Type | Meaning | Example |
|---|---|---|
| `str` | Text | `name = "Akash"` |
| `int` | Whole number | `age = 25` |
| `float` | Decimal number | `price = 99.99` |
| `bool` | True / False | `is_logged_in = True` |

Note capitalization: Python booleans are `True` and `False` (capital first letter), not `true`/`false`.

## 8. type()

`type()` tells you the data type of a value.
```python
name = "Akash"
age = 25
price = 99.99
is_student = True

print(type(name))
print(type(age))
print(type(price))
print(type(is_student))
```
Output:
```
<class 'str'>
<class 'int'>
<class 'float'>
<class 'bool'>
```
This is very useful for **debugging** — when something behaves unexpectedly (e.g., a calculation fails or a comparison doesn't work), checking the type of a value quickly shows if it's the type you assumed (a common bug is a number being stored as a string, like `"100"` instead of `100`).

## 9. Strings

- Strings are text, and can be written with single or double quotes — both work:
```python
name = "Akash"
name = 'Akash'
```
- **Concatenation** (joining strings with `+`):
```python
first_name = "Akash"
last_name = "Umair"

full_name = first_name + " " + last_name
print(full_name)
```
Output: `Akash Umair`

- **f-strings ⭐** — the preferred way to build strings with variables inside them. Instead of:
```python
print("My name is " + name + " and I am " + str(age))
```
use:
```python
print(f"My name is {name} and I am {age} years old.")
```
Output: `My name is Akash and I am 25 years old.`

f-strings matter a lot going forward — you'll use them constantly to build prompts, format API responses, and construct messages when working with LLM APIs and FastAPI.

## 10. Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `+` | Addition | `10 + 5` | `15` |
| `-` | Subtraction | `10 - 5` | `5` |
| `*` | Multiplication | `10 * 5` | `50` |
| `/` | Division | `10 / 5` | `2.0` |
| `//` | Floor division | `10 // 3` | `3` |
| `%` | Modulo (remainder) | `10 % 3` | `1` |
| `**` | Power | `2 ** 3` | `8` |

**`/` vs `//`:** `/` always returns a float (e.g., `10 / 3` → `3.3333...`), while `//` (floor division) divides and rounds *down* to the nearest whole number, discarding the remainder (`10 // 3` → `3`).

## 11. Comparison Operators

| Operator | Meaning |
|---|---|
| `==` | Equal to |
| `!=` | Not equal to |
| `>` | Greater than |
| `<` | Less than |
| `>=` | Greater than or equal to |
| `<=` | Less than or equal to |

Comparisons always produce `True` or `False`:
```python
10 == 10   # True
10 != 5    # True
10 > 5     # True
10 < 5     # False
10 >= 10   # True
10 <= 10   # True
```

## 12. = vs ==

This trips up almost every beginner, so make it automatic:

- **`=` → Assignment** — "put/reference this value using this name."
```python
age = 25   # age now refers to 25
```
- **`==` → Comparison** — "is this equal to that?"
```python
age == 25   # Is age equal to 25? → True or False
```

**Rule:** `=` assigns, `==` compares. Never mix them up — using `=` where you meant `==` (or vice versa) is one of the most common early Python bugs.

## 13. Dynamic Typing

Python is **dynamically typed**, meaning you don't have to declare a value's type manually:
```python
age = 25          # Python figures out this is an int
```
instead of something like `int age = 25` (as in some other languages).

A name can even be reassigned to a different type entirely:
```python
value = 10
value = "hello"   # now value refers to a string
```

**Type hints (a future topic):** Python also supports optional type hints like:
```python
age: int = 25
name: str = "Akash"
```
These make code easier to read and maintain, but you don't need to worry about them today — they'll come up later.

## 14. Agentic AI Connection

Today's basics map directly onto what you'll build soon:

- **LLM applications:** f-strings build the prompts you send to an LLM — `f"Explain {topic} to a beginner."`
- **FastAPI:** Variables and data types define request/response data (e.g., a `str` for a user's question, an `int` for a count).
- **Tools:** Tool functions take typed inputs (`int`, `str`, etc.) and return values — exactly like the `calculator(a, b)` style functions from Lesson 1.
- **Agents:** The agent's "state" is really just a set of variables being updated as the loop runs.
- **APIs:** Every API call/response you handle is just data stored in variables, checked with `type()`, and formatted with f-strings.
- **RAG:** Comparing values (`==`, `>`) and counting things (like tokens) are basic operations behind filtering and ranking retrieved documents.
- **Automation:** Simple scripts chaining variables, operators, and conditions are the backbone of automation workflows (similar in spirit to what you've already done in n8n/Make/Zapier, but now in code).

**Example connecting today to tokens (from Lesson 2):**
```python
input_tokens = 1500
output_tokens = 500
total_tokens = input_tokens + output_tokens

print(f"Total tokens: {total_tokens}")
```

## 15. Mental Models

- Variable = a name referring to a value/object.
- `=` assigns, `==` compares.
- `str` = text.
- `int` = whole number.
- `float` = decimal number.
- `bool` = True or False (capitalized).
- `/` always gives a float; `//` floors the result to a whole number.
- `%` gives you the remainder of a division.
- `type()` tells you what kind of value you're dealing with — use it when debugging.
- f-strings (`f"{variable}"`) are the standard way to build text with variables inside.

## 16. Common Beginner Mistakes

- **Confusing `=` and `==`** — remember: `=` assigns, `==` compares.
- **Forgetting quotes around strings** — `name = Akash` is invalid; it must be `name = "Akash"`.
- **Treating `"100"` as an integer** — `"100"` is a `str` because of the quotes, even though it looks like a number; use `type()` to confirm.
- **Incorrect f-string syntax** — forgetting the `f` prefix (`print("{name}")` won't substitute the variable) or forgetting curly braces around the variable name.
- **Confusing `/` and `//`** — `/` gives a float result, `//` gives a floored whole number.
- **Using unclear variable names** — `x = 100` tells you nothing; `price = 100` is self-explanatory.

## 17. Code Examples

```python
# Hello World
print("Hello, Agentic AI!")

# Comments
# Price includes a 10% service charge
total = price * 1.10

# Variables
name = "Ali"
age = 25
print(name)
print(age)

# Using variables in calculations
price = 100
quantity = 3
total = price * quantity
print(total)

# Data types
name = "Akash"       # str
age = 25              # int
price = 99.99         # float
is_student = True     # bool

# type()
print(type(name))
print(type(age))

# String concatenation
full_name = "Akash" + " " + "Umair"
print(full_name)

# f-strings
print(f"My name is {name} and I am {age} years old.")

# Operators
print(10 + 5)
print(10 / 3)     # 3.3333...
print(10 // 3)    # 3
print(10 % 3)     # 1
print(2 ** 3)     # 8

# Comparisons
print(10 == 10)   # True
print(10 != 5)    # True

# = vs ==
age = 25          # assignment
print(age == 25)  # comparison → True

# Dynamic typing
value = 10
value = "hello"
print(type(value))
```

## 18. Interview Questions

1. **Q: What is Python?**
   A: A high-level, general-purpose programming language used for web development, AI/ML, automation, data processing, and backend systems.
   *Deeper:* "High-level" means it abstracts away low-level machine details, letting developers focus on logic and readability.

2. **Q: What is a variable?**
   A: A name used to refer to a value.
   *Deeper:* More precisely, a variable is a name/reference associated with an object — it doesn't "contain" the value like a box, it points to it.

3. **Q: What's the difference between `=` and `==`?**
   A: `=` assigns a value to a name; `==` compares two values and returns `True` or `False`.

4. **Q: What are `str`, `int`, `float`, and `bool`?**
   A: The four basic data types covered today — text, whole numbers, decimal numbers, and True/False values respectively.

5. **Q: What does `type()` do?**
   A: It returns the data type of a given value, which is very useful for debugging unexpected behavior.

6. **Q: What's the difference between `10 / 3` and `10 // 3`?**
   A: `/` performs regular division and returns a float (`3.333...`); `//` performs floor division and returns the whole number result rounded down (`3`).

7. **Q: Why are f-strings useful?**
   A: They let you embed variables directly inside a string using `{}`, which is cleaner and less error-prone than concatenating with `+`.
   *Deeper:* This becomes essential later for building prompts and formatting API/tool outputs.

8. **Q: What does this code produce?**
```python
x = 10
x = 20
print(x)
```
   A: `20` — reassigning `x` makes it refer to the new value, replacing the old reference.

9. **Q: What type is `"100"`? Is it an int?**
   A: It's a `str`, not an `int`, because it's wrapped in quotes — Python treats it as text, not a number.

10. **Q: Explain what this code does:**
```python
name = "Akash"
age = 25
print(f"{name} is {age} years old.")
```
    A: It creates two variables, then uses an f-string to build and print the sentence "Akash is 25 years old." by substituting the variable values directly into the string.

## 19. Flashcards

Q: What is a variable?
A: A name that refers to a value/object.

Q: What does `=` do?
A: Assigns a value to a name.

Q: What does `==` do?
A: Compares two values and returns True or False.

Q: What is `str`?
A: A text data type.

Q: What is `int`?
A: A whole number data type.

Q: What is `float`?
A: A decimal number data type.

Q: What is `bool`?
A: A True/False data type.

Q: What does `type()` do?
A: Returns the data type of a value.

Q: What does `/` return?
A: A float result (regular division).

Q: What does `//` return?
A: A floored whole number result (floor division).

Q: What does `%` return?
A: The remainder of a division.

Q: What is an f-string?
A: A string prefixed with `f` that lets you embed variables using `{}`.

Q: Is Python statically or dynamically typed?
A: Dynamically typed — you don't declare types manually, and a name can refer to different types over time.

Q: What does the Python interpreter do?
A: Reads and executes your Python code.

Q: What does `print()` do?
A: Displays information on the screen.

## 20. Knowledge Test (No Answers)

1. What is Python, and name two areas it's commonly used for besides AI?
2. What is the difference between a variable "storing" a value versus "referring to" a value?
3. What will `print(20 / 5)` output, and why does it look the way it does?
4. What is the output of the following code?
```python
x = 5
x = "five"
print(type(x))
```
5. What's the difference between `10 % 3` and `10 // 3`?
6. Why is `"100"` not the same as `100` in Python?
7. What is the output of the following code?
```python
price = 50
quantity = 4
print(f"Total: {price * quantity}")
```
8. Explain the difference between `=` and `==` using an example of each.
9. Why might a beginner mistakenly think `age = 25` and `age == 25` do the same thing, and why don't they?
10. What is one reason `type()` is useful when debugging a Python program?

## 21. Five-Minute Revision Sheet

- **Interpreter:** reads and runs your `.py` file → produces output.
- **`print()`:** displays text, numbers, or calculation results.
- **Comments (`#`):** notes for humans; explain *why*, not the obvious.
- **Variable:** a name referring to a value (`name = "Ali"`).
- **Data types:** `str` (text), `int` (whole number), `float` (decimal), `bool` (True/False).
- **`type()`:** reveals a value's data type — key debugging tool.
- **f-strings:** `f"Hello {name}"` — the standard way to build strings with variables.
- **Operators:** `+ - * /` basic math; `//` floors; `%` gives remainder; `**` is power.
- **`/` vs `//`:** `/` → float; `//` → floored whole number.
- **Comparisons (`== != > < >= <=`):** always produce `True`/`False`.
- **`=` vs `==`:** `=` assigns, `==` compares.
- **Dynamic typing:** no manual type declarations; a name can be reassigned to any type.

## 22. What I Must Remember

1. Python is a high-level, general-purpose language used across web dev, AI, automation, data, and backend work.
2. The Python interpreter reads and executes your `.py` files.
3. `print()` displays strings, numbers, and calculation results.
4. Comments explain reasoning, not the obvious — don't over-comment simple lines.
5. A variable is a name that refers to a value/object, not a "box" containing it.
6. The four core data types today are `str`, `int`, `float`, and `bool`.
7. `type()` reveals a value's data type and is essential for debugging.
8. f-strings (`f"{variable}"`) are the standard, preferred way to build strings with embedded values.
9. `/` always returns a float; `//` floors the result; `%` returns the remainder; `=` assigns while `==` compares.
10. Python is dynamically typed — you never declare types manually, and a name can be reassigned to a different type.
