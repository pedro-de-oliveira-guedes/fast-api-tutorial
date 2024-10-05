from pydantic import BaseModel

class TaskCreateResponse(BaseModel):
    id: str


class TaskBase(BaseModel):
    name: str
    description: str
    done: bool


class TaskPost(TaskBase):
    pass


class TaskGet(TaskBase):
    _id: str
