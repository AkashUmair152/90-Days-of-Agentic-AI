# 🤖 90 Days of Mastering Agentic AI

**My journey to build deployable, full-stack AI Agent applications using Python, FastAPI, PostgreSQL/pgvector, LangGraph, and Next.js.**

[![LinkedIn](https://img.shields.io/badge/Connect%20on-LinkedIn-blue?style=flat&logo=linkedin)](YOUR_LINKEDIN_PROFILE)
[![#90DaysOfAgenticAI](https://img.shields.io/badge/%23-90DaysOfAgenticAI-000000.svg?style=flat&logo=codecademy)](https://github.com/topics/agentic-ai)
[![#BuildInPublic](https://img.shields.io/badge/%23-BuildInPublic-FF6F00.svg?style=flat&logo=python&logoColor=white)](https://github.com/topics/agentic-ai)

> **Focus:** This is not a "learn AI" challenge — it's a "build production-grade agents" challenge. Every day ends in code, not just notes. No niche or legacy tools — the stack is chosen based on what's actually used in AI agent production in 2026 (Python, FastAPI, LangGraph, pgvector).

## 📊 Progress Tracker

| Month | Weeks | Days | Focus | Status |
| :--- | :--- | :--- | :--- | :--- |
| **Month 1** | Weeks 1-4 | Days 1 - 30 | FastAPI + LLM + Agent Foundations | 🟡 In Progress |
| **Month 2** | Weeks 5-8 | Days 31 - 60 | pgvector + Retrieval (RAG) | ⏳ Upcoming |
| **Month 3** | Weeks 9-12 | Days 61 - 90 | Next.js + Full-Stack + Deployment | ⏳ Upcoming |

## 📅 Detailed Progress Log

### Month 1 (Days 1-30): FastAPI + LLM + Agent Foundations

#### 🟡 Week 1 (Days 1-7): FastAPI + Calling LLMs

- [ ] **Day 1:** Python async fundamentals (`async`/`await`) + FastAPI setup, routing, Pydantic models
- [ ] **Day 2:** FastAPI deeper: path/query params, dependency injection, error handling — mini CRUD API
- [ ] **Day 3:** Anthropic + OpenAI SDKs — message roles, system prompts, first `/chat` endpoint
- [ ] **Day 4:** Streaming responses with `StreamingResponse` (SSE) — convert `/chat` to stream tokens
- [ ] **Day 5:** Function/tool calling — the core agent skill (LLM decides, your code executes)
- [ ] **Day 6:** Pydantic for structured, validated LLM outputs
- [ ] **Day 7:** Review + practice: rebuild Days 3-6 from memory, no reference

#### ⏳ Week 2 (Days 8-14): First Real Agents

- [ ] **Day 8:** Intro to LangGraph — nodes, edges, state
- [ ] **Day 9:** Re-implement Day 5's tool-calling agent using LangGraph
- [ ] **Day 10:** Multi-tool agents — agent loop: call LLM → check tool → run → feed back → repeat
- [ ] **Day 11:** Production basics: retries, rate-limit handling, structured logging of tool calls
- [ ] **Day 12:** Mini Project — end-to-end tool-using agent (streaming + LangGraph + logging)
- [ ] **Day 13:** Debug/catch-up day — fix what broke in Day 12
- [ ] **Day 14:** Write up Day 12 project (README + short demo) — first portfolio piece

#### ⏳ Week 3 (Days 15-21): Multi-Agent Systems (CrewAI)

- [ ] **Day 15:** What are multi-agent systems? When one agent isn't enough (conceptual)
- [ ] **Day 16:** CrewAI overview: Agents, Tasks, Crews
- [ ] **Day 17:** CrewAI setup + first agent
- [ ] **Day 18:** Defining tasks & creating a crew (2+ agents collaborating)
- [ ] **Day 19:** Tool use inside CrewAI agents
- [ ] **Day 20:** Integrating CrewAI agents with your LangGraph/tool-calling code from Week 2
- [ ] **Day 21:** Mini Project — simple autonomous task-planner using CrewAI

#### ⏳ Week 4 (Days 22-30): Consolidation + Phase 1 Capstone

- [ ] **Day 22:** Review: FastAPI + LLM calls + streaming (no notes, rebuild from scratch)
- [ ] **Day 23:** Review: tool calling + LangGraph agent loop
- [ ] **Day 24:** Review: CrewAI multi-agent basics
- [ ] **Day 25:** Plan Phase 1 capstone: pick a real problem to solve with an agent
- [ ] **Day 26:** Build capstone — backend + agent logic
- [ ] **Day 27:** Build capstone — streaming, error handling, logging
- [ ] **Day 28:** Polish capstone — Swagger docs, README
- [ ] **Day 29:** Debug/catch-up day
- [ ] **Day 30:** Ship Phase 1 capstone + LinkedIn post on what was built

### Month 2 (Days 31-60): pgvector + Retrieval (RAG)

#### ⏳ Week 5 (Days 31-37): PostgreSQL + pgvector Setup

- [ ] **Day 31:** PostgreSQL refresher — tables, queries (if rusty)
- [ ] **Day 32:** Install pgvector, enable extension, understand vector columns
- [ ] **Day 33:** Distance functions: cosine vs L2 — when each matters
- [ ] **Day 34:** Manual practice: insert vectors, run similarity queries
- [ ] **Day 35:** Connect FastAPI to Postgres/pgvector (SQLAlchemy or `asyncpg`)
- [ ] **Day 36:** Practice: store/query vectors via FastAPI endpoints
- [ ] **Day 37:** Review + catch-up

#### ⏳ Week 6 (Days 38-44): Embeddings + Chunking

- [ ] **Day 38:** What embeddings are, how they're generated (OpenAI/Anthropic/local models)
- [ ] **Day 39:** Chunking strategies — why chunk size affects retrieval quality
- [ ] **Day 40:** Practice: extract text from a PDF, chunk it
- [ ] **Day 41:** Practice: embed chunks, store in pgvector
- [ ] **Day 42:** Query embedding → similarity search — first end-to-end retrieval test
- [ ] **Day 43:** Evaluate retrieval quality — is the right chunk coming back?
- [ ] **Day 44:** Review + catch-up

#### ⏳ Week 7 (Days 45-51): Full RAG Pipeline

- [ ] **Day 45:** Wire retrieval into LLM prompt — basic RAG loop
- [ ] **Day 46:** Handle multi-document retrieval (more than one PDF/source)
- [ ] **Day 47:** Streaming RAG answers back through FastAPI
- [ ] **Day 48:** Combine RAG with tool calling — agent that can retrieve AND act
- [ ] **Day 49:** Error handling for RAG (empty results, irrelevant context)
- [ ] **Day 50:** Practice: rebuild the RAG loop from scratch, no reference
- [ ] **Day 51:** Review + catch-up

#### ⏳ Week 8 (Days 52-60): Phase 2 Capstone

- [ ] **Day 52:** Plan capstone: AI document Q&A tool (upload → parse → embed → query → answer)
- [ ] **Day 53:** Build: upload + parsing pipeline
- [ ] **Day 54:** Build: chunking + embedding + pgvector storage
- [ ] **Day 55:** Build: retrieval + streamed LLM answers
- [ ] **Day 56:** Add error handling, logging
- [ ] **Day 57:** Polish: Swagger docs, README, short demo
- [ ] **Day 58:** Debug/catch-up day
- [ ] **Day 59:** Peer review / self-review against Week 7's eval checklist
- [ ] **Day 60:** Ship Phase 2 capstone + LinkedIn post

### Month 3 (Days 61-90): Next.js + Full-Stack Integration + Deployment

#### ⏳ Week 9 (Days 61-67): Next.js Essentials

- [ ] **Day 61:** Next.js setup, App Router, Server vs Client Components
- [ ] **Day 62:** Calling the FastAPI backend from Next.js
- [ ] **Day 63:** Building basic UI: forms, chat-style layout
- [ ] **Day 64:** Styling with TailwindCSS
- [ ] **Day 65:** Practice: build a UI for Phase 1's capstone agent
- [ ] **Day 66:** Practice: build a UI for Phase 2's RAG tool
- [ ] **Day 67:** Review + catch-up

#### ⏳ Week 10 (Days 68-74): Streaming UI + File Upload

- [ ] **Day 68:** Consuming SSE streams in the frontend (token-by-token rendering)
- [ ] **Day 69:** Drag-and-drop file upload component
- [ ] **Day 70:** Connect upload → FastAPI → pgvector pipeline end-to-end
- [ ] **Day 71:** Loading states, error states, UX polish
- [ ] **Day 72:** Practice: full chat UI with streaming + file upload combined
- [ ] **Day 73:** Cross-browser/device testing
- [ ] **Day 74:** Review + catch-up

#### ⏳ Week 11 (Days 75-81): Auth + Deployment

- [ ] **Day 75:** Basic auth (NextAuth or JWT against FastAPI)
- [ ] **Day 76:** Environment variables, secrets management for production
- [ ] **Day 77:** Deploy FastAPI (Railway/Render/Fly.io)
- [ ] **Day 78:** Deploy Postgres + pgvector (Supabase/Neon)
- [ ] **Day 79:** Deploy Next.js frontend (Vercel)
- [ ] **Day 80:** End-to-end test of the deployed stack
- [ ] **Day 81:** Review + catch-up

#### ⏳ Week 12 (Days 82-90): Final Capstone + Portfolio

- [ ] **Day 82:** Plan final capstone: combine agent + RAG + full-stack UI into one polished app
- [ ] **Day 83:** Build: backend integration (agent + RAG + tool calling)
- [ ] **Day 84:** Build: frontend integration (streaming UI + upload + auth)
- [ ] **Day 85:** Deploy full stack end-to-end
- [ ] **Day 86:** Polish: error handling, edge cases, UX
- [ ] **Day 87:** Write case-study documentation (architecture, decisions, what was hard)
- [ ] **Day 88:** Record a short demo video
- [ ] **Day 89:** Publish portfolio write-up on LinkedIn
- [ ] **Day 90:** Final review — what's next after Day 90

## 🎯 Challenge Goals

- Build a solid async **FastAPI** foundation for AI backends
- Learn to call and stream responses from **LLM APIs** (Anthropic/OpenAI)
- Master **function/tool calling** — the core skill that makes an agent an agent
- Get hands-on with **LangGraph** for stateful single-agent workflows
- Get hands-on with **CrewAI** for multi-agent collaboration
- Learn **PostgreSQL + pgvector** for production-grade RAG, without a separate vector DB
- Build a full **retrieval-augmented generation (RAG)** pipeline from scratch
- Learn **Next.js** well enough to ship a real, streaming, full-stack AI UI
- Deploy a complete stack (FastAPI + Postgres + Next.js) to production
- Ship **3 portfolio-ready capstone projects**, one per month
- Build in public — document and share progress on LinkedIn throughout

## 🗺️ The Roadmap

### Month 1 (Days 1-30): FastAPI + LLM + Agent Foundations
Solidify async FastAPI, learn to call and stream LLM responses, and build the core agent skill — function/tool calling — using LangGraph and CrewAI.

### Month 2 (Days 31-60): pgvector + Retrieval (RAG)
Set up PostgreSQL + pgvector, learn embeddings and chunking, and build a full RAG pipeline that lets an agent answer questions grounded in real documents.

### Month 3 (Days 61-90): Next.js + Full-Stack Integration + Deployment
Learn Next.js, build a streaming chat UI with file upload, add auth, and deploy the complete stack to production — turning all three months of work into one polished, shippable application.

## 📁 Repository Structure

```
/day-01-07/     FastAPI basics, LLM calls, streaming
/day-08-14/     Tool calling, LangGraph, first agent project
/day-15-21/     Multi-agent systems (CrewAI)
/day-22-30/     Phase 1 capstone project
/day-31-37/     PostgreSQL + pgvector setup
/day-38-44/     Embeddings + chunking
/day-45-51/     Full RAG pipeline
/day-52-60/     Phase 2 capstone project
/day-61-67/     Next.js essentials
/day-68-74/     Streaming UI + file upload
/day-75-81/     Auth + deployment
/day-82-90/     Final capstone project + portfolio
```

*(Folders and checkboxes fill in as each day is completed — this is a living repo, updated daily.)*

---

⭐ Follow along or fork this if you're on a similar path.
