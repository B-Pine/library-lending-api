from library import storage

REQUIRED_FIELDS = ["title", "author", "isbn"]


def validate_book_data(data):
    """Return an error message if the data is invalid, otherwise None."""
    if not isinstance(data, dict):
        return "Request body must be a JSON object"

    for field in REQUIRED_FIELDS:
        value = data.get(field)
        if not isinstance(value, str) or value.strip() == "":
            return f"'{field}' is required and must be a non-empty text value"

    return None


def isbn_exists(isbn):
    """Return True if a book with this ISBN is already stored."""
    for book in storage.books.values():
        if book["isbn"] == isbn.strip():
            return True
    return False


def add_book(data):
    """Create a new book, store it and return it."""
    book_id = len(storage.books) + 1
    book = {
        "id": book_id,
        "title": data["title"].strip(),
        "author": data["author"].strip(),
        "isbn": data["isbn"].strip(),
        "available": True,
    }
    storage.books[book_id] = book
    return book


def list_books():
    """Return all books as a list."""
    return list(storage.books.values())


def get_book(book_id):
    """Return the book with this id, or None if it doesn't exist."""
    return storage.books.get(book_id)
