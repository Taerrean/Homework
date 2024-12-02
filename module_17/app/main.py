from fastapi import FastAPI
from routers import task
from routers import user as u

app = FastAPI()


@app.get('/')
async def welcome():
    return {'message': 'Welcome to task manager'}

app.include_router(task.router)
app.include_router(u.router)