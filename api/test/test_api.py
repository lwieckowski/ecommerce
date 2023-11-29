import unittest
from dataclasses import asdict

from fastapi import status
from starlette.testclient import TestClient

import api
from definitions import User
from postgres import get_pool, get_users


TEST_CLIENT = TestClient(api.app)


def add_test_users():
    insert_query = """
        insert into ecommerce.users (username, email, password) values
        ('john776', 'jdoe@hotmail.com', 'h6hgd82hdy6ds'),
        ('jdoe', 'janedoe@gmail.com', 'j6hgd72huy68s');
        """
    pool = get_pool()
    with pool.connection() as conn:
        conn.execute(insert_query)


def delete_all_users():
    pool = get_pool()
    with pool.connection() as conn:
        conn.execute("delete from ecommerce.users")


class TestGetUsers(unittest.TestCase):
    """Test get_users function - GET /users endpoint."""

    def setUp(self) -> None:
        """Add test users to the database."""
        super().setUp()
        add_test_users()

    def tearDown(self) -> None:
        """Delete all users from the database."""
        super().tearDown()
        delete_all_users()

    def test_normal_case(self):
        """Test case with successful retrieval of at least some users."""
        with TEST_CLIENT:
            response = TEST_CLIENT.get("/users")
            assert response.status_code == status.HTTP_200_OK
            assert len(response.json()) > 0


class TestCreateUser(unittest.TestCase):
    """Test create_user function - POST /users endpoint."""

    def tearDown(self) -> None:
        """Delete all users from the database."""
        super().tearDown()
        delete_all_users()

    def test_normal_case(self):
        """Test case with user added once for the first time."""
        user = User(username="mike", email="mike.hike@gmail.com", password="123")
        with TEST_CLIENT:
            response = TEST_CLIENT.post("/users", json=asdict(user))
            assert response.status_code == status.HTTP_201_CREATED
            assert response.json() == asdict(user)
            assert user in get_users()

    def test_invalid_body(self):
        """Test case with invalid user object in the body of the POST request."""
        user = {"this is not": "a valid user"}
        with TEST_CLIENT:
            response = TEST_CLIENT.post("/users", json=user)
            assert response.status_code == status.HTTP_422_UNPROCESSABLE_ENTITY

    def test_user_already_exists(self):
        """Test case with subsequent requests trying to create user that exists."""
        user = User(username="mike", email="mike.hike@gmail.com", password="123")
        with TEST_CLIENT:
            response = TEST_CLIENT.post("/users", json=asdict(user))
            assert response.status_code == status.HTTP_201_CREATED
            response = TEST_CLIENT.post("/users", json=asdict(user))
            assert response.status_code == status.HTTP_201_CREATED
            assert user in get_users()
