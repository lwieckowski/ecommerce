from fastapi import FastAPI, status

import postgres as db
from definitions import User

app = FastAPI()


@app.get("/users")
async def get_users() -> list[User]:
    users = db.get_users()
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(user: User) -> User:
    added_user = db.add_user(user)
    return added_user
