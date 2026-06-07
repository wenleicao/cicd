import pytest
import sys
sys.path.append(r"D:\cicd\app")  # Add the app directory to the system path
from main import app

# @pytest.fixture
# def client():
#     with app.test_client() as client:
#         yield client

# def test_index_endpoint(client):
#     response = client.get("/")
#     assert response.status_code == 200
#     assert response.json["status"] == "healthy"