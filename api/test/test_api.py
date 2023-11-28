from dataclasses import asdict

import pytest
from fastapi import status
from starlette.testclient import TestClient

import api
from definitions import User
from postgres import get_pool, get_users

client = TestClient(api.app)


@pytest.fixture
def add_test_users():
    insert_query = """
        insert into ecommerce.users (username, email, password) values
        ('john776', 'jdoe@hotmail.com', 'h6hgd82hdy6ds'),
        ('jdoe', 'janedoe@gmail.com', 'j6hgd72huy68s');
        """
    pool = get_pool()
    with pool.connection() as conn:
        conn.execute(insert_query)
    yield


@pytest.fixture
def delete_all_users():
    yield
    pool = get_pool()
    with pool.connection() as conn:
        conn.execute("delete from ecommerce.users")


def test_index():
    response = client.get("/")
    assert response.status_code == 200


def test_get_users(add_test_users, delete_all_users):
    with client:
        response = client.get("/users")
        assert response.status_code == status.HTTP_200_OK
        assert len(response.json()) > 0


def test_create_user(delete_all_users):
    user = User(username="mike", email="mike.hike@gmail.com", password="123")
    with client:
        response = client.post("/users", json=asdict(user))
        assert response.status_code == status.HTTP_201_CREATED
        assert response.json() == asdict(user)
        assert user in get_users()


def test_create_user_invalid_body():
    user = {"not": "a valid user"}
    with client:
        response = client.post("/users", json=user)
        assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY


def test_create_user_already_exists(delete_all_users):
    user = User(username="mike", email="mike.hike@gmail.com", password="123")
    with client:
        response = client.post("/users", json=asdict(user))
        assert response.status_code == status.HTTP_201_CREATED
        response = client.post("/users", json=asdict(user))
        assert response.status_code == status.HTTP_201_CREATED
        assert user in get_users()
