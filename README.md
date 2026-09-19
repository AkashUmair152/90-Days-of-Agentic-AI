# 🤖 90 Days of Agentic AI

> A project-based roadmap to go from **Python + FastAPI** to building, evaluating, securing, and deploying **production-grade AI agents**.

![Python](https://img.shields.io/badge/Python-3.11+-blue)
![FastAPI](https://img.shields.io/badge/FastAPI-backend-009688)
![Status](https://img.shields.io/badge/status-in%20progress-orange)
![License](https://img.shields.io/badge/license-MIT-green)

---

## 📌 About This Repository

This repo tracks my 90-day journey to become a job-ready **Agentic AI developer**.
It is **not** a "watch 25 tutorials" plan. Every stage ends with a real project, and every project ships with documentation, tests, and a demo.

**Honest disclaimer:** no roadmap can guarantee a job. Hiring depends on the market, interviews, communication, and experience. What this roadmap *does* is structure learning around the skills employers actually ask for: tool calling, RAG, stateful agents, evaluation, security, and deployment.

---

## 🎯 Goals

By Day 90, I should be able to:

- [ ] Build LLM applications from scratch
- [ ] Build tool-using agents
- [ ] Build RAG systems with citations
- [ ] Build stateful agents with short- and long-term memory
- [ ] Build multi-agent systems
- [ ] Connect agents to real APIs
- [ ] Add authentication, permissions, and human approval
- [ ] Handle failures, retries, and timeouts
- [ ] Evaluate agent quality with a real test dataset
- [ ] Defend against prompt injection and unsafe tool use
- [ ] Deploy agents and monitor them
- [ ] Explain my architecture confidently in an interview

---

## 🧠 Learning Method

Every concept follows this loop:

```text
CONCEPT → Simple explanation → Real-world analogy → Tiny Python example
   → I write the code → Mini exercise → Debugging → Real project → Interview questions
```

### The Six-Question Rule

A concept counts as "learned" only if I can answer all six:

1. What is it?
2. Why do we need it?
3. How does it work?
4. When should I use it?
5. What problem does it solve?
6. Can I build a tiny version myself?

### Build manually first, framework second

I implement the agent loop by hand **before** using LangGraph or any framework, so I understand what the framework is doing for me.

---

## 🗓️ 90-Day Timeline

| Weeks | Days | Stage | Focus | Project |
|------|------|-------|-------|---------|
| 1 | 1–7 | **0** | Developer foundation (Python, async, FastAPI, Git, Docker) | P1 |
| 2 | 8–14 | **1** | LLM fundamentals, API usage, streaming | P2 |
| 3 | 15–21 | **2** | Structured outputs (Pydantic, JSON schemas, validation) | P3 |
| 4 | 22–28 | **3** | Tool calling and the agent loop | P4 |
| 5–6 | 29–42 | **4** | RAG: embeddings, chunking, vector DBs, reranking | P5 |
| 7 | 43–49 | **5** | Agent + RAG, memory, citations | P6 |
| 8 | 50–56 | **6** | Agent architecture: state, memory, planning (from scratch) | — |
| 9 | 57–63 | **7** | LangGraph: nodes, edges, checkpoints, human-in-the-loop | P7 |
| 10 | 64–70 | **8** | Multi-agent systems | P8 |
| 11 | 71–77 | **9** | Coding agents (sandboxed) | P9 |
| 12 | 78–84 | **10** | Production AI: security, observability, evaluation | P15 (start) |
| 13 | 85–90 | — | Deployment, polish, demo videos, interview prep | P15 (finish) |

> **Reality check:** 15 projects in 90 days is unrealistic without sacrificing quality. The **core track** is Projects 1–9 plus the Project 15 capstone. Projects 10–14 are **stretch goals** to complete after Day 90, or earlier if I'm ahead. Eight to ten projects I can explain and defend beat fifteen shallow ones.

---

## 🗺️ Stages in Detail

### Stage 0 — Developer Foundation
- **Python:** functions, classes/OOP, exceptions, modules, type hints, `async/await`, decorators, generators, virtual environments, package management
- **Web/API:** HTTP, REST, JSON, authentication, API keys, webhooks
- **FastAPI:** routes, Pydantic, request/response models, dependencies, error handling, middleware, async endpoints
- **Git:** branches, pull requests, GitHub workflow
- 🏗️ **Project 1:** Production Todo API (CRUD → Pydantic → DB → Auth → Docker)

### Stage 1 — LLM Fundamentals
- Tokens, context window, temperature, system/user/assistant messages
- Calling an LLM from Python, streaming, JSON output
- Error handling, retries, token and cost awareness
- 🏗️ **Project 2:** AI Chat API (streaming, history, system prompt, auth)

### Stage 2 — Structured Outputs
- Schemas, Pydantic models, structured generation, validation
- 🏗️ **Project 3:** AI Resume Analyzer (`POST /analyze-resume` returns skills, experience, education, missing skills)

### Stage 3 — Tool Calling
- LLM chooses a tool → arguments → Python function → result → LLM answers
- Error handling and multi-tool requests
- 🏗️ **Project 4:** Personal AI Assistant (calculator, search, weather)

### Stage 4 — RAG
- Embeddings, chunking, metadata, vector databases, similarity search, reranking, context construction, hallucination reduction
- 🏗️ **Project 5:** Chat With Your Documents (PDF/DOCX/TXT, citations, source pages, metadata filtering)

### Stage 5 — Agent + RAG
- Agent decides *whether* it needs documents, then retrieves
- 🏗️ **Project 6:** Company Knowledge Agent (RAG + tools + memory + citations + auth)

### Stage 6 — Agent Architecture
- The agent loop, state management, short-term vs long-term memory, planning

```text
while not finished:
    understand → decide → use_tool → observe
```

### Stage 7 — Agent Frameworks (LangGraph)
- Nodes, edges, state, conditional routing, persistence, checkpoints, human-in-the-loop
- 🏗️ **Project 7:** Web Research Agent (plan → search → read → analyze → write report with citations)

### Stage 8 — Advanced / Multi-Agent Systems
- Manager, researcher, writer, reviewer roles
- Each agent has a role, tools, instructions, and an output format
- Human approval for high-risk actions (e.g., sending email)
- 🏗️ **Project 8:** Multi-Agent Research Team

### Stage 9 — Coding Agents
- Read repo → understand → find issue → edit files → run tests → read errors → fix → re-run
- Start in a **sandboxed repository** to learn permissions and safety
- 🏗️ **Project 9:** AI Coding Agent

### Stage 10 — Production AI
- **Reliability:** retries, timeouts, fallbacks, validation
- **Security:** prompt injection, tool permissions, data leakage, authN/authZ, sandboxing
- **Observability:** what did the agent do, why that tool, how much did it cost, where did it fail, how long did it take
- **Evaluation:** 100+ test cases measuring accuracy, tool selection, latency, cost, and failure rate

---

## 🚀 Project Portfolio

| # | Project | Main Skills | Track | Status |
|---|---------|-------------|-------|--------|
| 1 | Production Todo API | Python, FastAPI, DB, Docker | Core | ⬜ |
| 2 | AI Chat API | LLM, streaming, FastAPI | Core | ⬜ |
| 3 | AI Resume Analyzer | Structured outputs | Core | ⬜ |
| 4 | Personal AI Assistant | Tool calling | Core | ⬜ |
| 5 | Document RAG Chatbot | RAG, vector DB | Core | ⬜ |
| 6 | Company Knowledge Agent | Agent + RAG + memory | Core | ⬜ |
| 7 | Web Research Agent | Planning, LangGraph | Core | ⬜ |
| 8 | Multi-Agent Research Team | Multi-agent orchestration | Core | ⬜ |
| 9 | AI Coding Agent | Code tools, testing, sandboxing | Core | ⬜ |
| 10 | Customer Support Agent | RAG + tools + memory | Stretch | ⬜ |
| 11 | SQL Data Analyst Agent | SQL, tools, security | Stretch | ⬜ |
| 12 | AI Email Agent | APIs, human approval | Stretch | ⬜ |
| 13 | E-commerce Agent | APIs, workflows | Stretch | ⬜ |
| 14 | Autonomous Research Platform | Advanced orchestration | Stretch | ⬜ |
| 15 | Production Agent Platform | Full-stack, deployment, evals | **Capstone** | ⬜ |

### Capstone Architecture (Project 15)

```text
                     USER
                       ↓
                  FastAPI API
                       ↓
                 Authentication
                       ↓
                  Agent Router
                       ↓
             ┌─────────┴─────────┐
             ↓                   ↓
        Research Agent      Support Agent
             ↓                   ↓
          Tools                 RAG
             ↓                   ↓
             └─────────┬─────────┘
                       ↓
                    Memory
                       ↓
                 Human Approval
                       ↓
                    Result
                       ↓
             Evaluation + Observability
```

---

## ✅ "Definition of Done" for Every Serious Project

A project is not finished until it has:

- [ ] `README.md` with problem, features, setup, and usage
- [ ] Architecture diagram
- [ ] Clean source code
- [ ] API documentation
- [ ] `.env.example` (never commit real keys)
- [ ] `Dockerfile`
- [ ] Automated tests
- [ ] Evaluation dataset and results
- [ ] Screenshots
- [ ] Demo video
- [ ] Live deployment link

---

## 📁 Repository Structure

```text
90-days-agentic-ai/
├── README.md
├── docs/
│   ├── roadmap.md
│   ├── notes/                  # concept notes (six-question rule)
│   └── interview-questions/
├── projects/
│   ├── 01-todo-api/
│   ├── 02-ai-chat-api/
│   ├── 03-resume-analyzer/
│   ├── 04-personal-ai-agent/
│   ├── 05-rag-document-chatbot/
│   ├── 06-company-knowledge-agent/
│   ├── 07-research-agent/
│   ├── 08-multi-agent-system/
│   ├── 09-coding-agent/
│   ├── 10-customer-support-agent/     # stretch
│   ├── 11-sql-agent/                  # stretch
│   ├── 12-email-agent/                # stretch
│   ├── 13-ecommerce-agent/            # stretch
│   ├── 14-autonomous-research/        # stretch
│   └── 15-production-agent-platform/  # capstone
└── progress/
    └── weekly-log.md
```

---

## 🔁 Weekly Rhythm

| Day | Activity |
|-----|----------|
| Mon–Thu | Learn + code (2–3 hrs/day) |
| Fri | Mini project |
| Sat | Main project work |
| Sun | Revision + interview questions |

Weekly loop: **Learn → Code → Build → Break → Debug → Review → Explain**

---

## 💼 Interview Prep (Starts Early, Not at the End)

After every major project I complete:

- [ ] 10 real interview questions on the topic
- [ ] 1 debugging challenge
- [ ] 1 system-design question
- [ ] 1 small coding test
- [ ] A 2-minute verbal explanation of the architecture

---

## 🔒 Future-Proofing Principles

Agent tech changes fast. I'm optimizing for skills that outlast any single framework:

1. **Understand the loop, not the library.** Frameworks change; state, tools, memory, and planning don't.
2. **Security by default.** Least-privilege tools, human approval for risky actions, prompt-injection defenses, sandboxed execution.
3. **Measure, don't guess.** Every agent gets an evaluation set and cost/latency tracking.
4. **Stay model-agnostic.** Wrap LLM providers behind a thin interface so swapping models is cheap.
5. **Prefer open standards** (e.g., MCP-style tool interfaces) where they fit.

---

## 📊 Progress Tracker

- [ ] Stage 0 — Developer Foundation
- [ ] Stage 1 — LLM Fundamentals
- [ ] Stage 2 — Structured Outputs
- [ ] Stage 3 — Tool Calling
- [ ] Stage 4 — RAG
- [ ] Stage 5 — Agent + RAG
- [ ] Stage 6 — Agent Architecture
- [ ] Stage 7 — LangGraph
- [ ] Stage 8 — Multi-Agent Systems
- [ ] Stage 9 — Coding Agents
- [ ] Stage 10 — Production AI
- [ ] Capstone deployed
- [ ] Interview-ready

---

## 🛠️ Tech Stack

**Languages & Backend:** Python, FastAPI, Pydantic, async I/O
**AI:** LLM APIs, embeddings, vector databases, LangGraph
**Data:** PostgreSQL, vector search (e.g., pgvector)
**DevOps:** Git, GitHub, Docker, CI, cloud deployment
**Testing & Evals:** pytest, custom evaluation harness

---

## 🤝 Connect

- GitHub: [`@your-username`](https://github.com/your-username)
- LinkedIn: [your-profile](https://linkedin.com/in/your-profile)
- Portfolio: [your-site.com](https://your-site.com)

---

## 📄 License

This project is licensed under the MIT License. See [LICENSE](LICENSE) for details.

---

⭐ If this roadmap helps you, consider starring the repo and following along.
