from fastapi import FastAPI
from os import getenv
import psycopg

def get_db():
    db = psycopg.connect(
        host="db",
        port=5432,
        dbname="postgres",
        user="postgres",
        password=getenv("POSTGRES_PASSWORD"),
    )
    db.autocommit = True
    print(getenv("POSTGRES_PASSWORD"))
    return db

def query(db: psycopg.Connection, sql):
    with db.cursor() as cursor:
        cursor.execute(sql)
        records = cursor.fetchall()
    return records

app = FastAPI()
db = get_db()

@app.get("/")
def hello_world():
    return {"message": "Hello world!"}

@app.get("/users")
def get_users():
    users = query(db, "SELECT * from ecommerce.users")
    return users