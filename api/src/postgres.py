import os
from functools import cache

from psycopg_pool import ConnectionPool


@cache
def get_pool():
    uri = os.getenv("POSTGRES_URL", "")
    return ConnectionPool(uri, open=True)


def get_users():
    query = "SELECT * from ecommerce.users"
    pool = get_pool()
    with pool.connection() as conn:
        users = conn.execute(query).fetchall()
    return users
