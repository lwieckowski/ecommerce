import os
from functools import cache
from typing import TypeAlias

from psycopg import Connection
from psycopg.errors import UniqueViolation
from psycopg.rows import TupleRow, class_row
from psycopg_pool import ConnectionPool

from definitions import User

Session: TypeAlias = Connection[TupleRow]


@cache
def get_pool():
    uri = os.getenv("POSTGRES_URL", "")
    return ConnectionPool(uri, open=True)


async def get_session():
    with get_pool().connection() as session:
        yield session


def get_users(db: Session) -> list[User]:
    sql = "select * from ecommerce.users"
    cursor = db.cursor(row_factory=class_row(User))
    users = cursor.execute(sql).fetchall()
    return users


def add_user(db: Session, user: User) -> User:
    sql = "insert into ecommerce.users (username, email, password) values (%s, %s, %s)"
    try:
        db.execute(sql, (user.username, user.email, user.password))
    except UniqueViolation:
        return user
    return user
