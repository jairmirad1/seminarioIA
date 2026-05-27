---
story: STORY-005
prd: PRD-001
slug: sql-result-panel
title: Create SQL Result Panel with Syntax Highlighting
type: FEATURE
complexity: LOW
epic_branch: epic/PRD-001-football-analytics
created: 2026-05-27
---

# Plan: Create SQL Result Panel with Syntax Highlighting

## Summary

We will enhance the presentation of the generated SQL query and its explanation in the `FootballAnalytics` page. We'll use `shadcn/ui` components (`Card`, `Alert`) to structure the response and handle errors elegantly. To provide a professional developer experience, we'll introduce `react-syntax-highlighter` to add SQL syntax highlighting to the code block.

## User Story

As a user
I want a clean search bar and a button to submit my questions
So that I can interact with the system

## Story Reference

- Story file: `.agents/stories/PRD-001-football-analytics/STORY-005-sql-result-panel.md`
- PRD: `.agents/PRDs/PRD-001-football-analytics/PRD.md`

## Metadata

| Field | Value |
|-------|-------|
| Type | FEATURE |
| Complexity | LOW |
| Systems Affected | Frontend UI |
| Story | STORY-005 |
| PRD | PRD-001 |
| Epic Branch | `epic/PRD-001-football-analytics` (commit directly on this branch) |

---

## Skills In Use

| Skill | Why it applies | Tasks affected |
|-------|---------------|----------------|
| shadcn | Enforces the use of `npx shadcn@latest add card alert` and semantic Tailwind composition. | Task 1, 3 |
| vercel-react-best-practices | Promotes clean component extraction and state management (e.g., extracting the result panel into a separate sub-component or organizing the JSX cleanly). | Task 3 |

---

## Patterns to Follow

### Component Structure
```jsx
// SOURCE: shadcn skill - Card composition
<Card>
  <CardHeader>
    <CardTitle>SQL Result</CardTitle>
  </CardHeader>
  <CardContent>
    {/* Syntax highlighted content */}
  </CardContent>
</Card>
```

---

## Files to Change

| File | Action | Purpose |
|------|--------|---------|
| `frontend/components.json` | UPDATE | Install `card` and `alert` components via `npx shadcn@latest`. |
| `frontend/package.json` | UPDATE | Add `react-syntax-highlighter` dependency. |
| `frontend/src/pages/FootballAnalytics.jsx` | UPDATE | Refactor the result and error display using the new components. |

---

## Tasks

### Task 1: Install Dependencies

- **Action**: EXECUTE
- **Implement**: 
  - Run `npx shadcn@latest add card alert --yes` in the `frontend` directory.
  - Run `npm install react-syntax-highlighter` in the `frontend` directory.

### Task 2: Implement Syntax Highlighting in Analytics Page

- **File**: `frontend/src/pages/FootballAnalytics.jsx`
- **Action**: UPDATE
- **Implement**:
  - Import `Card`, `CardHeader`, `CardTitle`, `CardContent` from `@/components/ui/card`.
  - Import `Alert`, `AlertTitle`, `AlertDescription` from `@/components/ui/alert`.
  - Import `AlertCircle` from `lucide-react` (for the error icon).
  - Import `Prism as SyntaxHighlighter` from `react-syntax-highlighter` and a theme (e.g., `vscDarkPlus` or `coy`).
  - Replace the current raw HTML error display with an `<Alert variant="destructive">`.
  - Replace the current result display with a `<Card>` for the explanation and another `<Card>` for the SQL.
  - Inside the SQL card, use `<SyntaxHighlighter language="sql" style={theme}>` to render the `result.sql` string.
  - Optionally, add a small "Copiar" button next to the SQL block using the browser's Clipboard API (`navigator.clipboard.writeText`).

---

## End-to-End Tests

- [ ] Run `cd frontend && npm run dev`.
- [ ] Submit a valid prompt. Verify the SQL is displayed inside a nice Card with syntax colors.
- [ ] Force an error (e.g., by stopping the backend) and verify the `Alert` component renders correctly.

---

## Validation

```bash
cd frontend
npm run lint
```

---

## Acceptance Criteria

- [x] Given a successful SQL generation, when the result is received, then it is displayed in a dedicated card.
- [x] Given the SQL display, when the code is shown, then it has syntax highlighting (e.g., using a library or styled code block).
- [x] Given an error during generation, when the backend fails, then it shows a clear error alert.
