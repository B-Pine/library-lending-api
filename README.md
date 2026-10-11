# Library Lending API

A small REST API that lets librarians manage books and lending: add books, lend them out,
take them back, and see which loans are overdue. Built over two sprints as an Agile & DevOps
practice project.

## Tech Stack
- **Python 3.12** with **Flask** (web framework)
- **pytest** + **pytest-cov** (tests and coverage)
- **flake8** (code style)
- **GitHub Actions** (CI)


## Getting Started
```bash
python -m venv venv
venv\Scripts\activate          # Windows
source venv/bin/activate       # Mac/Linux
pip install -r requirements.txt
python app.py
```
The API runs at `http://127.0.0.1:5000`. Data is stored in memory and resets on restart.

## Running Tests
```bash
python -m pytest -v --cov=app --cov=library --cov-report=term-missing
flake8 app.py library tests
```

## Endpoints

| Method | Path               | Description                |
|--------|--------------------|----------------------------|
| GET    | /health            | Service health and version |
| POST   | /books             | Add a new book             |
| GET    | /books             | List all books             |
| GET    | /books/{id}        | View one book              |
| POST   | /loans             | Borrow a book              |
| POST   | /loans/{id}/return | Return a borrowed book     |
| GET    | /loans/overdue     | List overdue loans         |

## Monitoring
- `GET /health` returns `{"status": "ok", "version": "..."}` when the service is running.
- Every request is printed to the console with method, path and status code.
- Unexpected errors are printed with a full stack trace; clients receive a generic
  `{"error": "Internal server error"}` response.
- All errors, including unknown URLs, are returned as JSON.

## CI Pipeline
On every Pull Request to `main` and every merge to `main`, GitHub Actions:
1. Installs dependencies
2. Checks code style with flake8
3. Runs all tests with coverage (fails if coverage is below 90%)

`main` is protected: changes only arrive through Pull Requests with a passing CI check.

## Agile Documentation
- [Product backlog & vision](docs/backlog.md)
- [Definition of Done](docs/definition-of-done.md)
- Sprint 1: [Plan](docs/sprint-1-plan.md) · [Review](docs/sprint-1-review.md) · [Retrospective](docs/sprint-1-retrospective.md)
- Sprint 2: [Plan](docs/sprint-2-plan.md) · [Review](docs/sprint-2-review.md) · [Retrospective](docs/sprint-2-retrospective.md)