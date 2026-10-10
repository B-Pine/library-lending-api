from datetime import date, timedelta

from library import storage

LOAN_PERIOD_DAYS = 14


def validate_loan_data(data):
    """Return an error message if the data is invalid, otherwise None."""
    if not isinstance(data, dict):
        return "Request body must be a JSON object"

    if not isinstance(data.get("book_id"), int):
        return "Please provide the book ID"

    name = data.get("borrower_name")
    if not isinstance(name, str) or name.strip() == "":
        return "'Please provide borrower name!"

    return None


def borrow_book(book, borrower_name):
    """Create a loan for this book, mark the book unavailable,
    return the loan.
    """
    today = date.today()
    loan_id = len(storage.loans) + 1
    loan = {
        "id": loan_id,
        "book_id": book["id"],
        "borrower_name": borrower_name.strip(),
        "borrowed_on": today.isoformat(),
        "due_date": (today + timedelta(days=LOAN_PERIOD_DAYS)).isoformat(),
        "returned_on": None,
    }
    storage.loans[loan_id] = loan
    book["available"] = False
    return loan
