from src.schama.user_schama import UserCreate
from src.database.database_connection import get_session,engine
from src.models.user_model import Users
from src.database.database_connection import get_session
from sqlmodel import select



session=get_session()
def creates_user(user: UserCreate):

    new_user = Users(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email
    )

    # session = get_session()

    session.add(new_user)

    session.commit()

    session.refresh(new_user)

    return {
        "status": "Successfully",
        "message": "User Added Successfully",
        "user": new_user
    }





def get_all_user():
    all_user=session.exec(select(Users)).all()
    return all_user


def get_single_user(id:int):
    get_user=session.exec(select(Users).where(Users.id==id)).first()
    return get_user


