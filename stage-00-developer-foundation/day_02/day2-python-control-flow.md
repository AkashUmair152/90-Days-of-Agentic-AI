# Day 2 — Stage 0: Python Control Flow

## 1. Day 2 Overview

**Control flow** is how a program makes decisions and repeats work, instead of just running top to bottom. Without it, a program can only ever do one fixed sequence of actions — with `if`/`elif`/`else` it can choose different paths depending on conditions, and with `for`/`while` it can repeat an action over many items or until something changes. This matters hugely for Agentic AI because agents constantly need to decide things ("does this need a tool?"), process collections ("go through each document/task"), and retry ("keep trying until this succeeds") — all of which are built directly on the conditions and loops you're learning today.

## 2. if Statements

- **`if`:** Runs a block of code only when a condition is true.
```python
age = 20

if age >= 18:
    print("You are an adult")
```
- **Conditions:** An expression that evaluates to `True` or `False` (e.g., `age >= 18`, or just a boolean variable like `is_logged_in`).
- **Boolean expressions:** Conditions don't have to be comparisons — a variable that's already `True`/`False` works directly:
```python
is_logged_in = True

if is_logged_in:
    print("Welcome!")
```
- **Indentation ⭐:** Python uses indentation (conventionally 4 spaces) to define which code belongs to the `if`. This is not optional style — it's required syntax.

Correct:
```python
if age >= 18:
    print("Adult")
```
Incorrect (will cause an error):
```python
if age >= 18:
print("Adult")
```
Think of it as:
```
if condition:
    └── code belonging to if
```

## 3. else

`else` runs when the `if` condition is false — it's the "otherwise" branch.
```python
age = 15

if age >= 18:
    print("Adult")
else:
    print("Minor")
```
```
age >= 18?
   ↓
 ┌───┴───┐
YES     NO
 ↓       ↓
Adult   Minor
```
Use `else` whenever you need a fallback action for "everything that isn't the `if` case."

## 4. elif

`elif` ("else if") lets you check multiple possibilities in sequence.
```python
score = 75

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs improvement")
```
**Evaluation order:** Python checks conditions **top to bottom** and stops at the *first* one that's true — it never evaluates the rest after that.

**Why order matters:** If you write broader conditions first, they can accidentally "steal" cases meant for later branches:
```python
score = 95

if score >= 70:
    print("C")
elif score >= 90:
    print("A")
```
This prints `C`, even though 95 should logically be an "A" — because `95 >= 70` is already true, so Python never even checks `>= 90`. **Fix:** put the more specific/higher thresholds first:
```python
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
```

## 5. Logical Operators

| Operator | Meaning | Example | Result |
|---|---|---|---|
| `and` | ALL conditions must be true | `True and False` | `False` |
| `or` | AT LEAST ONE must be true | `True or False` | `True` |
| `not` | Reverses the Boolean | `not True` | `False` |

**`and` truth table:**
```
True  and True   → True
True  and False  → False
False and True   → False
False and False  → False
```
Example:
```python
age = 25
has_ticket = True

if age >= 18 and has_ticket:
    print("You can enter")
```

**`or` truth table:**
```
True  or False  → True
False or True   → True
False or False  → False
```
Example:
```python
is_admin = False
is_manager = True

if is_admin or is_manager:
    print("Access granted")
```

**`not`:**
```
not True  → False
not False → True
```
Example:
```python
is_logged_in = False

if not is_logged_in:
    print("Please log in")
```

## 6. Nested Conditions

You can put an `if` inside another `if`:
```python
age = 25
has_id = True

if age >= 18:
    if has_id:
        print("Entry allowed")
```
**When to avoid unnecessary nesting:** If the nested condition can be expressed as a single combined condition, prefer that — it's simpler to read:
```python
if age >= 18 and has_id:
    print("Entry allowed")
```
Rule of thumb: reach for `and`/`or` before reaching for nested `if`s, whenever the logic allows it.

## 7. for Loops

**What it is:** A `for` loop repeats a block of code once for each item in a sequence (like a range of numbers or a list), instead of writing the same line over and over.
```python
for i in range(5):
    print("Hello")
```
Output:
```
Hello
Hello
Hello
Hello
Hello
```

