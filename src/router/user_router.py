from fastapi import APIRouter
from src.schama.user_schama import UserCreate
from src.models.user_model import Users
from src.services import create_user,get_users,get_sin_user,update_user
from src.database.database_connection import get_session
from sqlmodel import select
from src.schama.user_schama import UserUpdate
from fastapi import APIRouter

from src.services.delete_user import delete_user





session=get_session()
def get_all_user():
    all_user=session.exec(select(Users)).all()
    return all_user



router=APIRouter(
    prefix="/users",
)


@router.post("/create_user")
def create_new_user(user:UserCreate):
    return create_user(user)


# @router.get("/all_user")
@router.get("/all_users")
def get_all_users():
    return get_users()


@router.get("/single_user/{id}")
def get_single_user(id:int):
    return get_sin_user(id=id)


@router.put("/update_user/{id}")
def update_existing_user(id: int, user: UserUpdate):
    return update_user(id, user)


@router.delete("/delete_user/{id}")
def delete_existing_user(id: int):
    return delete_user(id)
