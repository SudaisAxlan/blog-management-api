from sqlmodel import select
from fastapi import HTTPException

from src.database.database_connection import get_session
from src.models.user_model import Users


def delete_user(id: int):

    with get_session() as session:

        delete = session.exec(
            select(Users).where(Users.id == id)
        ).first()

        if delete is None:
            raise HTTPException(
                status_code=404,
                detail="User not found"
            )

        session.delete(delete)
        session.commit()

        return {
            "status": "Success",
            "message": "User deleted successfully"
        }