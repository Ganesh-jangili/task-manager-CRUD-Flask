from flask import Blueprint, request, jsonify
from config import mongo
from bson import ObjectId

tasks_bp = Blueprint("tasks_bp", __name__)
#................................................................................................
#to create a new task
@tasks_bp.route("/createTask", methods=["POST"])
def create_task():
    data = request.json
    user=mongo.db.users.find_one({"_id": ObjectId(data["user_id"])})
    if not user:
        return {"message": "User not found"}, 404
    task = {
        "title": data["title"],
        "description": data.get("description", ""),
        "status": data.get("status", "pending"),
        "user_id": data["user_id"]
    }
    inserted = mongo.db.tasks.insert_one(task)
    task["_id"] = str(inserted.inserted_id)
    return {"message": "Task created successfully", "task": task}, 201
#................................................................................................
#to get tasks by user id
@tasks_bp.route("/getTasks/<user_id>", methods=["GET"])
def get_tasks_by_user(user_id):
    tasks = mongo.db.tasks.find({"user_id": ObjectId(user_id)})
    t_list = []
    for task in tasks:
        task["_id"] = str(task["_id"])
        task["user_id"] = str(task["user_id"])
        t_list.append(task)
    return jsonify(t_list), 200
#................................................................................................
   #get task by task id
@tasks_bp.route("/getTask/<task_id>", methods=["GET"])
def get_task(task_id):
    task = mongo.db.tasks.find_one({"_id": ObjectId(task_id)})
    if task:
        task["_id"] = str(task["_id"])
        task["user_id"] = str(task["user_id"])
        return jsonify(task), 200
    else:
        return {"message": "Task not found"}, 404
#................................................................................................
#to update task details
@tasks_bp.route("/updateTask/<task_id>", methods=["PATCH"])
def update_task(task_id):
    data=request.json
    updated=mongo.db.tasks.update_one({"_id": ObjectId(task_id)}, {"$set": data},return_document=True)
    if not updated:
        return {"message": "Task not found"}, 404
    updated["_id"] = str(updated["_id"])
    updated["user_id"] = str(updated["user_id"])
    return {"message": "Task updated successfully", "task": updated}, 200
#..................................................................................................
#to delete a task
@tasks_bp.route("/deleteTask/<task_id>", methods=["DELETE"])
def delete_task(task_id):
    result = mongo.db.tasks.delete_one({"_id": ObjectId(task_id)})
    if result.deleted_count == 0:
        return {"message": "Task not found"}, 404
    return {"message": "Task deleted successfully"}, 200
#..................................................................................................