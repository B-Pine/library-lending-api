import pytest

from app import app
from library import storage


@pytest.fixture(autouse=True)
def reset_storage():
    storage.reset()


@pytest.fixture
def client():
    return app.test_client()
