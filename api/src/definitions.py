from pydantic.dataclasses import dataclass


@dataclass
class User:
    username: str
    email: str
    password: str
