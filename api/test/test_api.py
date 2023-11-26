import pytest
from starlette.testclient import TestClient

import api

client = TestClient(api.app)


class MockDb:
    @staticmethod
    def get_users():
        return [["john776", "jdoe@hotmail.com", "John", "Doe", "h6hgd82hdy6ds"]]


mock_db = MockDb()


@pytest.fixture(autouse=True)
def no_requests(monkeypatch):
    monkeypatch.setattr(api, "db", mock_db)


def test_index():
    response = client.get("/")
    assert response.status_code == 200


def test_get_users():
    with client:
        response = client.get("/users")
        assert response.status_code == 200
        assert response.json() == mock_db.get_users()
