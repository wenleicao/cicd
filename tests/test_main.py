import pytest
from app.main import app

@pytest.fixture
def client():
    with app.test_client() as client:
        yield client

def test_index_endpoint(client):
    response = client.get("/")
    assert response.status_code == 200
    assert response.json["status"] == "healthy"