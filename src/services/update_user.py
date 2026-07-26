from src.database.database_connection import get_session
from src.schama.user_schama import UserUpdate
from src.models.user_model import Users
from fastapi import HTTPException


from sqlmodel import select

session=get_session()
def update_user(id:int,user:UserUpdate):
    update=session.exec(select(Users).where(Users.id==id)).first()

    if update is None:
        raise HTTPException(
                status_code=404,
                detail="User not found"
            )

    update.first_name=user.first_name
    update.last_name=user.last_name
    update.email=user.email
    session.add(update)
    session.commit()
    session.refresh(update)

    return {
            "status": "Success",
            "message": "User Updated Successfully",
            "user": update
        }

