# Day 10 — Stage 0: HTTP, APIs, JSON, Requests, Status Codes, and API Clients

## 1. Day 10 Overview

An AI agent is never isolated. To be useful, it has to talk to external systems: a weather service, a search service, a database, a payment system, other software. All of that communication happens through **APIs**, and most APIs are reached over **HTTP**, exchanging **JSON**. So today you learn how software talks to other software: what a request and response are, what the HTTP methods and status codes mean, and how to make real API calls from Python with the `requests` library.

This is the foundation of tool-using agents. When an agent "checks the weather," the LLM isn't calling the weather server itself. Your **tool code** makes the HTTP request, gets JSON back, and hands the result to the agent. Today you'll build exactly that pattern: `Tool → API Client → HTTP → External API → JSON`.

## 2. What Is an API?

**API** stands for **Application Programming Interface**. Simple definition: *a way for one software system to communicate with another software system.*

```
Your Python application
        ↓
      API
        ↓
Weather service
```

Your app doesn't need to know how the weather company stores its data internally. It only needs to know:
- How do I ask for weather?
- What information should I send?
- What response will I receive?

**Restaurant analogy:**
```
You
 ↓
Waiter
 ↓
Kitchen
 ↓
Food
```
You don't walk into the kitchen and cook the food yourself. You talk to the waiter, who is the *interface* to the kitchen. In the same way:
```
Application → API → Service
```

## 3. Client vs Server

- **Client:** the one that *requests* something. Examples: a browser, a mobile app, a Python program, an AI agent.
- **Server:** the one that *receives requests and provides responses*. Examples: a weather server, a database server, an AI API server, a web server.

```
CLIENT                  SERVER
  │                        │
  │──── request ──────────>│
  │                        │
  │<──── response ─────────│
  │                        │
```

Your Python script calling a weather API is the **client**. The weather company's machine answering is the **server**.

## 4. HTTP

- **What HTTP is:** **HyperText Transfer Protocol**, a protocol (a set of rules) used for communication over the web.
- **Basic communication flow:**
```
Client
  ↓
HTTP Request
  ↓
Server
  ↓
HTTP Response
  ↓
Client
```

**Request:** tells the server what you want.
```
HTTP Request
│
├── Method
├── URL
├── Headers
└── Body
```
Example: `GET /weather?city=Lahore` means roughly "Give me weather information for Lahore."

**Response:** what the server sends back.
```
HTTP Response
│
├── Status Code
├── Headers
└── Body
```
Example: `200 OK` with the body:
```json
{
  "city": "Lahore",
  "temperature": 30
}
```

## 5. HTTP Methods

| Method | Purpose | CRUD | Example |
|---|---|---|---|
| **GET** | Get data | Read | `GET /users`, `GET /users/10` |
| **POST** | Create/send data | Create | `POST /users` with a JSON body |
| **PUT** | Replace/update data | Update | `PUT /users/10` with a full body |
| **PATCH** | Partially update data | Update | `PATCH /users/10` with only `{"email": "..."}` |
| **DELETE** | Delete data | Delete | `DELETE /users/10` |

**CRUD memory trick:**
```
Create → POST
Read   → GET
Update → PUT / PATCH
Delete → DELETE
```

**Examples from the lesson:**
```
GET /users          → returns a list of users
GET /users/10       → "Give me user 10"

POST /users
Body: {"name": "Akash", "email": "akash@example.com"}   → server might create a user

PUT /users/10
Body: {"name": "Akash", "email": "new@example.com"}     → replace/update the resource

PATCH /users/10
Body: {"email": "new@example.com"}                      → only the email changes

DELETE /users/10    → remove user 10
```

**PUT vs PATCH:** PUT generally replaces/updates the whole resource; PATCH is for partial updates where only the sent fields change.

## 6. URLs and Endpoints

**URL** = Uniform Resource Locator. Example: `https://api.example.com/users`

```
https://
    ↓
Protocol

api.example.com
    ↓
Server/domain

/users
    ↓
Endpoint/path
```

- **Protocol:** how to communicate (`https://`).
- **Domain:** which server (`api.example.com`).
- **Path:** the location on that server (`/users`).
- **Endpoint:** a specific location where an API provides functionality. These are different endpoints/operations:
```
GET /users
GET /users/10
POST /users
DELETE /users/10
```