**`range()` forms:**

| Form | Meaning | Example | Output |
|---|---|---|---|
| `range(stop)` | 0 up to (not including) stop | `range(5)` | `0 1 2 3 4` |
| `range(start, stop)` | start up to (not including) stop | `range(1, 6)` | `1 2 3 4 5` |
| `range(start, stop, step)` | start up to stop, increasing by step | `range(0, 11, 2)` | `0 2 4 6 8 10` |

**The stop value is always excluded** — `range(5)` produces `0, 1, 2, 3, 4` (5 numbers total), stopping *before* 5. This is worth memorizing explicitly since it trips up almost everyone at first.

**Loop variable name:** It can be anything meaningful, not just `i`:
```python
for number in range(5):
    print(number)
```

**Iterating over a list:**
```python
names = ["Ali", "Ahmed", "Sara"]

for name in names:
    print(name)
```
Output:
```
Ali
Ahmed
Sara
```
This pattern — process each item in a collection — becomes essential later for looping through documents, search results, API responses, database records, tools, and files.

## 8. while Loops

**What it does:** A `while` loop keeps running *as long as* its condition stays true.
```python
count = 1

while count <= 5:
    print(count)
    count += 1
```
Output:
```
1
2
3
4
5
```
```
count <= 5?
    ↓
  YES
    ↓
 execute
    ↓
 update count
    ↓
 check again
```

**Updating variables:** The loop must change something that affects the condition (like `count += 1`) — otherwise the condition never becomes false.

**Infinite loops ⚠️:** If you forget to update the variable, the condition stays true forever:
```python
count = 1

while count <= 5:
    print(count)   # count never changes → runs forever
```

**How to avoid them:** Always make sure something inside the loop moves the condition toward becoming false (e.g., incrementing a counter, changing a flag, or shrinking a list).

## 9. break and continue

```
break
 ↓
STOP THE LOOP ENTIRELY

continue
 ↓
SKIP THIS ITERATION, KEEP LOOPING
```

**`break`** — exits the loop immediately:
```python
for number in range(10):
    if number == 5:
        break
    print(number)
```
Output:
```
0
1
2
3
4
```

**`continue`** — skips just the current iteration and moves to the next:
```python
for number in range(5):
    if number == 2:
        continue
    print(number)
```
Output:
```
0
1
3
4
```

## 10. Agentic AI Connection

Today's tools become the decision and repetition logic inside future agent code:

- **`if`** → deciding which action or tool fits a request, e.g. conceptually: `if user_wants_weather: use_weather_tool()`.
- **`for`** → processing multiple items in one go, e.g. `for task in tasks: process_task(task)`, or looping through a list of documents/search results.
- **`while`** → repeating until a condition changes, e.g. `while not task_completed: try_again()` — the basic shape behind retry logic.
- **`break`** → stopping a process early once a goal is met (e.g., stop retrying once a tool call finally succeeds).
- **`continue`** → skipping an item that doesn't need processing (e.g., skipping an empty or invalid document while looping through a batch).

**Important:** a plain `if` statement by itself does **not** make something an agent. These are just the basic building blocks (decisions, repetition, control) that agent logic is built out of — an actual agent additionally needs the LLM making the decision dynamically, tools, a loop, and state, as covered in Lesson 1. Today's constructs are the *plumbing*, not the agent itself.

## 11. Mental Models

- `if` = decision.
- `for` = repeat for each item.
- `while` = repeat while condition is true.
- `break` = leave the loop entirely.
- `continue` = skip this round, keep going.
- `and` = ALL conditions must be true.
- `or` = AT LEAST ONE condition must be true.
- `not` = reverse the Boolean.
- `range(stop)` always excludes the stop value.
- Indentation isn't style — it's what defines a block in Python.

## 12. Common Beginner Mistakes

