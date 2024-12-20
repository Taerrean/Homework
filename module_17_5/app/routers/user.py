from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from app.schemas.user import CreateUser
from app.backend.db_depends import get_db
from typing import Annotated
from sqlalchemy import insert, select, update, delete
from app.models import *
from sqlalchemy import insert
from slugify import slugify

router = APIRouter(prefix='/user', tags=['user'])


@router.get('/all')
async def all_users(db: Annotated[Session, Depends(get_db)]):
    users = db.scalars(select(User).where(User.is_active == True)).all()
    if users is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No users found.')
    return users


@router.get('/{user_id}')
async def this_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    target = db.scalars(select(User).where(User.uid == user_id)).all()
    if target is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
    return target


@router.get('/{user_id}/tasks')
async def tasks_of_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    tasks = db.scalars(select(Task).where(Task.user_id == user_id)).all()
    if tasks is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='No tasks found.')
    return tasks


@router.post('/create')
async def create_user(db: Annotated[Session, Depends(get_db)], user: CreateUser):
    db.execute(insert(User).values(username=user.username,
                                   first_name=user.first_name,
                                   last_name=user.last_name,
                                   age=user.age,
                                   slug=slugify(user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'User creation successful.'
    }


@router.put('/update/{user_id}')
async def update_user(user_id: int, upduser: CreateUser, db: Annotated[Session, Depends(get_db)]):
    target = db.scalars(select(User).where(User.uid == user_id))
    if target is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
    db.execute(update(User).where(User.uid == user_id).values(
        username=upduser.username,
        first_name=upduser.first_name,
        last_name=upduser.last_name,
        age=upduser.age,
        slug=slugify(upduser.username)
    ))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User update successful.'
    }

@router.delete('/delete/{user_id}')
async def delete_user(user_id: int, db: Annotated[Session, Depends(get_db)]):
    target = db.scalars(select(User).where(User.uid == user_id)).all()
    if target is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='User not found.')
    db.execute(delete(Task).where(Task.user_id == user_id))
    db.execute(delete(User).where(User.uid == user_id))
    db.commit()
    return {
        'status_code': status.HTTP_200_OK,
        'transaction': 'User deletion successful.'
    }