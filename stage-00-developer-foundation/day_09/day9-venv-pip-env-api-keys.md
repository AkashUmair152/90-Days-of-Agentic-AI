# Day 9 — Stage 0: Python Virtual Environments, pip, Dependencies, .env Files, Environment Variables, API Keys, and Git Security

## 1. Day 9 Overview

So far, working in Python has mostly meant "write code, run code." Real AI development adds several more layers: an isolated **environment** so dependencies don't conflict between projects, **packages** installed via pip, **configuration** (like model names) kept separate from code, and **secrets** (like API keys) that must never appear in source code or Git history. Getting comfortable with this now matters enormously, because the moment you connect Python to a real LLM API, database, or FastAPI service, you'll be handling credentials — and a developer who knows how to configure a project safely is far better prepared than one who only knows how to call an API.

## 2. Virtual Environments

- **What it is:** An isolated Python environment created specifically for one project.
```
Computer
│
├── Project A
│   └── Virtual Environment A
│       ├── FastAPI
│       └── Pydantic
│
├── Project B
│   └── Virtual Environment B
│       ├── Django
│       └── Requests
│
└── Project C
    └── Virtual Environment C
        └── AI packages
```
- **Why it's needed:** If Project A needs `requests 2.x` and Project B needs `requests 3.x`, installing everything globally creates a conflict — Python wouldn't know which version to use. A virtual environment gives each project its own isolated dependencies.
- **Project isolation:** Each project's packages live only inside that project's own environment, with no interference between projects.
- **`.venv`:** A common naming convention for the folder holding the virtual environment (you might also see `venv`, `env`, or `environment` used, but `.venv` is a very common modern convention).
- **Creating one:**
```
python -m venv .venv
```
This produces a `.venv/` folder inside your project.
- **Activating on Windows:**
```
PowerShell:
.venv\Scripts\Activate.ps1

Command Prompt:
.venv\Scripts\activate
```
After activation, your terminal typically shows `(.venv)` at the start of the prompt.
- **Deactivating:**
```
deactivate
```
The `(.venv)` indicator should disappear.

**Mental model:** Virtual environment = private Python workspace for one project.
```
activate   → use project environment
deactivate → leave project environment
```

## 3. pip

- **What pip is:** Python's package installer — the tool that downloads and installs Python packages.
- **Installing packages:**
```
pip install requests
```
- **`pip list`:** Shows all currently installed packages in the active environment:
```
Package      Version
------------ -------
pip          ...
requests     ...
```
- **`pip show`:** Shows details about a specific installed package:
```
pip show requests
```

## 4. Python Packages

A **package** is reusable code written by other developers, so you don't have to build everything (an HTTP client, JSON utilities, a web framework, database libraries, an AI SDK) from scratch yourself.

**Examples relevant to AI development** you'll encounter:
```
fastapi
uvicorn
pydantic
requests
httpx
python-dotenv
openai
```
Later you'll encounter many more AI-related packages as your projects grow.

## 5. requirements.txt

