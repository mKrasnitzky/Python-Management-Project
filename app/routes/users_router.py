from fastapi import APIRouter
from app.models.User import User
from app.models.LoginRequest import LoginRequest
from app.db_management import user_CRUD

users_router = APIRouter()


@users_router.post("/register")
async def register(user: User):
    return await user_CRUD.register(user)


@users_router.post('/login')
async def login(login_request: LoginRequest):
   return await user_CRUD.login(login_request)


@users_router.put("/userName", response_model=User)
async def update_user(userName: str, user: User):
    return await user_CRUD.update_user(userName, user)
