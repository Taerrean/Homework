from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.task import CreateTask
from app.backend.db_depends import get_db
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from app.models import *
from sqlalchemy import insert
from slugify import slugify

router = APIRouter(prefix='/task', tags=['task'])


@router.get('/all')
async def all_tasks(db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.is_active == True)).all()
    if tasks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No tasks found.')
    return tasks


@router.get('/{task_id}')
async def this_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    task = db.scalars(select(Task).where(Task.tid == task_id)).all()
    if task is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found.')
    return task


@router.post('/create')
async def create_task(user_id: int, task: CreateTask, db: Annotated[Session, Depends(get_db)]):
    target_user = db.scalars(select(User).where(User.uid == user_id)).all()
    if target_user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
    db.execute(insert(Task).values(title=task.title,
                                   content=task.content,
                                   priority=task.priority,
                                   user_id=user_id,
                                   slug=slugify(task.title)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Task creation successful.'
    }


@router.put('/update/{task_id}')
async def update_task(task_id: int, task: CreateTask, db: Annotated[Session, Depends(get_db)]):
    target = db.scalars(select(Task).where(Task.tid == task_id)).all()
    if target is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found.')
    db.execute(update(Task).values(title=task.title,
                                   content=task.content,
                                   priority=task.priority,
                                   slug=slugify(task.title)))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task update successful.'
    }


@router.delete('/delete/{task_id}')
async def delete_task(task_id: int, db: Annotated[Session, Depends(get_db)]):
    target = db.scalars(select(Task).where(Task.tid == task_id)).all()
    if target is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Task not found.')
    db.execute(delete(Task).where(Task.tid == task_id)).all()
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'Task deletion successful.'
    }
