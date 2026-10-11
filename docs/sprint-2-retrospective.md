# Sprint 2 Retrospective

**Format:** Review of Sprint 1 improvements / What went well / What didn't go well / Lessons

## Did the Sprint 1 Improvements Work?

| # | Improvement | Result | Evidence |
|---|-------------|--------|----------|
| 1 | Coverage report in CI | Done. Every run shows coverage, and CI fails below 90% | CI log screenshot |
| 2 | Controllable "today's date" | Done. Overdue tests use fixed dates and pass on any day | `test_loans.py`, US5 tests |
| 3 | Update the plan inside each story's PR | Done. Every Sprint 2 story PR included its plan update | Sprint 2 PRs |
| 4 | JSON for all errors | Done. `/books/abc` now returns a JSON 404, covered by a test | `test_monitoring.py` |

All four improvements were applied and verified.

## What Went Well
- **Improvements were planned, not just written down:** the Sprint 2 plan said where each
  improvement would happen, which made them easy to follow through on.
- **Controlling the date paid off:** the overdue logic, including edge cases like "due today"
  and "returned late", could be tested without waiting 14 days.
- **Tests made refactoring safe:** routing all dates through `get_today()` changed code in two
  places, and the existing tests confirmed nothing broke.
- **Velocity was stable:** 7 points planned and delivered in both sprints.

## What Didn't Go Well
- **Committing before running tests:** several times I committed work I trusted, then the tests
  failed. I had to use `git reset HEAD~1` to undo the commit, fix the code and commit again.
  This cost time and broke my flow.
- **Over-planning monitoring:** I first planned logging with request timing and a logging
  library. It was more than the brief required and more than I could confidently explain, so I
  simplified it to console prints.
- **Some features can't be demoed manually:** overdue loans can't be shown in Postman without
  waiting two weeks. The demo had to rely on test output.

## Lessons and Improvements for Future Sprints
| # | Improvement | Why |
|---|-------------|-----|
| 1 | Always run `pytest` and `flake8` **before** `git commit`, not after | Avoids undoing commits; every commit is then known to be working |
| 2 | Match the solution to the actual requirement before designing extras | Simple code is easier to explain, test and maintain |
| 3 | Plan how to demo a story while planning it | Time-based features need a test-based demo, decided up front |

## Overall Reflection
Across the two sprints, the biggest change was moving from *writing* improvements to
*planning where they happen*. Sprint 1's retrospective improvements were all applied because
the Sprint 2 plan gave each one a specific place. The main personal lesson is about order:
test first, then commit.