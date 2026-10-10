from app import app


def test_home_returns_welcome_message():
    client = app.test_client()

    response = client.get("/")

    assert response.status_code == 200
    assert response.get_json()["message"] == (
        "Welcome to the Library Lending API"
    )
