# Day 11 — Stage 0: REST APIs, API Design, Authentication, OpenAPI, Swagger UI, Postman, and Building APIs with FastAPI

## 1. Day 11 Overview

Yesterday you learned how a Python program *calls* an API. Today goes one level deeper: how APIs are *designed*, *documented*, and *secured*. This matters because your future AI agents won't only consume APIs someone else built — you will also build APIs, turn them into agent tools, authenticate with external services, document your own tools, and debug problems when things go wrong. REST conventions, authentication, and documentation are exactly the skills that separate "I can call an API" from "I can design and ship one an agent can safely use."

## 2. REST

- **What REST means:** Representational State Transfer. Don't worry about the name — for now, think: **REST is a set of conventions for designing web APIs.**
- **REST as a design style/convention:** it's not a strict law, but a widely followed pattern for organizing how APIs expose functionality.
- **Resources:** A REST-style API organizes information around **resources** — the "things" it manages (see Section 3).
- **URLs:** identify *which* resource you're working with.
- **HTTP methods:** identify *what operation* you want to perform on that resource.

## 3. REST Resources

A **resource** is a thing your API manages. Examples:
```
users
tasks
products
orders
messages
documents
agents
tools
```
A todo application's resources might be `/tasks` and `/users`.

**Collection vs individual resource:**
```
/tasks     → the collection of tasks
/tasks/10  → one specific task
```
This distinction matters throughout REST design — a plural path with no ID refers to *all* of something; the same path with an ID refers to *one* specific item.

## 4. REST + CRUD

| Operation | HTTP Method | Example |
|---|---|---|
| Create | POST | `POST /tasks` — create a task |
| Read | GET | `GET /tasks`, `GET /tasks/10` — give me tasks / one task |
| Update | PUT / PATCH | `PATCH /tasks/10` — update a task |
| Delete | DELETE | `DELETE /tasks/10` — delete a task |

**REST task API example:**
```
Get all tasks    → GET    /tasks
Get one task     → GET    /tasks/10
Create a task    → POST   /tasks
Update a task    → PATCH  /tasks/10
Delete a task    → DELETE /tasks/10
```

## 5. API Endpoint Design

**Bad (less REST-like) — verbs baked into the URL:**
```
/getAllTasks
/createTask
/deleteTask
/updateTask
```

**Better (REST-style) — nouns in the URL, verbs expressed by the HTTP method:**
```
GET    /tasks
POST   /tasks
PATCH  /tasks/10
DELETE /tasks/10
```

**Why:** the HTTP method describes the action; the URL identifies the resource.
```
HTTP method = what I want to do
URL         = what I want to do it to
```

**Products example:**
```
GET    /products       → get products
GET    /products/25    → get product 25
POST   /products       → create a product
PATCH  /products/25    → update product 25
DELETE /products/25    → delete product 25
```

**API naming:** use nouns (`/users`, `/tasks`, `/products`), not verbs (`/getUsers`, `/createTask`, `/deleteProduct`).

## 6. Nested Resources

Sometimes resources are related to each other. Examples:
```
GET /users/10/orders     → orders belonging to user 10
GET /projects/5/tasks    → tasks belonging to project 5
```
Nesting expresses a relationship (this order belongs to this user; this task belongs to this project). The lesson notes: don't overuse nesting, but you'll see this pattern often.

## 7. HTTP Status Codes

| Code | Meaning | When you'd see it |
|---|---|---|
| **200** | OK | A GET request succeeded |
| **201** | Created | A POST successfully created a resource |
| **204** | No Content | The request succeeded but there's nothing to return (e.g., after DELETE) |
| **400** | Bad Request | The request itself was invalid |
| **401** | Unauthorized | Authentication problem — "I don't know who you are" |
| **403** | Forbidden | Authorization problem — "I know who you are, but you can't do this" |
| **404** | Not Found | The requested resource doesn't exist |
| **422** | Unprocessable Content | Request data failed validation (common in FastAPI) |
| **500** | Internal Server Error | Something went wrong on the server |

**204 No Content — worth learning specifically today:** it means the request succeeded, but there is no response body to return. A common example is `DELETE /tasks/10` — the server deletes the task and doesn't need to send back any JSON.

## 8. Authentication vs Authorization

These two are often confused.

- **Authentication:** *Who are you?*
- **Authorization:** *What are you allowed to do?*

**Example:**
```
Authentication: "I am Akash."
Authorization:  "Akash is allowed to read these documents."
```

**Memory trick:**
```
Authentication → WHO?
Authorization  → WHAT CAN THEY DO?
```

