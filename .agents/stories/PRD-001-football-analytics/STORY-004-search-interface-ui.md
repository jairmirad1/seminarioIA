---
id: STORY-004
prd: PRD-001
slug: search-interface-ui
title: Create Search Interface with React and shadcn/ui
type: feature
priority: medium
complexity: medium
phase: "3"
status: todo
labels: [frontend, ui]
epic_branch: epic/PRD-001-football-analytics
plan: null
report: null
commit: null
depends_on: [STORY-003]
blocks: [STORY-005]
skills: [shadcn, react-router-declarative-mode, vercel-react-best-practices]
created: 2026-05-27
updated: 2026-05-27
---

# STORY-004: Create Search Interface with React and shadcn/ui

## Description

As a user, I want a clean search bar and a button to submit my questions, so that I can interact with the system.

## Acceptance Criteria

- [ ] Given the home page, when the user visits it, then it shows a prominent search input.
- [ ] Given a search query, when the user clicks "Generate SQL", then it triggers a request to the backend.
- [ ] Given a pending request, when the system is processing, then it shows a loading state (e.g., Skeleton or Spinner).

## Technical Notes

- Use `Input` and `Button` components from `shadcn/ui`.
- Follow `vercel-react-best-practices` for state management and fetching.
- Implement in a new page `frontend/src/pages/FootballAnalytics.jsx`.

## Dependencies

- **Blocked by**: STORY-003
- **Blocks**: STORY-005

## PRD Reference

Source: [PRD-001/PRD.md](../../PRDs/PRD-001-football-analytics/PRD.md) — section 4, 12 (Phase 3)
