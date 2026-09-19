# Lesson 2: LLM APIs and Your First Python LLM Application

## 1. Lesson Overview

An **LLM API** is how your Python code talks to a language model that lives on someone else's server — you send it text, it sends text back. Python applications use APIs because the LLM isn't running inside your program; it's a separate service, so you need a standard way to send requests and receive responses. This lesson is about understanding that plumbing (API calls, messages, keys, context) *before* you build anything agentic — you're learning the LLM as a component, not yet building a decision-making agent.

## 2. Core Concepts

### API
- **Definition:** A defined way for one piece of software to talk to another.
- **Why it matters:** It lets your Python program use the LLM without knowing how the model works internally.
- **Analogy:** A waiter between you and the kitchen — you don't need to know how the food is cooked.
- **Example:** `client.responses.create(...)` — you send a request, the API returns a response.

### LLM API
- **Definition:** The specific API a provider exposes so you can send prompts to their language model and get generated text back.
- **Why it matters:** It's the entry point for every AI feature you'll build — chatbots, agents, RAG systems, all start with an LLM API call.
- **Analogy:** Ordering from a specific restaurant's menu (that restaurant = one LLM provider).
- **Example:**
```python
response = client.responses.create(
    model="YOUR_MODEL",
    input="Explain Python functions in simple words."
)
```

### System Message
- **Definition:** An instruction that tells the model how to behave, before the user says anything.
- **Why it matters:** It shapes tone, behavior, and constraints — critical once you build agents with specific jobs.
- **Analogy:** Briefing a new employee on the rules before their first customer walks in.
- **Example:** `"You are a beginner-friendly Python teacher. Use simple English."`

### User Message
- **Definition:** The actual request or question from the user.
- **Why it matters:** It's the task the model needs to respond to.
- **Analogy:** The customer's order.
- **Example:** `"What is FastAPI?"`

### Assistant Response
- **Definition:** The model's generated reply.
- **Why it matters:** It's the output your application shows to the user (or feeds into the next step).
- **Analogy:** The food that comes back from the kitchen.
- **Example:** `"FastAPI is a Python web framework..."`

### Context
- **Definition:** All the information given to the model for the *current* request (system message + history + user question + any documents).
- **Why it matters:** The model can only reason using what's inside this context — nothing outside of it.
- **Analogy:** Everything on the waiter's notepad when they walk into the kitchen — the chef only knows what's written there.
- **Example:** System message + last 2 messages + new question, all sent together.

### Conversation History
- **Definition:** The sequence of past user/assistant messages from a conversation.
- **Why it matters:** Without sending it back to the model, the model has no idea what was said earlier.
- **Analogy:** Notes from previous meetings you bring to the next one so people remember what was decided.
- **Example:**
```python
messages = [
    {"role": "user", "content": "My name is Ali."},
    {"role": "assistant", "content": "Nice to meet you, Ali."},
    {"role": "user", "content": "What's my name?"}
]
```

### Tokens
- **Definition:** The basic chunks of text (not exactly words) that a model processes.
- **Why it matters:** They determine cost, speed, and how much text fits in one request.
- **Analogy:** Puzzle pieces — a sentence is broken into pieces, and the model works piece by piece, not word by word.
- **Example:** `"Hello world"` might be 2–3 tokens, not necessarily 2.

### Context Window
- **Definition:** The maximum number of tokens (input + output combined) a model can handle in a single request.
- **Why it matters:** If your system message + history + documents + question exceed it, something has to be cut or summarized.
- **Analogy:** The size of the notepad the waiter is allowed to carry into the kitchen — only so much fits.
- **Example:** System instructions + conversation + documents + question, all competing for the same limited space.

### Environment Variables
- **Definition:** Values (like secrets) stored outside your code, typically in a `.env` file, and loaded at runtime.
- **Why it matters:** Keeps sensitive values out of your source code and out of version control.
- **Analogy:** Keeping your house key in a lockbox instead of taped to the front door.
- **Example:** `.env` file containing `OPENAI_API_KEY=your_api_key_here`.

### API Keys
- **Definition:** A secret credential that authenticates your requests to the LLM provider.
- **Why it matters:** Anyone with your key can use your account and run up charges — it must stay private.
- **Analogy:** A password to your account — you wouldn't post it publicly.
- **Example:** Never `api_key = "sk-..."` in code — load it from `.env` instead.

### Prompt vs Agent
- **Definition:** A prompt is just text sent to an LLM for a response; an agent adds the ability to decide and use tools across multiple steps.
- **Why it matters:** Many beginners think any LLM call is "an agent" — it isn't, unless there's decision-making and tool use involved.
- **Analogy:** Asking a friend a question (prompt) vs. asking them to go run errands and report back, deciding the route themselves (agent).
- **Example:** `"Calculate 20 + 30"` sent straight to the LLM is a prompt, not an agent.

## 3. LLM API Flow

```
Python Application
        ↓
   API Request
        ↓
       LLM
        ↓
Generated Response
        ↓
Python Application
```

