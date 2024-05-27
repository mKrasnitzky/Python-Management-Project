from app.db_management.config_db import usersCollection
from app.models import LoginRequest
from app.models.User import User
from app.db_management.config_db import usersCollection
import re


async def register(user: User):
    if not re.fullmatch(r'^\w{3,20}$', user.userName):
        return "Invalid userName: must be 3-20 alphanumeric characters or underscores."
    if not re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', user.password):
        return "Invalid password: must be at least 8 characters long and contain at least one letter and one number."
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


async def update_user(userName:str, user:User):
    current_user = usersCollection.find_one({
        "userName": userName,
    })
    if current_user is None:
        return None

    if not re.fullmatch(r'^\w{3,20}$', user.userName):
        return "Invalid userName: must be 3-20 alphanumeric characters or underscores."
    if not re.fullmatch(r'^(?=.*[A-Za-z])(?=.*\d)[A-Za-z\d]{8,}$', user.password):
        return "Invalid password: must be at least 8 characters long and contain at least one letter and one number."

    update_fields = {k: v for k, v in user.dict().items() if v is not None}
    if not update_fields:
        return current_user

    result = usersCollection.update_one(
        {"userName": userName},
        {"$set": update_fields}
    )

    if result.modified_count == 1:
        updated_user = usersCollection.find_one({"userName": userName})
        return updated_user
    else:
        return current_user