- **Why it exists:** If your project uses `requests`, `fastapi`, `pydantic`, and `python-dotenv`, and you send the project to another developer, they need to install the exact same dependencies. Instead of listing them manually one by one, you record them in a single file.
- **`pip freeze`:** Generates a list of installed packages (with versions) and writes it to a file:
```
pip freeze > requirements.txt
```
Example content:
```
requests==...
```
(Your actual versions will depend on what you've installed.)
- **`pip install -r requirements.txt`:** Installs every package listed in the file — telling pip "install everything listed here."
- **Reproducible environments:** With `requirements.txt`, someone else (or you, on a new machine) can recreate the exact environment needed to run the project.

**Mental model:**
```
requirements.txt
      ↓
Project's shopping list
      ↓
Python packages
```

**Why this matters for Agentic AI:** A future agent project might require FastAPI, Pydantic, an OpenAI SDK, a database library, and an environment-variable library — `requirements.txt` means you don't have to manually remember and reinstall each one every time.

## 6. Environment Variables

- **What they are:** Values (often configuration or secrets) provided by the operating system to a running program, rather than being written directly into the source code.
```
Operating System
      ↓
Environment Variable
      ↓
Python Application
```
- **Why configuration should be separated from source code:** Hard-coding a key like `api_key = "sk-something-secret"` risks exposing it if the code is ever shared or committed — this is described as something you should **never** do in code you intend to share or commit.
- **`os.getenv()`:**
```python
import os

api_key = os.getenv("OPENAI_API_KEY")
```
This means: "get the value of the `OPENAI_API_KEY` environment variable."
- **Default values:** `os.getenv()` can take a fallback value used when the variable isn't set:
```python
port = os.getenv("PORT", "8000")
```
If `PORT` isn't defined, `port` becomes `"8000"`.
- **Checking a required variable exists:**
```python
import os

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")
```
This is better than letting the application fail later in a confusing, unclear way.

## 7. .env Files

- **What `.env` is:** A local file used to store configuration and secrets for local development.
```
OPENAI_API_KEY=your_real_key_here
```
⚠️ Never put a real key into code examples, screenshots, GitHub, or messages you share with others.
- **Why it's useful in local development:** It keeps configuration values out of your actual code files, in one central, easily-managed local file.
- **`python-dotenv`:** A package that lets Python read values from a `.env` file.
```
pip install python-dotenv
```
- **`load_dotenv()`:**
```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
```
Now Python can read values defined in your local `.env` file.

**How it works:**
```
.env
 │
 │ load_dotenv()
 ↓
Environment
 │
 │ os.getenv()
 ↓
Python application
```

**Example:**
```
# .env
APP_NAME=AgenticAI
DEBUG=True
OPENAI_API_KEY=your_key_here
```
```python
import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
debug = os.getenv("DEBUG")
api_key = os.getenv("OPENAI_API_KEY")

print(app_name)   # AgenticAI
print(debug)      # True
# Never print the actual API key
```

**Important — environment variables are always strings:** `DEBUG=True` in `.env` gives you the *string* `"True"`, not the boolean `True`. Likewise, `PORT=8000` gives `"8000"`, not the integer `8000`. Convert when needed:
```python
port = int(os.getenv("PORT", "8000"))
```

## 8. API Keys and Secrets

- **What an API key is:** A credential (like `API_KEY=xxxxxxxxxxxxxxxx`) your application needs to authenticate with an external service, such as an AI provider's API.
- **Why API keys are sensitive:** They grant access to an account/service — anyone who has your key can use it as if they were you.
- **Why they should never be hard-coded:** Writing `api_key = "sk-something-secret"` directly in code that gets shared or committed (e.g., pushed to GitHub) exposes the secret to anyone who can view that code.
- **What happens if a secret is exposed:** Potential consequences include unauthorized API usage, unexpected charges, account compromise, and other security problems.
- **Key rotation/revocation:** If a real API key is ever accidentally committed, simply deleting the line later is **not enough** — the key may still exist in Git's history. The correct response generally is: (1) revoke/rotate the exposed key, (2) remove the secret from the repository/history as appropriate, (3) replace it with a new secret.

**Golden Rule:** Never hard-code API keys or other secrets into source code.

## 9. .gitignore

- **What it does:** Tells Git which files/folders it should not track or commit.
```
.env
.venv/
__pycache__/
```
- **Why `.env` should normally be ignored:** It contains local configuration and secrets that should never be pushed to a shared repository.
- **Why `.venv` should normally be ignored:** It contains many installed environment files that don't need to be committed — instead, `requirements.txt` describes what needs to be installed, and anyone can recreate the environment from that.
- **`__pycache__`:** An auto-generated folder of Python bytecode cache files, also commonly excluded since it's regenerated automatically and isn't meaningful to track.

## 10. .env vs requirements.txt

| | `.env` | `requirements.txt` |
|---|---|---|
| **Contains** | Configuration/secrets (`OPENAI_API_KEY=...`, `DATABASE_URL=...`, `DEBUG=True`) | Python package dependencies (`fastapi==...`, `python-dotenv==...`, `requests==...`) |
| **Answers the question** | "What configuration does my app need?" | "What Python packages does my app need?" |
| **Should be committed to Git?** | No — normally in `.gitignore` | Yes — this one *should* be committed |

## 11. Configuration Architecture

```
Source Code
     ↓
Configuration
     ↓
Environment
     ↓
API Keys / Model / Database
```
The core principle: your application's *logic* (source code) should be separate from its *configuration* (API keys, model names, database URLs), and that configuration should be read from the environment rather than written directly into the code.

## 12. Professional Project Structure

```
day-09/
│
├── .venv/
│
├── .env
├── .gitignore
├── requirements.txt
│
└── main.py
```
Conceptually, this separates:
```
Code + Dependencies + Configuration + Secrets
```
Each piece has its own clear place: `main.py` (and other `.py` files) hold logic; `requirements.txt` records dependencies; `.env` holds configuration/secrets locally (and is gitignored); `.venv/` is the isolated environment (also gitignored).

A more complete configuration setup adds `config.py`:
```python
# config.py
import os
from dotenv import load_dotenv

load_dotenv()

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
```
```python
# main.py
from config import OPENAI_API_KEY

if not OPENAI_API_KEY:
    raise ValueError("OPENAI_API_KEY is not configured")
```
This keeps configuration logic in one separate, reusable place. An even more reusable version wraps it in a function:
```python
import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured")
    return api_key
```

## 13. Agentic AI Connection

```
Agent
 │
 ├── LLM
 │
 ├── Tools
 │
 ├── Memory
 │
 └── Configuration
        │
        ├── API keys
        ├── Model name
        └── Database URL
```
You don't want an agent whose API key is hardcoded directly into its logic:
```
Agent
 │
 └── API KEY HARDCODED 😨
```
Instead, you want:
```
Agent
 │
 └── Configuration
       ↓
   Environment
```
API keys, model names, and database URLs should never be hard-coded because: they're sensitive (keys), they change between environments (a model name might differ between development and production), and separating them keeps your agent's core logic clean, portable, and safe to share.

**The bigger picture forming:**
```
                 AI APPLICATION
                       │
          ┌────────────┼────────────┐
          ↓            ↓            ↓
         LLM          Tools       Memory
          │            │            │
          └────────────┼────────────┘
                       ↓
                 Configuration
                       │
              ┌────────┼────────┐
              ↓        ↓        ↓
           API Key   Model    Database
```
Today covers how that bottom "Configuration" layer works — the foundation for safely connecting Python to a real LLM API soon.

## 14. Security Rules

- **Never hard-code API keys** — always read them from environment variables (`.env` locally, platform secrets in production).
- **Never commit `.env`** — always add it to `.gitignore` before it ever gets a chance to be tracked.
- **Never expose secrets in logs** — never `print(api_key)`; instead print whether it exists (`bool(api_key)`), not the value itself.
- **Rotate/revoke exposed keys** — if a real secret is ever committed, deleting the line isn't enough; the key must be revoked/rotated because it may remain in Git history.
- **Use environment/configuration systems** — keep secrets and configuration in `.env`/environment variables, read through functions like `os.getenv()`, and validate that required values exist before use.

## 15. Practical Code Examples

```python
# Basic os.getenv()
import os
api_key = os.getenv("OPENAI_API_KEY")

# load_dotenv() + os.getenv()
from dotenv import load_dotenv
import os

load_dotenv()
app_name = os.getenv("APP_NAME")

# Checking a required environment variable
import os

api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("OPENAI_API_KEY is not set")

# Default environment values
port = os.getenv("PORT", "8000")

# Type conversion
port = int(os.getenv("PORT", "8000"))

# A reusable configuration function
import os
from dotenv import load_dotenv

load_dotenv()

def get_openai_api_key() -> str:
    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OPENAI_API_KEY is not configured")
    return api_key

api_key = get_openai_api_key()

# Printing safely (never print the key itself)
print(f"API Key configured: {bool(api_key)}")
```

## 16. Common Beginner Mistakes

- **Forgetting to activate the virtual environment** — installing packages or running the project without `(.venv)` active, so packages don't end up where expected.
- **Installing packages globally by accident** — running `pip install` without activating the project's virtual environment first.
- **Confusing `.env` and `requirements.txt`** — `.env` holds configuration/secrets; `requirements.txt` holds package dependencies. They serve entirely different purposes.
- **Committing `.env`** — forgetting to add it to `.gitignore` before the first commit, exposing secrets.
- **Printing API keys** — using `print(api_key)` for debugging, which leaks the secret into logs/terminal output.
- **Assuming environment variables are automatically typed** — expecting `os.getenv("DEBUG")` to return a boolean or `os.getenv("PORT")` to return an integer, when both actually return strings.
- **Forgetting to install `python-dotenv`** — trying to use `load_dotenv()` without first running `pip install python-dotenv`.
- **Committing `.venv`** — accidentally tracking the entire virtual environment folder in Git instead of relying on `requirements.txt`.

## 17. Mental Models

- `.venv` = private Python workspace for one project.
- pip = Python's package installer.
- `requirements.txt` = the project's dependency shopping list.
- `.env` = local configuration/secrets.
- `os.getenv()` = read a configuration value from the environment.
- `load_dotenv()` = load `.env` values into the environment so `os.getenv()` can see them.
- `.gitignore` = tells Git what not to track.
- Environment variables are always strings — convert when you need another type.
- `pip freeze > requirements.txt` = capture your current installed packages into a file.
- `pip install -r requirements.txt` = recreate someone else's (or your own) environment.
- API key = a secret credential — treat it like a password.
- Never hard-code secrets; never print secrets.
- If a secret leaks, rotate it — don't just delete the line.
- Source Code → Configuration → Environment → API Keys/Model/Database.
- A developer who configures projects safely is more valuable than one who only knows how to call an API.

## 18. Interview Questions

1. **Q: What problem does a virtual environment solve?**
   A: It isolates a project's dependencies so different projects can use different package versions without conflicting with each other.

2. **Q: What command creates a virtual environment?**
   A: `python -m venv .venv`.

3. **Q: How do you activate a virtual environment on Windows?**
   A: `.venv\Scripts\Activate.ps1` in PowerShell, or `.venv\Scripts\activate` in Command Prompt.

4. **Q: What does pip do?**
   A: It's Python's package installer, used to install, list, and manage external libraries.

5. **Q: What is a Python package?**
   A: Reusable code written by other developers that you can install instead of building the same functionality yourself.

6. **Q: What is `requirements.txt`?**
   A: A file listing a project's Python dependencies (and typically their versions), so anyone can reinstall the exact same setup.

7. **Q: What does `pip freeze > requirements.txt` do?**
   A: Captures the currently installed packages (and versions) into the `requirements.txt` file.

8. **Q: What does `pip install -r requirements.txt` do?**
   A: Installs every package listed in that file.

9. **Q: What is an environment variable?**
   A: A configuration value provided by the operating system to a running program, rather than being hard-coded into the source code.

10. **Q: Why shouldn't API keys be hard-coded?**
    A: If the code is ever shared or committed, the secret becomes exposed, risking unauthorized use, unexpected charges, or account compromise.

11. **Q: What does `os.getenv("OPENAI_API_KEY")` do?**
    A: Reads the value of the `OPENAI_API_KEY` environment variable, returning `None` if it isn't set.

12. **Q: What is `.env` used for?**
    A: Storing local configuration and secrets for development, separate from the source code.

13. **Q: What package lets Python load `.env` values during local development?**
    A: `python-dotenv`, via its `load_dotenv()` function.

14. **Q: Why should `.env` normally be in `.gitignore`?**
    A: Because it contains secrets/configuration that should never be pushed to a shared or public repository.

15. **Q: What's the difference between `.env` and `requirements.txt`?**
    A: `.env` holds configuration/secrets for the app; `requirements.txt` holds the Python package dependencies needed to run it.

16. **Q: Why shouldn't `.venv` normally be committed to Git?**
    A: It contains a large number of installed environment files that can be recreated from `requirements.txt`, so committing it is unnecessary and bloats the repository.

17. **Q: What does `os.getenv("PORT", "8000")` mean?**
    A: Read the `PORT` environment variable, and if it isn't set, default to the string `"8000"`.

18. **Q: Why might you need `int(os.getenv("PORT", "8000"))` instead of just `os.getenv("PORT", "8000")`?**
    A: Because environment variables are always returned as strings, so you need to explicitly convert to `int` if you need a numeric value.

19. **Q: If a real API key is accidentally committed to GitHub, why isn't simply deleting the line enough?**
    A: The key may still exist in the repository's Git history, remaining exposed even after the current version of the file no longer shows it — so the key should be revoked/rotated.

20. **Q: Explain this architecture:**
```
Agent → Configuration → Environment Variables → API Key / Model / Database
```
    A: An agent's configuration (like which API key, model, or database to use) is read from environment variables rather than hard-coded, keeping the agent's core logic separate from sensitive or environment-specific values.

21. **Q: Why is `requirements.txt` described as making a project "reproducible"?**
    A: Because anyone can install the exact same dependencies the project needs, recreating a working environment without guesswork.

22. **Q: What's a safer alternative to `print(api_key)` for debugging whether a key was loaded?**
    A: `print(f"API Key configured: {bool(api_key)}")` — this confirms the key exists without exposing its value.

23. **Q: Why does the lesson recommend raising a `ValueError` when a required environment variable is missing?**
    A: So the application fails clearly and immediately, instead of failing later in a confusing, hard-to-diagnose way.

24. **Q: What's the conceptual difference between how `.env` is used locally versus in production?**
    A: Locally, `.env` plus `python-dotenv` loads configuration; in production, cloud platforms typically provide their own environment-variable/secrets settings, but the application still reads values the same way via `os.getenv()`.

25. **Q: Why is understanding configuration and secrets management considered foundational before building agents?**
    A: Because a future agent's LLM, tools, and memory all depend on configuration (API keys, model names, database URLs) that must be handled safely — skipping this foundation risks building agents around insecure, hard-coded secrets.

## 19. Flashcards

Q: What is a virtual environment?
A: An isolated Python environment for one project.

Q: What command creates a virtual environment?
A: `python -m venv .venv`.

Q: How do you deactivate a virtual environment?
A: `deactivate`.

Q: What is pip?
A: Python's package installer.

Q: What does `pip list` show?
A: All currently installed packages.

Q: What does `pip show <package>` do?
A: Shows details about a specific installed package.

Q: What is a Python package?
A: Reusable code written by other developers that you can install and use.

Q: What does `pip freeze > requirements.txt` do?
A: Saves the currently installed packages and versions into `requirements.txt`.

Q: What does `pip install -r requirements.txt` do?
A: Installs every package listed in that file.

Q: What is an environment variable?
A: A configuration value provided by the OS/environment rather than hard-coded in source code.

Q: What does `os.getenv("KEY")` return if `KEY` isn't set?
A: `None` (unless a default value is given).

Q: What is `.env` used for?
A: Storing local configuration/secrets for development.

Q: What package loads `.env` values into the environment?
A: `python-dotenv`.

Q: What function loads a `.env` file?
A: `load_dotenv()`.

Q: What type does `os.getenv()` always return the value as?
A: A string.

Q: How do you convert an environment variable to an integer?
A: Wrap it with `int()`, e.g. `int(os.getenv("PORT", "8000"))`.

Q: What does `.gitignore` do?
A: Tells Git which files/folders not to track.

Q: Why should `.env` be in `.gitignore`?
A: To prevent secrets from being committed to the repository.

Q: Why should `.venv/` be in `.gitignore`?
A: It's recreatable from `requirements.txt` and doesn't need to be tracked.

Q: What's the golden rule about API keys in source code?
A: Never hard-code them.

Q: What should you do instead of `print(api_key)`?
A: Print whether it exists, e.g. `bool(api_key)`, not the value itself.

Q: If a real API key leaks into Git history, is deleting the line enough?
A: No — the key may still exist in history; it should be revoked/rotated.

Q: What does `requirements.txt` primarily describe?
A: The Python packages a project depends on.

Q: What does `.env` primarily describe?
A: The configuration/secrets a project needs.

Q: What is the "configuration architecture" chain from today's lesson?
A: Source Code → Configuration → Environment → API Keys/Model/Database.

Q: Why validate a required environment variable and raise an error if missing?
A: So failures happen clearly and immediately, not confusingly later.

Q: What's an example of a package relevant to AI development mentioned today?
A: `fastapi`, `pydantic`, `python-dotenv`, `openai`, `requests`, `httpx`, `uvicorn`.

Q: What does "reproducible environment" mean?
A: Someone else can recreate the exact dependencies needed to run your project.

Q: Should `.env` values ever be assumed to already be the "correct" Python type?
A: No — they're always strings and must be explicitly converted if another type is needed.

Q: What symbol typically shows a virtual environment is active in the terminal?
A: `(.venv)` at the start of the prompt.

Q: Why is keeping configuration separate from code described as important for agents specifically?
A: Because an agent's LLM, tools, and memory all rely on configuration (API keys, model, database) that must stay safe, portable, and not hard-coded.

## 20. Command Practice

1. Create a virtual environment named `.venv` in your current project folder.
2. Activate that virtual environment using PowerShell.
3. Activate that virtual environment using Command Prompt.
4. Deactivate the currently active virtual environment.
5. Install the `requests` package using pip.
6. Install both `python-dotenv` and `requests` in a single command.
7. List all currently installed packages in the active environment.
8. Show detailed information about the installed `requests` package.
9. Generate a `requirements.txt` file from your currently installed packages.
10. Install all dependencies listed in an existing `requirements.txt` file.
11. Create a new virtual environment for a fresh project called `day-09-practice`, activate it, then check the Python version.
12. After activating a virtual environment and installing a package, deactivate it, then reactivate it and confirm the package is still listed.
13. Create a `.gitignore` file that excludes `.venv/`, `.env`, and `__pycache__/`.
14. Create a `.env` file containing `APP_NAME`, `ENVIRONMENT`, and `API_KEY`, then write Python code that reads and prints all three (without printing the real key value).
15. Simulate checking whether your project is safely ignoring `.env` by running `git status` after adding it to `.gitignore` (assuming the folder is a Git repository).

## 21. Security Practice

For each scenario, decide: is the developer's approach **safe** or **unsafe**? (Reasoning is up to you — answers aren't given here.)

