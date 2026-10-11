from datetime import date, timedelta

from library import books, loans


def add_sample_book():
    return books.add_book(
        {"title": "1984", "author": "George Orwell", "isbn": "123"}
    )


def set_today(monkeypatch, year, month, day):
    """Make loan logic believe today is the given date for this test."""
    def fake_today():
        return date(year, month, day)
    monkeypatch.setattr(loans, "get_today", fake_today)


def test_valid_loan_data_has_no_error():
    data = {"book_id": 1, "borrower_name": "Aline"}
    assert loans.validate_loan_data(data) is None


def test_missing_book_id_returns_error():
    assert "book_id" in loans.validate_loan_data({"borrower_name": "Aline"})


def test_text_book_id_returns_error():
    data = {"book_id": "1", "borrower_name": "Aline"}
    assert "book_id" in loans.validate_loan_data(data)


def test_blank_borrower_name_returns_error():
    data = {"book_id": 1, "borrower_name": "  "}
    assert "borrower_name" in loans.validate_loan_data(data)


def test_borrow_sets_today_and_due_date():
    book = add_sample_book()
    loan = loans.borrow_book(book, "Aline")
    today = date.today()
    assert loan["borrowed_on"] == today.isoformat()
    assert loan["due_date"] == (today + timedelta(days=14)).isoformat()
    assert loan["returned_on"] is None


def test_borrow_marks_book_unavailable():
    book = add_sample_book()
    loans.borrow_book(book, "Aline")
    assert books.get_book(1)["available"] is False


def test_get_loan_unknown_id_returns_none():
    assert loans.get_loan(99) is None


def test_return_sets_returned_on_today():
    book = add_sample_book()
    loan = loans.borrow_book(book, "Aline")
    loans.return_book(loan)
    assert loan["returned_on"] == date.today().isoformat()


def test_return_makes_book_available_again():
    book = add_sample_book()
    loan = loans.borrow_book(book, "Aline")
    loans.return_book(loan)
    assert books.get_book(1)["available"] is True


def test_borrow_uses_controlled_date(monkeypatch):
    set_today(monkeypatch, 2026, 1, 1)
    loan = loans.borrow_book(add_sample_book(), "Aline")
    assert loan["borrowed_on"] == "2026-01-01"
    assert loan["due_date"] == "2026-01-15"


def test_no_loans_means_no_overdue():
    assert loans.find_overdue_loans() == []


def test_loan_past_due_date_is_overdue(monkeypatch):
    set_today(monkeypatch, 2026, 1, 1)
    loans.borrow_book(add_sample_book(), "Aline")   # due 2026-01-15
    set_today(monkeypatch, 2026, 1, 20)
    assert len(loans.find_overdue_loans()) == 1


def test_loan_due_today_is_not_overdue(monkeypatch):
    set_today(monkeypatch, 2026, 1, 1)
    loans.borrow_book(add_sample_book(), "Aline")   # due 2026-01-15
    set_today(monkeypatch, 2026, 1, 15)
    assert loans.find_overdue_loans() == []


def test_returned_late_loan_is_not_overdue(monkeypatch):
    set_today(monkeypatch, 2026, 1, 1)
    loan = loans.borrow_book(add_sample_book(), "Aline")   # due 2026-01-15
    set_today(monkeypatch, 2026, 1, 18)
    loans.return_book(loan)                                # returned 3 days late
    set_today(monkeypatch, 2026, 1, 20)
    assert loans.find_overdue_loans() == []
