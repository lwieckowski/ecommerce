from fastapi import Depends, FastAPI, status
from psycopg import Connection
from psycopg.rows import TupleRow

import postgres
from definitions import User

app = FastAPI()


@app.get("/users")
async def get_users(db: Connection[TupleRow] = Depends(postgres.get_db)) -> list[User]:
    users = postgres.get_users(db)
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: User, db: Connection[TupleRow] = Depends(postgres.get_db)
) -> User:
    added_user = postgres.add_user(db, user)
    return added_user
