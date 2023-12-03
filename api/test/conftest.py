import pytest
from starlette.testclient import TestClient

import api
import db


@pytest.fixture(scope="function")
def db_session():
    with db.get_pool().connection() as session:
        yield session
        session.rollback()


@pytest.fixture(scope="function")
def test_client(db_session):
    api.app.dependency_overrides[db.get_session] = lambda: db_session
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
