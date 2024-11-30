from fastapi import FastAPI, Path, HTTPException

app = FastAPI()

users = {'1': 'Имя: Example, возраст: 18'}


@app.get('/users')
async def get_users() -> dict:
    return users


@app.post('/user/{username}/{age}')
async def add_user(username: str = Path(min_length = 5, max_length = 20, description = 'Enter username', examples = ['Terrarum']),
               age: int = Path(ge = 18, le = 120, description= 'Enter age', example = '18')):
    newid = max(int(uid) for uid in users.keys()) + 1 if users else 1
    newuser = {str(newid) : f'Имя: {username}, возраст: {age}'}
    users.update(newuser)
    return {'message': f'User {newid} is registered.'}

@app.delete('/user/{user_id}')
async def del_user(user_id: int):
    for ids in users.keys():
        if int(ids) == user_id:
            users.pop(ids)
            return f'User {user_id} has been deleted.'
    raise HTTPException(status_code=404, detail = 'User not found.')


@app.put('/user/{user_id}/{username}/{age}')
async def update_params(username: str = Path(min_length = 5, max_length = 20, description = 'Enter username', example = 'Terrarum'),
                        age: int = Path(ge = 18, le = 120, description= 'Enter age', examples = ['18']), user_id: int = Path()):
    for ids in users.keys():
        if int(ids) == user_id:
            users.update({ids: f'Имя: {username}, возраст: {age}'})
            return {'message' : f"User {user_id} has been updated."}
    raise HTTPException(status_code = 404, detail = 'User not found.')

@app.get('/')
async def welcome() -> dict:
    return {'message': 'Hello World'}