## Endpoints

| Method | Path   | Description      |
|--------|--------|------------------|
| POST   | /books | Add a new book   |
| GET    | /books      | List all books           |
| GET    | /books/{id} | View one book            |
| POST   | /loans      | Borrow a book            |
| POST   | /loans/{id}/return | Return a borrowed book |
| GET    | /loans/overdue     | List overdue loans     |

## Monitoring
- `GET /health` returns `{"status": "ok", "version": "..."}` when the service is running.
- Every request is printed to the console with method, path and status code.
- Unexpected errors are printed with a full stack trace; clients receive a generic
  `{"error": "Internal server error"}` response.
- All errors, including unknown URLs, are returned as JSON.