1. A developer writes `api_key = "sk-abc123..."` directly inside `main.py` for local testing, planning to remove it before committing.
2. A developer stores their API key in a `.env` file and adds `.env` to `.gitignore` before their first commit.
3. A developer runs `print(api_key)` temporarily to debug a connection issue, then removes the line before pushing to GitHub.
4. A developer commits `.venv/` to Git so teammates don't have to reinstall packages themselves.
5. A developer accidentally pushes a real API key to a public repository, then simply deletes the line in a new commit and considers the issue resolved.
6. A developer keeps `requirements.txt` in version control but excludes `.env` from it.
7. A developer uses `os.getenv("API_KEY")` and raises a `ValueError` if it's missing, rather than letting the app silently use `None`.
8. A developer hardcodes a placeholder value like `"test-key"` directly in `.env` for local development only, without ever committing `.env`.
9. A developer shares a screenshot of their terminal in a public forum to ask for help, and the screenshot shows their `.env` file's contents, including a real key.
10. A developer's `config.py` reads `OPENAI_API_KEY` from the environment and never logs or prints its actual value anywhere in the codebase.

## 22. Debugging Practice

Each scenario/snippet has a problem — diagnose and fix it:

1.
```python
import os
api_key = os.getenv(OPENAI_API_KEY)
```

