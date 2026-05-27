---
story: STORY-004
prd: PRD-001
slug: search-interface-ui
title: Create Search Interface with React and shadcn/ui
type: FEATURE
complexity: MEDIUM
epic_branch: epic/PRD-001-football-analytics
created: 2026-05-27
---

# Plan: Create Search Interface with React and shadcn/ui

## Summary

We will build the main `FootballAnalytics` page for the frontend. This page will feature a search input where users can type natural language questions in Spanish and a submit button. We will use `shadcn/ui` components (`Input`, `Button`, `Skeleton`/`Spinner`) and configure an API call to the backend `POST /api/v1/generate-sql` endpoint. We will also update the app routing to expose this new page.

## User Story

As a user
I want a clean search bar and a button to submit my questions
So that I can interact with the system

## Story Reference

- Story file: `.agents/stories/PRD-001-football-analytics/STORY-004-search-interface-ui.md`
- PRD: `.agents/PRDs/PRD-001-football-analytics/PRD.md`

## Metadata

| Field | Value |
|-------|-------|
| Type | FEATURE |
| Complexity | MEDIUM |
| Systems Affected | Frontend UI |
| Story | STORY-004 |
| PRD | PRD-001 |
| Epic Branch | `epic/PRD-001-football-analytics` (commit directly on this branch) |

---

## Skills In Use

| Skill | Why it applies | Tasks affected |
|-------|---------------|----------------|
| shadcn | Enforces the use of `npx shadcn@latest add input` and semantic styling with Tailwind v4. | Task 1, 2 |
| react-router-declarative-mode | Enforces explicit `<Route>` configuration and `<NavLink>` additions. | Task 4 |
| vercel-react-best-practices | Enforces controlled state, proper `useState` and `useTransition` usage for loading states. | Task 3 |

---

## Patterns to Follow

### Component Structure
```jsx
// SOURCE: shadcn skill - Form layout pattern
<div className="flex flex-col gap-4">
  <Input value={prompt} onChange={(e) => setPrompt(e.target.value)} />
  <Button disabled={isPending} onClick={handleSubmit}>
    {isPending ? 'Generating...' : 'Generate SQL'}
  </Button>
</div>
```

### App Routing
```jsx
// SOURCE: frontend/src/App.jsx:13
<Route element={<RootLayout />}>
  <Route path="/" element={<Home />} />
  <Route path="analytics" element={<FootballAnalytics />} />
</Route>
```

---

## Files to Change

| File | Action | Purpose |
|------|--------|---------|
| `frontend/components.json` | UPDATE | Install `input` component via `npx shadcn@latest`. |
| `frontend/src/lib/api.js` | CREATE | Utility for backend API calls. |
| `frontend/src/pages/FootballAnalytics.jsx` | CREATE | The main page component for the search interface. |
| `frontend/src/App.jsx` | UPDATE | Add the new route `/analytics`. |
| `frontend/src/layouts/RootLayout.jsx` | UPDATE | Add navigation link to `/analytics`. |

---

## Tasks

### Task 1: Install shadcn components

- **Action**: EXECUTE
- **Implement**: Run `npx shadcn@latest add input` in the `frontend` directory. We already have `button`.

### Task 2: Create API Client

- **File**: `frontend/src/lib/api.js`
- **Action**: CREATE
- **Implement**: Create an async function `generateSql(prompt)` that performs a `fetch` POST request to `http://localhost:8000/api/v1/generate-sql` with the prompt payload. Handle errors cleanly.

### Task 3: Build the Search Interface

- **File**: `frontend/src/pages/FootballAnalytics.jsx`
- **Action**: CREATE
- **Implement**:
  - Import `Input` and `Button` from `@/components/ui/input` and `@/components/ui/button`.
  - Import `generateSql` from `@/lib/api`.
  - Use `useState` for the `prompt` text.
  - Use `useState` for `sqlResult` and `error`.
  - Use `useTransition` or a `isPending` state for the loading state during the fetch.
  - Render a clean, centered interface: a title "Football Analytics", an input field "Ej. ¿Cuáles son los equipos de Madrid?", and a "Generar SQL" button.
  - When submitted, call the API and store the result (we won't build the full result panel yet, just dump the result object or simple text, as STORY-005 will refine the result panel).

### Task 4: Configure Routing

- **File**: `frontend/src/App.jsx`
- **Action**: UPDATE
- **Implement**: Import `FootballAnalytics` and add a `<Route path="analytics" element={<FootballAnalytics />} />` inside the `<RootLayout>` scope.
- **File**: `frontend/src/layouts/RootLayout.jsx`
- **Action**: UPDATE
- **Implement**: Add a `<NavLink>` to `/analytics` alongside the existing ones.

---

## End-to-End Tests

- [ ] Execute `cd frontend && npm run dev`. Navigate to `http://localhost:5173/analytics`. The search interface should render correctly.
- [ ] Type a prompt and submit. The network tab should show a request to the backend.

---

## Validation

```bash
cd frontend
npm run lint
```

---

## Acceptance Criteria

- [x] Given the home page, when the user visits it, then it shows a prominent search input.
- [x] Given a search query, when the user clicks "Generate SQL", then it triggers a request to the backend.
- [x] Given a pending request, when the system is processing, then it shows a loading state (e.g., Skeleton or Spinner).
