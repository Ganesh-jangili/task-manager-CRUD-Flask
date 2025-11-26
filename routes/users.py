from flask import Blueprint, request, jsonify
from config import mongo
from utils.profile_completion import clct_profile_completion
import bcrypt
from bson import ObjectId
from datetime import datetime, timezone

users_bp = Blueprint("users_bp", __name__)
#................................................................................................
@users_bp.route("/createUser", methods=["POST"])
def create_user():
    data = request.json
    hashed=bcrypt.hashpw(data["password"].encode("utf-8"), bcrypt.gensalt())
    user={
        "name": data["name"],
        "email": data["email"],
        "password": hashed,
        "bio": data.get("bio", ""),
        "address": data.get("address", ""),
        "pincode": data.get("pincode", ""),
        "state": data.get("state", ""),
        "country": data.get("country", ""),
        "phone": data.get("phone", ""),
        "created_at": datetime.now(timezone.utc),
        "updated_at": datetime.now(timezone.utc)
    }
    user["profile_completion"] = clct_profile_completion(user)
    inserted = mongo.db.users.insert_one(user)
    user["_id"] = str(inserted.inserted_id)
    return {"message": "User created successfully", "user": user}, 201

#................................................................................................
#to get user details by id
@users_bp.route("/<user_id>", methods=["GET"])
def get_user(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        user["_id"] = str(user["_id"])
        return jsonify(user), 200
    else:
        return {"message": "User not found"}, 404
    
#................................................................................................
#to get all users
@users_bp.route("/", methods=["GET"])
def get_all_users():
    users = []
    for user in mongo.db.users.find():
        user["_id"] = str(user["_id"])
        users.append(user)
    return jsonify(users), 200
#................................................................................................
#to update user details
@users_bp.route("/updateUser/<user_id>", methods=["PATCH"])
def update_user(user_id):
    data=request.json
    user=mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if not user:
        return {"message": "User not found"}, 404
    merged_data = {**user, **data}
    updated_completion = clct_profile_completion(merged_data)
    update_fields = {**data, "profile_completion": updated_completion, "updated_at": datetime.now(timezone.utc)}
    mongo.db.users.update_one({"_id": ObjectId(user_id)}, {"$set": update_fields})
    updated_user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    updated_user["_id"] = str(updated_user["_id"])
    return {"message": "User updated successfully", "user": updated_user}, 200
#................................................................................................
#to get profile completion percentage
@users_bp.route("/profileCompletion/<user_id>", methods=["GET"])
def get_profile_completion(user_id):
    user = mongo.db.users.find_one({"_id": ObjectId(user_id)})
    if user:
        completion = user.get("profile_completion", 0)
        return {"profile_completion": completion}, 200
    else:
        return {"message": "User not found"}, 404