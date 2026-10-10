# In-memory data store. Data is lost when the app restarts.

books = {}   # book_id -> book dictionary
loans = {}   # loan_id -> loan dictionary


def reset():
    """Empty all data. Used by tests so each test starts clean."""
    books.clear()
    loans.clear()
