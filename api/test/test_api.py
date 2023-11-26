from api import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200
