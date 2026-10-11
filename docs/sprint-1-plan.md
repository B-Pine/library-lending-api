# Sprint 1 Plan

**Sprint Goal:** A librarian can add books, see what is available, and lend a book out, with
every change automatically tested in CI.

**Status:** ✅ Completed. All 7 points delivered (see `sprint-1-review.md`).

**Capacity:** ~7 story points (first sprint, no velocity history yet, so kept conservative).

## Selected Stories
| ID  | Story | Points |
|-----|-------|--------|
| US1 | Add a book | 2 |
| US2 | List and view books | 2 |
| US3 | Borrow a book | 3 |
| **Total** | | **7** |

**Why these:** They are the highest-priority "Must" stories, and they build on each other
(a book must exist before it can be listed or borrowed). Together they deliver a usable
end-to-end slice.

## Task Breakdown
**Setup (enables the sprint)**
- [x] Project skeleton (Flask app, requirements, folder structure)
- [x] GitHub Actions CI pipeline (lint + pytest)
- [x] Branch protection on main (ruleset) and PR template

**US1 – Add a book**
- [x] Book model and in-memory storage
- [x] POST /books endpoint with validation
- [x] Duplicate ISBN check (409)
- [x] Tests for all acceptance criteria

**US2 – List and view books**
- [x] GET /books and GET /books/{id}
- [x] 404 handling
- [x] Tests

**US3 – Borrow a book**
- [x] Loan model, POST /loans
- [x] Due date = today + 14 days, mark book unavailable
- [x] 404 / 409 error cases
- [x] Validation for missing or invalid loan data (400) *(added during the sprint)*
- [x] Tests

## Risks / Assumptions
- Data is stored **in memory** for now (lost on restart). This is acceptable for the prototype;
  a database can be a future backlog item.
- One record = one physical copy of a book.
- Code is split into modules: `app.py` handles HTTP only, `library/` holds the logic and data.
  This keeps logic testable without the web layer.