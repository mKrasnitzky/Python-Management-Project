import uvicorn as uvicorn
from fastapi import FastAPI
from app.routes.users_router import users_router

app = FastAPI()
app.include_router(users_router, prefix='/user')

if __name__ == '__main__':
    uvicorn.run(app, host="127.0.0.1", port=8000)
