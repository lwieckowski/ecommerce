from dataclasses import asdict

from fastapi import status

from definitions import User


def test_get_users(client, test_users):
    """Test case with successful retrieval of at least some users."""
    with client:
        response = client.get("/users")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 0


def test_create_user(client):
    """Test case with user added once for the first time."""
    user = User(username="mike", email="mike.hike@gmail.com", password="123")
    with client:
        response = client.post("/users", json=asdict(user))
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == asdict(user)


def test_create_user_invalid_body(client):
    """Test case with invalid user object in the body of the POST request."""
    user = {"this is not": "a valid user"}
    with client:
        response = client.post("/users", json=user)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_create_user_already_exists(client):
    """Test case with subsequent requests trying to create user that exists."""
    user = User(username="mike", email="mike.hike@gmail.com", password="123")
    with client:
        response = client.post("/users", json=asdict(user))
        assert response.status_code == status.HTTP_201_CREATED
        response = client.post("/users", json=asdict(user))
        assert response.status_code == status.HTTP_201_CREATED
