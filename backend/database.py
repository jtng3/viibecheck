from models import Todo, UpdateTodoModel
import motor.motor_asyncio  # MongoDB Driver
from bson.objectid import ObjectId
import os
from dotenv import load_dotenv
load_dotenv()
connection_string = os.environ.get('CONNECTION_STRING')

client = motor.motor_asyncio.AsyncIOMotorClient(connection_string)
database = client.TodoList  # name of database
# same thing as a table in SQL not really sure on why this isnt deploying
collection = database.todo


async def fetch_all_todos():
    todos = []
    cursor = collection.find({})
    async for document in cursor:
        todos.append(Todo(**document))
    return todos


async def create_todo(todo):
    document = todo
    result = await collection.insert_one(document)
    return document


async def fetch_one_todo(id):
    todo = await collection.find_one({"_id": id})
    if todo is not None:
        return todo


async def update_todo(id, todo):
    update_result = await collection.update_one({"_id": id}, {"$set": todo})
    if update_result.modified_count == 1:
        updated_todo = await collection.find_one({"_id": id})
        if updated_todo is not None:
            return updated_todo
    existing_todo = await collection.find_one({"_id": id})
    if existing_todo is not None:
        return existing_todo


async def remove_todo(id):
    await collection.delete_one({"_id": id})
    return True
