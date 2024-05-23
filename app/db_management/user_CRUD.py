from app.db_management.config_db import usersCollection
from app.models import LoginRequest
from app.models.User import User
from app.db_management.config_db import usersCollection


async def register(user: User):
    res = usersCollection.insert_one(user.dict())
    return "hello " + user.firstName + " " + user.lastName


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