- **Indentation errors** — forgetting to indent code under `if`, `for`, or `while`, which causes a syntax error.
- **Incorrect condition ordering** — putting a broad `elif` (like `>= 70`) before a more specific one (like `>= 90`), so the specific case never gets reached.
- **Infinite while loops** — forgetting to update the variable that the `while` condition depends on.
- **Confusing `break` and `continue`** — `break` stops the whole loop; `continue` only skips the current iteration and keeps looping.
- **Incorrect `range()` expectations** — assuming `range(5)` includes 5, when it actually stops right before it.
- **Forgetting that `range()`'s stop value is excluded** — `range(1, 6)` gives `1, 2, 3, 4, 5`, not up to 6.

## 13. Code Examples

```python
# if / elif / else
score = 85

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("Needs improvement")

# Logical operators
age = 25
has_ticket = True
if age >= 18 and has_ticket:
    print("You can enter")

is_admin = False
is_manager = True
if is_admin or is_manager:
    print("Access granted")

is_logged_in = False
if not is_logged_in:
    print("Please log in")

# for loop with range
for number in range(1, 6):
    print(number)

# for loop with step
for number in range(0, 11, 2):
    print(number)

# for loop over a list
names = ["Ali", "Ahmed", "Sara"]
for name in names:
    print(name)

# while loop
count = 1
while count <= 5:
    print(count)
    count += 1

# break
for number in range(10):
    if number == 5:
        break
    print(number)

# continue
for number in range(5):
    if number == 2:
        continue
    print(number)
```

## 14. Interview Questions

1. **Q: What is control flow?**
   A: The mechanism that lets a program make decisions and repeat actions instead of always running the same sequence of instructions top to bottom.

2. **Q: What's the difference between `if`, `elif`, and `else`?**
   A: `if` checks the first condition; `elif` checks additional conditions if the earlier ones were false; `else` runs when none of the previous conditions were true.
   *Deeper:* Python evaluates them top to bottom and stops at the first true condition, skipping the rest.

3. **Q: Why does indentation matter in Python?**
   A: Indentation defines which lines belong to a block (like inside an `if` or loop) — it's required syntax, not just a style choice.

4. **Q: What does this produce?**
```python
for i in range(5):
    print(i)
```
   A: `0 1 2 3 4`, each on its own line, since `range(5)` produces 0 through 4 and excludes 5.

5. **Q: What does `range(2, 10, 2)` represent?**
   A: Numbers starting at 2, up to (but excluding) 10, increasing by 2 each time — so `2, 4, 6, 8`.

6. **Q: What's the difference between `for` and `while`?**
   A: `for` repeats over a known sequence of items (like a range or list); `while` repeats as long as a condition stays true, which may be an unknown number of times.

7. **Q: What's the difference between `break` and `continue`?**
   A: `break` exits the loop entirely; `continue` skips only the current iteration and continues with the next one.

8. **Q: What does `and` mean in a condition?**
   A: All the combined conditions must be true for the overall expression to be true.

9. **Q: What does `or` mean in a condition?**
   A: At least one of the combined conditions must be true for the overall expression to be true.

10. **Q: What's wrong with this code?**
```python
count = 1

while count <= 5:
    print(count)
```
    A: `count` is never updated inside the loop, so `count <= 5` stays true forever — it's an infinite loop.

## 15. Flashcards

Q: What does `if` do?
A: Runs code only when its condition is true.

Q: What does `else` do?
A: Runs when the `if` (and any `elif`) conditions were false.

Q: What does `elif` do?
A: Checks another condition if the previous ones were false.

Q: In what order does Python check `if`/`elif` conditions?
A: Top to bottom, stopping at the first true one.

Q: What does `and` require?
A: All combined conditions to be true.

Q: What does `or` require?
A: At least one combined condition to be true.

Q: What does `not` do?
A: Reverses a Boolean value.

Q: What does `for number in range(5):` loop over?
A: The numbers 0, 1, 2, 3, 4.

Q: Does `range()`'s stop value get included?
A: No — it's always excluded.

Q: What does a `while` loop need to avoid running forever?
A: Something inside it that eventually makes the condition false.

Q: What does `break` do?
A: Immediately exits the loop.

Q: What does `continue` do?
A: Skips the current iteration and moves to the next one.

Q: What defines a code block in Python?
A: Indentation.

Q: Can you loop through a list directly with `for`?
A: Yes — `for item in my_list:` processes each item in order.

