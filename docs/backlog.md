# Product Backlog – Library Lending API

## Product Vision
For small community and school libraries that track loans on paper, the Library Lending API
is a simple service that lets librarians manage books and lending, so they always know
what is available, who has what, and what is overdue.

## Estimation & Prioritization Approach
- **Estimation:** Story points on the Fibonacci scale (1, 2, 3, 5, 8). Points measure relative
  effort, complexity and uncertainty, not hours.
- **Prioritization:** MoSCoW (Must / Should / Could / Won't), ordered by business value and
  dependencies (e.g. you can't borrow a book that can't be added).

## Backlog (ordered by priority)

| ID  | User Story | Points | Priority | Sprint |
|-----|-----------|--------|----------|--------|
| US1 | As a librarian, I want to add a book to the catalogue so that it can be lent out. | 2 | Must | 1 |
| US2 | As a librarian, I want to list and view books with their availability so that I know what can be borrowed. | 2 | Must | 1 |
| US3 | As a librarian, I want to record a book being borrowed by a member so that I know who has it and when it is due. | 3 | Must | 1 |
| US4 | As a librarian, I want to record a book being returned so that it becomes available again. | 2 | Must | 2 |
| US5 | As a librarian, I want to see all overdue loans so that I can follow up with borrowers. | 3 | Should | 2 |
| US6 | As an operator, I want a health endpoint and request/error logging so that I can tell if the service is running and diagnose problems. | 2 | Should | 2 |
| US7 | As a librarian, I want to search books by title or author so that I can find books quickly. | 2 | Could | Backlog |
| US8 | As a librarian, I want to register library members so that only known members can borrow. | 3 | Could | Backlog |

**Total:** 19 points | **Planned:** Sprint 1 = 7 pts, Sprint 2 = 7 pts | **Remaining:** 5 pts

## Acceptance Criteria

### US1 – Add a book
- Given valid `title`, `author` and `isbn`, when I POST to `/books`, then I get **201 Created**
  and the book is returned with an `id` and `available: true`.
- Given a missing or empty `title`, `author` or `isbn`, when I POST to `/books`, then I get **422**.
- Given an `isbn` that already exists, when I POST to `/books`, then I get **409 Conflict**.

### US2 – List and view books
- When I GET `/books`, then I get **200** and a list of all books (empty list if none).
- Given a book exists, when I GET `/books/{id}`, then I get **200** and that book's details,
  including `available`.
- Given a book does not exist, when I GET `/books/{id}`, then I get **404**.

### US3 – Borrow a book
- Given an available book, when I POST to `/loans` with `book_id` and `borrower_name`, then I
  get **201** and a loan with `borrowed_on` = today and `due_date` = today + 14 days.
- After borrowing, the book shows `available: false`.
- Given the book is already on loan, when I try to borrow it, then I get **409 Conflict**.
- Given the book does not exist, when I try to borrow it, then I get **404**.

### US4 – Return a book
- Given an active loan, when I POST to `/loans/{id}/return`, then I get **200**, the loan has a
  `returned_on` date, and the book is `available: true` again.
- Given the loan was already returned, when I return it again, then I get **409 Conflict**.
- Given the loan does not exist, then I get **404**.

### US5 – Overdue loans
- When I GET `/loans/overdue`, then I get **200** and only loans that are not returned and whose
  `due_date` is before today.
- Returned loans never appear in the overdue list, even if they were returned late.

### US6 – Health & logging
- When I GET `/health`, then I get **200** with `{"status": "ok"}` and the app version.
- Every request is logged with method, path, status code and duration.
- Unhandled errors are logged with a stack trace and the client gets a clean **500** JSON
  response (no stack trace leaked).

### US7 – Search books
- When I GET `/books?q=orwell`, then I get books whose title or author contains the text
  (case-insensitive).

### US8 – Register members
- When I POST to `/members` with a name and email, then I get **201**; duplicate email gives **409**.