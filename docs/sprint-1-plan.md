# Sprint 1 Plan

**Sprint Goal:** A librarian can add books, see what is available, and lend a book out, with
every change automatically tested in CI.

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
- [ ] Project skeleton (FastAPI app, requirements, folder structure)
- [ ] GitHub Actions CI pipeline (lint + pytest)

**US1 – Add a book**
- [ ] Book model and in-memory storage
- [ ] POST /books endpoint with validation
- [ ] Duplicate ISBN check (409)
- [ ] Tests for all acceptance criteria

**US2 – List and view books**
- [ ] GET /books and GET /books/{id}
- [ ] 404 handling
- [ ] Tests

**US3 – Borrow a book**
- [ ] Loan model, POST /loans
- [ ] Due date = today + 14 days, mark book unavailable
- [ ] 404 / 409 error cases
- [ ] Tests

## Risks / Assumptions
- Data is stored **in memory** for now (lost on restart). This is acceptable for the prototype;
  a database can be a future backlog item.
- One record = one physical copy of a book.