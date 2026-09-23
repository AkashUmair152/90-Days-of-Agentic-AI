# Day 5 — Stage 0: Python Modules, Packages, Virtual Environments, pip, Dependencies, and Project Structure

## 1. Day 5 Overview

Up to now you've written single-file scripts. But a real Agentic AI application eventually needs separate pieces — `agent.py`, `tools.py`, `llm.py`, `memory.py`, `database.py`, `rag.py`, `api.py`, `config.py` — and cramming all of that into one `main.py` quickly becomes an unmanageable 2,000–5,000-line file. Today you learn how real developers organize code: splitting logic into reusable **modules**, grouping related modules into **packages**, isolating each project's dependencies with **virtual environments**, and tracking those dependencies with **pip** and `requirements.txt`. This is the exact organizational skill you'll need the moment your FastAPI, LLM, and agent projects grow beyond a single file.

## 2. Python Modules

- **What a module is:** A Python file that you use as a reusable unit — any `.py` file counts once other code imports from it. For example, `calculator.py` containing:
```python
def add(a, b):
    return a + b

def subtract(a, b):
    return a - b
```

- **`import`:** Brings a whole module into another file so you can use its contents through the module's name.
```python
import calculator

result = calculator.add(10, 20)
print(result)   # 30
```
```
main.py
   ↓
import calculator
   ↓
calculator.py
   ↓
use its functions
```

- **`from ... import ...`:** Imports specific names directly, so you can use them without the module prefix.
```python
from calculator import add

print(add(10, 20))
```

- **Importing multiple functions:**
```python
from calculator import add, subtract

print(add(10, 20))
print(subtract(20, 5))
```

- **Aliases:** Give an imported module (or function) a shorter name using `as`.
```python
import calculator as calc
calc.add(10, 20)

import datetime as dt
dt.datetime.now()
```

- **Why wildcard imports should generally be avoided:**
```python
from calculator import *
```
This imports everything from the module at once. It's understandable to see it as a beginner, but it's discouraged as a habit because it becomes unclear *where* a given function actually came from once your project has many modules. Prefer `from calculator import add` or `import calculator` instead.

## 3. `__name__` and `__main__`

- **`__name__`:** A special built-in variable Python sets automatically for every file. When you run a file *directly*, Python sets `__name__` to `"__main__"` for that file.
```python
if __name__ == "__main__":
    print("Program started")
```
This means: "run this code only when this file is executed directly."

- **Why we need it:** Importing a module executes its top-level code — which is sometimes unwanted. Example:
```python
# calculator.py
def add(a, b):
    return a + b

print("Calculator loaded")
```
```python
# main.py
import calculator
```
Running `main.py` will *also* print `"Calculator loaded"`, because importing runs the module's top-level statements.

- **Fix using `__name__ == "__main__"`:**
```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(10, 20))
```

**Running the file directly:**
```
python calculator.py
```
Output: `30` (the code inside the `if` block runs).

**Importing the file:**
```python
import calculator
```
The `if __name__ == "__main__":` block does **not** run — only the function definitions are made available.

## 4. Python Packages

- **What a package is:** A way of organizing several related modules together inside a folder.
```
project/
│
├── main.py
│
└── tools/
    ├── __init__.py
    ├── calculator.py
    └── weather.py
```
```
tools     → package
calculator.py → module
weather.py    → module
```

- **Importing modules from packages:**
```python
from tools.calculator import add
from tools.weather import get_weather
```
This becomes very useful once your application has many tools organized into their own files.

- **`__init__.py`:** Traditionally, this file tells Python that a directory should be treated as a package. Modern Python has more flexible package behavior, but you'll still encounter `__init__.py` constantly in real projects — for now, just remember it's commonly used to define/configure a Python package. Deeper package mechanics aren't needed yet.

**Agentic AI example:**
```
agent/
│
├── main.py
│
└── tools/
    ├── __init__.py
    ├── calculator.py
    ├── weather.py
    ├── search.py
    └── email.py
```
```python
from tools.calculator import calculate
from tools.weather import get_weather
from tools.search import search
```

## 5. Virtual Environments ⭐⭐⭐

- **Why they exist:** If Project A needs one version of a package and Project B needs a different version, installing everything globally on your computer can cause version conflicts between projects.
- **Dependency isolation:** A virtual environment gives each project its own isolated Python environment and its own set of installed packages, so projects never interfere with each other.
```
Computer
│
├── Project A
│   └── Virtual Environment A
│
└── Project B
    └── Virtual Environment B
```

