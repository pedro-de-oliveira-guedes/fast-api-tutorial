from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

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

@app.get("/api/tasks")
async def get_all_tasks():
    return 1

@app.get("/api/tasks/{id}")
async def get_task_by_id(id: int):
    return id

@app.post("/api/tasks")
async def create_task():
    return 1

@app.put("/api/tasks/{id}")
async def update_task(id: int):
    return id

@app.delete("/api/tasks/{id}")
async def delete_task(id: int):
    return id