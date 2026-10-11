from library import books


# US6 AC1: health endpoint
def test_health_returns_ok_and_version(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "1.0.0"}


# US6 AC2: every request is printed to the console
def test_requests_are_printed(client, capsys):
    client.get("/health")
    output = capsys.readouterr().out
    assert "GET /health 200" in output


# Improvement 4: Flask's own errors return JSON
def test_unknown_url_returns_json_404(client):
    response = client.get("/does-not-exist")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Not Found"}


def test_non_numeric_book_id_returns_json_404(client):
    response = client.get("/books/abc")
    assert response.status_code == 404
    assert response.get_json() == {"error": "Not Found"}


def test_wrong_method_returns_json_405(client):
    response = client.delete("/books")
    assert response.status_code == 405
    assert response.get_json() == {"error": "Method Not Allowed"}


# US6 AC3: unexpected errors give a clean 500 and are printed
def test_unexpected_error_returns_json_500_and_is_printed(
            client,
            monkeypatch,
            capsys
        ):
    def broken_list_books():
        raise RuntimeError("something broke inside")

    monkeypatch.setattr(books, "list_books", broken_list_books)
    response = client.get("/books")

    assert response.status_code == 500
    assert response.get_json() == {"error": "Internal server error"}
    assert "something broke inside" not in response.get_data(as_text=True)
    assert "ERROR: unhandled error" in capsys.readouterr().out
