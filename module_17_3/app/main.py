from fastapi import FastAPI
from app.routers import task, user as u

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Welcome to task manager'}

app.include_router(task.router)
app.include_router(u.router)