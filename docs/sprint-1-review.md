# Sprint 1 Review

**Sprint Goal:** A librarian can add books, see what is available, and lend a book out,
with every change automatically tested in CI.

**Goal met:** ✅ Yes

## Delivered Stories

| ID  | Story               | Points | Status | Pull Request |
|-----|---------------------|--------|--------|--------------|
| US1 | Add a book          | 2      | Done   | #2           |
| US2 | List and view books | 2      | Done   | #3           |
| US3 | Borrow a book       | 3      | Done   | #4           |

**Planned:** 7 points | **Completed:** 7 points | **Velocity:** 7

## Demo

### US1 – Add a book
Valid book created with `available: true` (201):
![Create book](evidence/sprint-1/us1-create-201.png)

Duplicate ISBN rejected (409):
![Duplicate ISBN](evidence/sprint-1/us1-duplicate-409.png)

Missing field rejected (400):
![Missing field](evidence/sprint-1/us1-missing-field-400.png)

### US2 – List and view books
Empty list when no books exist (200):
![Empty list](evidence/sprint-1/us2-list-empty.png)

List after adding a book (200):
![List books](evidence/sprint-1/us2-list-books.png)

Unknown book (404):
![Not found](evidence/sprint-1/us2-not-found-404.png)

### US3 – Borrow a book
Loan created with a due date 14 days from today (201):
![Borrow book](evidence/sprint-1/us3-borrow-201.png)

## DevOps Evidence

**CI pipeline:** GitHub Actions runs flake8 and pytest on every Pull Request to `main` and
on every merge to `main`.
![CI run](evidence/sprint-1/ci-green-pr.png)

**Protected main branch:** a ruleset requires a Pull Request and a passing CI check before
anything can be merged.
![Ruleset](evidence/sprint-1/ruleset.png)

**Tests:** 26 tests passing, covering every acceptance criterion of US1–US3. Unit tests check
the logic in `library/` directly; integration tests check the HTTP endpoints.
![Test results](evidence/sprint-1/pytest-results.png)

## Not Delivered
Nothing. All planned stories were completed.

## Backlog Changes
- **US3 refined:** while building US3, I found the backlog didn't say what happens when
  `book_id` or `borrower_name` is missing. I added a 400 acceptance criterion to the backlog
  and implemented it in the same sprint.
- **Observation for US6:** `GET /books/abc` returns Flask's default 404 page in HTML, not JSON
  like the rest of the API. This will be handled with the error-handling work in US6 (Sprint 2).
- US4 (Return a book), US5 (Overdue loans) and US6 (Health & logging) are ready for Sprint 2.