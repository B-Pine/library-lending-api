import logging

from library import books


# US6 AC1: health endpoint
def test_health_returns_ok_and_version(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok", "version": "1.0.0"}