- **Python Application:** Your code decides what to ask and prepares the request.
- **API Request:** Your code sends the prompt (and any messages/config) to the provider's API endpoint.
- **LLM:** The model processes the request and generates text based on it.
- **Generated Response:** The API sends the model's output back to your application.
- **Python Application:** Your code receives the response and does something with it — print it, store it, pass it to the next step.

## 4. Messages and Roles

| Role | Purpose | Example |
|---|---|---|
| **System** | Sets behavior/instructions | "You are a helpful, beginner-friendly Python teacher." |
| **User** | The actual question/request | "What is FastAPI?" |
| **Assistant** | The model's generated reply | "FastAPI is a Python web framework..." |

**Example conversation:**
```
SYSTEM:    "You are a Python teacher. Explain things simply."
USER:      "Explain FastAPI."
ASSISTANT: "FastAPI is a modern Python framework for building APIs quickly..."
```

## 5. Context and Conversation History

An LLM does **not** automatically remember past conversations — each API call is independent unless your application resends the relevant history. If you ask "My name is Ali," then later ask "What's my name?" in a *new, separate* request without including the earlier message, the model has no way to know the answer.

- **Context** — everything included in the *current* request (system message + history + new question + documents). This is what the model can actually "see" right now.
- **Conversation History** — the specific past user/assistant messages from this chat, which your application stores and can choose to include as part of context.
- **Memory** — a broader concept (short-term or long-term) for retaining and retrieving relevant information across time; conversation history is one simple form of it, but true memory systems (and RAG) go further and will be covered later.

```
Conversation
     ↓
Your application stores history
     ↓
Relevant history
     ↓
LLM (as part of context)
```

## 6. API Keys and Security

- **Store in environment variables** — keep the key in `.env`, not hardcoded in your `.py` files, so it isn't exposed if you share your code.
- **Never write it directly in source code** — `api_key = "sk-..."` in a script can easily leak (screenshots, copy-pasting, code reviews).
- **Never commit it to GitHub** — once pushed, it's in your repo's history forever (even if you delete it later), and anyone can misuse it.

**`.env` file:**
```
OPENAI_API_KEY=your_api_key_here
```

**`.gitignore` file:**
```
venv/
.env
__pycache__/
```

Your Python code then loads the key from the environment instead of hardcoding it — see the example below.

## 7. Python Example (Line by Line)

```python
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

client = OpenAI()

response = client.responses.create(
    model="YOUR_MODEL",
    input="Explain Python functions in simple words."
)

print(response.output_text)
```

- `from dotenv import load_dotenv` — imports the function that reads your `.env` file.
- `from openai import OpenAI` — imports the SDK's client class for talking to the API.
- `load_dotenv()` — reads `.env` and loads `OPENAI_API_KEY` (and any other variables) into the environment.
- `client = OpenAI()` — creates a client object; it automatically picks up the API key from the environment.
- `client.responses.create(...)` — sends the actual API request: which model to use, and what input to send.
- `response` — the object the API sends back, containing the generated output plus metadata.
- `response.output_text` — the plain text of the model's reply.
- `print(response.output_text)` — displays the answer to the user.

**Project structure used in this lesson:**
```
agentic-ai/
│
├── lesson-02/
│   └── main.py
│
└── .env
```

## 8. Prompt vs Agent

**Prompt only:**
```
Prompt
 ↓
LLM
 ↓
Response
```

**Agent:**
```
Prompt
 ↓
LLM
 ↓
Decide
 ↓
Tool
 ↓
Result
 ↓
LLM
 ↓
Response
```

An API call by itself — even with a well-crafted prompt like "Calculate 20 + 30" — is **not** an agent. It's just one request and one response. It becomes agentic only when the system can **decide to take an action** (like calling a tool), observe the result, and reason again before answering. Lesson 2's chatbot is intentionally *not* an agent yet — it's the LLM-as-a-component piece you need before adding decision-making.

## 9. Important Mental Models

- API = bridge between your application and the model.
- Context = everything given to the model for the current request.
- Conversation history = past messages your app chooses to resend.
- Tokens = the pieces of text the model actually processes (not the same as words).
- Context window = the size limit on how much can fit into one request.
- System message = the "job description" you give the model.
- API key = a password — never hardcode it, never commit it.
- .env = where secrets live; .gitignore = what keeps secrets out of GitHub.
- An LLM has no memory by default — your app is responsible for providing it.
- Prompt ≠ Agent: decision-making + tools is what makes something agentic.

## 10. Common Beginner Mistakes

- **Hardcoding the API key in source code** — instead, always load it from `.env` via environment variables.
- **Forgetting to add `.env` to `.gitignore`** — this can leak your key the moment you push to GitHub.
- **Assuming the model remembers earlier conversations automatically** — instead, resend relevant history yourself as part of the context.
- **Confusing "context" with "conversation history"** — history is just one ingredient inside the full context sent per request.
- **Thinking any LLM API call is an "agent"** — a single request/response with no tool use or decision-making is just a prompt, not an agent.
- **Ignoring the context window limit** — sending too much text (long history + big documents) can exceed what the model can process in one request.

## 11. Interview Questions

