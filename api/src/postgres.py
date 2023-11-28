import os
from functools import cache

import psycopg
from psycopg.rows import class_row
from psycopg_pool import ConnectionPool

from definitions import User


@cache
def get_pool():
    uri = os.getenv("POSTGRES_URL", "")
    return ConnectionPool(uri, open=True)


def get_users() -> list[User]:
    query = "select * from ecommerce.users"
    pool = get_pool()
    with pool.connection() as conn:
        cursor = conn.cursor(row_factory=class_row(User))
        users = cursor.execute(query).fetchall()
    return users


def add_user(user: User) -> User:
    query = (
        "insert into ecommerce.users (username, email, password) values (%s, %s, %s)"
    )
    pool = get_pool()
    with pool.connection() as conn:
        try:
            conn.execute(query, (user.username, user.email, user.password))
        except psycopg.errors.UniqueViolation:
            return user
    return user
