from fastapi import FastAPI, Path

app = FastAPI()

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}

@app.get('/user/admin')
async def welcome() -> dict:
    return {'message': "Вы вошли как администратор"}

@app.get('/user/id')
async def id_info(username: str, age: int = Path()) -> dict:
    return {'message': f"Информация о пользователе. Имя: {username}, Возраст: {age}"}

@app.get('/user/{uid}')
async def login(uid: int = Path(ge = 1, le = 100, description = 'Enter user ID', example = 1)) -> dict:
    return {'message': f"Вы вошли как пользователь № {uid}"}

@app.get('/user/{username}/{age}')
async def user(username: str = Path(min_length = 5, max_length = 20, description = 'Enter username', example = 'Terrarum'),
               age: int = Path(ge = 18, le = 120, description= 'Enter age', example = '16')) -> dict:
    return {'message': f'Подтвердите введённые данные: Имя: {username}, Возраст: {age}'}