VALID_BOOK = {
    "title": "1984",
    "author": "George Orwell",
    "isbn": "9780451524935",
}


# US1 AC1: valid book is created
def test_create_book_returns_201(client):
    response = client.post("/books", json=VALID_BOOK)
    assert response.status_code == 201
    body = response.get_json()
    assert body["id"] == 1
    assert body["available"] is True


# US1 AC2: missing or empty field gives 400
def test_create_book_missing_field_returns_400(client):
    response = client.post("/books", json={"title": "1984"})
    assert response.status_code == 400


def test_create_book_empty_title_returns_400(client):
    response = client.post("/books", json={**VALID_BOOK, "title": ""})
    assert response.status_code == 400


def test_create_book_without_json_returns_400(client):
    response = client.post("/books", data="not json")
    assert response.status_code == 400


# US1 AC3: duplicate ISBN gives 409
def test_create_book_duplicate_isbn_returns_409(client):
    client.post("/books", json=VALID_BOOK)
    response = client.post("/books", json=VALID_BOOK)
    assert response.status_code == 409
