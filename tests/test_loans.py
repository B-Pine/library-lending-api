from datetime import date, timedelta

from library import books, loans


def add_sample_book():
    return books.add_book(
        {"title": "1984", "author": "George Orwell", "isbn": "123"}
    )


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
