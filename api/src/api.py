from fastapi import FastAPI

import postgres as database


app = FastAPI(lifespan=database.lifespan)


@app.get("/")
async def hello_world():
    return {"message": "Hello world!"}


@app.get("/users")
async def users():
    users = await database.get_users()
    return users