## 7. Path Parameters vs Query Parameters

**Path parameter:** part of the path that identifies a *specific resource*.
```
/users/123
     ↑
 specific resource
```

**Query parameter:** extra information after `?` that *filters or modifies* the request.
```
/users?city=Lahore
       ↑
     filtering
```

More examples:
```
/weather?city=Lahore
/products?category=shoes&limit=10
```
The second has two query parameters: `category=shoes` and `limit=10` (joined by `&`).

| | Path parameter | Query parameter |
|---|---|---|
| **Example** | `/users/123` | `/users?city=Lahore` |
| **Purpose** | Identifies a particular resource | Filters or modifies the request |

This distinction shows up again in FastAPI.

## 8. Headers

**Headers** are metadata about a request (or response): extra information that isn't the main data itself.

- **Content-Type:** tells the server what format the body is in.
```
Content-Type: application/json
```
This means: "The body I'm sending is JSON."

- **Authorization:** used by many APIs for authentication.
```
Authorization: Bearer YOUR_TOKEN
```
Conceptually: the client says "Here is my authentication token" to the server.

- **Bearer tokens:** the `Bearer YOUR_TOKEN` form is a common way to send an authentication token in the `Authorization` header. (Deeper authentication topics like OAuth come later.)

Never expose real tokens publicly.

## 9. JSON

