# Definition of Done (DoD)

A user story is **Done** only when ALL of the following are true:

1. **Acceptance criteria met:** every acceptance criterion works when checked manually
   (using curl, Postman or the browser).
2. **Tested:** every acceptance criterion has at least one automated test (pytest).
3. **CI green:** the GitHub Actions pipeline passes on the pushed commit.
4. **Code style:** no flake8 warnings.
5. **Small commits:** work is committed in small steps with clear messages.
6. **Documented:** the README lists any new endpoint.
7. **Branch & PR:** work is done on a feature branch, opened as a Pull Request,
   self-reviewed using the PR checklist, and merged to `main` only after CI passes.
8. **Plan updated:** the story is ticked off in the sprint plan.