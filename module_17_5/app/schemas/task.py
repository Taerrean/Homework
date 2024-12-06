from pydantic import BaseModel


class Task(BaseModel):
    tid: int
    title: str
    content: str
    priority: str
    completed: bool = False
    user_id: int

    class Config:
        orm_mode = True


class CreateTask(BaseModel):
    title: str
    content: str
    priority: str
    completed: bool = False
