import os
from psycopg_pool import ConnectionPool

uri = os.getenv("POSTGRES_URL", "")
pool = ConnectionPool(uri, open=True)


def get_users():
    query = "SELECT * from ecommerce.users"
    with pool.connection() as conn:
        users = conn.execute(query).fetchall()
    return users
