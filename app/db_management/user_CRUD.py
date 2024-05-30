# from http.client import HTTPException
from fastapi import HTTPException, APIRouter

from pymongo import DESCENDING

from app.db_management.config_db import usersCollection
from app.models import LoginRequest
from app.models import User
from app.db_management.config_db import usersCollection


async def register(user: User):
    user.id = await set_id()
    res = usersCollection.insert_one(user.dict())
    return user.id


async def login(loginRequest: LoginRequest):
    current_user = usersCollection.find_one({
        "userName": loginRequest.userName,
        "password": loginRequest.password
    })
    if current_user is None:
        return None

    return current_user


async def update_user(userName: str, user: User):
    current_user = usersCollection.find_one({
        "userName": userName,
    })
    if current_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    updated_user = user.dict()
    updated_user["id"] = current_user["id"]
    result = usersCollection.update_one(
        {"userName": userName},
        {"$set": updated_user}
    )
    return updated_user


async def set_id():
    max_id = usersCollection.find_one({}, sort=[("id", DESCENDING)])
    if max_id:
        return max_id["id"] + 1
    else:
        return 0

def func(x):
    return x>10
