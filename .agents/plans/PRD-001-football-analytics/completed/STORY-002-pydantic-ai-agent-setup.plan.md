---
story: STORY-002
prd: PRD-001
slug: pydantic-ai-agent-setup
title: Setup Pydantic AI Agent for SQL Generation
type: FEATURE
complexity: MEDIUM
epic_branch: epic/PRD-001-football-analytics
created: 2026-05-27
---

# Plan: Setup Pydantic AI Agent for SQL Generation

## Summary

We will configure a `pydantic-ai` agent that utilizes `google-gla:gemini-1.5-flash` to translate natural language questions in Spanish into valid SQL SELECT queries. The agent will be provided with the previously generated `football_schema.sql` as context. We will define a structured output model to ensure the agent returns the SQL string and a brief explanation.

## User Story

As a developer
I want to configure a Pydantic AI agent with the database schema context
So that it can translate Spanish questions into valid SQL SELECT queries

## Story Reference

- Story file: `.agents/stories/PRD-001-football-analytics/STORY-002-pydantic-ai-agent-setup.md`
- PRD: `.agents/PRDs/PRD-001-football-analytics/PRD.md`

## Metadata

| Field | Value |
|-------|-------|
| Type | FEATURE |
| Complexity | MEDIUM |
| Systems Affected | Backend AI Service |
| Story | STORY-002 |
| PRD | PRD-001 |
| Epic Branch | `epic/PRD-001-football-analytics` (commit directly on this branch) |

---

## Skills In Use

| Skill | Why it applies | Tasks affected |
|-------|---------------|----------------|
| building-pydantic-ai-agents | Provides the core syntax for initializing the `Agent`, defining `output_type` using Pydantic, and structuring instructions. | Task 1, 2 |
| fastapi-python | Influences the location of the logic (creating a new service module) and the use of Pydantic models. | Task 1, 2 |

---

## Patterns to Follow

### Structured Output with Pydantic Models
```python
# SOURCE: building-pydantic-ai-agents skill
from pydantic import BaseModel
from pydantic_ai import Agent

class CityLocation(BaseModel):
    city: str
    country: str

agent = Agent('google-gla:gemini-1.5-flash', output_type=CityLocation)
```

---

## Files to Change

| File | Action | Purpose |
|------|--------|---------|
| `backend/app/schemas/ai.py` | CREATE | Define the Pydantic schema for the agent's output (`SQLGenerationResult`). |
| `backend/app/services/ai/sql_agent.py` | CREATE | Initialize the Pydantic AI agent, load the schema DDL, and set the system instructions. |
| `backend/scripts/test_agent.py` | CREATE | Script to verify the agent works as expected before hooking it up to an endpoint. |

---

## Tasks

### Task 1: Define Output Schema

- **File**: `backend/app/schemas/ai.py`
- **Action**: CREATE
- **Implement**: Create a Pydantic model `SQLGenerationResult` with two fields:
  - `sql`: str (The generated SQL query)
  - `explanation`: str (A brief explanation in Spanish of what the query does)

### Task 2: Implement the Pydantic AI Agent

- **File**: `backend/app/services/ai/sql_agent.py`
- **Action**: CREATE
- **Implement**:
  - Import `Agent` from `pydantic_ai` and `SQLGenerationResult` from the schema.
  - Read the content of `backend/app/models/football_schema.sql` into a string dynamically using `pathlib` relative to the current file.
  - Initialize the `Agent`:
    - `model`: `'google-gla:gemini-1.5-flash'`
    - `output_type`: `SQLGenerationResult`
    - `system_prompt`: Instruct the agent to act as a SQL expert. It must translate questions in Spanish into PostgreSQL-compatible SELECT queries based on the provided schema. Emphasize that it MUST ONLY return SELECT statements and never DML/DDL (no INSERT, UPDATE, DELETE). Include the DDL string dynamically in the instructions. Use the `@agent.system_prompt` decorator for dynamic injection.

### Task 3: Create a Test Script

- **File**: `backend/scripts/test_agent.py`
- **Action**: CREATE
- **Implement**: Write an async script that imports the configured `agent`, runs it using `agent.run_sync()` against a sample query like "¿Cuáles son los equipos de la ciudad de Madrid?", and prints the result's `.output` which should be the `SQLGenerationResult` object.
- **Validate**: Run `python -m scripts.test_agent` from the backend directory to ensure it returns valid structured output.

---

## End-to-End Tests

- [ ] Execute `cd backend && python -m scripts.test_agent` -> confirms the agent connects to Gemini and returns a structured SQL response based on the schema.

---

## Validation

```bash
cd backend
python -m scripts.test_agent
```

---

## Acceptance Criteria

- [x] Given a user prompt in Spanish, when the agent processes it, then it returns a valid SQL SELECT statement.
- [x] Given the agent configuration, when it's initialized, then it includes the database schema DDL in its system instructions.
- [x] Given the agent output, when it returns a query, then it is strictly a SELECT statement and does not include DML/DDL.
