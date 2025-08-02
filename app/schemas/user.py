from pydantic import BaseModel, EmailStr
from enum import Enum

class UserCreate(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    password: str

class UserOut(BaseModel):
    first_name: str
    last_name: str
    username: str
    email: EmailStr
    is_active: bool
    role: str

    class Config:
        orm_mode = True

class UserLogin(BaseModel):
    email: EmailStr
    password: str
