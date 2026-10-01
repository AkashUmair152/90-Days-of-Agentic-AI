# Day 12 — LLM APIs: Your First Real LLM-Powered Program

## 1. Lesson Overview

Today connects everything built so far — Python, HTTP, APIs, REST, FastAPI, tools — to the thing at the center of Agentic AI: the **LLM**. By the end of today you understand how a Python program sends a prompt to an LLM API and gets a response back, why LLM APIs use the same HTTP/JSON concepts from Days 10–11, and the single most important architectural idea in this whole course: **the LLM decides, your code executes.** You'll build an AI Chat CLI, then upgrade it into an AI Task Assistant that bridges an LLM's structured output into your Day 11 FastAPI Task API — your first real connection between an LLM and a tool.

## 2. What Is an LLM?

A more precise definition than "gives reasoning and text answers": **an LLM is a machine-learning model trained to process and generate language by learning patterns from large amounts of data.**
```
User: Explain REST APIs.
        ↓
       LLM
        ↓
Generated text
```
**Important:** an LLM by itself doesn't automatically interact with your computer or the external world. That's where tools and agents come in — today focuses mainly on the simpler slice: `Python → LLM API → LLM → Response`.

**The big picture to hold in mind:**
```
                 AI APPLICATION
                      │
        ┌─────────────┴─────────────┐
        ↓                           ↓
      LLM                         TOOLS
        │                           │
        │                           ├── Calculator
        │                           ├── Weather API
        │                           ├── Database
        │                           └── Web/API
        │
        └──────────────┬────────────┘
                       ↓
                     AGENT
```

## 3. LLM API, SDK, and AI Application — Three Distinct Things

- **LLM:** the model itself. `Input → model → output`.
- **LLM API:** the interface that lets *software* communicate with the model.
```
Python
 ↓
HTTP/API
 ↓
LLM
 ↓
Response
 ↓
Python
```
This matters because agents are software programs — they need *programmatic* access to models, not a chat website a human clicks through.
- **AI Application:** your software built around the model.
```
User
 ↓
Python application
 ↓
LLM
 ↓
Tools
 ↓
Database
 ↓
UI
```
This three-way distinction (LLM vs LLM API vs AI Application) is described as extremely important for interviews.

**Why an LLM API matters — example:** a "Customer Support Agent" receives "Where is my order?" from a customer. Your application needs to route that to an LLM:
```
Customer message
       ↓
Your Python program
       ↓
LLM API
       ↓
LLM
       ↓
Response
       ↓
Your Python program
       ↓
Customer
```

**LLM API = another API:** it uses the same concepts you already know from Days 10–11 — HTTP, POST, headers, JSON, authentication, REST. That existing knowledge is directly useful here.

**The basic request/response shape (conceptual — exact format varies by provider):**
```json
POST /chat
{
  "model": "some-model",
  "messages": [
    {"role": "user", "content": "Explain REST APIs"}
  ]
}
```
```json
{
  "response": "REST APIs are..."
}
```

## 4. Messages: system, user, assistant

Modern LLM APIs organize conversation input into **messages** with **roles**:
```
system    → How the AI should behave
user      → What the user asks
assistant → What the AI previously answered
```

- **System message:** high-level instructions for behavior/role, e.g. `"You are a helpful Python tutor. Explain concepts using simple examples."`
- **User message:** the actual request, e.g. `"Explain FastAPI in simple English."`
- **Assistant message:** the generated answer. In multi-turn applications, previous assistant responses can also become part of the ongoing conversation context.

**Mental model:**
```
SYSTEM:    "What rules should I follow?"
USER:      "What do you want?"
ASSISTANT: "What should I respond?"
```

## 5. Tokens and Tokenization

A **token** is a chunk of text used by the model — **not necessarily one word.** `"hello"` might be one token in some tokenizer contexts, while `"Understanding"` might be split into multiple tokens.

```
Don't think: 1 word = 1 token
Think:       Text → Tokenizer → Tokens → LLM
```

