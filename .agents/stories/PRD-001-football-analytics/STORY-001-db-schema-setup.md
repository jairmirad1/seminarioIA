---
id: STORY-001
prd: PRD-001
slug: db-schema-setup
title: Setup Database Schema for Football Analytics
type: technical
priority: high
complexity: small
phase: "1"
status: done
labels: [backend, database]
epic_branch: epic/PRD-001-football-analytics
plan: .agents/plans/PRD-001-football-analytics/completed/STORY-001-db-schema-setup.plan.md
report: .agents/reports/PRD-001-football-analytics/STORY-001-db-schema-setup.report.md
commit: 225d2025dccb0af96f963f3db865d1b42781522f
depends_on: []
blocks: [STORY-002]
skills: [fastapi-python]
created: 2026-05-27
updated: 2026-05-27
---

# STORY-001: Setup Database Schema for Football Analytics

## Description

As a developer, I want to define the relational database schema for football data, so that the AI agent has a clear structure to reference when generating SQL.

## Acceptance Criteria

- [ ] Given a set of requirements, when I define the schema, then it must include tables for teams, players, matches, and statistics.
- [ ] Given the schema definition, when I create a DDL file, then it must be compatible with SQLite (for local dev) and PostgreSQL (reference).
- [ ] Given the database structure, when I run the creation script, then all tables and constraints must be correctly established.

## Technical Notes

- Use SQLAlchemy models or a raw SQL DDL file in `backend/app/models/`.
- Ensure foreign keys and common indexes are defined (e.g., player_id, team_id).
- Follow the `snake_case` convention for table and column names.

## Dependencies

- **Blocked by**: None
- **Blocks**: STORY-002

## PRD Reference

Source: [PRD-001/PRD.md](../../PRDs/PRD-001-football-analytics/PRD.md) — section 12 (Phase 1)
