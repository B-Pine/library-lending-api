from datetime import date, timedelta

from library import loans

BOOK = {"title": "1984", "author": "George Orwell", "isbn": "123"}
LOAN = {"book_id": 1, "borrower_name": "Aline"}


def set_today(monkeypatch, year, month, day):
    def fake_today():
        return date(year, month, day)
    monkeypatch.setattr(loans, "get_today", fake_today)


# US3 AC1: borrowing an available book gives 201 with dates
def test_borrow_book_returns_201(client):
    client.post("/books", json=BOOK)
    response = client.post("/loans", json=LOAN)
    assert response.status_code == 201
    body = response.get_json()
    assert body["borrowed_on"] == date.today().isoformat()
    assert body["due_date"] == (date.today() + timedelta(days=14)).isoformat()


# US3 AC2: the book becomes unavailable
def test_borrowed_book_is_unavailable(client):
    client.post("/books", json=BOOK)
    client.post("/loans", json=LOAN)
    response = client.get("/books/1")
    assert response.get_json()["available"] is False


# US3 AC3: borrowing a book already on loan gives 409
def test_borrow_book_already_on_loan_returns_409(client):
    client.post("/books", json=BOOK)
    client.post("/loans", json=LOAN)
    response = client.post(
        "/loans", json={"book_id": 1, "borrower_name": "Eric"}
    )
    assert response.status_code == 409


# US3 AC4: borrowing a book that doesn't exist gives 404
def test_borrow_unknown_book_returns_404(client):
    response = client.post("/loans", json=LOAN)
    assert response.status_code == 404


# US3 AC5 (added during the sprint): missing borrower name gives 400
def test_borrow_without_name_returns_400(client):
    client.post("/books", json=BOOK)
    response = client.post("/loans", json={"book_id": 1})
    assert response.status_code == 400


# US4 AC1: returning an active loan gives 200 and frees the book
def test_return_loan_returns_200(client):
    client.post("/books", json=BOOK)
    client.post("/loans", json=LOAN)
    response = client.post("/loans/1/return")
    assert response.status_code == 200
    assert response.get_json()["returned_on"] == date.today().isoformat()
    assert client.get("/books/1").get_json()["available"] is True


# US4 AC2: returning twice gives 409
def test_return_loan_twice_returns_409(client):
    client.post("/books", json=BOOK)
    client.post("/loans", json=LOAN)
    client.post("/loans/1/return")
    response = client.post("/loans/1/return")
    assert response.status_code == 409


# US4 AC3: unknown loan gives 404
def test_return_unknown_loan_returns_404(client):
    response = client.post("/loans/99/return")
    assert response.status_code == 404


# Full cycle: a returned book can be borrowed again
def test_returned_book_can_be_borrowed_again(client):
    client.post("/books", json=BOOK)
    client.post("/loans", json=LOAN)
    client.post("/loans/1/return")
    response = client.post(
        "/loans", json={"book_id": 1, "borrower_name": "Eric"}
    )
    assert response.status_code == 201


# US5 AC1: overdue loans are listed
def test_overdue_lists_late_loan(client, monkeypatch):
    client.post("/books", json=BOOK)
    set_today(monkeypatch, 2026, 1, 1)
    client.post("/loans", json=LOAN)
    set_today(monkeypatch, 2026, 1, 20)
    response = client.get("/loans/overdue")
    assert response.status_code == 200
    assert response.get_json()[0]["borrower_name"] == "Aline"


# US5 AC1: loans not yet due are not listed
def test_overdue_excludes_loan_not_yet_due(client, monkeypatch):
    client.post("/books", json=BOOK)
    set_today(monkeypatch, 2026, 1, 1)
    client.post("/loans", json=LOAN)
    set_today(monkeypatch, 2026, 1, 10)
    assert client.get("/loans/overdue").get_json() == []


# US5 AC2: returned loans never appear, even if returned late
def test_overdue_excludes_returned_loan(client, monkeypatch):
    client.post("/books", json=BOOK)
    set_today(monkeypatch, 2026, 1, 1)
    client.post("/loans", json=LOAN)
    set_today(monkeypatch, 2026, 1, 18)
    client.post("/loans/1/return")
    set_today(monkeypatch, 2026, 1, 20)
    assert client.get("/loans/overdue").get_json() == []
