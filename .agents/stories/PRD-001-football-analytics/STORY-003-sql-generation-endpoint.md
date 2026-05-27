---
id: STORY-003
prd: PRD-001
slug: sql-generation-endpoint
title: Create SQL Generation Endpoint in FastAPI
type: feature
priority: high
complexity: small
phase: "2"
status: done
labels: [backend, api]
epic_branch: epic/PRD-001-football-analytics
plan: .agents/plans/PRD-001-football-analytics/completed/STORY-003-sql-generation-endpoint.plan.md
report: .agents/reports/PRD-001-football-analytics/STORY-003-sql-generation-endpoint.report.md
commit: e4e7a3cb9de32fd926da7c18985499a07e7d0e88
depends_on: [STORY-002]
blocks: [STORY-004]
skills: [fastapi-python]
created: 2026-05-27
updated: 2026-05-27
---

# STORY-003: Create SQL Generation Endpoint in FastAPI

## Description

As a frontend developer, I want a REST endpoint to send user prompts and receive generated SQL, so that I can display it in the UI.

## Acceptance Criteria

- [ ] Given a POST request to `/api/v1/generate-sql`, when a prompt is provided, then it returns a 200 status code with the generated SQL.
- [ ] Given an invalid request, when the input validation fails, then it returns a 422 Unprocessable Entity error.
- [ ] Given the API response, when the agent fails to generate SQL, then it returns a clear error message.

## Technical Notes

- Implement in `backend/app/routers/sql_generator.py` (new file).
- Use Pydantic schemas for request and response validation.
- Register the router in `app/main.py`.

## Dependencies

- **Blocked by**: STORY-002
- **Blocks**: STORY-004

## PRD Reference

Source: [PRD-001/PRD.md](../../PRDs/PRD-001-football-analytics/PRD.md) — section 10, 12 (Phase 2)
