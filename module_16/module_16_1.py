from fastapi import FastAPI

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}

@app.get('/user/admin')
async def welcome() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get('/id')
async def id_info(username: str, age: int) -> dict:
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get('user/{uid}')
async def login(uid: str) -> dict:
    return {'message': f"Вы вошли как пользователь № {uid}"}