- **Creating one:**
```
python -m venv .venv
```
This creates a `.venv/` folder inside your project.

- **Activating on Windows:**
```
Command Prompt:
.venv\Scripts\activate

PowerShell:
.venv\Scripts\Activate.ps1
```
After activation, your terminal typically shows `(.venv)` at the start of the prompt.

- **Activating on macOS/Linux:**
```
source .venv/bin/activate
```

- **Deactivating:**
```
deactivate
```

- **Why `.venv` shouldn't usually be committed to Git:** It contains a large number of installed package files specific to your machine/setup — instead, you commit `requirements.txt` (see below) so anyone can recreate the same environment, and you add `.venv/` to `.gitignore`.

## 6. pip

- **What pip is:** Python's package installer — the tool you use to install external libraries into your (usually active) virtual environment.
- **Installing packages:**
```
pip install requests
pip install fastapi
pip install uvicorn
```
- **Checking installed packages:**
```
pip list
pip show requests
```
- **Basic useful commands:** `pip install <package>` to install, `pip list` to see everything installed, `pip show <package>` for details on one package.

## 7. requirements.txt

- **What it is:** A text file listing your project's dependencies, one per line.
```
fastapi
uvicorn
requests
```
- **Why it matters:** Without it, sharing your project with another developer means they have no record of which packages you installed. With `requirements.txt`, they know exactly what's needed.
- **Installing dependencies from it:**
```
pip install -r requirements.txt
```
This installs every package listed in the file in one command.

## 8. .gitignore

- **Why it exists:** To tell Git which files/folders it should *not* track or commit — useful for things that are large, machine-specific, or sensitive.
- **Commonly ignored items:**
```
.venv/
__pycache__/
.env
```
`.venv/` is machine-specific and easily recreated from `requirements.txt`; `__pycache__/` is auto-generated Python bytecode cache; `.env` contains secrets (like API keys) that should never be shared or committed.

## 9. Environment Variables

- **The basic idea:** Values — especially secrets like API keys — are kept outside your source code and loaded at runtime instead.
```
OPENAI_API_KEY=your_key_here
```
- **`.env`:** The file where these values are typically stored locally.
- **API keys:** Credentials that authenticate your requests to services like an LLM provider.
- **Why secrets shouldn't be hard-coded:** Writing `api_key = "sk-xxxxxxxx"` directly in your code risks exposing it if the code is shared, viewed, or committed to Git. The rule to remember for now:
```
Secrets
  ↓
environment variables
  ↓
don't hard-code them
  ↓
don't commit them to Git
```
(Deeper environment-variable management will be covered later.)

## 10. Project Structure

A realistic structure you'll gradually build toward:
```
my-agent/
│
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
├── README.md
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   │
│   ├── agent/
│   │   ├── __init__.py
│   │   └── agent.py
│   │
│   ├── tools/
│   │   ├── __init__.py
│   │   ├── calculator.py
│   │   ├── weather.py
│   │   └── search.py
│   │
│   └── services/
│       ├── __init__.py
│       └── llm.py
│
└── tests/
```

**Separation of responsibilities** — each file/folder has one clear job:
```
main.py      → Application entry point
agent.py     → Agent logic
tools/       → Tools/actions
llm.py       → LLM interaction
memory.py    → Memory/state
database.py  → Database operations
```
This idea is called **separation of concerns** — you don't need to master software architecture yet, but start thinking this way as your projects grow.

**Bad vs Better:**
```
❌ Bad: main.py containing 5,000 lines — LLM code, database, tools, API, agent, everything mixed together

✅ Better: main.py, agent.py, tools.py, llm.py, database.py — each file has a clear job
```

## 11. Agentic AI Connection

```
Function
   ↓
Module
   ↓
Package
   ↓
Application
   ↓
Agentic AI system
```

Modules and packages are how future tools will be organized: `calculator.py`, `weather.py`, `search.py`, `email.py` for tools; `llm.py` for LLM services; `memory.py` for agent memory; `agent.py` for the core agent logic; `database.py` for database code. Each of these can live as its own module inside a `tools/` or `services/` package, instead of being crammed into one giant file — exactly the pattern shown in Section 4's `agent/` example.

## 12. Tool Library Architecture

