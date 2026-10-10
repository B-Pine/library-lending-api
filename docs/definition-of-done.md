# Definition of Done (DoD)

A user story is **Done** only when ALL of the following are true:

1. **Acceptance criteria met:** every acceptance criterion is implemented and manually
   verified via the `/docs` page.
2. **Tested:** every acceptance criterion has at least one automated test (pytest).
3. **CI green:** the GitHub Actions pipeline passes (lint + tests) on the commit merged to `main`.
4. **Small, meaningful commits:** work is committed incrementally with clear messages
   (no single "big-bang" commit per story).
5. **Branch & merge:** work is done on a feature branch and merged to `main` via a Pull Request.
6. **Code quality:** no lint errors (ruff), no commented-out dead code.
7. **Documented:** the README is updated if the story adds or changes an endpoint.
8. **Backlog updated:** the story is marked Done in the sprint plan.