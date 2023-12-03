from fastapi import Depends, FastAPI, status

import db
from definitions import User

app = FastAPI()


@app.get("/users")
async def get_users(
    db_session: db.Session = Depends(db.get_session),
) -> list[User]:
    users = db.get_users(db_session)
    return users


@app.post("/users", status_code=status.HTTP_201_CREATED)
async def create_user(
    user: User, db_session: db.Session = Depends(db.get_session)
) -> User:
    added_user = db.add_user(db_session, user)
    return added_user
