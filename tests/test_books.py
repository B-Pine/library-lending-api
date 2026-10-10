from library import books


def test_valid_data_has_no_error():
    data = {
        "title": "1984",
        "author": "George Orwell",
        "isbn": "9780451524935",
    }
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


def test_list_books_is_empty_at_start():
    assert books.list_books() == []


def test_list_books_returns_added_books():
    books.add_book({"title": "1984", "author": "George Orwell", "isbn": "123"})
    books.add_book({"title": "Dune", "author": "Frank Herbert", "isbn": "456"})
    assert len(books.list_books()) == 2


def test_get_book_returns_the_book():
    books.add_book({"title": "1984", "author": "George Orwell", "isbn": "123"})
    assert books.get_book(1)["title"] == "1984"


def test_get_book_unknown_id_returns_none():
    assert books.get_book(99) is None
