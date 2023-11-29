import os
from functools import cache

from psycopg import Connection
from psycopg.rows import class_row, TupleRow
from psycopg.errors import UniqueViolation
from psycopg_pool import ConnectionPool

from definitions import User


@cache
def get_pool():
    uri = os.getenv("POSTGRES_URL", "")
    return ConnectionPool(uri, open=True)


async def get_db():
    with get_pool().connection() as conn:
        yield conn


def get_users(db: Connection[TupleRow]) -> list[User]:
    sql = "select * from ecommerce.users"
    cursor = db.cursor(row_factory=class_row(User))
    users = cursor.execute(sql).fetchall()
    return users


def add_user(db: Connection[TupleRow], user: User) -> User:
    sql = "insert into ecommerce.users (username, email, password) values (%s, %s, %s)"
    try:
        db.execute(sql, (user.username, user.email, user.password))
    except UniqueViolation:
        return user
    return user
