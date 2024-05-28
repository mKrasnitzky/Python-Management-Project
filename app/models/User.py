from pydantic import BaseModel, conint, constr


class User(BaseModel):
    id: int
    userName: constr(min_length=3, max_length=30, pattern=r'^[a-zA-Z0-9_]+$')
    password: constr(min_length=8, pattern=r'^[^\s]+$')
    firstName: constr(min_length=1, max_length=50, pattern=r'^[a-zA-Zא-ת]+$')
    lastName: constr(min_length=1, max_length=50, pattern=r'^[a-zA-Zא-ת]+$')
    city: constr(min_length=1, max_length=50, pattern=r'^[a-zA-Zא-ת\s-]+$')
    phoneNumber: constr(pattern=r'^\+?[0-9]{10,15}$')