**Tokenization process:**
```
"Hello, how are you?"
           ↓
       tokenizer
           ↓
        tokens
           ↓
          LLM
```
The LLM doesn't process raw human text the way a person reads it — text is converted into token representations first.

**Why tokens matter (at least three reasons):**
1. **Context limits** — models can only process so much input/output per request.
2. **Cost** — many providers price usage partly based on token counts.
3. **Performance** — larger prompts can require more processing.
4. *(also: memory/context — more conversation history means more tokens)*

## 6. Context Window

The model doesn't have unlimited context. How much information it can consider in one request relates to its **context window**.
```
┌───────────────────────────┐
│       CONTEXT WINDOW      │
│                           │
│ system instructions       │
│ user messages             │
│ previous conversation     │
│ tool results              │
│ current request           │
└───────────────────────────┘
```

**Context ≠ permanent memory:** context is the information available for *this* request/conversation — it is not automatically saved anywhere. Persistent memory would instead come from something like a database, a vector database, a file, or application-level memory. Agentic systems often combine context with these separate memory systems (covered later).

## 7. Prompts

A **prompt** is the input/instructions given to the model, e.g. `"Explain Python decorators in simple English."` Good prompt design isn't "write something clever" — it's about giving the model enough useful information and constraints to perform reliably.

**Bad prompt:** `"Tell me about Python."` — far too broad.

**Better prompt:**
```
Explain Python decorators to a beginner.

Use:
1. A simple definition
2. One analogy
3. One short code example
4. Three common mistakes
```
Now the desired output is much clearer.

**A useful mental model:**
```
PROMPT = Instructions + Context + Task + Constraints + Expected format
```
Not every prompt needs all five parts, but this structure is very useful when designing one.

**Example — vague vs structured:**
```
Vague: "Analyze this."

Structured:
You are a customer-support assistant.

Context:
The customer purchased a laptop 3 days ago.

Task:
Explain the return process.

Constraints:
- Be concise.
- Don't invent policies.
- If information is missing, say so.

Format:
Use 3 bullet points.
```

## 8. Temperature

`temperature` influences the randomness/variability of model outputs.
```
Lower temperature  → more predictable/focused outputs
Higher temperature → more varied/creative outputs
```
**Not** a measure of intelligence — a higher temperature doesn't make the model "smarter."

**Example:** for "Extract the customer's email address" (a deterministic-ish task), you generally don't need much variability. For "Write 10 creative startup names," more variation may help.

**Important warning:** temperature is not a reliability switch. `temperature = 0` does **not** guarantee factual correctness — the model can still be wrong.

## 9. Model Selection

Different models have different characteristics you might choose based on: reasoning capability, speed, cost, context size, tool support, multimodal capability, latency, output quality. In production, model selection is an engineering decision — **not** "always use the biggest model."
```
                  Capability
                     ↑
                     │
                     └────────────→ Cost
```
Your job as an AI engineer is often to find an appropriate balance: an expensive model may be unnecessary for a simple classification task, while complex reasoning may genuinely benefit from a stronger model.

## 10. Environment Variables (Recap from Day 9)

LLM API keys must be stored securely, never hard-coded.
```
# .env
LLM_API_KEY=your_secret_key
```
```python
import os
api_key = os.getenv("LLM_API_KEY")
```
Never write `api_key = "sk-actual-secret-key"` inside code that might be committed to Git.

## 11. Your First LLM Program — Architecture

**Project structure:**
```
day-12/
│
├── .venv/
├── .env
├── .gitignore
├── requirements.txt
└── main.py
```
Install `python-dotenv`, plus whichever LLM provider's SDK you're using (the exact SDK varies by provider — for learning, focus on the architecture rather than memorizing provider-specific syntax).

**Loading the key:**
```python
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("LLM_API_KEY")
```

**Program shape:**
```
main.py
   │
   ├── load API key
   │
   ├── create LLM client
   │
   ├── send message
   │
   └── print response
```

**Provider SDK (conceptual):**
```python
client = SomeLLMClient(api_key=api_key)

response = client.generate(
    model="...",
    messages=[{"role": "user", "content": "Explain APIs."}]
)

print(response)
```
⚠️ Don't memorize this exact code — **memorize the architecture:**
```
API KEY → CLIENT → MODEL → MESSAGES → REQUEST → RESPONSE
```

