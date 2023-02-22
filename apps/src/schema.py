from pydantic import BaseModel, EmailStr
from typing import Optional

class Users(BaseModel):
    id: Optional[int] = None
    name: str
    email: EmailStr
    phone_number: str
    password: str

    class Config:
        orm_mode = True

class UsersSimple(BaseModel):
    id:Optional[int] = None
    name: str
    email: EmailStr

    class Config:
        orm_mode = True