```
tools/
├── calculator.py
├── weather.py
└── search.py
```
```python
from tools.calculator import calculate
from tools.weather import get_weather
from tools.search import search

tools = {
    "calculator": calculate,
    "weather": get_weather,
    "search": search
}
```
This connects directly to yesterday's tool registry pattern (`tools = {"calculator": calculator, ...}`) — now the actual functions live in their own organized modules inside a `tools/` package instead of all being defined in one file. This is exactly the shape of a future **agent tool registry**: each tool has a clear home, and the registry dictionary simply points to the real function, wherever it's defined.

```
                    AGENT
                      │
          ┌───────────┼───────────┐
          ↓           ↓           ↓
     Calculator    Weather      Search
          │           │           │
          ↓           ↓           ↓
       function     function     function
          │           │           │
          └───────────┼───────────┘
                      ↓
                 Tool Registry
```

## 13. Mental Models

- Module = one reusable Python file.
- Package = organized collection of modules (a folder with `__init__.py`).
- `import` = bring code from another module into this one.
- `from ... import ...` = bring in only specific names.
- Virtual environment = isolated project environment for dependencies.
- pip = Python's package installer.
- `requirements.txt` = a project's dependency list, so others can recreate your setup.
- `if __name__ == "__main__":` = run this part only when this file is the main program.
- `.gitignore` = tells Git what *not* to track (`.venv/`, `__pycache__/`, `.env`).
- Function → Module → Package → Application (the organizational ladder).

## 14. Common Beginner Mistakes

