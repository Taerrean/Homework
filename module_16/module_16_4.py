from fastapi import FastAPI, Path, HTTPException
from pydantic import BaseModel, Field
from typing import List


class User(BaseModel):
    id: int
    username: str
    age: int

class CreateUser(BaseModel):
    username: str = Field(..., min_length=3, max_length=50, description='Enter username')
    age: int


app = FastAPI()


users: List[User] = []


@app.get('/users', response_model=List[User])
async def get_users():
    return users


@app.post('/user/{username}/{age}', response_model=User)
async def add_user(user: CreateUser):
    newid = max((u.id for u in users), default=0) + 1
    newuser = User(id=newid, username=user.username, age=user.age)
    users.append(newuser)
    return newuser


@app.put('/user/{uid}/{username}/{age}')
async def update_params(uid:int, user:CreateUser):
    for u in users:
        if u.id == uid:
            newuser = User(id=uid, username=user.username, age=user.age)
            users.append(newuser)
            return newuser
    raise HTTPException(status_code = 404, detail = 'User not found.')


@app.delete('/user/{uid}')
async def del_user(uid: int):
    for u in users:
        if u.id == uid:
            return users.pop(uid)
    raise HTTPException(status_code=404, detail = 'User not found.')


@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}