2.
```python
from dotenv import load_dotenv
api_key = os.getenv("OPENAI_API_KEY")
```
(Missing something before reading the variable.)

3. A developer runs `pip install python-dotenv` but forgets to activate `.venv` first — later, `from dotenv import load_dotenv` fails with a `ModuleNotFoundError` when running the project. What likely went wrong?

4.
```python
port = os.getenv("PORT", "8000")
server.run(port=port)
```
(The server expects an integer port number and fails.)

5. A `.gitignore` file contains:
```
venv/
```
but the project's virtual environment folder is actually named `.venv/`. What's the problem?

6.
```python
def get_api_key():
    api_key = os.getenv("OPENAI_API_KEY")
    return api_key
```
(This function should raise an error if the key is missing, but currently doesn't.)

7. A developer's `requirements.txt` file is empty even though several packages are installed. What command did they likely forget to run correctly?

8. A teammate clones the repository and runs the project, but it crashes immediately with `OPENAI_API_KEY is not configured`. What two files should they check/create locally?

9.
```python
# .env
DEBUG=True
```
```python
debug = os.getenv("DEBUG")
if debug:
    print("Debug mode is on")
```
(This always prints "Debug mode is on," even if someone sets `DEBUG=False` — why?)

10. A developer wants to share their project on GitHub. They've created `.gitignore` with `.env` listed, but they had already committed `.env` in an earlier commit before creating `.gitignore`. What's the issue, and why won't `.gitignore` alone fix it?

## 23. Knowledge Test (No Answers)

1. Why does installing packages globally (without a virtual environment) risk conflicts between projects?
2. What is the practical difference between `pip list` and `pip show <package>`?
3. Why is `requirements.txt` important when handing a project to another developer?
4. What's the difference between what `.env` stores versus what `requirements.txt` stores?
5. Why are environment variables always returned as strings by `os.getenv()`, and what problem can that cause if you forget to convert them?
6. Why should `.env` never be committed to Git, even for a private repository?
7. Why should `.venv/` typically be excluded from Git as well, even though it's not exactly a "secret"?
8. Explain, step by step, what happens when you run `load_dotenv()` followed by `os.getenv("OPENAI_API_KEY")`.
9. Why is raising a `ValueError` for a missing required environment variable better than letting the app continue with `None`?
10. Scenario: You accidentally commit `.env` containing a real API key, then delete the line and commit again. Why is the key still considered compromised?
11. What are the three general steps recommended when a secret is accidentally exposed?
12. Why should you generally avoid `print(api_key)` even temporarily, and what's a safer alternative for debugging?
13. Explain the configuration architecture chain: Source Code → Configuration → Environment → API Keys/Model/Database.
14. Why does the lesson describe local development (`.env`) and production (platform secrets) as conceptually similar even though the mechanism differs?
15. Scenario: A future agent needs an API key, a model name, and a database URL. Why should none of these be hard-coded directly into the agent's class or functions?
16. What's the purpose of a dedicated `config.py` file, and how does it differ from scattering `os.getenv()` calls throughout your codebase?
17. Why might `get_openai_api_key()` (a function) be considered more reusable than a bare module-level variable like `OPENAI_API_KEY = os.getenv(...)`?
18. Scenario: Your `.env` contains `PORT=8000`, but your code does `port = os.getenv("PORT", "8000")` and later tries `port + 1`. What happens, and how would you fix it?
19. Why is `.gitignore` alone insufficient to protect a secret that was already committed in an earlier commit?
20. What's the difference between installing a package while a virtual environment is active versus while it's not active?
21. Scenario: Two projects on the same machine need different versions of `fastapi`. How does a virtual environment solve this?
22. Why does the lesson emphasize that a developer who configures projects safely is "better prepared" than one who only knows how to call an LLM API?
23. What does it mean for an environment to be "reproducible," and why does that matter for team collaboration?
24. Scenario: You're deploying your project to a cloud platform instead of running it locally. How does your code's use of `os.getenv()` change, if at all?
25. Why is it good practice to print `bool(api_key)` instead of the key itself when verifying configuration during setup?

## 24. Five-Minute Revision Sheet

- **Virtual environment:** isolates a project's dependencies — `python -m venv .venv`, activate/deactivate per OS.
- **pip:** `pip install <pkg>`, `pip list`, `pip show <pkg>`.
- **`requirements.txt`:** `pip freeze > requirements.txt` to create it; `pip install -r requirements.txt` to install from it — makes environments reproducible.
- **Environment variables:** configuration read from the OS/environment, not hard-coded; always strings — convert with `int()`, etc. when needed.
- **`.env` + `python-dotenv`:** `.env` holds local config/secrets; `load_dotenv()` loads them; `os.getenv("KEY")` reads them, with an optional default.
- **`.gitignore`:** exclude `.env`, `.venv/`, `__pycache__/` — secrets and recreatable/generated files don't belong in Git.
- **`.env` vs `requirements.txt`:** configuration/secrets vs. package dependencies — very different purposes.
- **Never hard-code or print secrets.** If a real key leaks, rotate/revoke it — deleting the line isn't enough.
- **Configuration architecture:** Source Code → Configuration → Environment → API Keys/Model/Database.
- **Agentic AI link:** an agent's LLM, tools, and memory rely on configuration (API keys, model, database) that must be handled through environment variables, never hard-coded.

## 25. What I Must Remember

1. A virtual environment isolates a project's dependencies, preventing version conflicts between different projects on the same machine.
2. `python -m venv .venv` creates a virtual environment; it must be activated before installing packages for that project.
3. pip is Python's package installer — `pip install`, `pip list`, and `pip show` are the core commands to know.
4. `requirements.txt` records a project's dependencies (`pip freeze > requirements.txt`) so anyone can recreate the same environment (`pip install -r requirements.txt`).
5. Environment variables keep configuration and secrets out of source code, and are always returned as strings by `os.getenv()` — convert them explicitly when another type is needed.
6. `.env` files (loaded via `python-dotenv`'s `load_dotenv()`) are the standard way to manage local configuration and secrets during development.
7. `.gitignore` should exclude `.env`, `.venv/`, and `__pycache__/` — secrets should never be committed, and recreatable environment files don't need to be tracked.
8. `.env` and `requirements.txt` serve very different purposes: one holds configuration/secrets, the other holds Python package dependencies.
9. API keys and other secrets should never be hard-coded into source code, and never printed — always read them from the environment and check their existence safely.
10. If a real secret is accidentally committed to Git, deleting the line is not enough — the key must be revoked/rotated, since it may remain in Git history.
11. The configuration architecture Source Code → Configuration → Environment → API Keys/Model/Database is the foundation for safely building any real AI application, including future agents.
12. A future agent's LLM, tools, memory, and configuration (API keys, model name, database URL) must be kept separate from hard-coded values — today's practices are the groundwork for that.