1. **Q: What is an LLM API?**
   A: An interface that lets your application send prompts to a language model hosted on a provider's server and receive generated text back.

2. **Q: What is a system message?**
   A: An instruction given to the model before the user's input, defining its behavior, tone, or role.

3. **Q: What is a context window?**
   A: The maximum number of tokens (input plus output) the model can process in a single request.

4. **Q: What are tokens?**
   A: The basic units of text (often smaller than whole words) that the model reads and generates, which affect cost and context limits.

5. **Q: Why shouldn't API keys be hardcoded?**
   A: Because hardcoded keys can leak through shared code, screenshots, or version control, letting others misuse your account.
   *Deeper:* Storing keys in environment variables and excluding `.env` via `.gitignore` keeps secrets out of your codebase entirely.

6. **Q: Is an LLM API call an agent?**
   A: No — it's just a prompt-response exchange; an agent additionally requires decision-making over tools/actions across a loop.

7. **Q: What's the difference between conversation history and context?**
   A: Conversation history is the stored past messages; context is everything actually sent to the model for the current request, which may include that history plus more.

8. **Q: Why doesn't an LLM remember past conversations by default?**
   A: Each API call is independent — the model only "knows" what's included in that specific request's context, so history must be resent by the application.

9. **Q: What's the role of the `assistant` message in a conversation array?**
   A: It represents the model's own past responses, included so the model has continuity when reasoning about further questions.

10. **Q: What does `load_dotenv()` do?**
    A: It reads variables (like API keys) from a `.env` file and loads them into the environment so your code can access them securely.

## 12. Flashcards

Q: What is an API?
A: A defined way for one piece of software to communicate with another.

Q: What is an LLM API?
A: The interface for sending prompts to a language model and getting responses back.

Q: What does a system message do?
A: Sets the model's behavior/instructions before the user's request.

Q: What is a user message?
A: The actual question or request from the user.

Q: What is an assistant response?
A: The model's generated reply.

Q: What is context?
A: Everything provided to the model for the current request.

Q: What is conversation history?
A: The past messages exchanged in a chat, which the app can choose to resend.

Q: What is a token?
A: A basic unit of text the model processes; not the same as a word.

Q: What is a context window?
A: The maximum tokens a model can handle in one request.

Q: What is an environment variable?
A: A value (like a secret) stored outside your code and loaded at runtime.

Q: Where should an API key be stored?
A: In an environment variable (e.g., via a `.env` file), never hardcoded.

Q: What does `.gitignore` do for `.env`?
A: Prevents the `.env` file (and your secret key) from being committed to GitHub.

Q: Is a single LLM API call an agent?
A: No — it's just a prompt and response, with no decision-making or tool use.

Q: What makes something an agent instead of just a prompt?
A: The ability to decide on and use tools, observing results before answering.

Q: Does an LLM remember previous chats by default?
A: No — the application must resend relevant history as part of the context.

## 13. Five-Minute Revision Sheet

- **API** = bridge between your app and the LLM.
- **Roles:** System (instructions) → User (question) → Assistant (answer).
- **Context** = everything sent in the current request; **history** = past messages your app resends; **memory** = broader retention concept (covered later).
- **Tokens** = text units the model processes; **context window** = max tokens per request.
- **Security:** API key → `.env` → never hardcoded → `.env` in `.gitignore`.
- **Flow:** Python App → API Request → LLM → Response → Python App.
- **Prompt vs Agent:** Prompt = LLM → Response. Agent = LLM → Decide → Tool → Result → LLM → Response.
- **Key fact:** An LLM has no memory by default; your application provides it.

## 14. Knowledge Test (No Answers)

1. What's the difference between conversation history and the full context sent to the model?
2. Why is it risky to hardcode an API key directly in a Python file, even for a "quick test"?
3. Scenario: You ask the model "What's my name?" in a brand-new request without any prior messages included. Why won't it know the answer, even if you told it your name earlier that day?
4. Scenario: Your chatbot's conversation has grown very long, and the model starts giving degraded or cut-off responses. What concept explains why this might be happening?
5. Explain why `Prompt → LLM → Response` is not the same thing as an agent.
6. What is the purpose of a system message, and how does it change the model's output compared to not having one?
7. What is a token, and why does it matter beyond just "how much text you can send"?

## 15. What I Should Remember

1. An LLM API lets your Python code send prompts and receive generated responses from a model hosted elsewhere.
2. Messages have roles: system (instructions), user (request), assistant (response).
3. Context is everything sent to the model for the current request — it has no memory beyond that.
4. Conversation history must be explicitly resent by your application if you want the model to "remember" earlier messages.
5. Tokens are the units of text the model processes, and they directly affect the context window and cost.
6. The context window is the hard limit on how much information (system + history + documents + question) fits in one request.
7. API keys are secrets — store them in environment variables via `.env`, and never hardcode or commit them.
8. `.gitignore` should always exclude `.env` to prevent leaking secrets to GitHub.
9. A prompt sent to an LLM is not automatically an agent — it's just a single request/response exchange.
10. An agent requires decision-making plus tool use across a loop; Lesson 2's chatbot is intentionally just the LLM component, not yet an agent.
