from model import Task

# MongoDB Driver
import motor.motor_asyncio

client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

database = client.TodoList
collection = database.tasks

async def fetch_all_tasks():
    tasks = []

    async for task in collection.find():
        tasks.append(Task(**task))

    return tasks

async def fetch_one_task(id):
    task = await collection.find_one({"id": id})

    return Task(**task)

async def fetch_one_by_name(name):
    query = {
        "name": {
            "$regex": f"{name}",
            "$options": "i"
        }
    }

    tasks = []
    async for task in collection.find(query):
        tasks.append(Task(**task))
    
    return tasks

async def create_task(task: Task):
    result = await collection.insert_one(task)

    return result

async def update_task(id, task: Task):
    result = await collection.replace_one({"id": id}, task)

    return result

async def delete_task(id):
    result = await collection.delete_one({"id": id})

    return result