- **Incorrect imports** — mixing up `import calculator` (needs `calculator.add(...)`) with `from calculator import add` (can call `add(...)` directly).
- **Circular imports (basic level)** — two modules trying to import from each other at the same time, which can cause errors; generally avoided by keeping a clear, one-directional structure (e.g., tools don't import from `main.py`).
- **Forgetting to activate the virtual environment** — installing packages or running the project without activating `.venv` first, so packages end up somewhere unexpected (or globally).
- **Installing packages globally** — instead of inside an activated virtual environment, which can cause the version conflicts virtual environments are meant to prevent.
- **Committing `.venv`** — bloats the repository with machine-specific files that should instead be recreated via `requirements.txt`.
- **Committing API keys** — hard-coding secrets or forgetting to add `.env` to `.gitignore`, exposing credentials.
- **Misunderstanding `__main__`** — expecting code inside `if __name__ == "__main__":` to run automatically even when the file is only *imported*, not run directly.
- **Putting everything in one file** — losing the organizational benefits of modules/packages as the project grows.

## 15. Practical Commands

| Command | Purpose |
|---|---|
| `python -m venv .venv` | Create a virtual environment in `.venv/` |
| `.venv\Scripts\activate` (Command Prompt) | Activate the virtual environment (Windows) |
| `.venv\Scripts\Activate.ps1` (PowerShell) | Activate the virtual environment (Windows PowerShell) |
| `source .venv/bin/activate` | Activate the virtual environment (macOS/Linux) |
| `deactivate` | Exit the active virtual environment |
| `pip install <package>` | Install a package into the active environment |
| `pip list` | Show installed packages |
| `pip freeze` | Output installed packages in a requirements-file format (from the lesson's command reference) |
| `pip install -r requirements.txt` | Install every dependency listed in the file |

## 16. Interview Questions

1. **Q: What is a Python module?**
   A: A Python file used as a reusable unit — code from it can be imported and used in other files.

2. **Q: What does `import` do?**
   A: Loads another module so you can access its functions/variables through the module's name.

3. **Q: What's the difference between `import calculator` and `from calculator import add`?**
   A: `import calculator` requires calling functions with the module prefix (`calculator.add(...)`); `from calculator import add` brings `add` in directly, so you call it as `add(...)`.

4. **Q: What is an alias?**
   A: A shorter or renamed reference to an imported module or function, created with `as` (e.g., `import calculator as calc`).

5. **Q: What does this mean: `if __name__ == "__main__":`?**
   A: It means "only run this block of code when this file is executed directly, not when it's imported by another file."

6. **Q: What is a Python package?**
   A: A folder containing related modules, organized together, typically with an `__init__.py` file.

7. **Q: What is the purpose of `__init__.py`?**
   A: Traditionally, it tells Python a directory should be treated as a package; it's commonly used to define/configure the package.

8. **Q: Why do we use virtual environments?**
   A: To isolate each project's dependencies so different projects can use different package versions without conflicting.

9. **Q: What does pip do?**
   A: It's Python's package installer, used to install, list, and manage external libraries.

10. **Q: What is `requirements.txt`?**
    A: A file listing a project's dependencies, so anyone can install the exact same packages with `pip install -r requirements.txt`.

11. **Q: Why should `.venv/` normally be in `.gitignore`?**
    A: It's a large, machine-specific folder that can be recreated from `requirements.txt`, so committing it bloats the repo unnecessarily.

12. **Q: Why shouldn't API keys be hard-coded?**
    A: Hard-coded secrets can leak if the code is shared or committed to version control; they should instead be stored as environment variables (e.g., in `.env`, which is itself gitignored).

13. **Q: Why is separating tools into different modules useful?**
    A: It keeps each tool's logic organized and easy to find/maintain, rather than mixing everything into a single large file — and it maps naturally onto a future tool registry for an agent.

14. **Q: What happens here?**
```python
from tools.calculator import add

result = add(10, 20)
```
    A: It imports the `add` function directly from the `calculator` module inside the `tools` package, then calls it with `10` and `20`, producing `30`.

15. **Q: Explain this architecture:**
```
tools/
├── calculator.py
├── weather.py
└── search.py
```
```python
tools = {
    "calculator": calculate,
    "weather": get_weather,
    "search": search
}
```
    A: Each file in the `tools/` package holds one tool's function(s); the `tools` dictionary maps a tool name (string) to the actual imported function, creating a lookup table — this is the beginning of a tool registry an agent could use to dynamically select and call a tool by name.

## 17. Flashcards

Q: What is a module?
A: A Python file used as a reusable unit of code.

Q: What does `import calculator` let you do?
A: Access its contents via `calculator.function_name(...)`.

Q: What does `from calculator import add` let you do?
A: Call `add(...)` directly, without the module prefix.

Q: Why avoid `from module import *`?
A: It becomes unclear where each imported name actually came from.

Q: What does `import calculator as calc` do?
A: Creates a shorter alias, `calc`, for the `calculator` module.

Q: What is `__name__` set to when a file is run directly?
A: `"__main__"`.

Q: What does `if __name__ == "__main__":` control?
A: Code that should run only when the file is executed directly, not when imported.

Q: What is a package?
A: A folder containing related modules, organized together.

Q: What is `__init__.py` traditionally used for?
A: To mark a directory as a Python package.

Q: Why do virtual environments exist?
A: To isolate each project's dependencies from other projects and the system.

Q: How do you create a virtual environment?
A: `python -m venv .venv`.

Q: How do you activate a virtual environment on Windows (Command Prompt)?
A: `.venv\Scripts\activate`.

Q: How do you deactivate a virtual environment?
A: `deactivate`.

Q: What is pip?
A: Python's package installer.

Q: How do you install a package with pip?
A: `pip install <package_name>`.

Q: What is `requirements.txt` used for?
A: Listing a project's dependencies so others can install the same packages.

Q: How do you install everything listed in `requirements.txt`?
A: `pip install -r requirements.txt`.

Q: What does `.gitignore` do?
A: Tells Git which files/folders not to track or commit.

Q: Why is `.env` usually gitignored?
A: Because it contains secrets like API keys that shouldn't be shared or committed.

Q: What's the organizational ladder from today's lesson?
A: Function → Module → Package → Application → Agentic AI system.

## 18. Code Output Practice

Predict what happens for each (no answers given — verify yourself):

1.
```python
# calculator.py
def add(a, b):
    return a + b

print("Calculator loaded")
```
```python
# main.py
import calculator
print(calculator.add(2, 3))
```
What gets printed, and in what order?

2.
```python
# calculator.py
def add(a, b):
    return a + b

if __name__ == "__main__":
    print(add(5, 5))
```
Running `python calculator.py` directly — what happens?

3. Using the same `calculator.py` from #2, but this time it's imported from another file with `import calculator` — does `add(5, 5)` get printed?

4.
```python
from calculator import add, subtract
print(add(10, 5))
print(subtract(10, 5))
```

5.
```python
import calculator as calc
print(calc.add(1, 1))
```

6.
```python
from tools.calculator import add, multiply
print(add(2, 3))
print(multiply(2, 3))
```

7. If `.venv/` is listed in `.gitignore`, and you run `git status` after creating a virtual environment — will `.venv/` show up as an untracked file to commit?

8. If you run `pip install requests` *without* activating your virtual environment first — where does the package most likely get installed?

9. Given `requirements.txt` containing `fastapi`, `uvicorn`, and `requests`, what command installs all three at once?

10.
```python
tools = {
    "calculator": lambda a, b: a + b
}

tool = tools["calculator"]
print(tool(4, 6))
```
(You haven't formally learned `lambda` yet — just reason about what looking up and calling a function from a dictionary produces.)

## 19. Knowledge Test (No Answers)

1. Why does a large Agentic AI project need to be split across multiple files instead of staying in one `main.py`?
2. What's the practical difference between `import calculator` and `from calculator import add` in terms of how you call the function afterward?
3. Why should wildcard imports (`from module import *`) generally be avoided in real projects?
4. Explain what `__name__ == "__main__"` evaluates to when a file is imported versus when it's run directly.
5. Why might a module print unwanted output when imported, and how does `if __name__ == "__main__":` solve that?
6. What is the practical purpose of a package's `__init__.py` file?
7. Why can installing packages globally (without a virtual environment) cause problems across multiple projects?
8. What steps would you take to create and activate a virtual environment on Windows?
9. Why is `requirements.txt` important when sharing a project with another developer?
10. Why should `.venv/` and `.env` both typically be listed in `.gitignore`, even though they're ignored for different reasons?
11. Scenario: You're building a `tools/` package with `calculator.py`, `weather.py`, and `search.py`. Describe how you would import and register all three functions into a single `tools` dictionary.
12. Scenario: A teammate clones your repository but gets import errors because they're missing several packages. What file should have prevented this, and what command would they run?
13. Scenario: You accidentally hard-coded an API key directly in `main.py` and already committed it to Git. Why is this a problem even if you delete the line afterward, and what should you have done instead from the start?
14. Why does the lesson describe `tools/` as a step toward a future "tool registry" for an agent?
15. Explain, in your own words, the progression: Function → Module → Package → Application → Agentic AI system.

## 20. Five-Minute Revision Sheet

- **Module** = one reusable `.py` file; **Package** = a folder of related modules (commonly with `__init__.py`).
- **`import x`** → use `x.func()`; **`from x import func`** → use `func()` directly; avoid `from x import *`.
- **Alias:** `import x as y` shortens the reference.
- **`if __name__ == "__main__":`** → runs only when the file is executed directly, not when imported.
- **Virtual environment:** isolates a project's dependencies — create with `python -m venv .venv`, activate/deactivate per OS.
- **pip:** `pip install <pkg>`, `pip list`, `pip freeze`.
- **`requirements.txt`:** lists dependencies; install all with `pip install -r requirements.txt`.
- **`.gitignore`:** commonly excludes `.venv/`, `__pycache__/`, `.env`.
- **Secrets:** never hard-code API keys — use environment variables (`.env`), never commit them.
- **Agentic AI link:** Function → Module → Package → Application → Agentic AI system; a `tools/` package + a `tools = {...}` dictionary is the foundation of a future agent tool registry.

## 21. What I Must Remember

1. A module is a reusable Python file; a package is a folder of related modules, commonly marked with `__init__.py`.
2. `import module` requires the module prefix to call functions; `from module import func` lets you call the function directly — avoid `from module import *`.
3. `__name__ == "__main__"` is `True` only when a file is run directly, not when it's imported — use it to prevent unwanted code from running on import.
4. Virtual environments isolate each project's dependencies, preventing version conflicts between projects; create one with `python -m venv .venv` and activate it before installing packages.
5. pip is Python's package installer — `pip install`, `pip list`, and `pip freeze` are the core commands to know.
6. `requirements.txt` lists a project's dependencies so anyone can recreate the same environment with `pip install -r requirements.txt`.
7. `.gitignore` should typically exclude `.venv/`, `__pycache__/`, and `.env` to avoid committing machine-specific files and secrets.
8. API keys and other secrets should be stored as environment variables (e.g., in `.env`) — never hard-coded and never committed.
9. Good project structure separates responsibilities into clear files/folders (e.g., `agent.py`, `tools/`, `llm.py`) rather than putting everything into one giant file — this is called separation of concerns.
10. The organizational ladder Function → Module → Package → Application → Agentic AI system is exactly how a `tools/` package of individual tool functions becomes the foundation of a future agent's tool registry.
