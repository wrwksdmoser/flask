import pytest
from main import app

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_get_status(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.get_json() == {"status": "ok"}