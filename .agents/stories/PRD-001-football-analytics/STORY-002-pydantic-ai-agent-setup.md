---
id: STORY-002
prd: PRD-001
slug: pydantic-ai-agent-setup
title: Setup Pydantic AI Agent for SQL Generation
type: feature
priority: high
complexity: medium
phase: "2"
status: done
labels: [backend, ai]
epic_branch: epic/PRD-001-football-analytics
plan: .agents/plans/PRD-001-football-analytics/completed/STORY-002-pydantic-ai-agent-setup.plan.md
report: .agents/reports/PRD-001-football-analytics/STORY-002-pydantic-ai-agent-setup.report.md
commit: e4a4c23d3f6b0a2b09c5c878f20b948bcc956ee3
depends_on: [STORY-001]
blocks: [STORY-003]
skills: [building-pydantic-ai-agents, fastapi-python]
created: 2026-05-27
updated: 2026-05-27
---

# STORY-002: Setup Pydantic AI Agent for SQL Generation

## Description

As a developer, I want to configure a Pydantic AI agent with the database schema context, so that it can translate Spanish questions into valid SQL SELECT queries.

## Acceptance Criteria

- [ ] Given a user prompt in Spanish, when the agent processes it, then it returns a valid SQL SELECT statement.
- [ ] Given the agent configuration, when it's initialized, then it includes the database schema DDL in its system instructions.
- [ ] Given the agent output, when it returns a query, then it is strictly a SELECT statement and does not include DML/DDL.

## Technical Notes

- Use `pydantic-ai` to define the agent.
- Model: `google-gla:gemini-1.5-flash`.
- System prompt should emphasize Spanish-to-SQL translation and safety (SELECT only).
- Reference `building-pydantic-ai-agents` skill for agent patterns.

## Dependencies

- **Blocked by**: STORY-001
- **Blocks**: STORY-003

## PRD Reference

Source: [PRD-001/PRD.md](../../PRDs/PRD-001-football-analytics/PRD.md) — section 6, 12 (Phase 2)
