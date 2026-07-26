from pydantic import BaseModel, EmailStr


class UserCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr


class UserUpdate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr