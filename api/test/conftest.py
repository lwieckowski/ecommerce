import pytest
from starlette.testclient import TestClient

import api
from postgres import get_db, get_pool


@pytest.fixture(scope="session")
def db_pool():
    return get_pool()


@pytest.fixture(scope="function")
def db_session(db_pool):
    with db_pool.connection() as conn:
        yield conn
        conn.rollback()


@pytest.fixture(scope="function")
def client(db_session):
    api.app.dependency_overrides[get_db] = lambda: db_session
    with TestClient(api.app) as test_client:
        yield test_client


@pytest.fixture
def test_users(db_session):
    insert_query = """
        insert into ecommerce.users (username, email, password) values
        ('john776', 'jdoe@hotmail.com', 'h6hgd82hdy6ds'),
        ('jdoe', 'janedoe@gmail.com', 'j6hgd72huy68s');
        """
    db_session.execute(insert_query)