**JSON** = JavaScript Object Notation: a structured text format for exchanging data. (Don't worry about the JavaScript part.)

**Objects:**
```json
{
  "name": "Akash",
  "age": 29,
  "city": "Lahore"
}
```
**Arrays:**
```json
["calculator", "weather", "search"]
```
**Nested JSON:** real APIs often return nested structures.
```json
{
  "user": {
    "name": "Akash",
    "location": {
      "city": "Lahore",
      "country": "Pakistan"
    }
  }
}
```
This is common with AI APIs, search APIs, payment APIs, database APIs, and SaaS APIs.

**JSON vs Python dictionaries/lists:** they look almost identical, and that similarity is why JSON is so convenient in Python. JSON objects map to Python dictionaries, and JSON arrays map to Python lists. But JSON is a *text format* for exchanging data, while dictionaries and lists are *Python objects in memory*. When you call `response.json()`, `requests` converts the JSON text into Python data for you.

## 10. HTTP Status Codes

Status codes tell you *what happened*.

```
1xx → Informational
2xx → Success
3xx → Redirection
4xx → Client error
5xx → Server error
```

| Code | Name | Meaning | Easy memory |
|---|---|---|---|
| **200** | OK | The request succeeded | OK |
| **201** | Created | A new resource was created (common with `POST /users`) | Created |
| **400** | Bad Request | The request was invalid (e.g. `"age": "hello"` when a number is expected) | Bad request |
| **401** | Unauthorized | Authentication is missing or invalid (e.g. API key missing) | Authentication problem |
| **403** | Forbidden | Server understood you, but you're not allowed to do that | Forbidden |
| **404** | Not Found | The requested resource wasn't found | Not found |
| **422** | Unprocessable Content | Request data failed validation (common in FastAPI) | Validation problem |
| **500** | Internal Server Error | Something went wrong on the server side | Server problem |

```
Your request → Server → 💥 Something failed → 500
```

Rule of thumb: **4xx = the client did something wrong, 5xx = the server had a problem.**

## 11. Python requests

Install (inside your activated virtual environment):
```
pip install requests
```

**`requests.get()`:**
```python
import requests

response = requests.get("https://api.example.com/users")

print(response.status_code)
print(response.text)
```

**`response.status_code`:** the HTTP status code.
```python
if response.status_code == 200:
    print("Success")
```

**`response.text`:** the raw response body, usually a string.

**`response.json()`:** if the server returned JSON, this converts it into Python data.
```python
data = response.json()
print(data["name"])
```

**`response.raise_for_status()`:** if the response has an error status code, `requests` raises an exception. Often cleaner than checking manually.
```python
response = requests.get(url)
response.raise_for_status()
data = response.json()
```

**`timeout`:** never let an external request wait forever.
```python
response = requests.get(url, timeout=10)
```
Meaning: wait at most about 10 seconds before giving up. *(A small accuracy note: `timeout` limits how long `requests` waits to connect and to receive data, rather than being a strict limit on the entire request. For now, "don't wait forever" is the right mental model.)*

**`requests.post()`:** sends data to the server.
```python
data = {"title": "My post", "body": "Hello", "userId": 1}

response = requests.post(url, json=data)
```
With `json=data`, `requests` converts your dictionary to JSON for you.

**Practice API:** the lesson uses `https://jsonplaceholder.typicode.com`, a public test API that needs no authentication.
```python
import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

response = requests.get(url)
print(response.status_code)

data = response.json()
print(data["title"])
```

## 12. Query Parameters and Headers in requests

**`params=`:** cleaner than manually writing `?city=Lahore` in the URL.
```python
params = {"city": "Lahore"}

response = requests.get(url, params=params)
```

**`headers=`:**
```python
headers = {
    "Authorization": "Bearer YOUR_TOKEN",
    "Content-Type": "application/json"
}

response = requests.get(url, headers=headers)
```
⚠️ Don't hard-code real secrets. Read them from environment variables (Day 9).

**`json=`:** send a dictionary as a JSON body.
```python
response = requests.post(url, json={"title": "My post"})
```

**`timeout=`:** always set one.

**The complete request pattern:**
```python
response = requests.get(
    url,
    params=params,
    headers=headers,
    timeout=10
)

response.raise_for_status()

data = response.json()
```
```
URL
 ↓
Request
 ↓
Status check
 ↓
JSON
 ↓
Python data
```

## 13. Error Handling

**Why external API calls can fail:** the network may be down, the server may be unavailable or slow, the URL may be wrong, or the server may return an error status (4xx or 5xx). Don't assume every request succeeds. You don't control the other side.

**Bad:**
```python
response = requests.get(url)
data = response.json()
```

**Better (manual status check):**
```python
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print(data)
else:
    print("Request failed")
```

**Better still (exceptions):**
```python
import requests

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
    data = response.json()
except requests.RequestException as error:
    print(f"API request failed: {error}")
```
`requests.RequestException` is the general exception for problems with a request. Catching it means a network problem or bad status won't crash your program with an ugly traceback.

## 14. Building an API Client

Instead of writing `requests.get(...)` everywhere, wrap the logic once.

**A reusable function:**
```python
import requests

def get_post(post_id: int) -> dict:
    url = f"https://jsonplaceholder.typicode.com/posts/{post_id}"

    response = requests.get(url, timeout=10)
    response.raise_for_status()

    return response.json()

post = get_post(1)
print(post["title"])
```

**An `APIClient` class** (combining Day 7 classes and Day 8 type hints; this is one way to build what the project asks for):
```python
import requests

class APIClient:
    def __init__(self, base_url: str, timeout: int = 10):
        self.base_url = base_url
        self.timeout = timeout

    def get(self, path: str, params: dict | None = None):
        url = f"{self.base_url}{path}"

        try:
            response = requests.get(
                url,
                params=params,
                timeout=self.timeout
            )
            response.raise_for_status()
            return response.json()

        except requests.RequestException as error:
            print(f"API request failed: {error}")
            return None

client = APIClient("https://jsonplaceholder.typicode.com")
post = client.get("/posts/1")
```

What each part does:
- **`base_url`:** the shared start of every URL (`https://jsonplaceholder.typicode.com`). Each call only supplies the path.
- **`get()`:** builds the full URL and performs the request.
- **Timeout:** stored once, applied to every request.
- **Error handling:** `try/except requests.RequestException` so failures don't crash the program.
- **JSON parsing:** `response.json()` returns Python data.

The request flow inside the client:
```
request → timeout → status check → JSON
```

## 15. Building an API Tool

An **API tool** is a class or function that wraps an API call so an agent can use it.

```python
class PostSearchTool:
    def __init__(self):
        self.name = "post_search"
        self.description = "Searches posts by keyword in the title"
        self.client = APIClient("https://jsonplaceholder.typicode.com")

    def run(self, keyword: str) -> list[dict]:
        posts = self.client.get("/posts")

        if posts is None:
            return []

        return [
            post
            for post in posts
            if keyword.lower() in post["title"].lower()
        ]

tool = PostSearchTool()
results = tool.run("qui")
```

The layers:
```
Tool
 ↓
API Client
 ↓
HTTP
 ↓
External API
 ↓
JSON
```

- **Tool:** the agent-facing piece: it has a name, a description, and `run()`. The agent only knows "I can run this tool with a keyword."
- **API Client:** handles the mechanics of talking to the API (URL building, timeout, status check, JSON parsing, errors).
- **HTTP:** the request/response communication over the web.
- **External API:** the service outside your program (here, JSONPlaceholder).
- **JSON:** the structured data that comes back, converted to Python data.

Each layer has one job. That separation is what makes real AI applications maintainable.

## 16. Agentic AI Connection

```
User
 ↓
Agent
 ↓
Tool
 ↓
API Client
 ↓
External API
 ↓
JSON
 ↓
Tool
 ↓
Agent
 ↓
Final Answer
```

Example with a weather tool:
```python
def get_weather(city: str) -> dict:
    response = requests.get(
        WEATHER_API_URL,
        params={"city": city},
        timeout=10
    )
    response.raise_for_status()
    return response.json()
```
Flow for "What's the weather in Lahore?":
1. The agent decides, "I need weather information."
2. It selects the weather tool.
3. The tool sends an HTTP request to the weather API.
4. The API returns JSON.
5. The tool returns the result to the agent.
6. The agent writes the final answer.

**Important:** the LLM doesn't necessarily talk to the weather server directly. **Your tool code does.** The LLM decides *what* to do; your Python code *does* it. That's a fundamental Agentic AI pattern.

## 17. Practical API Project

The lesson's **API Explorer / Post Search Tool** project:

```
day-10/
│
├── .venv/
├── requirements.txt
└── main.py
```
Install: `pip install requests`

- **Part 1: `get_post(post_id: int) -> dict`:** build the URL, send GET, use a timeout, check status, return JSON.
- **Part 2: `get_posts(limit: int = 5) -> list[dict]`:** call `GET /posts`, return only the first `limit` posts (for example `posts[:limit]`).
- **Part 3: `find_posts(posts, keyword) -> list[dict]`:** local search using a list comprehension:
```python
matches = [
    post
    for post in posts
    if keyword.lower() in post["title"].lower()
]
```
- **Part 4: `APIClient` class:** with `base_url` and `get()`.
- **Part 5: error handling:** `try/except requests.RequestException`.
- **Part 6: `PostSearchTool`:** input keyword → API → search → return matching posts.

Final architecture:
```
                       Agent
                         │
                         ↓
                  PostSearchTool
                         │
                         ↓
                     APIClient
                         │
                         ↓
                      HTTP
                         │
                         ↓
                    External API
```

**Final challenge goals:** create a client, get posts, search them, create a tool, run it, and make sure the program doesn't crash with an ugly traceback just because the API is unavailable.

## 18. Common Beginner Mistakes

- **Not checking status codes:** calling `.json()` on an error response and getting confusing failures. Use `raise_for_status()` or check `status_code`.
- **No timeout:** a slow or dead server can make your program wait forever. Always set `timeout=`.
- **Assuming every response is JSON:** error pages or other responses may not be JSON, so `.json()` can fail. Check status first, and use `response.text` when you just need to look at the raw body.
- **Hard-coding API keys:** put keys in `.env` and read them with `os.getenv()`.
- **Confusing path and query parameters:** `/users/123` identifies a resource; `/users?city=Lahore` filters.
- **Confusing PUT and PATCH:** PUT replaces/updates the whole resource; PATCH partially updates it.
- **Exposing authentication tokens:** never print them, commit them, or paste them into public places.
- **Not handling network errors:** internet problems and unavailable servers are normal. Catch `requests.RequestException`.

## 19. Mental Models

- API = communication interface between software systems.
- HTTP = the communication protocol of the web.
- Client asks; server answers.
- Request = method + URL + headers + body.
- Response = status code + headers + body.
- GET = give me data.
- POST = create/send data.
- PUT = replace/update the whole thing.
- PATCH = change part of something.
- DELETE = remove something.
- CRUD = Create (POST), Read (GET), Update (PUT/PATCH), Delete (DELETE).
- URL = protocol + domain + path.
- Endpoint = a specific place an API offers functionality.
- Path parameter = which resource; query parameter = how to filter.
- Headers = metadata about the request.
- JSON = structured data exchange.
- Status code = what happened?
- 4xx = client's fault; 5xx = server's fault.
- Timeout = don't wait forever.
- `raise_for_status()` = turn bad status codes into exceptions.
- `response.json()` = JSON text → Python data.
- Tool = API wrapper an agent can use.
- The LLM decides; your tool code makes the HTTP call.

## 20. Interview Questions

*(REST appears in today's goals but is only lightly touched in the lesson, so REST answers below stay at the basic level shown in the lesson: URLs as resources, HTTP methods as operations.)*

1. **Q: What is an API?**
   A: A way for one software system to communicate with another.
   *Deeper:* You only need to know how to ask and what you'll get back, not how the service works internally.

2. **Q: What is HTTP?**
   A: HyperText Transfer Protocol, the protocol used for communication over the web.

3. **Q: What is a client?**
   A: The side that sends requests, such as a browser, mobile app, Python program, or AI agent.

4. **Q: What is a server?**
   A: The side that receives requests and returns responses.

5. **Q: What does an HTTP request contain?**
   A: A method, a URL, headers, and (sometimes) a body.

6. **Q: What does an HTTP response contain?**
   A: A status code, headers, and a body.

7. **Q: What is GET used for?**
   A: Retrieving data.
   ```python
   requests.get("https://jsonplaceholder.typicode.com/posts/1")
   ```

8. **Q: What is POST commonly used for?**
   A: Creating something or submitting data, with the data in the request body.

9. **Q: What's the difference between PUT and PATCH?**
   A: PUT generally replaces/updates the whole resource; PATCH updates only part of it.
   *Deeper:* `PATCH /users/10` with `{"email": "new@example.com"}` changes only the email.

10. **Q: What is DELETE used for?**
    A: Removing a resource, e.g. `DELETE /users/10`.

11. **Q: How do HTTP methods map to CRUD?**
    A: Create → POST, Read → GET, Update → PUT/PATCH, Delete → DELETE.

12. **Q: What is a URL, and what are its parts?**
    A: A Uniform Resource Locator. In `https://api.example.com/users`: protocol (`https://`), domain (`api.example.com`), path (`/users`).

13. **Q: What is an endpoint?**
    A: A specific location where an API provides functionality, such as `GET /users/10`.

14. **Q: What is a query parameter?**
    A: Extra information after `?` in a URL that filters or modifies the request, e.g. `/products?category=shoes&limit=10`.

15. **Q: What's the difference between a path parameter and a query parameter?**
    A: A path parameter identifies a specific resource (`/users/123`); a query parameter filters or modifies the request (`/users?city=Lahore`).

16. **Q: What is a request header?**
    A: Metadata about the request, such as `Content-Type` or `Authorization`.

17. **Q: What does `Content-Type: application/json` mean?**
    A: The body being sent is JSON.

18. **Q: What does `Authorization: Bearer TOKEN` usually indicate?**
    A: The client is sending an authentication token to prove who it is.
    *Deeper:* Never expose real tokens publicly; load them from environment variables.

19. **Q: What is JSON?**
    A: A structured text format for exchanging data, made of objects and arrays.

20. **Q: How does JSON relate to Python dictionaries and lists?**
    A: JSON objects look like dictionaries and JSON arrays look like lists, but JSON is a text format while dictionaries/lists are Python objects.

21. **Q: What does status code 200 mean? 201?**
    A: 200 means the request succeeded; 201 means a new resource was created.

22. **Q: What do 400, 401, 403, and 404 mean?**
    A: 400 bad request (invalid), 401 authentication missing/invalid, 403 forbidden (understood but not allowed), 404 not found.

23. **Q: What does 422 usually mean, and where do you often see it?**
    A: The request data failed validation. It appears often in FastAPI.

24. **Q: What does 500 mean, and whose fault is it?**
    A: Internal Server Error: something went wrong on the server side.

25. **Q: What does `response.json()` do?**
    A: Converts a JSON response body into Python data (dictionaries/lists).

26. **Q: What's the difference between `response.text` and `response.json()`?**
    A: `response.text` is the raw body as a string; `response.json()` parses JSON into Python data structures.

27. **Q: Why should you use a timeout on API requests?**
    A: So your program doesn't wait forever on a slow or unresponsive server.
    ```python
    requests.get(url, timeout=10)
    ```

28. **Q: What does `response.raise_for_status()` do, and why use it?**
    A: It raises an exception for error status codes, so you don't accidentally treat a failed response as success.

29. **Q: How would you handle network errors from `requests`?**
    A: Wrap the call in `try/except requests.RequestException`.
    ```python
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except requests.RequestException as error:
        print(f"API request failed: {error}")
    ```

30. **Q: How does an API tool fit into an AI agent?**
    A: The agent decides to use a tool; the tool uses an API client to make an HTTP request to an external API; the JSON response goes back through the tool to the agent, which produces the final answer.
    *Deeper:* The LLM doesn't call the external server directly. Your tool code does.

## 21. Flashcards

Q: What does API stand for?
A: Application Programming Interface.

Q: What is an API in one sentence?
A: A way for one software system to communicate with another.

Q: What's the API analogy from the lesson?
A: A waiter between you and the kitchen.

Q: What is a client?
A: The side that sends requests.

Q: What is a server?
A: The side that receives requests and sends responses.

Q: What does HTTP stand for?
A: HyperText Transfer Protocol.

Q: What are the four parts of an HTTP request (conceptually)?
A: Method, URL, headers, body.

Q: What are the three parts of an HTTP response (conceptually)?
A: Status code, headers, body.

Q: What does GET do?
A: Gets data.

Q: What does POST do?
A: Creates/sends data.

Q: What does PUT do?
A: Replaces/updates the resource.

Q: What does PATCH do?
A: Partially updates the resource.

Q: What does DELETE do?
A: Deletes the resource.

Q: CRUD mapping?
A: Create=POST, Read=GET, Update=PUT/PATCH, Delete=DELETE.

Q: What is a URL?
A: Uniform Resource Locator, the address of a resource.

Q: What is an endpoint?
A: A specific location where an API provides functionality.

Q: What is a path parameter?
A: A URL path part identifying a specific resource, like `/users/123`.

Q: What is a query parameter?
A: A `?key=value` part that filters or modifies a request.

Q: How are multiple query parameters joined?
A: With `&`, e.g. `?category=shoes&limit=10`.

Q: What are headers?
A: Metadata about the request or response.

Q: What does `Content-Type: application/json` mean?
A: The body is JSON.

Q: What does `Authorization: Bearer TOKEN` do?
A: Sends an authentication token to the server.

Q: What is JSON?
A: A structured text format for exchanging data.

Q: What does status code 200 mean?
A: OK, the request succeeded.

Q: What does 201 mean?
A: Created, a new resource was made.

Q: What does 400 mean?
A: Bad request, the request was invalid.

Q: What does 401 mean?
A: Authentication is missing or invalid.

Q: What does 403 mean?
A: Forbidden, you're not allowed to do that.

Q: What does 404 mean?
A: Not found.

Q: What does 422 mean?
A: Validation failed (common in FastAPI).

Q: What does 500 mean?
A: Internal server error, a server-side problem.

Q: What do 4xx codes indicate?
A: Client errors.

Q: What do 5xx codes indicate?
A: Server errors.

Q: What does `response.json()` return?
A: The response body parsed into Python data.

Q: Why use `timeout=`?
A: So the program doesn't wait forever.

## 22. Code Output Practice

Predict the output of each snippet. No answers are given; run them yourself to check.

1.
```python
status = 404

if status == 200:
    print("OK")
elif status == 404:
    print("Not found")
else:
    print("Other")
```

2.
```python
data = {"user": {"location": {"city": "Lahore"}}}
print(data["user"]["location"]["city"])
```

3.
```python
base_url = "https://api.example.com"
path = "/users/10"
print(f"{base_url}{path}")
```

4.
```python
status = 503
print(status // 100)
```

5.
```python
token = "abc123"
headers = {"Authorization": f"Bearer {token}"}
print(headers["Authorization"])
```

6.
```python
posts = [
    {"title": "Hello World"},
    {"title": "Python Tips"},
    {"title": "Hello Again"},
]
matches = [p for p in posts if "hello" in p["title"].lower()]
print(len(matches))
```

7.
```python
posts = [1, 2, 3, 4, 5, 6, 7]
limit = 3
print(posts[:limit])
```

8.
```python
params = {"category": "shoes", "limit": 10}
parts = [f"{key}={value}" for key, value in params.items()]
print("&".join(parts))
```

9.
```python
import requests

try:
    raise requests.RequestException("boom")
except requests.RequestException as error:
    print(f"API request failed: {error}")
```

10.
```python
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def build_url(self, path):
        return f"{self.base_url}{path}"

client = APIClient("https://example.com")
print(client.build_url("/posts/1"))
```

11.
```python
response_data = [{"id": 1, "name": "Ali"}, {"id": 2, "name": "Ahmed"}]
names = [user["name"] for user in response_data]
print(names)
```

12.
```python
def check(status_code):
    if 200 <= status_code < 300:
        return "success"
    elif 400 <= status_code < 500:
        return "client error"
    elif status_code >= 500:
        return "server error"
    return "other"

print(check(201), check(401), check(500))
```

## 23. Debugging Practice

Each snippet has a problem. Identify it and fix it.

1.
```python
response = requests.get(url)
data = response.json()
```
(What's missing for production-quality code? Name at least two things.)

2.
```python
response = requests.get(url, header={"Authorization": "Bearer TOKEN"})
```

3.
```python
response = requests.get(url, timeout=10)
if response.status_code == "200":
    print("Success")
```

4.
```python
response = requests.get("https://jsonplaceholder.typicode.com/posts")
data = response.json()
print(data["title"])
```
(The endpoint returns a list of posts.)

5.
```python
API_KEY = "sk-real-secret-key"
headers = {"Authorization": f"Bearer {API_KEY}"}
```

6.
```python
post_id = 1
url = "https://jsonplaceholder.typicode.com/posts/{post_id}"
response = requests.get(url, timeout=10)
```

7.
```python
response = requests.post(url, data=my_dict)
```
(The API expects a JSON body. Which requests argument is intended for that?)

8.
```python
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except:
    print("Something went wrong")
```

9.
```python
class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path):
        response = requests.get(base_url + path, timeout=10)
        return response.json()
```

10.
```python
def get_weather(city):
    response = requests.get(WEATHER_URL + "?city=" + city)
    return response.text["temperature"]
```
(Find at least two problems.)

## 24. API Design Practice

For each scenario, choose the **HTTP method**, the **endpoint**, any **path/query parameters**, and the **expected status code** on success. No answers are given.

1. Fetch the list of all products.
2. Fetch the product with ID 42.
3. Create a new user with a name and email.
4. Replace all the details of user 10 with a completely new set of details.
5. Change only the email address of user 10.
6. Delete order 5.
7. List products in the "shoes" category, returning at most 10 results.
8. Request user data but forget to send your API token. What status code should the server respond with?
9. Send a new user with `"age": "hello"` to an API that requires a number, and the API rejects the data as failing validation. What status code do you expect (in a FastAPI-style API)?
10. You're logged in but try to delete another user's account, and the server understands the request but refuses. What status code should come back?

## 25. Knowledge Test (No Answers)

1. In your own words, what is an API, and why does the waiter analogy fit?
2. What's the difference between a client and a server? Give two examples of each.
3. What does HTTP stand for, and what is it used for?
4. What are the parts of an HTTP request?
5. What are the parts of an HTTP response?
6. When would you use GET versus POST?
7. What's the difference between PUT and PATCH?
8. How do HTTP methods map to CRUD operations?
9. Break down `https://api.example.com/users/10` into protocol, domain, and path.
10. What is an endpoint, and how is `GET /users` different from `POST /users`?
11. What's the difference between `/users/123` and `/users?city=Lahore`?
12. What's a header? Give two examples.
13. What does `Content-Type: application/json` tell the server?
14. What does `Authorization: Bearer TOKEN` usually indicate, and why must the token stay private?
15. How is JSON similar to a Python dictionary, and how is it different?
16. What's the difference between a 4xx and a 5xx status code?
17. What do 200 and 201 mean, and when might you see each?
18. What's the difference between 401 and 403?
19. When would you see a 422 in a FastAPI-style API?
20. Why isn't checking `response.status_code` optional in real applications?
21. What does `response.raise_for_status()` do?
22. What's the difference between `response.text` and `response.json()`?
23. Why must every API request have a timeout?
24. What do the `params=`, `headers=`, and `json=` arguments do in `requests`?
25. Why should API keys be loaded from environment variables rather than hard-coded in request headers?
26. Why catch `requests.RequestException` instead of using a bare `except:`?
27. Why wrap `requests.get()` in an `APIClient` class rather than calling it everywhere?
28. In the `PostSearchTool` design, what is the responsibility of the tool versus the API client?
29. Scenario: an agent needs the weather in Lahore. Walk through every step from user question to final answer.
30. Why does the lesson say "the LLM doesn't necessarily directly talk to the weather server. Your tool code does"?

## 26. Five-Minute Revision Sheet

- **API:** a way for software to talk to software (waiter between you and the kitchen).
- **Client** requests; **server** responds. **HTTP** is the protocol.
- **Request:** method + URL + headers + body. **Response:** status code + headers + body.
- **Methods:** GET (read), POST (create), PUT (replace/update), PATCH (partial update), DELETE (remove). CRUD = POST/GET/PUT-PATCH/DELETE.
- **URL:** protocol + domain + path. **Endpoint:** a specific API location.
- **Path parameter** (`/users/123`) identifies a resource; **query parameter** (`/users?city=Lahore`) filters.
- **Headers:** metadata: `Content-Type: application/json`, `Authorization: Bearer TOKEN`.
- **JSON:** objects `{}` ≈ dictionaries, arrays `[]` ≈ lists; a text format, not a Python object.
- **Status codes:** 200 OK, 201 Created, 400 bad request, 401 auth problem, 403 forbidden, 404 not found, 422 validation, 500 server error. 4xx = client, 5xx = server.
- **requests:** `get()`, `post()`, `status_code`, `text`, `json()`, `raise_for_status()`, `params=`, `headers=`, `json=`, `timeout=`.
- **Pattern:** URL → request → status check → JSON → Python data.
- **Errors:** always use a timeout; catch `requests.RequestException`.
- **Agent pattern:** Agent → Tool → API Client → HTTP → External API → JSON → Tool → Agent. Your tool code makes the HTTP call, not the LLM.

## 27. What I Must Remember

1. An API is a way for one software system to communicate with another, and AI agents depend on APIs to reach the outside world.
2. HTTP is a client/server protocol: the client sends a request (method, URL, headers, body) and the server sends back a response (status code, headers, body).
3. GET reads, POST creates/sends, PUT replaces/updates, PATCH partially updates, DELETE removes; these map onto CRUD.
4. A URL is made of a protocol, a domain, and a path; an endpoint is a specific place where an API offers functionality.
5. Path parameters identify a specific resource (`/users/123`); query parameters filter or modify the request (`/users?city=Lahore`).
6. Headers carry request metadata, such as `Content-Type: application/json` and `Authorization: Bearer TOKEN`, and tokens must never be exposed.
7. JSON is a structured text format that maps naturally onto Python dictionaries and lists, but it is not itself a Python object.
8. Status codes tell you what happened: 200 OK, 201 Created, 400 bad request, 401 authentication problem, 403 forbidden, 404 not found, 422 validation problem, 500 server problem.
9. `response.json()` converts a JSON response into Python data, while `response.text` is the raw string body.
10. Always use `timeout=` so your program never waits forever on an external service.
11. Never assume a request succeeded: use `raise_for_status()` or check `status_code`.
12. Wrap external calls in `try/except requests.RequestException` so network problems don't crash your program with an ugly traceback.
13. Use `params=`, `headers=`, and `json=` in `requests` instead of building query strings and JSON bodies by hand, and load secrets from environment variables.
14. An `APIClient` class centralizes base URL, timeout, error handling, and JSON parsing so every API call is consistent.
15. An API-backed tool follows Agent → Tool → API Client → HTTP → External API → JSON → Tool → Agent: the LLM decides what to do, and your tool code performs the HTTP request.
