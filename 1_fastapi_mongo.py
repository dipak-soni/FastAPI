from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi
from bson import ObjectId

app = FastAPI()

# MongoDB Atlas Connection
uri = "mongodb+srv://dipak:CEVzQb4I4fa4PcpZ@cluster0.axm8h.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, server_api=ServerApi('1'))
db = client["todo"]
collection = db["tasks"]

# Pydantic Model
class Task(BaseModel):
    title: str
    description: str

# Create a Task
@app.post("/tasks/")
def create_task(task: Task):
    new_task = dict(task)
    result = collection.insert_one(new_task)
    return {"id": str(result.inserted_id), "message": "Task added successfully"}

# Get All Tasks
@app.get("/tasks/")
def get_tasks():
    tasks = list(collection.find())
    return [{"id": str(task["_id"]), "title": task["title"], "description": task["description"]} for task in tasks]

# Get Task by ID
@app.get("/tasks/{task_id}")
def get_task(task_id: str):
    task = collection.find_one({"_id": ObjectId(task_id)})
    if task:
        return {"id": str(task["_id"]), "title": task["title"], "description": task["description"]}
    raise HTTPException(status_code=404, detail="Task not found")

# Update a Task
@app.patch("/tasks/{task_id}")
def update_task(task_id: str, updated_task: Task):
    result = collection.update_one(
        {"_id": ObjectId(task_id)},
        {"$set": updated_task.dict()}
    )
    if result.modified_count:
        return {"message": "Task updated successfully"}
    raise HTTPException(status_code=404, detail="Task not found")

# Delete a Task
@app.delete("/tasks/{task_id}")
def delete_task(task_id: str):
    result = collection.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count:
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")
