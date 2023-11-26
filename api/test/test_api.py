from api import app
from starlette.testclient import TestClient

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200


def test_get_users():
    with client:
        response = client.get("/users")
        assert response.status_code == 200
