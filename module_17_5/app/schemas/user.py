from pydantic import BaseModel


class User(BaseModel):
    uid: int
    username: str
    first_name: str
    last_name: str
    age: int

    class Config:
        orm_mode = True


class CreateUser(BaseModel):
    username: str
    first_name: str
    last_name: str
    age: int
