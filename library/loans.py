from datetime import date, timedelta

from library import storage

LOAN_PERIOD_DAYS = 14


def validate_loan_data(data):
    """Return an error message if the data is invalid, otherwise None."""
    if not isinstance(data, dict):
        return "Request body must be a JSON object"

    if not isinstance(data.get("book_id"), int):
        return "Please provide 'book_id' as a whole number"

    name = data.get("borrower_name")
    if not isinstance(name, str) or name.strip() == "":
        return "Please provide 'borrower_name'"

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


def get_loan(loan_id):
    """Return the loan with this id, or None if it doesn't exist."""
    return storage.loans.get(loan_id)


def return_book(loan):
    """Mark the loan as returned and make the book available again."""
    loan["returned_on"] = date.today().isoformat()
    book = storage.books[loan["book_id"]]
    book["available"] = True
    return loan
