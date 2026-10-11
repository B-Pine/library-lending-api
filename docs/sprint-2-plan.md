# Sprint 2 Plan

**Sprint Goal:** A librarian can complete the lending cycle (return books and see overdue
loans), and the service can be monitored through a health endpoint, request logs and
consistent error responses.

**Capacity:** 7 story points, based on Sprint 1 velocity (7 points planned, 7 delivered).

## Selected Stories
| ID  | Story | Points |
|-----|-------|--------|
| US4 | Return a book | 2 |
| US5 | See overdue loans | 3 |
| US6 | Health endpoint and logging | 2 |
| **Total** | | **7** |

**Why these:** US4 and US5 complete the lending cycle started in Sprint 1 (borrow → return →
follow up on overdue). US6 adds the monitoring the service needs before it could be run for
real. US7 (Search) and US8 (Members) stay in the backlog as lower-priority "Could" stories.

## Applying the Sprint 1 Retrospective
| # | Improvement | Where it is applied |
|---|-------------|---------------------|
| 1 | Test coverage report in CI | First task of the sprint, before any story |
| 2 | Controllable "today's date" | Part of US5, before the overdue logic |
| 3 | Update the plan inside each story's PR | Every story PR in this sprint |
| 4 | JSON for all errors (incl. Flask's 404/500) | Part of US6 |

## Task Breakdown
**Retro improvements**
- [ ] Add coverage report to CI with a 90% minimum (Improvement 1)

**US4 – Return a book**
- [ ] Return logic: set `returned_on`, make the book available again
- [ ] POST /loans/{id}/return endpoint
- [ ] 404 (unknown loan) / 409 (already returned) cases
- [ ] Tests

**US5 – See overdue loans**
- [ ] Make "today's date" controllable in tests (Improvement 2)
- [ ] Overdue logic: not returned and due date before today
- [ ] GET /loans/overdue endpoint
- [ ] Tests, including "returned late is not overdue"

**US6 – Health endpoint and logging**
- [ ] GET /health returning status and app version
- [ ] Log every request: method, path, status code, duration
- [ ] JSON error responses for 404 and 500, with unhandled errors logged (Improvement 4)
- [ ] Tests

## Risks / Assumptions
- Logging and error handling are new areas for me, so US6 may take longer than its 2 points
  suggest. US6 is last, so if it runs over, US4 and US5 are already delivered.
- Data is still in memory; this does not affect Sprint 2 stories.
