from fastapi import FastAPI
from app.models import task, user

# создали сущность FastAPI
app = FastAPI()


@app.get("/")  # созд.1 маршрут "/"
async def welcome() -> dict:  # возвр.словарь
    return {"message": "Welcome to Taskmanager"}

# подкл. объектов APIRouter к созд.FastAPI
app.include_router(task.router)
app.include_router(user.router)