**Why APIs need authentication:** you wouldn't want just anyone to call `DELETE /accounts/123` on a banking API without proving who they are. AI APIs may also require authentication because requests can consume paid resources.

## 9. API Keys

- **What they are:** A common authentication mechanism — a secret value (e.g., `API_KEY=secret_value`) the client sends to prove who it is.
- **How they're sent:** the exact format depends on the API — for example:
```
Authorization: Bearer YOUR_API_KEY
```
or:
```
X-API-Key: YOUR_API_KEY
```
**Never assume the authentication format** — some APIs use `Authorization: Bearer ...`, others use `X-API-Key: ...`, others use different systems entirely. Always read the API documentation.
- **Why they're secrets, and why they must not be hard-coded:** exactly as in Day 9 — read them from environment variables, never write them directly into code:
```python
import os

api_key = os.getenv("API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}"
}

response = requests.get(url, headers=headers, timeout=10)
```

## 10. Bearer Tokens

```
Authorization: Bearer TOKEN
```
```
Authorization
      ↓
   Bearer
      ↓
   Token
```
The token is proof that the client has valid credentials — think of it as a temporary key that says "I've already authenticated." Treat tokens as secrets, exactly like API keys. (Deeper systems like OAuth, which manage how these tokens are issued and refreshed, aren't covered yet.)

## 11. API Documentation

Now imagine someone hands you an API URL with no explanation. How would you know what endpoints exist, what methods to use, what parameters to send, what headers are required, what JSON body is expected, or what the responses look like? You read the **API documentation.**

Good API documentation typically includes:
```
Endpoint
Method
Parameters
Headers
Request body
Response
Errors
Authentication
Examples
```
Example:
```
POST /tasks

Request:
{ "title": "Learn APIs" }

Response:
{ "id": 1, "title": "Learn APIs", "completed": false }
```

**API documentation is a contract** between the API provider and the API consumer — it tells you how to communicate correctly:
```
API Provider
     ↕
API Consumer
```

## 12. OpenAPI

**OpenAPI** is a standard for describing APIs — you'll hear this term constantly with FastAPI. It can describe endpoints, methods, parameters, request bodies, responses, authentication, and schemas. This machine-readable description can then power documentation and testing tools (like Swagger UI, below).

## 13. Swagger UI

**Swagger UI** is an interactive documentation/testing interface, generated automatically from an API's OpenAPI description. FastAPI generates this for you automatically — usually accessible at `/docs`.

```
See endpoints
     ↓
Choose endpoint
     ↓
Enter parameters
     ↓
Click "Execute"
     ↓
See response
```

**FastAPI's `/docs`:**
```python
from fastapi import FastAPI

app = FastAPI()
```
Running the app and visiting `/docs` shows something like:
```
GET    /tasks
POST   /tasks
GET    /tasks/{task_id}
PATCH  /tasks/{task_id}
DELETE /tasks/{task_id}
```
This is one reason FastAPI is so valuable for your Agentic AI journey — documentation comes essentially for free.

**Important distinction — Swagger UI is not the API itself:**
```
Your API
    ↓
OpenAPI specification
    ↓
Swagger UI
```
Swagger UI is an *interface* for exploring/testing the API; the actual API is your HTTP endpoints.

## 14. Postman

**Postman** is a general-purpose tool for manually sending HTTP requests — instead of writing `requests.get(...)` in Python, you use a GUI to specify method, URL, headers, query parameters, and body, then send the request.

**Why it matters — debugging:**
```
Python application → ❌
```
You can test the same request in Postman:
```
Postman → API
```
- If Postman works but your Python code doesn't → the problem is likely in your Python client.
- If Postman also fails → the problem is likely the API/server/request itself.
This makes isolating bugs much easier.

**Swagger UI vs Postman:**

| | Swagger UI | Postman |
|---|---|---|
| **Generated from** | Your API's own OpenAPI specification | Not tied to any specific API — general purpose |
| **Best for** | Exploring/testing your own documented endpoints | Testing any API, saving requests/collections, general debugging |

## 15. FastAPI REST API

**Day 11 project — Agent Tool API:**
```
day-11/
│
├── .venv/
├── requirements.txt
└── main.py
```
Install: `pip install fastapi uvicorn`

**Create the app:**
```python
from fastapi import FastAPI

app = FastAPI(
    title="Agent Tool API",
    description="A simple API for Agentic AI practice"
)
```

**In-memory data (temporary — a real database comes later):**
```python
tasks = [
    {"id": 1, "title": "Learn APIs", "completed": False},
    {"id": 2, "title": "Build an AI tool", "completed": False}
]
```

**GET all tasks:**
```python
@app.get("/tasks")
def get_tasks():
    return tasks
```
Run with `uvicorn main:app --reload`, then open `/docs` to see the endpoint.

**GET one task:**
```python
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    return {"error": "Task not found"}
```
`GET /tasks/1` returns `{"id": 1, "title": "Learn APIs", "completed": false}`.

**⚠️ The problem:** if the task doesn't exist, the code above returns `{"error": "Task not found"}` with a *successful* HTTP status (200) unless explicitly changed — that's not correct API design. It should return `404 Not Found` (see Section 17).

**POST — create a task**, using Pydantic for input validation (Section 16):
```python
@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    new_task = {
        "id": len(tasks) + 1,
        "title": task.title,
        "completed": False
    }
    tasks.append(new_task)
    return new_task
```
**What happens:**
```
Client sends POST /tasks with {"title": "Learn Agents"}
 ↓
JSON → Pydantic → TaskCreate → Python object
 ↓
Create task
 ↓
JSON response
```

**PATCH — update a task:**
```python
@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = task_update.completed
            return task

    raise HTTPException(status_code=404, detail="Task not found")
```

**DELETE:**
```python
@app.delete("/tasks/{task_id}", status_code=204)
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return

    raise HTTPException(status_code=404, detail="Task not found")
```

**Architecture so far:**
```
                FastAPI
                   │
       ┌───────────┼───────────┐
       ↓           ↓           ↓
     GET          POST        PATCH
   /tasks        /tasks      /tasks/1
       │           │           │
       └───────────┼───────────┘
                   ↓
                 tasks
```

## 16. Pydantic

Pydantic models describe the *shape* of incoming request data, so FastAPI can validate it automatically before your function runs.

```python
from pydantic import BaseModel

class TaskCreate(BaseModel):
    title: str

class TaskUpdate(BaseModel):
    completed: bool
```
`TaskCreate` says "a created task must include a `title` that's a string." `TaskUpdate` says "an update must include a `completed` boolean." If the incoming JSON doesn't match, FastAPI automatically responds with a `422` validation error (Section 7) before your endpoint code even runs — you don't have to write that validation logic yourself.

## 17. HTTPException

APIs should return status codes that accurately reflect what happened, not always `200`. FastAPI provides `HTTPException` for this:
```python
from fastapi import HTTPException

raise HTTPException(status_code=404, detail="Task not found")
```
Using this inside `get_task()`:
```python
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task

    raise HTTPException(status_code=404, detail="Task not found")
```
Now a missing task correctly returns `404`, instead of a misleading `200` with an error message buried in the body. This matters for anyone (or any agent) consuming your API — they can check the *status code* reliably instead of having to inspect the body to guess whether something went wrong.

## 18. Agentic AI Connection

```
LLM
 ↓
Tool
 ↓
API Client
 ↓
HTTP
 ↓
REST API
 ↓
Database
```

Each layer has a distinct responsibility:
- **LLM:** decides *what* action is needed (e.g., "create a task") and generates the arguments (e.g., the title).
- **Tool:** the agent-facing wrapper — a function/class the LLM's decision maps onto (e.g., `create_task(title)`).
- **API Client:** handles the mechanics of making the actual HTTP call (URL, timeout, error handling, JSON parsing) — as built on Day 10.
- **HTTP:** the request/response communication itself.
- **REST API:** your (or someone else's) FastAPI application, exposing endpoints like `POST /tasks`.
- **Database:** where the data ultimately lives (today, an in-memory list stands in for this).

## 19. API Endpoint → Agent Tool

An API endpoint like `POST /tasks` can become an agent tool conceptually represented as `create_task(title)`. The tool internally calls `POST /tasks`:
```
LLM
 ↓
Tool
 ↓
API
 ↓
Database
```

**Why the LLM shouldn't need to understand every HTTP detail:** Imagine the LLM produces:
```python
create_task(title="Learn Agentic AI")
```
The LLM doesn't need to think about POST, HTTP headers, `Content-Type`, the URL, or JSON serialization — your tool implementation handles all of that.
```
LLM
 ↓
"What action should I take?"
 ↓
Tool
 ↓
"How do I perform that action?"
 ↓
API Client
 ↓
HTTP
 ↓
External system
```

**Why tools matter:** the LLM is good at understanding language, reasoning, choosing actions, and generating structured arguments. Your code is good at calling APIs, validating input, handling errors, authenticating, and executing actions. Together, **LLM + Tools** becomes far more capable than an LLM alone.

**Example flow:**
```
User: "Add 'Study Agentic AI' to my tasks."
 ↓
Agent: "Need to create task."
 ↓
Task Tool
 ↓
POST /tasks
 ↓
FastAPI
 ↓
Task created
 ↓
JSON
 ↓
Agent
 ↓
"Done."
```

## 20. Security Rules

- **API keys:** never hard-code them; load them via `os.getenv()` from environment variables.
- **Bearer tokens:** treat exactly like secrets — never print, log, or commit them.
- **`.env`:** store local secrets/configuration here, never inside your actual code files.
- **`.gitignore`:** always exclude `.env`, `.venv/`, and `__pycache__/` (from Day 9).
- **Authentication:** verify *who* is calling your API before letting sensitive operations proceed.
- **Authorization:** even an authenticated caller shouldn't automatically be allowed to do *everything* — check what they're permitted to do.
- **Logging:** never log full API keys, tokens, or other secrets in application logs.
- **Secret exposure:** if a real secret is ever exposed (committed, logged, or shared), rotate/revoke it — don't just delete the line (as covered on Day 9).

## 21. Common Beginner Mistakes

- **Using verbs in REST URLs unnecessarily** — `/getAllTasks`, `/createTask` instead of `GET /tasks`, `POST /tasks`.
- **Confusing authentication and authorization** — authentication is "who are you," authorization is "what can you do."
- **Confusing 401 and 403** — 401 means the server doesn't know who you are; 403 means it knows but won't let you do that.
- **Not returning correct status codes** — e.g., returning `200` with an error message in the body instead of a proper `404`.
- **Exposing tokens** — printing, logging, or committing bearer tokens/API keys.
- **Not validating request data** — skipping Pydantic models and manually trusting whatever JSON arrives.
- **Poor endpoint naming** — verbs and inconsistent naming instead of clear, noun-based resource paths.
- **Not documenting APIs** — leaving consumers (including future agent tools) to guess endpoints, parameters, and expected responses.

## 22. Mental Models

- REST = a style/convention for designing web APIs.
- Resource = a thing your API manages (users, tasks, products...).
- URL = which resource?
- HTTP method = what operation?
- `/tasks` = collection; `/tasks/10` = one specific item.
- Nested resources express relationships (`/users/10/orders`).
- Authentication = WHO are you?
- Authorization = WHAT are you allowed to do?
- 401 = "I don't know who you are." 403 = "I know you, but no."
- API key/bearer token = a secret that proves you're allowed to call the API.
- API documentation = a contract between provider and consumer.
- OpenAPI = a machine-readable description of an API.
- Swagger UI = interactive documentation/testing interface generated from that description.
- Postman = a general-purpose tool for manually testing any API.
- HTTPException = how a FastAPI endpoint reports the *correct* status code for what happened.
- Pydantic model = the expected shape of incoming request data.
- 204 No Content = success, but nothing to send back.
- Tool = an API abstraction the agent can use without needing to know HTTP details.
- LLM decides the action; your code executes it.
- LLM + Tools > LLM alone.

## 23. Interview Questions

1. **Q: What does REST stand for, and what is it in practice?**
   A: Representational State Transfer — in practice, a set of conventions for designing web APIs around resources.

2. **Q: What is a resource in REST terms?**
   A: A "thing" the API manages, such as users, tasks, or products.

3. **Q: What's the difference between `/tasks` and `/tasks/10`?**
   A: `/tasks` refers to the collection of tasks; `/tasks/10` refers to one specific task.

4. **Q: Map CRUD operations to HTTP methods.**
   A: Create → POST, Read → GET, Update → PUT/PATCH, Delete → DELETE.

5. **Q: Why are REST URLs usually nouns rather than verbs?**
   A: Because the HTTP method already describes the action (verb); the URL should identify the resource being acted on.

6. **Q: What's an example of a nested resource, and what does it represent?**
   A: `GET /users/10/orders` — the orders belonging to user 10, expressing a relationship between two resources.

7. **Q: What does status code 200 mean, and 201?**
   A: 200 = the request succeeded; 201 = a new resource was created.

8. **Q: What does 204 No Content mean, and when would you use it?**
   A: The request succeeded but there's no body to return — commonly used after a successful DELETE.

9. **Q: What's the difference between 400 and 422?**
   A: 400 generally means the request itself was invalid; 422 (common in FastAPI) specifically means the request data failed validation.

10. **Q: What is authentication?**
    A: Verifying who is making the request.

11. **Q: What is authorization?**
    A: Determining what an authenticated party is allowed to do.

12. **Q: What does 401 mean?**
    A: Authentication problem — the server doesn't know who you are (missing/invalid credentials).

13. **Q: What does 403 mean?**
    A: Authorization problem — the server knows who you are, but you're not allowed to do that action.

14. **Q: What's a common memory trick for 401 vs 403?**
    A: 401 = "Who are you?" 403 = "I know you, but no."

15. **Q: What is an API key?**
    A: A secret credential the client sends to the server to authenticate itself.

16. **Q: How are API keys commonly sent?**
    A: Often in headers, like `Authorization: Bearer YOUR_API_KEY` or `X-API-Key: YOUR_API_KEY` — the exact format depends on the API.

17. **Q: Why should you never assume an API's authentication format?**
    A: Different APIs use different conventions (Bearer tokens, custom headers, etc.); always check the documentation.

18. **Q: What is a bearer token?**
    A: A token sent in the `Authorization: Bearer TOKEN` header, proving the client has valid credentials.

19. **Q: Why should API keys/tokens never be hard-coded?**
    A: Hard-coded secrets risk exposure if the code is shared or committed; use environment variables instead.

20. **Q: What is API documentation, and why does it matter?**
    A: A description of an API's endpoints, methods, parameters, and responses — it's the contract that tells consumers how to use the API correctly.

21. **Q: What is OpenAPI?**
    A: A standard for machine-readably describing an API's endpoints, methods, parameters, request/response shapes, and authentication.

22. **Q: What is Swagger UI?**
    A: An interactive documentation/testing interface, often auto-generated from an API's OpenAPI description (e.g., at FastAPI's `/docs`).

23. **Q: Is Swagger UI the same thing as the API itself?**
    A: No — Swagger UI is an interface for exploring/testing the API; the actual API is the HTTP endpoints themselves.

24. **Q: What is Postman used for?**
    A: Manually sending HTTP requests through a GUI, useful for testing and debugging any API.

25. **Q: How can Postman help you debug an API issue?**
    A: If Postman succeeds but your Python client fails, the bug is likely in your client code; if Postman also fails, the issue is likely the API/server itself.

26. **Q: What's the key difference between Swagger UI and Postman?**
    A: Swagger UI is generated from your specific API's own specification; Postman is a general-purpose tool for testing any API.

27. **Q: What does a Pydantic model like `TaskCreate` do in a FastAPI endpoint?**
    A: Defines the expected shape of incoming request data, so FastAPI can validate it automatically before the endpoint code runs.

28. **Q: Why use `HTTPException` instead of just returning an error dictionary?**
    A: `HTTPException` sets the actual HTTP status code (e.g., 404), so consumers can rely on the status code rather than parsing the response body to detect errors.

29. **Q: What's the problem with `return {"error": "Task not found"}` without `raise HTTPException`?**
    A: The response still has a `200 OK` status even though something went wrong, which is misleading.

30. **Q: Explain how `POST /tasks` can become the agent tool `create_task(title)`.**
    A: The tool function internally makes the `POST /tasks` HTTP call; the LLM only needs to know it can call `create_task(title)`, not the underlying HTTP details.

31. **Q: Why shouldn't an LLM directly handle API authentication logic?**
    A: The LLM's role is deciding actions and arguments, not implementing security-sensitive mechanics like sending credentials — that's the tool/API client's job.

32. **Q: What's the difference between an LLM deciding an action and code executing it?**
    A: The LLM reasons about *what* should happen (e.g., "create this task"); your code (tool + API client) is responsible for *how* it actually happens (the HTTP request).

33. **Q: Explain this architecture: User → Agent → Tool → API Client → HTTP → REST API → Database.**
    A: The user's request flows to the agent, which picks a tool; the tool uses an API client to make an HTTP call to a REST API, which reads/writes data in a database, and the result flows back up to the agent's final answer.

34. **Q: Why is proper status-code usage important for an API an agent will consume?**
    A: An agent's tool code often checks status codes to decide success/failure; incorrect codes (like always returning 200) can cause the agent to misinterpret what happened.

35. **Q: Why does good API documentation matter specifically for building agent tools?**
    A: A tool's implementation depends on knowing exactly what endpoints, parameters, and responses to expect — without documentation, building a reliable tool becomes guesswork.

## 24. Flashcards

Q: What does REST stand for?
A: Representational State Transfer.

Q: What is a resource?
A: A thing an API manages (users, tasks, products, etc.).

Q: What does `/tasks` (no ID) represent?
A: The collection of tasks.

Q: What does `/tasks/10` represent?
A: One specific task.

Q: What HTTP method maps to Create?
A: POST.

Q: What HTTP method maps to Read?
A: GET.

Q: What HTTP methods map to Update?
A: PUT or PATCH.

Q: What HTTP method maps to Delete?
A: DELETE.

Q: Should REST URLs use verbs or nouns?
A: Nouns — the HTTP method supplies the verb.

Q: What does `GET /users/10/orders` represent?
A: The orders belonging to user 10 (a nested resource).

Q: What does status 200 mean?
A: OK, the request succeeded.

Q: What does status 201 mean?
A: Created, a new resource was made.

Q: What does status 204 mean?
A: No Content — success, but nothing to return.

Q: What does status 400 mean?
A: Bad Request, the request was invalid.

Q: What does status 401 mean?
A: Unauthorized, an authentication problem.

Q: What does status 403 mean?
A: Forbidden, an authorization problem.

Q: What does status 404 mean?
A: Not Found.

Q: What does status 422 mean?
A: Validation failed (common in FastAPI).

Q: What does status 500 mean?
A: Internal Server Error.

Q: What is authentication?
A: Verifying who you are.

Q: What is authorization?
A: Determining what you're allowed to do.

Q: What is an API key?
A: A secret credential used to authenticate with an API.

Q: What header commonly carries a bearer token?
A: `Authorization: Bearer TOKEN`.

Q: Should you assume all APIs use the same auth header format?
A: No — always check the documentation.

Q: What is API documentation?
A: A description of how to correctly use an API (endpoints, methods, parameters, responses, etc.).

Q: What is OpenAPI?
A: A standard for machine-readably describing an API.

Q: What is Swagger UI?
A: An interactive documentation/testing interface generated from an API's specification.

Q: Where does FastAPI expose Swagger UI by default?
A: `/docs`.

Q: Is Swagger UI the API itself?
A: No, it's an interface for exploring/testing the API.

Q: What is Postman?
A: A general-purpose GUI tool for sending and testing HTTP requests.

Q: How can Postman help debug an issue?
A: By isolating whether the problem is in your client code or the API/server itself.

Q: What does a Pydantic model do in FastAPI?
A: Defines and validates the expected shape of request data.

Q: What does `HTTPException(status_code=404, detail="...")` do?
A: Returns the correct 404 status code with an error message.

Q: Why is returning `{"error": "..."}` without `HTTPException` a problem?
A: The response still shows a 200 OK status despite the error.

Q: What's the agent architecture chain from today?
A: LLM → Tool → API Client → HTTP → REST API → Database.

Q: How can `POST /tasks` become an agent tool?
A: As a function like `create_task(title)` that internally calls `POST /tasks`.

Q: Why doesn't the LLM need to understand HTTP details?
A: Because the tool/API client layer handles those mechanics for it.

Q: What's the combined strength of "LLM + Tools"?
A: The LLM reasons and chooses actions; tools reliably execute them — together more capable than either alone.

Q: Where should API keys be stored, never in code?
A: In environment variables (e.g., via `.env`).

Q: What should you do if a secret is accidentally exposed?
A: Rotate/revoke it, not just delete the line.

## 25. API Design Exercises

For each scenario, design the **resource**, **endpoint(s)**, **HTTP method(s)**, any **parameters**, and the **expected response status**. No answers are given — work through them yourself.

1. An API for managing books: list all books, get one book, add a book, update a book's details, delete a book.
2. An API for an AI agent's memories: create a memory, list all memories, get one memory, update a memory, delete a memory.
3. An API for a user's shopping cart: view the cart, add an item, remove an item, clear the entire cart.
4. An API for blog comments nested under posts: list comments for a specific post, add a comment to a post.
5. An API to mark a task as complete (only the completion status changes, nothing else).
6. An API to search a user's documents by keyword.
7. An API endpoint to summarize a document (think about whether this is standard CRUD or an "action" endpoint).
8. An API for a project management tool: list all projects, get one project's details, create a project, archive (not delete) a project.
9. An API for user authentication: register a new user, log in an existing user.
10. An API for an agent's available tools: list all tools, get details for one specific tool.
11. An API to reset a user's password (think about whether this fits neatly into standard CRUD).
12. An API for order history: list a specific customer's past orders.
13. An API to upload a new profile picture for a user.
14. An API to like/unlike a post (think about what HTTP method and endpoint shape fit best).
15. An API for an agent to send an email through a tool.

## 26. Authentication Exercises

For each scenario, identify whether it's an **authentication problem**, an **authorization problem**, an **API key problem**, and name the **correct status code**. No answers are given.

1. A request is sent with no API key at all.
2. A request includes a valid API key, but that account isn't allowed to delete other users' data.
3. A request includes an expired or invalid bearer token.
4. A logged-in user tries to access an admin-only endpoint.
5. A request includes the wrong header name for the API's authentication scheme (e.g., sends `Authorization: Bearer` when the API expects `X-API-Key`).
6. A user is correctly authenticated and requests their own profile data.
7. A request is missing the `Authorization` header entirely on an endpoint that requires it.
8. An authenticated user tries to view another user's private messages.
9. A developer hard-codes their API key directly into a public GitHub repository.
10. A request includes a valid, correctly-formatted API key, and the action requested is fully permitted for that account.

## 27. Debugging Exercises

Diagnose the problem in each broken FastAPI design:

1.
```python
@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    for task in tasks:
        if task["id"] == task_id:
            return task
    return {"error": "Task not found"}
```

2.
```python
@app.post("/tasks")
def create_task(task: TaskCreate):
    new_task = {"id": len(tasks) + 1, "title": task.title, "completed": False}
    tasks.append(new_task)
    return new_task
```
(This creates a task successfully but always returns a default 200 status instead of signaling that something new was created.)

3.
```python
class TaskUpdate(BaseModel):
    completed: bool

@app.patch("/tasks/{task_id}")
def update_task(task_id: int, task_update: TaskUpdate):
    for task in tasks:
        if task["id"] == task_id:
            task["completed"] = task_update.completed
            return task
```
(What happens if `task_id` doesn't exist?)

4.
```python
@app.delete("/tasks/{task_id}")
def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task["id"] == task_id:
            tasks.pop(index)
            return {"message": "Deleted"}
```
(According to REST conventions from today, what status code and response shape would be more appropriate here?)

5.
```
GET /getTaskById?id=5
```
(Rewrite this to follow REST conventions from today's lesson.)

6.
```python
headers = {
    "Authorization": "Bearer sk-real-secret-token-here"
}
```
(This is committed directly into a Python file that gets pushed to GitHub.)

7. An API always responds with `200 OK` even when a resource doesn't exist, requiring consumers to check the response body for an `"error"` key instead of the status code. What's the design problem?

8.
```python
@app.post("/tasks")
def create_task(title: str):
    ...
```
(This skips using a Pydantic model entirely — what's lost by doing this?)

9. A developer building an agent tool writes: `create_task(title, api_key)`, requiring the LLM to supply the API key as an argument every time it wants to create a task. What's wrong with this design given today's "LLM shouldn't need to know HTTP/auth details" principle?

10. An endpoint `POST /users/{user_id}/deleteAccount` is created to delete a user account. What naming/design issue does this have according to REST conventions?

## 28. Knowledge Test (No Answers)

1. What does REST mean, and why is it described as a "style" rather than a strict rule?
2. What's the difference between a collection endpoint and an individual resource endpoint?
3. Why are HTTP methods considered the "verbs" and URLs the "nouns" in REST design?
4. Give an example of a nested resource and explain what relationship it expresses.
5. Why does `204 No Content` make sense as a response to a successful DELETE request?
6. What's the practical difference between a 400 and a 422 status code?
7. Explain, in your own words, the difference between authentication and authorization.
8. Why would an API return 401 instead of 403 in a given situation, and vice versa?
9. Why must API keys and bearer tokens be kept secret, and where should they be stored?
10. Why should a developer never assume all APIs authenticate the same way?
11. What role does API documentation play between an API provider and an API consumer?
12. What is OpenAPI, and how does it relate to tools like Swagger UI?
13. What is the practical difference between Swagger UI and Postman?
14. How can Postman help you determine whether a bug is in your code or in the API itself?
15. What does a Pydantic model like `TaskCreate` actually validate, and what happens if the incoming data doesn't match?
16. Why is `raise HTTPException(status_code=404, ...)` better than manually returning `{"error": "..."}` with a default 200 status?
17. Walk through, step by step, what happens when a client sends `POST /tasks` with `{"title": "Learn Agents"}` to the Day 11 FastAPI example.
18. Why is a properly designed REST API considered a good foundation for an agent tool?
19. Explain how `POST /tasks` could become the tool `create_task(title)` from an agent's perspective.
20. Why shouldn't an LLM need to understand HTTP headers, methods, or authentication directly?
21. What's the combined benefit of "LLM + Tools" compared to an LLM operating alone?
22. Scenario: your agent's tool calls an API that returns `403`. What should the tool/agent conclude, versus if it received `401`?
23. Scenario: you design an endpoint called `/deleteUserAccount`. How would you rewrite this following today's REST conventions?
24. Why does documentation matter specifically when a future teammate (or another AI) needs to build a tool around your API?
25. Explain the full chain: LLM → Tool → API Client → HTTP → REST API → Database, and what each layer is responsible for.
26. Why is it considered poor practice to have an agent's LLM directly hold or pass around a raw API key?
27. Scenario: you're deciding between PUT and PATCH for an endpoint that only changes a task's completion status. Which fits better, and why?
28. Why might "summarize a document" not fit as neatly into standard CRUD as "create a task"?
29. What security steps should you take if you discover a real API key was accidentally committed to a public repository?
30. Why is understanding REST design, authentication, and documentation considered foundational before building LLM-powered tools, rather than something to skip past quickly?

## 29. Five-Minute Revision Sheet

- **REST:** convention for designing APIs around **resources**, identified by **URLs**, acted on via **HTTP methods**.
- **CRUD → HTTP:** Create=POST, Read=GET, Update=PUT/PATCH, Delete=DELETE.
- **`/tasks`** = collection; **`/tasks/10`** = one resource. Nested: `/users/10/orders`.
- **Naming:** use nouns in URLs; let the HTTP method be the verb.
- **Status codes:** 200 OK, 201 Created, 204 No Content, 400 bad request, 401 auth problem, 403 authorization problem, 404 not found, 422 validation, 500 server error.
- **Authentication** = WHO are you? **Authorization** = WHAT can you do?
- **API keys / Bearer tokens:** secrets sent in headers (format varies by API) — never hard-code, never log/print.
- **API documentation:** the contract between provider and consumer (endpoints, methods, parameters, responses, auth, errors, examples).
- **OpenAPI:** machine-readable API description. **Swagger UI:** interactive docs/testing generated from it (FastAPI's `/docs`). **Postman:** general-purpose manual API testing tool.
- **FastAPI:** Pydantic models validate request bodies; `HTTPException` returns correct status codes.
- **Agentic AI chain:** LLM → Tool → API Client → HTTP → REST API → Database — the LLM decides the action; your code executes it via HTTP.

## 30. What I Must Remember

1. REST is a convention for designing APIs around resources, identified by URLs and acted on via HTTP methods.
2. CRUD maps to HTTP methods: Create=POST, Read=GET, Update=PUT/PATCH, Delete=DELETE.
3. `/tasks` refers to a collection, while `/tasks/10` refers to one specific resource; nested resources (`/users/10/orders`) express relationships.
4. REST URLs should use nouns, not verbs — the HTTP method already supplies the action.
5. Key status codes: 200 OK, 201 Created, 204 No Content, 400/422 client-side problems, 401 authentication problem, 403 authorization problem, 404 not found, 500 server problem.
6. Authentication answers "who are you," while authorization answers "what are you allowed to do" — 401 vs 403 map onto this distinction.
7. API keys and bearer tokens are secrets sent (in a format that varies per API) to authenticate requests, and must never be hard-coded, logged, or exposed.
8. Good API documentation is a contract between provider and consumer, describing endpoints, methods, parameters, headers, bodies, responses, errors, and authentication.
9. OpenAPI is a machine-readable API description; Swagger UI (FastAPI's `/docs`) is an interactive documentation/testing interface generated from it; Postman is a general-purpose tool for manually testing any API.
10. Pydantic models validate the shape of incoming request data in FastAPI, and `HTTPException` ensures endpoints return the correct HTTP status code instead of always defaulting to 200.
11. A well-designed REST API, with correct status codes and clear documentation, is a strong foundation for turning endpoints into reliable agent tools.
12. An API endpoint like `POST /tasks` can become an agent tool such as `create_task(title)`, with the tool internally handling the HTTP call.
13. The LLM should never need to understand HTTP methods, headers, or authentication directly — that responsibility belongs to the tool and API client layers.
14. The architecture LLM → Tool → API Client → HTTP → REST API → Database separates "deciding what to do" (LLM) from "actually doing it" (code), which is a foundational Agentic AI pattern.
15. Security discipline (no hard-coded secrets, correct auth handling, rotating exposed keys) is just as important when building APIs as when consuming them.
