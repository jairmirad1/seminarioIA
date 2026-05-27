---
story: STORY-003
prd: PRD-001
slug: sql-generation-endpoint
title: Create SQL Generation Endpoint in FastAPI
type: FEATURE
complexity: LOW
epic_branch: epic/PRD-001-football-analytics
created: 2026-05-27
---

# Plan: Create SQL Generation Endpoint in FastAPI

## Summary

We will create a new REST API endpoint `POST /api/v1/generate-sql` using FastAPI. This endpoint will receive a natural language prompt from the user, pass it to the previously configured Pydantic AI agent, and return the generated SQL and explanation. We will use Pydantic schemas for request validation.

## User Story

As a frontend developer
I want a REST endpoint to send user prompts and receive generated SQL
So that I can display it in the UI

## Story Reference

- Story file: `.agents/stories/PRD-001-football-analytics/STORY-003-sql-generation-endpoint.md`
- PRD: `.agents/PRDs/PRD-001-football-analytics/PRD.md`

## Metadata

| Field | Value |
|-------|-------|
| Type | FEATURE |
| Complexity | LOW |
| Systems Affected | Backend API |
| Story | STORY-003 |
| PRD | PRD-001 |
| Epic Branch | `epic/PRD-001-football-analytics` (commit directly on this branch) |

---

## Skills In Use

| Skill | Why it applies | Tasks affected |
|-------|---------------|----------------|
| fastapi-python | Defines router structure, dependency injection, exception handling (HTTPException), and strict Pydantic usage. | Task 1, 2, 3 |

---

## Patterns to Follow

### Router Registration
```python
# SOURCE: backend/app/main.py:23
app.include_router(pais_router.router, prefix="/api/v1")
```

### Route Definition
```python
# SOURCE: backend/app/routers/pais.py:12
router = APIRouter(prefix="/paises", tags=["paises"])

@router.post("/", response_model=PaisRead, status_code=status.HTTP_201_CREATED)
def create_pais(data: PaisCreate, db: Session = Depends(get_db)):
    logger.info("POST /paises nombre=%s", data.nombre)
    return svc.create_pais(db, data)
```

---

## Files to Change

| File | Action | Purpose |
|------|--------|---------|
| `backend/app/schemas/ai.py` | UPDATE | Add `SQLGenerationRequest` schema for the incoming payload. |
| `backend/app/routers/sql_generator.py` | CREATE | Define the `POST /generate-sql` route. |
| `backend/app/routers/__init__.py` | UPDATE | Export the new router. |
| `backend/app/main.py` | UPDATE | Register the new router with the FastAPI app. |

---

## Tasks

### Task 1: Add Request Schema

- **File**: `backend/app/schemas/ai.py`
- **Action**: UPDATE
- **Implement**: Add a `SQLGenerationRequest` model extending `BaseModel`. It should contain a single field `prompt: str` with a description. This validates the incoming POST body.

### Task 2: Implement the Router

- **File**: `backend/app/routers/sql_generator.py`
- **Action**: CREATE
- **Implement**:
  - Import `APIRouter`, `HTTPException`, `status` from FastAPI.
  - Import `SQLGenerationRequest` and `SQLGenerationResult` from `app.schemas.ai`.
  - Import `sql_agent` from `app.services.ai.sql_agent`.
  - Initialize the router (without prefix here, we'll mount it directly or via `api/v1` in main). Let's use `router = APIRouter(tags=["sql-generator"])`.
  - Create a route `@router.post("/generate-sql", response_model=SQLGenerationResult)`.
  - Make the handler `async def generate_sql(request: SQLGenerationRequest):`.
  - Inside the handler, try/except around the agent call:
    - Use `result = await sql_agent.run(request.prompt)`
    - Return `result.data`
  - On exception, raise `HTTPException(status_code=500, detail=str(e))`.

### Task 3: Export the Router

- **File**: `backend/app/routers/__init__.py`
- **Action**: UPDATE
- **Implement**: Import `sql_generator` and add it to `__all__`.

### Task 4: Register Router in Main App

- **File**: `backend/app/main.py`
- **Action**: UPDATE
- **Implement**: Import the `sql_generator` router and call `app.include_router(sql_generator.router, prefix="/api/v1")`.

---

## End-to-End Tests

- [ ] Execute `curl -X POST "http://localhost:8000/api/v1/generate-sql" -H "Content-Type: application/json" -d '{"prompt": "equipos"}'`. It should either return the expected JSON or a 500 if the `GOOGLE_API_KEY` is missing, but it must be a valid API response.

---

## Validation

```bash
cd backend
uvicorn app.main:app --reload & sleep 2 && kill $!
```

---

## Acceptance Criteria

- [x] Given a POST request to `/api/v1/generate-sql`, when a prompt is provided, then it returns a 200 status code with the generated SQL.
- [x] Given an invalid request, when the input validation fails, then it returns a 422 Unprocessable Entity error (handled automatically by FastAPI and Pydantic).
- [x] Given the API response, when the agent fails to generate SQL, then it returns a clear error message.
