---
id: STORY-005
prd: PRD-001
slug: sql-result-panel
title: Create SQL Result Panel with Syntax Highlighting
type: feature
priority: medium
complexity: small
phase: "3"
status: done
labels: [frontend, ui]
epic_branch: epic/PRD-001-football-analytics
plan: .agents/plans/PRD-001-football-analytics/completed/STORY-005-sql-result-panel.plan.md
report: .agents/reports/PRD-001-football-analytics/STORY-005-sql-result-panel.report.md
commit: 7ff7fe4a57e7d894bec9ab28b5aa01ff2ef668c3
depends_on: [STORY-004]
blocks: []
skills: [shadcn, vercel-react-best-practices]
created: 2026-05-27
updated: 2026-05-27
---

# STORY-005: Create SQL Result Panel with Syntax Highlighting

## Description

As a user, I want to see the generated SQL in a formatted panel, so that it is easy to read and understand.

## Acceptance Criteria

- [ ] Given a successful SQL generation, when the result is received, then it is displayed in a dedicated card.
- [ ] Given the SQL display, when the code is shown, then it has syntax highlighting (e.g., using a library or styled code block).
- [ ] Given an error during generation, when the backend fails, then it shows a clear error alert.

## Technical Notes

- Use `Card` and `Alert` components from `shadcn/ui`.
- Consider using a library like `prismjs` or `react-syntax-highlighter` if needed, or a simple styled `<pre>` tag for MVP.
- Ensure the panel is only shown when there's a result or error.

## Dependencies

- **Blocked by**: STORY-004
- **Blocks**: None

## PRD Reference

Source: [PRD-001/PRD.md](../../PRDs/PRD-001-football-analytics/PRD.md) — section 4, 12 (Phase 3)
