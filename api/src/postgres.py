from contextlib import asynccontextmanager
import os
import databases
from fastapi import FastAPI

url = os.getenv("POSTGRES_URL", "")
db = databases.Database(url)


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


async def get_users():
    return await db.fetch_all("SELECT * from ecommerce.users")
