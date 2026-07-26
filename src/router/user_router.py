from fastapi import APIRouter
from src.schama.user_schama import UserCreate
from src.models.user_model import Users
from src.services import create_user,get_users,get_sin_user
from src.database.database_connection import get_session
from sqlmodel import select

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


