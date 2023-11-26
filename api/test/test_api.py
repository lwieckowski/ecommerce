from starlette.testclient import TestClient

from api import app

client = TestClient(app)


def test_index():
    response = client.get("/")
    assert response.status_code == 200


def test_get_users():
    with client:
        response = client.get("/users")
        assert response.status_code == 200
