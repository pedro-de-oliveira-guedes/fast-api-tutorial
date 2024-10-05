from model import TaskGet, TaskPost

# MongoDB Driver
import motor.motor_asyncio

class Database:
    def __init__(self):
        self.client = motor.motor_asyncio.AsyncIOMotorClient('mongodb://localhost:27017')

        self.database = self.client.TodoList
        self.collection = self.database.tasks

    async def fetch_all_tasks(self, ):
        tasks = []

        async for task in self.collection.find():
            tasks.append(TaskGet(**task))

        return tasks

    async def fetch_one_task(self, id):
        task = await self.collection.find_one({"id": id})

        return TaskGet(**task)

    async def fetch_by_name(self, name):
        query = {
            "name": {
                "$regex": f"{name}",
                "$options": "i"
            }
        }

        tasks = []
        async for task in self.collection.find(query):
            tasks.append(TaskGet(**task))
        
        return tasks

    async def create_task(self, task: TaskPost):
        result = await self.collection.insert_one(task.model_dump())

        return result

    async def update_task(self, id, task: TaskPost):
        result = await self.collection.replace_one({"id": id}, task)

        return result

    async def delete_task(self, id):
        result = await self.collection.delete_one({"id": id})

        return result
