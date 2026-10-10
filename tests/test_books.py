from library import books


def test_valid_data_has_no_error():
    data = {"title": "1984", "author": "George Orwell", "isbn": "9780451524935"}
    assert books.validate_book_data(data) is None


def test_missing_field_returns_error():
    data = {"title": "1984", "author": "George Orwell"}
    assert "isbn" in books.validate_book_data(data)


def test_blank_field_returns_error():
    data = {"title": "   ", "author": "George Orwell", "isbn": "123"}
    assert "title" in books.validate_book_data(data)


def test_non_dict_data_returns_error():
    assert books.validate_book_data(None) is not None


def test_add_book_sets_id_and_available():
    data = {"title": " 1984 ", "author": "George Orwell", "isbn": "123"}
    book = books.add_book(data)
    assert book["id"] == 1
    assert book["available"] is True
    assert book["title"] == "1984"


def test_isbn_exists_after_adding_book():
    books.add_book({"title": "1984", "author": "George Orwell", "isbn": "123"})
    assert books.isbn_exists("123") is True
    assert books.isbn_exists("999") is False
