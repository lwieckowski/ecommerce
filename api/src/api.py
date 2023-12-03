from fastapi import Depends, FastAPI, HTTPException, status

import db
from definitions import User

app = FastAPI()


@app.get("/users")
async def get_users(
    db_session: db.Session = Depends(db.get_session),
) -> list[User]:
    users = db.get_users(db_session)
    return users


@app.post(
    "/users",
    status_code=status.HTTP_201_CREATED,
    responses={
        400: {
            "description": "Username or email already exist",
            "content": {
                "application/json": {
                    "example": {"detail": "User exists"}
                }
            },
        }
    },
)
async def create_user(
    user: User, db_session: db.Session = Depends(db.get_session)
) -> User:
    added_user = db.add_user(db_session, user)
    if not added_user:
        raise HTTPException(400, detail="User exists")
    return added_user
