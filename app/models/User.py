from pydantic import BaseModel


class User(BaseModel):
    id: int
    userName: str
    password: str
    firstName: str
    lastName: str
    city: str
    phoneNumber: str
