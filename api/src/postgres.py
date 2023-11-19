from contextlib import asynccontextmanager
import databases
from fastapi import FastAPI


db = databases.Database("postgresql://postgres:123456@db/postgres")


@asynccontextmanager
async def lifespan(app: FastAPI):
    await db.connect()
    yield
    await db.disconnect()


async def get_users():
    return await db.fetch_all("SELECT * from ecommerce.users")
