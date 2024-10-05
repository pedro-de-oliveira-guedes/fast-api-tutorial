from database import Database
from model import TaskGet, TaskPost

from fastapi import FastAPI, Response, HTTPException
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

MongoDB = Database()

origins = ['https://localhost:3000']

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.get("/")
def read_root():
    return {"name": "John Doe", "Message": "Hello World"}

@app.get("/api/tasks", response_model=list[TaskGet])
async def get_all_tasks():
    res = await MongoDB.fetch_all_tasks()

    return res

@app.get("/api/tasks/{id}", response_model=TaskGet)
async def get_task_by_id(id: int):
    task = await MongoDB.fetch_one_task(id)

    if task is None:
        raise HTTPException(status_code=404, detail=f"Task with id '{id}' not found")

    return task

@app.get("/api/tasks/{name}", response_model=list[TaskGet])
async def get_task_by_name(name: str):
    tasks = await MongoDB.fetch_by_name(name)

    if tasks is None or len(tasks) == 0:
        raise HTTPException(status_code=404, detail="Task with name containing '{name}' not found")

    return tasks

@app.post("/api/tasks/", response_model=TaskPost)
async def create_task(task: TaskPost):
    res = await MongoDB.create_task(task)

    if res is None:
        raise HTTPException(status_code=500, detail="Failed to create task '{task}'")

    return Response(status_code=201, content=res.__str__())

@app.put("/api/tasks/{id}/", response_model=TaskPost)
async def update_task(id: int, task: TaskPost):
    res = await MongoDB.update_task(id, task)

    if res is None:
        raise HTTPException(status_code=500, detail="Failed to update task with id '{id}'")

    return res

@app.delete("/api/tasks/{id}")
async def delete_task(id: int):
    res = await MongoDB.delete_task(id)

    if res is None:
        raise HTTPException(status_code=500, detail="Failed to delete task with id '{id}'")
    
    return Response(status_code=204)