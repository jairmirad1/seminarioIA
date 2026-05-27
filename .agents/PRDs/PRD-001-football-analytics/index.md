# PRD-001: Football Analytics — Story Board

**PRD**: [PRD.md](./PRD.md)
**Epic Branch**: `epic/PRD-001-football-analytics` (base: `main`)
**Status**: active

## Progress

3/5 stories done — 60%

## Stories

All stories commit on the epic branch `epic/PRD-001-football-analytics`. No per-story branches.

| ID | Title | Type | Status | Complexity | Plan | Commit |
|----|-------|------|--------|------------|------|--------|
| STORY-001 | Setup Database Schema for Football Analytics | technical | ✅ done | small | [plan](../../plans/PRD-001-football-analytics/completed/STORY-001-db-schema-setup.plan.md) | `225d202` |
| STORY-002 | Setup Pydantic AI Agent for SQL Generation | feature | ✅ done | medium | [plan](../../plans/PRD-001-football-analytics/completed/STORY-002-pydantic-ai-agent-setup.plan.md) | `e4a4c23` |
| STORY-003 | Create SQL Generation Endpoint in FastAPI | feature | ✅ done | small | [plan](../../plans/PRD-001-football-analytics/completed/STORY-003-sql-generation-endpoint.plan.md) | `e4e7a3c` |
| STORY-004 | Create Search Interface with React and shadcn/ui | feature | ⬜ todo | medium | — | — |
| STORY-005 | Create SQL Result Panel with Syntax Highlighting | feature | ⬜ todo | small | — | — |

## Status Icons
- ⬜ todo
- 🟡 in-progress
- ✅ done
- 🔴 blocked

## Dependencies

- STORY-002 blocked by STORY-001
- STORY-003 blocked by STORY-002
- STORY-004 blocked by STORY-003
- STORY-005 blocked by STORY-004