**The full LLM API pipeline (today's most important diagram):**
```
Python Program
      ↓
   API Key
      ↓
  LLM Client
      ↓
    Model
      ↓
   Messages
      ↓
 HTTP Request
      ↓
 LLM Provider
      ↓
Model Processing
      ↓
   Response
      ↓
Python Program
```

## 12. SDK vs Raw HTTP

When you call `client.generate(...)`, the SDK may be handling authentication, the HTTP request, JSON serialization, headers, the endpoint, response parsing, and error handling for you — that's why SDKs are convenient. Without one, you'd construct HTTP requests manually (exactly as you did with `requests` on Day 10).
```
Python → requests    → HTTP → LLM API   (raw HTTP)
Python → Official SDK → HTTP → LLM API   (SDK abstraction)
```
The SDK is simply an abstraction layer over the same underlying HTTP API.

**How this connects to Day 11's tool architecture:**
```
Tool → API Client → HTTP → REST API        (Day 11)
Agent → LLM → LLM API                       (today)
Agent → LLM → Tool → External API           (where we're heading)
```

## 13. Structured Output

Suppose you ask the model to "Extract the task from this sentence" for: *"Remind me to study FastAPI tomorrow."* You don't want conversational filler like *"Sure! I'd be happy to help..."* — you want structured data:
```json
{
  "task": "study FastAPI",
  "date": "tomorrow"
}
```
This is **structured output.**

**Why it matters:** LLMs naturally generate language; programs prefer structured data. Compare `"Sure, I'll remind you tomorrow!"` with `{"task": "study FastAPI", "date": "2026-10-01"}` — the second is trivially easy for your program to work with.

**Structured output in agents:** for "What's the weather in Lahore?" the model might produce something conceptually like:
```json
{
  "tool": "get_weather",
  "arguments": {"city": "Lahore"}
}
```
Your program then executes the tool. This is the beginning of **tool calling** (explored more deeply in a future lesson).

## 14. LLM Decides; Code Executes ⭐⭐⭐

This is described as one of the most important concepts in the entire course.

The LLM might decide `get_weather("Lahore")` is the right action — but the LLM itself isn't making the HTTP request. **Your application does.**
```
LLM
 ↓
Decision
 ↓
Your code
 ↓
Tool execution
 ↓
Result
 ↓
LLM
```

**First mini agent, worked through:**
```
User: "What's 20 + 30?"

LLM:  calculator, arguments: 20 + 30

Your program: calculator(20, 30) → 50

LLM: "The answer is 50."
```
The separation:
```
LLM  = decides
Code = executes
```

## 15. Tool Calling Loop (Preview)

```
             ┌───────────────┐
             │     USER      │
             └───────┬───────┘
                     ↓
             ┌───────────────┐
             │      LLM      │
             └───────┬───────┘
                     ↓
              Need a tool?
                /       \
              NO         YES
              ↓           ↓
           Answer       Tool call
                          ↓
                       Execute
                          ↓
                        Result
                          ↓
                         LLM
                          ↓
                       Answer
```
This loop is described as the heart of Agentic AI — it will be built directly in a future lesson.

## 16. Token Usage

LLM APIs often return usage information alongside the response:
```json
{
  "usage": {
    "input_tokens": 100,
    "output_tokens": 50,
    "total_tokens": 150
  }
}
```
Production AI systems monitor this because it relates directly to cost, latency, token usage, and performance.
```
Your prompt      → INPUT TOKENS
Model response   → OUTPUT TOKENS
INPUT + OUTPUT   = TOTAL TOKENS
```
(Exact billing depends on the provider and model.)

**Context growth:** a running agent's context might include the system prompt + user message + previous messages + tool results + the new request — every piece adds tokens. More context → more tokens → potentially more cost. This becomes very important for long-running agents.

## 17. API Errors, Timeouts, and Retries

**LLM APIs can fail.** Examples:
```
401 → invalid authentication
429 → rate limit / too many requests
500 → server-side problem
```

**Never assume the API always works.** A production mindset asks: what if the API key is missing? The network fails? The provider is unavailable? A rate limit occurs? The response is malformed? The model returns unexpected output? The request times out? This mindset is what separates a beginner demo from production software.

**Timeout:** just like HTTP requests generally, don't let your application wait forever.
```
Your application → wait → wait → timeout → handle failure
```

**Retry:** some failures are temporary — a `429` might just mean "try again later."
```
Request → Failure → Wait → Retry
```
But **don't blindly retry every error.** An invalid API key (`401`) won't be fixed by retrying 10 times.

**Idempotency (just know the word for now):** some operations can safely be repeated without changing the result beyond the first successful execution — e.g., `GET /tasks/1` can generally be repeated safely, but `POST /orders` could create multiple orders if blindly repeated. This will be revisited later.

## 18. Project 1 — AI Chat CLI

**Goal:**
```
User types: "Explain Python decorators"
        ↓
      Python
        ↓
     LLM API
        ↓
    Response
        ↓
     Terminal
```
Continues in a loop until the user types `exit`.

**Requirements for `ai_chat.py`:**
1. Load API key from `.env`
2. Create the LLM client
3. Ask the user for input
4. Send input to the model
5. Print the response
6. Repeat
7. Exit on `"exit"`

**Architecture:**
```
User → Python CLI → LLM API → LLM → Response → User
```

## 19. Project 2 — AI Task Assistant

**Upgrade:** user says `"I need to learn FastAPI tomorrow."` The program asks the LLM to extract:
```json
{"task": "Learn FastAPI", "date": "tomorrow"}
```
Then the Python program creates a task by calling the Day 11 API: `POST /tasks`.

**Architecture:**
```
User
 ↓
LLM
 ↓
Structured Output
 ↓
Python
 ↓
POST /tasks
 ↓
FastAPI
 ↓
Task created
```
This is described as your **first real bridge between LLMs and tools/APIs.**

## 20. Mental Models

- LLM = a language model — reasoning/generation engine, not automatically connected to the outside world.
- LLM API = programmatic access to a model (another kind of API, using HTTP/JSON like any other).
- AI Application = your software wrapped around the LLM (UI, tools, database, logic).
- System = behavior/instructions. User = the request. Assistant = the generated response.
- Text gets converted into tokens — don't assume 1 word = 1 token.
- Tokens affect context limits, cost, and performance.
- Context window = the information available to the model for the current request — not permanent memory.
- Prompt = instructions + context + task + constraints + expected format.
- Structured output makes model results easy for programs (and tools) to use.
- Temperature controls output variability, not intelligence or reliability.
- Model selection is a cost-vs-capability engineering decision, not "always pick the biggest model."
- API keys are secrets — load from `.env`, never hard-code.
- SDKs abstract away raw HTTP details (auth, serialization, headers, parsing).
- LLM decides; your code executes tools.
- Agent = LLM + tools + an execution loop.
- Never assume an API call always succeeds — plan for timeouts, errors, and selective retries.

## 21. Common Beginner Mistakes

- **Assuming 1 word = 1 token** — leading to wrong expectations about context/cost.
- **Treating context as permanent memory** — forgetting that context only covers the current request/conversation unless explicitly re-sent or stored elsewhere.
- **Writing vague prompts** — "Tell me about Python" instead of a structured prompt with task, constraints, and format.
- **Believing `temperature = 0` guarantees accuracy** — it only reduces randomness, not factual correctness.
- **Choosing the "biggest" model by default** — instead of balancing capability against cost/speed for the actual task.
- **Hard-coding LLM API keys** — instead of loading them from `.env`/environment variables.
- **Assuming the LLM executes tools itself** — it only decides; your code performs the actual execution.
- **Not handling API errors** — assuming every request to the LLM API succeeds, with no timeout or error handling.
- **Blindly retrying every failure** — retrying a `401` (bad credentials) won't help, unlike a `429` (rate limit).

## 22. Practical Examples

```python
# Loading the API key
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("LLM_API_KEY")

# Conceptual client usage (exact SDK syntax varies by provider)
client = SomeLLMClient(api_key=api_key)

response = client.generate(
    model="...",
    messages=[
        {"role": "system", "content": "You are a helpful Python tutor."},
        {"role": "user", "content": "Explain FastAPI in simple English."}
    ]
)

print(response)

# A simple chat loop shape
while True:
    user_input = input("You: ")
    if user_input == "exit":
        break

    response = client.generate(
        model="...",
        messages=[{"role": "user", "content": user_input}]
    )
    print("AI:", response)

# LLM decides, code executes (conceptual)
decision = {"tool": "calculator", "arguments": {"a": 20, "b": 30}}

if decision["tool"] == "calculator":
    result = calculator(decision["arguments"]["a"], decision["arguments"]["b"])
    print(result)   # 50
```

## 23. Interview Questions

1. **Q: What is an LLM?**
   A: A machine-learning model trained to process and generate language by learning patterns from large amounts of data.

2. **Q: What is an LLM API?**
   A: The interface that lets software (not just a human via chat UI) programmatically communicate with an LLM.

3. **Q: Why do applications use LLM APIs instead of a chat website?**
   A: Agents and applications are software programs that need programmatic, automatable access to the model.

4. **Q: What is a system message?**
   A: High-level instructions defining the model's behavior or role.

5. **Q: What is a user message?**
   A: The actual request or input from the user.

6. **Q: What is an assistant message?**
   A: The model's generated response, which can also become part of ongoing conversation context.

7. **Q: What is tokenization?**
   A: The process of converting text into token representations before the model processes it.

8. **Q: What is a token?**
   A: A chunk of text used by the model — not necessarily equal to one word.

9. **Q: Why do tokens affect cost?**
   A: Many providers price API usage partly based on the number of input/output tokens processed.

10. **Q: What is a context window?**
    A: The amount of information (in tokens) a model can consider within a single request.

11. **Q: Is context the same as permanent memory?**
    A: No — context is available only for the current request/conversation; permanent memory requires a separate system like a database.

12. **Q: What is a prompt?**
    A: The instructions/input given to the model, ideally structured with task, context, constraints, and expected format.

13. **Q: What is structured output?**
    A: Model output formatted as structured data (like JSON) rather than free-form natural language.

14. **Q: Why is structured output useful for agents?**
    A: Programs can reliably parse and act on structured data, such as a tool name and arguments, far more easily than free text.

15. **Q: What does temperature control?**
    A: The randomness/variability of the model's output — lower is more predictable, higher is more varied.

16. **Q: Does temperature control intelligence or accuracy?**
    A: No — it only affects output variability, not correctness or reliability.

17. **Q: Why should API keys be stored in `.env`?**
    A: To keep secrets out of source code and prevent accidental exposure if code is shared or committed.

18. **Q: What's the difference between using an SDK and raw HTTP for an LLM API?**
    A: An SDK abstracts away the HTTP details (auth, serialization, headers, parsing); raw HTTP means handling all of that yourself, as with `requests`.

19. **Q: What does a client SDK usually handle for you?**
    A: Authentication, the HTTP request, JSON serialization, headers, the endpoint, response parsing, and error handling.

20. **Q: What's the difference between an LLM deciding to call a tool and the tool actually executing?**
    A: The LLM only produces a decision (e.g., which tool and what arguments); your application code is what actually performs the tool's action.

21. **Q: What does a 429 error mean?**
    A: Rate limiting — too many requests have been made.

22. **Q: Why might you retry a 429?**
    A: Because it often represents a temporary condition that can succeed if retried after a wait.

23. **Q: Why shouldn't you endlessly retry a 401?**
    A: Because invalid authentication won't be fixed by retrying — the credentials themselves need to be corrected.

24. **Q: What is token usage, and why track it?**
    A: The input/output/total token counts for a request, tracked because it relates to cost, latency, and performance.

25. **Q: Explain: User → Python → LLM API → LLM → Response.**
    A: The user's input goes to your Python program, which sends it through the LLM API to the model; the model generates a response that flows back through the API to your program.

26. **Q: Explain: User → LLM → Tool → API → Result → LLM → User.**
    A: The user's request goes to the LLM, which decides a tool is needed; your code executes that tool (possibly calling an external API), the result is fed back to the LLM, which then produces the final answer for the user.

## 24. Flashcards

Q: What is an LLM?
A: A model trained to process and generate language from patterns in data.

Q: What is an LLM API?
A: The interface letting software communicate programmatically with an LLM.

Q: What is an AI Application?
A: The software built around an LLM (UI, tools, database, logic).

Q: What does the system role define?
A: The model's behavior/instructions.

Q: What does the user role contain?
A: The actual request.

Q: What does the assistant role contain?
A: The model's generated response.

Q: Is 1 word always 1 token?
A: No.

Q: What is a context window?
A: The amount of information the model can consider per request.

Q: Is context the same as permanent memory?
A: No.

Q: What is a prompt?
A: The instructions/input given to the model.

Q: What five parts can a well-structured prompt include?
A: Instructions, context, task, constraints, expected format.

Q: What does lower temperature do?
A: Makes output more predictable/focused.

Q: What does higher temperature do?
A: Makes output more varied/creative.

Q: Does temperature=0 guarantee accuracy?
A: No.

Q: What is structured output?
A: Model output formatted as structured data (e.g. JSON) rather than free text.

Q: Why does structured output matter for tool calling?
A: Programs can reliably parse it to know which tool/arguments to use.

Q: What is the core LLM-agent separation to remember?
A: LLM decides; code executes.

Q: What does a 401 error mean for an LLM API?
A: Invalid authentication.

Q: What does a 429 error mean?
A: Rate limit exceeded.

Q: What does a 500 error mean?
A: Server-side problem.

Q: Should you retry every API error?
A: No — only errors likely to be temporary, like 429.

Q: What is idempotency (in one sentence)?
A: An operation that can safely be repeated without changing the result beyond the first success.

Q: What does an SDK abstract away?
A: Raw HTTP details like auth, serialization, headers, and parsing.

Q: What's the LLM API pipeline, in order?
A: API Key → Client → Model → Messages → HTTP Request → Provider → Processing → Response.

Q: Why must LLM API keys be kept out of source code?
A: To prevent exposure if the code is shared or committed.

Q: What does token usage typically report?
A: Input tokens, output tokens, and total tokens.

Q: Why does context growth matter for long-running agents?
A: More context means more tokens, which can mean more cost.

Q: What's the tool-calling loop's core question?
A: "Need a tool?" — if yes, execute and feed the result back to the LLM; if no, answer directly.

Q: What connects Day 11's Tool → API Client → HTTP → REST API to today?
A: The same pattern extends to Agent → LLM → Tool → External API.

Q: What was the first mini-agent example today?
A: A calculator: the LLM decides `calculator(20, 30)`, the code executes it and returns 50, and the LLM reports the answer.

Q: What's the AI Task Assistant project's key architecture?
A: User → LLM → Structured Output → Python → POST /tasks → FastAPI → Task created.

## 25. Knowledge Test (No Answers)

1. What is the difference between an LLM, an LLM API, and an AI Application?
2. Why do applications need programmatic (API) access to a model rather than a chat interface?
3. What role does a system message play compared to a user message?
4. Why is "1 word = 1 token" a misleading assumption?
5. Name three reasons tokens matter in LLM engineering.
6. What is a context window, and why isn't it unlimited?
7. Why is context not the same thing as permanent memory?
8. What five elements can make up a well-structured prompt?
9. Why is "Tell me about Python" considered a weak prompt?
10. What does temperature control, and what does it NOT control?
11. Why doesn't `temperature = 0` guarantee factual correctness?
12. What factors go into model selection besides "which model is strongest"?
13. Why should LLM API keys be stored in `.env` rather than hard-coded?
14. What's the difference between using a provider's SDK and making raw HTTP requests yourself?
15. What does a typical LLM SDK handle on your behalf?
16. Explain the full LLM API pipeline from Python program to response.
17. What is structured output, and why is it more useful to a program than free-form text?
18. Walk through the calculator example showing "LLM decides; code executes."
19. Describe the tool-calling loop diagram in your own words.
20. What information does token usage typically report, and why would a production system track it?
21. Why does context growth in a long-running agent matter for cost?
22. What do 401, 429, and 500 errors mean for an LLM API call?
23. Why should a 429 be retried but not a 401?
24. What is idempotency, and why does it matter when considering retries for something like `POST /orders`?
25. Why should a production AI engineer never assume an LLM API call will always succeed?
26. Describe the AI Chat CLI project's required features and flow.
27. Describe the AI Task Assistant project's architecture, from user message to created task.
28. Why is the distinction "LLM decides; code executes" described as one of the most important concepts in the whole course?
29. How does today's LLM API pipeline connect to Day 11's Tool → API Client → HTTP → REST API pattern?
30. Why is understanding tokens, context windows, and structured output foundational before building a real tool-calling agent?

## 26. Five-Minute Revision Sheet

- **LLM** = model; **LLM API** = programmatic access to it; **AI Application** = your software built around it.
- **Roles:** system (behavior), user (request), assistant (response).
- **Tokens:** chunks of text, not words — affect context limits, cost, performance.
- **Context window:** how much the model can consider per request; context ≠ permanent memory.
- **Prompt** = instructions + context + task + constraints + expected format.
- **Temperature:** controls variability (low = predictable, high = varied) — not intelligence or accuracy.
- **Model selection:** a cost-vs-capability engineering decision, not "always biggest."
- **`.env`:** LLM API keys are secrets — never hard-code.
- **Pipeline:** API Key → Client → Model → Messages → HTTP Request → Provider → Response.
- **SDK vs raw HTTP:** SDK abstracts auth/serialization/parsing; raw HTTP (via `requests`) does it manually.
- **Structured output:** JSON-shaped model output your program can act on, including tool calls.
- **LLM decides; code executes** — the LLM never directly performs the tool's action.
- **Tool-calling loop:** User → LLM → need a tool? → execute → result → LLM → answer.
- **Errors:** 401 auth, 429 rate limit, 500 server — use timeouts, and retry only what's likely temporary.
- **Projects:** AI Chat CLI (basic loop); AI Task Assistant (LLM → structured output → `POST /tasks`).

## 27. What I Must Remember

1. An LLM generates language from learned patterns; it does not, by itself, interact with the outside world — tools and agents add that.
2. An LLM API, an AI Application, and the LLM itself are three distinct things, and the difference matters for interviews.
3. Messages use roles — system (behavior), user (request), assistant (response) — to structure the conversation sent to the model.
4. Text is converted into tokens before the model processes it; tokens are not the same as words, and they drive context limits, cost, and performance.
5. A context window limits how much information a model can consider per request, and context is not the same as permanent memory.
6. A well-structured prompt combines instructions, context, task, constraints, and expected format — vague prompts produce vague results.
7. Temperature controls output variability, not intelligence or factual accuracy — `temperature = 0` does not guarantee correctness.
8. Model selection is a practical cost-vs-capability decision, not simply choosing the largest available model.
9. LLM API keys must be stored in environment variables (`.env`), never hard-coded into source code.
10. The full pipeline — API key → client → model → messages → HTTP request → provider → response — is what matters, more than any specific SDK's exact syntax.
11. Structured output (like JSON) lets your program reliably act on model results, including deciding which tool to call and with what arguments.
12. The most important idea in this course so far: the LLM decides what action to take; your code is what actually executes it.
13. The tool-calling loop (User → LLM → tool decision → execute → result → LLM → answer) is the heart of Agentic AI and will be built directly soon.
14. Production systems must never assume an LLM API call will succeed — timeouts, error handling, and selective retries (not blind retries) are essential.
15. The AI Task Assistant project — turning a user's natural-language request into structured output that triggers a real `POST /tasks` call — is the first genuine bridge between an LLM and a tool/API in this course.
