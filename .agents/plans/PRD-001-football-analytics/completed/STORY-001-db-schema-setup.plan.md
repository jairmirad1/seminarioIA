---
story: STORY-001
prd: PRD-001
slug: db-schema-setup
title: Setup Database Schema for Football Analytics
type: REFACTOR
complexity: LOW
epic_branch: epic/PRD-001-football-analytics
created: 2026-05-27
---

# Plan: Setup Database Schema for Football Analytics

## Summary

We will design the football schema using SQLAlchemy models (`equipos`, `jugadores`, `partidos`, `estadisticas`) to ensure programmatic control, easy foreign key management, and cross-compatibility between SQLite and PostgreSQL. Then, we will create a script to dump the explicit SQL DDL to a `.sql` file, which will serve as the system prompt context for the Pydantic AI agent in the next story. Finally, we'll write an initialization script to create these tables in the local database.

## User Story

As a developer
I want to define the relational database schema for football data
So that the AI agent has a clear structure to reference when generating SQL

## Story Reference

- Story file: `.agents/stories/PRD-001-football-analytics/STORY-001-db-schema-setup.md`
- PRD: `.agents/PRDs/PRD-001-football-analytics/PRD.md`

## Metadata

| Field | Value |
|-------|-------|
| Type | REFACTOR |
| Complexity | LOW |
| Systems Affected | Backend Database |
| Story | STORY-001 |
| PRD | PRD-001 |
| Epic Branch | `epic/PRD-001-football-analytics` (commit directly on this branch) |

---

## Skills In Use

| Skill | Why it applies | Tasks affected |
|-------|---------------|----------------|
| fastapi-python | Enforces concise, functional, typed Python patterns and SQLAlchemy 2.0 best practices | Task 1, 2, 3 |

---

## Patterns to Follow

### Naming
```python
// SOURCE: backend/app/models/pais.py:6-12
class Pais(Base):
    __tablename__ = "paises"

    id: Mapped[int] = mapped_column(primary_key=True, index=True)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False, unique=True, index=True)
```

---

## Files to Change

| File | Action | Purpose |
|------|--------|---------|
| `backend/app/models/football.py` | CREATE | SQLAlchemy models for Equipo, Jugador, Partido, Estadistica |
| `backend/app/models/__init__.py` | UPDATE | Export the new models |
| `backend/scripts/generate_ddl.py` | CREATE | Script to export the schema DDL to a text file for the agent context |
| `backend/scripts/init_db.py` | CREATE | Script to execute table creation on the local database |

---

## Tasks

### Task 1: Create Football SQLAlchemy Models

- **File**: `backend/app/models/football.py`
- **Action**: CREATE
- **Implement**: Define classes `Equipo`, `Jugador`, `Partido`, and `Estadistica` inheriting from `Base` (from `app.core.database`). Use `Mapped` and `mapped_column` with explicit foreign keys.
  - `Equipo`: id, nombre, ciudad, estadio.
  - `Jugador`: id, nombre, posicion, equipo_id, numero_camiseta.
  - `Partido`: id, equipo_local_id, equipo_visitante_id, fecha, goles_local, goles_visitante.
  - `Estadistica`: id, partido_id, jugador_id, goles, asistencias, tarjetas_amarillas, tarjetas_rojas, minutos_jugados.
- **Mirror**: `backend/app/models/pais.py:6-12`

### Task 2: Export Models

- **File**: `backend/app/models/__init__.py`
- **Action**: UPDATE
- **Implement**: Import and expose the new models (`Equipo`, `Jugador`, `Partido`, `Estadistica`) and the existing `Pais` model to ensure they register correctly with SQLAlchemy's `Base.metadata`.

### Task 3: Create DDL Export Script

- **File**: `backend/scripts/generate_ddl.py`
- **Action**: CREATE
- **Implement**: Write a script that uses SQLAlchemy's `schema.CreateTable` and a Mock engine/dialect to generate raw SQL string from `Base.metadata` and writes it to `backend/app/models/football_schema.sql`. This file acts as the schema contract required by the agent.

### Task 4: Create DB Initialization Script

- **File**: `backend/scripts/init_db.py`
- **Action**: CREATE
- **Implement**: Write a script that imports `engine` from `app.core.database` and calls `Base.metadata.create_all(bind=engine)`. Add a brief success print statement.
- **Validate**: Run `python -m scripts.init_db` from the `backend` directory.

---

## End-to-End Tests

- [ ] Execute `cd backend && python -m scripts.generate_ddl` -> confirms `backend/app/models/football_schema.sql` is generated.
- [ ] Execute `cd backend && python -m scripts.init_db` -> confirms database is initialized without errors.

---

## Validation

```bash
cd backend
python -m scripts.generate_ddl
python -m scripts.init_db
uvicorn app.main:app --reload & sleep 2 && kill $!
```

---

## Acceptance Criteria

- [x] Given a set of requirements, when I define the schema, then it must include tables for teams, players, matches, and statistics.
- [x] Given the schema definition, when I create a DDL file, then it must be compatible with SQLite (for local dev) and PostgreSQL (reference).
- [x] Given the database structure, when I run the creation script, then all tables and constraints must be correctly established.
- [x] All tasks completed
- [x] Follows existing patterns
