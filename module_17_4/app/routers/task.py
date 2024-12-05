from fastapi import APIRouter
from app.schemas.task import Task, CreateTask
from fastapi import HTTPException
router = APIRouter(prefix='/task', tags=['task'])

tasks = [{"tid": 1, "title": "startertask", "content": "Сколько будет дважды два?", "priority": "69", "completed": False, "user_id": 1},
         {"tid": 2, "title": "advancedtask", "content": "Сколько будет два в квадрате?", "priority": "420", "completed": False, "user_id": 2}]


@router.get('/all', response_model=list[Task])
async def all_tasks():
    return tasks


@router.get('/{task_id}', response_model=Task)
async def this_task(task_id: int):
    for t in tasks:
        if t['tid'] == task_id:
            return t
    raise HTTPException(status_code=404, detail='Task not found.')


@router.post('/create', response_model=Task)
async def create_task(task: CreateTask):
    new_task = {'tid': len(tasks) + 1, 'title': task.title, 'content': task.content, 'priority': task.priority, 'user_id': 2}
    tasks.append(new_task)
    return new_task


@router.put('/update/{task_id}', response_model=Task)
async def update_task(task_id: int, task: CreateTask):
    for t in tasks:
        if t['tid'] == task_id:
            t['title'] = task.title
            t['content'] = task.content
            t['priority'] = task.priority
            t['completed'] = task.completed
            return t
    raise HTTPException(status_code=404, detail='Task not found.')


@router.delete('/delete/{task_id}')
async def delete_task(task_id: int):
    for t in tasks:
        if t['tid'] == task_id:
            tasks.remove(tasks[t['tid'] - 1])
            return {'message': 'Task deleted successfully.'}
    raise HTTPException(status_code=404, detail='Task not found.')