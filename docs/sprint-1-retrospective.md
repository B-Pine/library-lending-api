# Sprint 1 Retrospective

**Format:** What went well / What didn't go well / Improvements for Sprint 2

## What Went Well
- **CI before features:** the pipeline was set up before any feature code, so every story
  was tested automatically from its first commit.
- **Protected main:** the ruleset meant nothing reached `main` without green CI, so `main`
  was always in a working state.
- **Tests caught a real problem:** during US3 I reworded the loan error messages, and 3 unit
  tests failed. The tests showed the messages no longer named the field, and one was misleading:
  it said "provide the book ID" when the ID *was* provided, just as text instead of a number.
  I fixed the messages before merging. *Lesson:* error messages should name the exact field
  and say what is wrong with it.
- **Modular structure:** keeping logic (`library/`) separate from HTTP (`app.py`) made unit
  tests simple, because logic could be tested without Flask.
- **Traceable tests:** each test is labelled with the acceptance criterion it checks, and the
  PR template made the Definition of Done a checklist on every PR.

## What Didn't Go Well
- **The plan changed early:** I switched from FastAPI to Flask after realising FastAPI relied on
  concepts beyond what I had covered, and the DoD was edited twice. *Lesson:* choose tools I can
  fully explain before writing the plan.
- **PR template surprise:** the template did not fill in on the first PR, because GitHub only
  reads it from `main`. I had to paste it in manually.
- **Sprint plan not updated per story:** my DoD says the plan is updated when a story is done,
  but I ticked off US2 and US3 only at the end of the sprint. The plan didn't show real progress
  during the sprint.
- **Inconsistent error format:** `GET /books/abc` returns Flask's HTML 404 page instead of JSON.
- **Risk for Sprint 2:** borrowing uses the real current date. US5 (Overdue loans) depends on
  dates changing, so its tests would depend on what day they run.

## Improvements for Sprint 2

| # | Improvement | Why | How I'll know it worked |
|---|-------------|-----|-------------------------|
| 1 | Add a test coverage report to CI (`pytest-cov`) | I know tests pass, but not how much of the code they actually run | Every CI run shows a coverage %; target ≥ 90% |
| 2 | Make "today's date" controllable in the loan logic | Overdue tests must give the same result on any day | US5 tests pass regardless of the real date |
| 3 | Update the sprint plan inside each story's PR | Keep the plan showing real progress, as the DoD requires | Every Sprint 2 story PR includes its plan update |
| 4 | Return JSON for all errors, including Flask's own 404/500 | Clients should always get the same error format | `GET /books/abc` returns a JSON error; covered by a test |

These will be reviewed at the start of the Sprint 2 retrospective.