Q: Does a plain `if` statement make something an "agent"?
A: No — it's just a basic building block; a real agent needs an LLM deciding dynamically, tools, a loop, and state.

## 16. Code Output Practice

Predict the output of each snippet before running it (no answers given — check yourself):

1.
```python
x = 12
if x > 10:
    print("Big")
else:
    print("Small")
```

2.
```python
score = 60
if score >= 90:
    print("A")
elif score >= 70:
    print("C")
else:
    print("F")
```

3.
```python
for i in range(3):
    print(i)
```

4.
```python
for i in range(2, 9, 3):
    print(i)
```

5.
```python
names = ["Sara", "Ali"]
for name in names:
    print(f"Hi {name}")
```

6.
```python
count = 3
while count > 0:
    print(count)
    count -= 1
```

7.
```python
for number in range(5):
    if number == 3:
        break
    print(number)
```

8.
```python
for number in range(5):
    if number == 3:
        continue
    print(number)
```

9.
```python
a = True
b = False
print(a and b)
print(a or b)
print(not a)
```

10.
```python
x = 5
if x > 1 and x < 10:
    print("In range")
elif x >= 10:
    print("Too big")
```

## 17. Knowledge Test (No Answers)

1. What is control flow, and why does a program need it?
2. Why does Python require consistent indentation inside `if` blocks and loops?
3. Explain, in your own words, why condition order matters in an `if`/`elif` chain.
4. What values does `range(3, 12, 3)` produce?
5. Write (in words) the difference between a `for` loop and a `while` loop in terms of when you'd choose each.
6. What specifically causes an infinite `while` loop, and how do you prevent one?
7. If a loop needs to stop entirely once a certain item is found, would you use `break` or `continue`? Why?
8. If a loop needs to skip just one specific item but keep processing the rest, would you use `break` or `continue`? Why?
9. Scenario: You're processing a list of 10 tasks with a `for` loop, and one task is invalid and should be skipped without stopping the rest. Which control-flow tool fits, and how would you use it?
10. Scenario: You want an agent-like script to keep retrying a tool call until it succeeds, but stop after it works. Which loop type fits best, and why?

## 18. Five-Minute Revision Sheet

- **Control flow** = decisions (`if`/`elif`/`else`) + repetition (`for`/`while`).
- **`if`/`elif`/`else`:** checked top to bottom, stops at first true condition — order matters, put specific/high thresholds first.
- **Indentation** defines code blocks — required, not optional.
- **`and`** = all true; **`or`** = at least one true; **`not`** = reverse the Boolean.
- **Nested `if`** works, but prefer combining conditions with `and`/`or` when possible.
- **`for`** loops over a known sequence (range or list); **`while`** loops while a condition holds.
- **`range(stop)` / `range(start, stop)` / `range(start, stop, step)`** — stop value is always excluded.
- **`while` loops** need something inside them that changes the condition, or they run forever.
- **`break`** = stop the loop entirely; **`continue`** = skip this iteration only.
- **Agentic AI link:** `if` = tool/action decisions, `for` = processing multiple items, `while` = retries — but these alone are not an agent.

## 19. What I Must Remember

1. Control flow lets a program make decisions (`if`/`elif`/`else`) and repeat work (`for`/`while`) instead of running the same fixed sequence every time.
2. `if`/`elif`/`else` conditions are checked top to bottom, and Python stops at the first one that's true.
3. Condition order matters — broad conditions placed before specific ones can accidentally block the specific ones from ever running.
4. Indentation in Python defines code blocks and is required syntax, not just style.
5. `and` requires all conditions to be true; `or` requires at least one; `not` reverses a Boolean.
6. Prefer combining conditions with `and`/`or` over deeply nested `if` statements when the logic allows it.
7. `for` loops iterate over a known sequence (like `range()` or a list); `range()`'s stop value is always excluded.
8. `while` loops repeat as long as a condition is true, and must update something inside the loop to avoid running forever (an infinite loop).
9. `break` stops a loop entirely; `continue` skips only the current iteration and keeps looping.
10. These constructs are the basic building blocks used in agent logic (deciding on tools, processing tasks, retrying) — but a plain `if`/`for`/`while` alone does not make something an "agent."
