from fastapi import FastAPI

import postgres as db

app = FastAPI()


@app.get("/")
async def hello_world():
    return {"message": "Hello world!"}


@app.get("/users")
async def users():
    users = db.get_users()
    return users
